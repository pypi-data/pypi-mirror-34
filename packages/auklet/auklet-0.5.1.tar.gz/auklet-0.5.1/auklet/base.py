# Portions of this file are taken from
# https://github.com/what-studio/profiling/tree/0.1.1,
# the license for which can be found in the "licenses/profiling.txt" file
# in this repository/package.
from __future__ import absolute_import, unicode_literals

import os
import io
import sys
import ssl
import uuid
import json
import zipfile
import hashlib

from uuid import uuid4
from datetime import datetime
from contextlib import contextmanager
from collections import deque
from kafka import KafkaProducer
from kafka.errors import KafkaError
from auklet.stats import Event, SystemMetrics
from auklet.errors import AukletConfigurationError
from ipify import get_ip
from ipify.exceptions import IpifyException

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError, URLError
    from urllib.request import Request, urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, Request, HTTPError, URLError

__all__ = ['Client', 'Runnable', 'frame_stack', 'deferral', 'get_commit_hash',
           'get_mac', 'get_device_ip', 'setup_thread_excepthook',
           'get_abs_path', 'b', 'u']

MB_TO_B = 1e6
S_TO_MS = 1000


class Client(object):
    producer_types = None
    brokers = None
    commit_hash = None
    mac_hash = None
    offline_filename = ".auklet/local.txt"
    limits_filename = ".auklet/limits"
    usage_filename = ".auklet/usage"
    com_config_filename = ".auklet/communication"
    abs_path = None

    reset_data = False
    data_day = 1
    data_limit = None
    data_current = 0
    offline_limit = None
    offline_current = 0

    system_metrics = None

    def __init__(self, apikey=None, app_id=None,
                 base_url="https://api.auklet.io/", mac_hash=None):
        self.apikey = apikey
        self.app_id = app_id
        self.base_url = base_url
        self.send_enabled = True
        self.producer = None
        self._get_kafka_brokers()
        self.mac_hash = mac_hash
        self._load_limits()
        self._create_file(self.offline_filename)
        self._create_file(self.limits_filename)
        self._create_file(self.usage_filename)
        self._create_file(self.com_config_filename)
        self.commit_hash = get_commit_hash()
        self.abs_path = get_abs_path(".auklet/version")
        self.system_metrics = SystemMetrics()
        if self._get_kafka_certs():
            try:
                ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
                ctx.options &= ~ssl.OP_NO_SSLv3
                self.producer = KafkaProducer(**{
                    "bootstrap_servers": self.brokers,
                    "ssl_cafile": ".auklet/ck_ca.pem",
                    "security_protocol": "SSL",
                    "ssl_check_hostname": False,
                    "value_serializer": lambda m: b(json.dumps(m)),
                    "ssl_context": ctx
                })
            except (KafkaError, Exception):
                # TODO log off to kafka if kafka fails to connect
                pass

    def _create_file(self, filename):
        open(filename, "a").close()

    def _build_url(self, extension):
        return '%s%s' % (self.base_url, extension)

    def _open_auklet_url(self, url):
        url = Request(url, headers={"Authorization": "JWT %s" % self.apikey})
        try:
            res = urlopen(url)
        except HTTPError as e:
            if e.code == 401:
                raise AukletConfigurationError(
                    "Invalid configuration of Auklet Monitoring, "
                    "ensure proper API key and app ID passed to "
                    "Monitoring class"
                )
            raise e
        except URLError:
            return None
        return res

    def _get_config(self):
        res = self._open_auklet_url(
            self._build_url(
                "private/devices/{}/app_config/".format(self.app_id)))
        if res is not None:
            return json.loads(u(res.read()))['config']

    def _get_kafka_brokers(self):
        res = self._open_auklet_url(
            self._build_url("private/devices/config/"))
        if res is None:
            return self._load_kafka_conf()
        kafka_info = json.loads(u(res.read()))
        self._write_kafka_conf(kafka_info)
        self.brokers = kafka_info['brokers']
        self.producer_types = {
            "monitoring": kafka_info['prof_topic'],
            "event": kafka_info['event_topic'],
            "log": kafka_info['log_topic']
        }

    def _write_kafka_conf(self, info):
        with open(self.com_config_filename, "w") as conf:
            conf.write(json.dumps(info))

    def _load_kafka_conf(self):
        try:
            with open(self.com_config_filename, "r") as conf:
                kafka_str = conf.read()
                if kafka_str:
                    data = json.loads(kafka_str)
                    self.brokers = data['brokers']
                    self.producer_types = {
                        "monitoring": data['prof_topic'],
                        "event": data['event_topic'],
                        "log": data['log_topic']
                    }
                    return True
                else:
                    return False
        except OSError:
            return False

    def _load_limits(self):
        try:
            with open(self.limits_filename, "r") as limits:
                limits_str = limits.read()
                if limits_str:
                    data = json.loads(limits_str)
                    self.data_day = data['data']['normalized_cell_plan_date']
                    temp_limit = data['data']['cellular_data_limit']
                    if temp_limit is not None:
                        self.data_limit = data['data'][
                                              'cellular_data_limit'] * MB_TO_B
                    else:
                        self.data_limit = temp_limit
                    temp_offline = data['storage']['storage_limit']
                    if temp_offline is not None:
                        self.offline_limit = data['storage'][
                                                 'storage_limit'] * MB_TO_B
                    else:
                        self.offline_limit = data['storage']['storage_limit']
        except IOError:
            return

    def _get_kafka_certs(self):
        url = Request(self._build_url("private/devices/certificates/"),
                      headers={"Authorization": "JWT %s" % self.apikey})
        try:
            try:
                res = urlopen(url)
            except HTTPError as e:
                # Allow for accessing redirect w/o including the
                # Authorization token.
                res = urlopen(e.geturl())
        except URLError:
            return False
        mlz = zipfile.ZipFile(io.BytesIO(res.read()))
        for temp_file in mlz.filelist:
            filename = ".auklet/%s.pem" % temp_file.filename
            self._create_file(filename)
            f = open(filename, "wb")
            f.write(mlz.open(temp_file.filename).read())
        return True

    def _write_to_local(self, data):
        try:
            if self._check_data_limit(data, self.offline_current, True):
                with open(self.offline_filename, "a") as offline:
                    offline.write(json.dumps(data))
                    offline.write("\n")
        except IOError:
            # TODO determine what to do with data we fail to write
            return False

    def _clear_file(self, file_name):
        open(file_name, "w").close()

    def _produce_from_local(self):
        try:
            with open(self.offline_filename, 'r+') as offline:
                lines = offline.read().splitlines()
                for line in lines:
                    loaded = json.loads(line)
                    if 'stackTrace' in loaded.keys() \
                            or 'message' in loaded.keys():
                        data_type = "event"
                    else:
                        data_type = "monitoring"

                    if self._check_data_limit(loaded, self.data_current):
                        self._produce(loaded, data_type)
            self._clear_file(self.offline_filename)
        except IOError:
            # TODO determine what to do if we can't read the file
            return False

    def _build_usage_json(self):
        return {"data": self.data_current, "offline": self.offline_current}

    def _update_usage_file(self):
        try:
            with open(self.usage_filename, 'w') as usage:
                usage.write(json.dumps(self._build_usage_json()))
        except IOError:
            return False

    def _check_data_limit(self, data, current_use, offline=False):
        if self.offline_limit is None and offline:
            return True
        if self.data_limit is None and not offline:
            return True
        data_size = len(json.dumps(data))
        temp_current = current_use + data_size
        if temp_current >= self.data_limit:
            return False
        if offline:
            self.offline_current = temp_current
        else:
            self.data_current = temp_current
        self._update_usage_file()
        return True

    def _kafka_error_callback(self, error, msg):
        self._write_to_local(msg)

    def update_network_metrics(self, interval):
        self.system_metrics.update_network(interval)

    def check_date(self):
        if datetime.today().day == self.data_day:
            if self.reset_data:
                self.data_current = 0
                self.reset_data = False
        else:
            self.reset_data = True

    def update_limits(self):
        config = self._get_config()
        if config is None:
            return 60
        with open(self.limits_filename, 'w+') as limits:
            limits.truncate()
            limits.write(json.dumps(config))
        new_day = config['data']['normalized_cell_plan_date']
        temp_limit = config['data']['cellular_data_limit']
        if temp_limit is not None:
            new_data = config['data']['cellular_data_limit'] * MB_TO_B
        else:
            new_data = temp_limit
        temp_offline = config['storage']['storage_limit']
        if temp_offline is not None:
            new_offline = config['storage']['storage_limit'] * MB_TO_B
        else:
            new_offline = config['storage']['storage_limit']
        if self.data_day != new_day:
            self.data_day = new_day
            self.data_current = 0
        if self.data_limit != new_data:
            self.data_limit = new_data
        if self.offline_limit != new_offline:
            self.offline_limit = new_offline
        # return emission period in ms
        return config['emission_period'] * S_TO_MS

    def build_event_data(self, type, traceback, tree):
        event = Event(type, traceback, tree, self.abs_path)
        event_dict = dict(event)
        event_dict['application'] = self.app_id
        event_dict['publicIP'] = get_device_ip()
        event_dict['id'] = str(uuid4())
        event_dict['timestamp'] = str(datetime.utcnow())
        event_dict['systemMetrics'] = dict(self.system_metrics)
        event_dict['macAddressHash'] = self.mac_hash
        event_dict['commitHash'] = self.commit_hash
        return event_dict

    def build_log_data(self, msg, data_type, level):
        log_dict = {
            "message": msg,
            "type": data_type,
            "level": level,
            "application": self.app_id,
            "publicIP": get_device_ip(),
            "id": str(uuid4()),
            "timestamp": str(datetime.utcnow()),
            "systemMetrics": dict(SystemMetrics()),
            "macAddressHash": self.mac_hash,
            "commitHash": self.commit_hash
        }
        return log_dict

    def _produce(self, data, data_type="monitoring"):
        self.producer.send(self.producer_types[data_type],
                           value=data) \
            .add_errback(self._kafka_error_callback, msg=data)

    def produce(self, data, data_type="monitoring"):
        if self.producer is not None:
            try:
                if self._check_data_limit(data, self.data_current):
                    self._produce(data, data_type)
                    self._produce_from_local()
                else:
                    self._write_to_local(data)
            except KafkaError:
                self._write_to_local(data)


class Runnable(object):
    """The base class for runnable classes such as :class:`monitoring.
    MonitoringBase`.
    """

    #: The generator :meth:`run` returns.  It will be set by :meth:`start`.
    _running = None

    def is_running(self):
        """Whether the instance is running."""
        return self._running is not None

    def start(self, *args, **kwargs):
        """Starts the instance.
        :raises RuntimeError: has been already started.
        :raises TypeError: :meth:`run` is not canonical.
        """
        if self.is_running():
            raise RuntimeError('Already started')
        self._running = self.run(*args, **kwargs)
        try:
            yielded = next(self._running)
        except StopIteration:
            raise TypeError('run() must yield just one time')
        if yielded is not None:
            raise TypeError('run() must yield without value')

    def stop(self):
        """Stops the instance.
        :raises RuntimeError: has not been started.
        :raises TypeError: :meth:`run` is not canonical.
        """
        if not self.is_running():
            raise RuntimeError('Not started')
        running, self._running = self._running, None
        try:
            next(running)
        except StopIteration:
            # expected.
            pass
        else:
            raise TypeError('run() must yield just one time')

    def run(self, *args, **kwargs):
        """Override it to implement the starting and stopping behavior.
        An overriding method must be a generator function which yields just one
        time without any value.  :meth:`start` creates and iterates once the
        generator it returns.  Then :meth:`stop` will iterates again.
        :raises NotImplementedError: :meth:`run` is not overridden.
        """
        raise NotImplementedError('Implement run()')
        yield

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *exc_info):
        self.stop()


def frame_stack(frame):
    """Returns a deque of frame stack."""
    frames = deque()
    while frame is not None:
        frames.appendleft(frame)
        frame = frame.f_back
    return frames


def get_mac():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return hashlib.md5(b(mac)).hexdigest()


def get_commit_hash():
    try:
        with open(".auklet/version", "r") as auklet_file:
            return auklet_file.read().rstrip()
    except IOError:
        # TODO Error out app if no commit hash
        return ""


def get_abs_path(path):
    try:
        return os.path.abspath(path).split('/.auklet')[0]
    except IndexError:
        return ''


def get_device_ip():
    try:
        return get_ip()
    except IpifyException:
        # TODO log to kafka if the ip service fails for any reason
        return None
    except Exception:
        return None


def setup_thread_excepthook():
    import threading
    """
    Workaround for `sys.excepthook` thread bug from:
    http://bugs.python.org/issue1230540

    Call once from the main thread before creating any threads.
    """
    init_original = threading.Thread.__init__

    def init(self, *args, **kwargs):

        init_original(self, *args, **kwargs)
        run_original = self.run

        def run_with_except_hook(*args2, **kwargs2):
            try:
                run_original(*args2, **kwargs2)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                sys.excepthook(*sys.exc_info())

        self.run = run_with_except_hook

    threading.Thread.__init__ = init


if sys.version_info < (3,):
    # Python 2 and 3 String Compatibility
    def b(x):
        return x

    def u(x):
        return x
else:
    # https://pythonhosted.org/six/#binary-and-text-data
    import codecs

    def b(x):
        # Produces a unicode string to encoded bytes
        return codecs.utf_8_encode(x)[0]

    def u(x):
        # Produces a byte string from a unicode object
        return codecs.utf_8_decode(x)[0]


@contextmanager
def deferral():
    """Defers a function call when it is being required.
    ::
       with deferral() as defer:
           sys.setprofile(f)
           defer(sys.setprofile, None)
           # do something.
    """
    deferred = []
    defer = lambda func, *args, **kwargs: deferred.append(
        (func, args, kwargs))
    try:
        yield defer
    finally:
        while deferred:
            func, args, kwargs = deferred.pop()
            func(*args, **kwargs)

import datetime
import logging
import logging.config
import os
import os.path
import re
import sys

from ..compat import fspath
from ..utils import ensure_dir_exists
from ..utils import get_path_infos
from .vars import _colored_tags
from .vars import _tags
from .vars import FAIL
from .vars import SUCCESS


class PzFileHandler(logging.FileHandler):
    """FileHandler with dynamic log path creation"""

    def __init__(self, filename, mode='a', encoding='utf-8', delay=False):
        filename = _set_log_path(filename)
        super(PzFileHandler, self).__init__(filename, mode, encoding, delay)

    def _open(self):
        log_dir = os.path.dirname(os.path.abspath(self.baseFilename))
        ensure_dir_exists(log_dir, mode=0o600)
        return open(self.baseFilename, self.mode, encoding=self.encoding)


class PzTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    """TimedRotatingFileHandler with dynamic log path creation"""

    def __init__(self, filename, when='midnight', interval=1, backupCount=31,
                 encoding=None, delay=False, utc=False,
                 suffix=None, extMatch=None, **kwargs):

        filename = _set_log_path(filename)
        super(PzTimedRotatingFileHandler, self).__init__(
            filename, when, interval, backupCount, encoding, delay, utc,
            **kwargs
        )

        # Allow user to set how time-rotating filename suffix looks like
        if isinstance(suffix, str) and isinstance(extMatch, str):
            self.suffix = suffix
            self.extMatch = re.compile(extMatch)

    def _open(self):
        log_dir = os.path.dirname(os.path.abspath(self.baseFilename))
        ensure_dir_exists(log_dir, mode=0o600)
        return open(self.baseFilename, self.mode, encoding=self.encoding)


class PzStreamFormatter(logging.Formatter):
    """Subclass to add ability to use colors and custom record attributes"""

    def __init__(self, fmt=None, datefmt=None, colored=True,
                 tracebacks=False):
        self.formatter = logging.Formatter(fmt, datefmt)
        self.used_tags = _colored_tags if colored else _tags
        self.tracebacks = tracebacks

    def format(self, record):

        # Ensure that original record is not impacted by these modifications
        new_record = logging.makeLogRecord(vars(record))

        # Shortens the level name (add colors if required)
        new_record.levelname = self.used_tags[new_record.levelno]

        # Avoid duplicated traceback on console
        if new_record.exc_info and not self.tracebacks:
            new_record.exc_info = None

        return self.formatter.format(new_record)


class PzLogger(logging.getLoggerClass()):
    """Subclass from Logger to add custom logging level methods"""

    def fail(self, msg, *args, **kwargs):
        if self.isEnabledFor(FAIL):
            self._log(FAIL, msg, args, **kwargs)

    def success(self, msg, *args, **kwargs):
        if self.isEnabledFor(SUCCESS):
            self._log(SUCCESS, msg, args, **kwargs)


def _set_log_path(log_path):

    log_path = fspath(log_path)

    if '%(script_name)s' in log_path:
        script_file = _get_default_log_path(today_suffix=False)
        script_name = get_path_infos(script_file).stem
        log_path = log_path.replace('%(script_name)s', script_name)

    if '%(date)s' in log_path:
        date = datetime.datetime.now().strftime('%Y%m%d')
        log_path = log_path.replace('%(date)s', date)

    return log_path


def _get_default_log_path(today_suffix=True):
    """Define default logger's file path relative to main script directory
       rather than current working directory
    """

    # Extract main script path directory and filename (without extension)
    # Main script directory is preferable over current working directory
    script = sys.modules['__main__'].__file__

    script_infos = get_path_infos(script)
    script_dir, script_name = script_infos.parent, script_infos.stem

    # Avoid modifying python install directory
    if script_dir.lower().startswith(sys.exec_prefix.lower()):
        script_dir = os.getcwd()
        script_name = __package__.split('.')[0]

    return os.path.join(script_dir, 'logs', script_name + '.log')


# Register the new logger and add custom logging levels
logging.setLoggerClass(PzLogger)
logging.addLevelName(FAIL, 'FAIL')
logging.addLevelName(SUCCESS, 'SUCCESS')

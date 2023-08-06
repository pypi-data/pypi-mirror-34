import logging
import logging.config
import warnings

import colorama

# Allows imports from pyzzy.logs.XXXX (useful for configuration files)
from logging import getLogger
from .core import PzFileHandler
from .core import PzStreamFormatter
from .core import PzTimedRotatingFileHandler

# Logging configuration handling
from ..data import load, dump
from ..utils import is_file
from .vars import DEFAULT_CONFIG


__all__ = [
    "getLogger",
    "PzFileHandler",
    "PzStreamFormatter",
    "PzTimedRotatingFileHandler",
    "init_logger",
    "load_config",
    "dump_config",
]


colorama.init()


def init_logger(name, config=True, captureWarnings=True, raiseExceptions=False):
    """Load (or not) a logging configuration and create the logger

    Parameters
    ----------
    name (None, str) :
        Name used to identify the logger
        Same name used by `logging.getLogger(name=None)`
    config (True, dict, PathLike) :
        Configuration to load before the logger creation
        If config is True, DEFAULT_CONFIG will be loaded
    """

    if config:
        load_config(config, captureWarnings, raiseExceptions)

    return logging.getLogger(name)


def load_config(config=None, captureWarnings=True, raiseExceptions=False):
    """Load logging configuration from user or default configuration"""

    if config is True or not config:
        config = DEFAULT_CONFIG

    # config can be loaded from files handled by pyzzy.data
    if config and is_file(config):
        config = load(config)

    try:
        logging.config.dictConfig(config)
    except (ValueError, TypeError, AttributeError, ImportError) as exc:
        warnings.warn(str(exc))
        logging.config.dictConfig(DEFAULT_CONFIG)

    logging.captureWarnings(captureWarnings)
    if captureWarnings:
        warnings.formatwarning = _logging_format_warning

    # Should be true for development, false in production
    logging.raiseExceptions = raiseExceptions


def dump_config(target, config=None):
    """Dump logging configuration from user or default configuration"""
    dump(config or DEFAULT_CONFIG, target, silent_fail=False)


def _simple_format_warning(message, category, filename, lineno, **kwargs):
    return "%s:%s [%s] %s\n" % (
        __name__,
        lineno,
        category.__name__,
        str(message),
    )


def _logging_format_warning(message, *args, **kwargs):
    return str(message)


warnings.formatwarning = _simple_format_warning

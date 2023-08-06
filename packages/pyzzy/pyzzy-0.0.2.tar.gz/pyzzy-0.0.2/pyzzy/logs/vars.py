from colorama import Back as AnsiBack
from colorama import Fore as AnsiFore
from colorama import Style as AnsiStyle

from ..data import load_json


def _set_tag(text, color):
    """Create tags with colors and format like [LEVL]"""

    # Some levels have specific brackets color else gray color
    brackets_color = {
        'CRIT': 'LIGHTRED_EX',
        'ERRO': 'LIGHTRED_EX',
        'WARN': 'LIGHTYELLOW_EX',
    }.get(text, 'LIGHTBLACK_EX')

    return '{}{}{}'.format(
        _fg_colorize('[', brackets_color),
        _fg_colorize(text, color),
        _fg_colorize(']', brackets_color)
    )


def _fg_colorize(text, color):
    """Wrap string with ANSI color codes"""

    return '{}{}{}'.format(
        getattr(AnsiFore, color, AnsiFore.WHITE),
        text,
        AnsiStyle.RESET_ALL
    )


CRITICAL = 50  # Serious problem, program may be unable to continue running
ERROR = 40  # Serious problem, program not been able to perform some function
WARNING = 30  # Something unexpected happened, program is still working as expected
FAIL = 22  # Similar to WARNING but for checks or tests
SUCCESS = 21  # Similar to INFO but for checks or tests
INFO = 20  # Confirmation that things are working as expected
DEBUG = 10  # Detailed information for diagnosing problems


_colored_tags = {
    CRITICAL: _set_tag('CRIT', 'LIGHTRED_EX'),
    ERROR: _set_tag('ERRO', 'LIGHTRED_EX'),
    WARNING: _set_tag('WARN', 'LIGHTYELLOW_EX'),
    FAIL: _set_tag('FAIL', 'LIGHTYELLOW_EX'),
    SUCCESS: _set_tag('PASS', 'LIGHTGREEN_EX'),
    INFO: _set_tag('INFO', 'LIGHTBLUE_EX'),
    DEBUG: _set_tag('DBUG', 'LIGHTBLACK_EX')
}

_tags = {
    CRITICAL: '[CRIT]',
    ERROR: '[ERRO]',
    WARNING: '[WARN]',
    FAIL: '[FAIL]',
    SUCCESS: '[PASS]',
    INFO: '[INFO]',
    DEBUG: '[DBUG]'
}


DEFAULT_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "console": {
            "()": "pyzzy.logs.PzStreamFormatter",
            "datefmt": "%Y-%m-%d_%H:%M:%S",
            "format": "%(levelname)-6s %(message)s",
            "colored": True,
            "tracebacks": False,
        },
        "file": {
            "datefmt": "%Y-%m-%d_%H:%M:%S",
            "format": (
                "%(asctime)s:%(msecs)-03.0f - %(levelname)-8s"
                " - %(name)-10.10s - %(module)10.10s:%(lineno)03d"
                " :: %(message)s"
            ),
        },
    },

    "handlers": {
        "console_prod": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "console",
        },
        "console_dev": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "console",
        },
        "file": {
            "()": "pyzzy.logs.PzFileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "logs/%(script_name)s_%(date)s.log",
            "mode": "a",
            "encoding": "utf-8",
            "delay": True,
        },
        "tr_file": {
            "()": "pyzzy.logs.PzTimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "logs/%(script_name)s.log",
            "when": "midnight",
            "interval": 1,
            "backupCount": 90,
            "encoding": "utf-8",
            "delay": True,
            "utc": False,
            "suffix": "%Y%m%d%H%M%S.log",
            "extMatch": "^\\d{8}([-_]?\\d{2,6})?(\\.\\w+)?$",
        },
    },

    "loggers": {
        "console": {
            "propagate": False,
            "level": "DEBUG",
            "handlers": ["console_dev"],
        },
        "file": {
            "propagate": False,
            "level": "DEBUG",
            "handlers": ["file"],
        },
        "tr_file": {
            "propagate": False,
            "level": "DEBUG",
            "handlers": ["tr_file"],
        },
        "production": {
            "propagate": False,
            "level": "DEBUG",
            "handlers": ["console_prod", "tr_file"],
        },
        "development": {
            "propagate": False,
            "level": "DEBUG",
            "handlers": ["console_dev", "file"],
        },
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["console_prod", "tr_file"],
    },
}

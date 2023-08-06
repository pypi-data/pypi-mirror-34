import collections
import configparser

from ..utils import open_stream, identity
from . import defaults

__all__ = ["dump_conf", "load_conf", "conf2dict"]


def dump_conf(data, target=None, **settings):

    settings = settings or defaults.conf
    parser = _conf_factory(settings)

    with open_stream(target, mode="w+", encoding="utf-8") as stream:
        parser.read_dict(data)
        parser.write(stream)
        stream.seek(0)
        data_dump = stream.read()

    return data_dump


def load_conf(source, **settings):

    settings = settings or defaults.conf
    parser = _conf_factory(settings)

    with open_stream(source, mode="r", encoding="utf-8") as stream:
        parser.read_file(stream)

    return parser


def conf2dict(conf, include_default=True, factory=None):

    factory = factory or collections.OrderedDict
    conf_dict = factory()

    for section_name in conf:

        if section_name == configparser.DEFAULTSECT and not include_default:
            continue

        section = conf[section_name]
        conf_dict[section_name] = factory(
            (key, section.get(key, raw=False))
            for key in section
            if not _in_defaults(conf, section_name, key)
        )

    return conf_dict


def _conf_factory(settings):

    # By default, each option name are converted in lowercase by python
    # If no optionxform is given, identity avoid option name modifications
    optionxform = settings.pop("optionxform", identity)
    optionxform = optionxform if callable else identity

    parser = configparser.ConfigParser(**settings)
    parser.optionxform = optionxform

    return parser


def _in_defaults(conf, section, key):
    if configparser.DEFAULTSECT not in conf:
        return False

    return (
        section != "DEFAULT"
        and key in conf["DEFAULT"]
        and conf["DEFAULT"][key] == conf[section][key]
    )

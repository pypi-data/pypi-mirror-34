from ..compat import fspath

from .io_conf import dump_conf, load_conf
from .io_json import dump_json, load_json
from .io_raw import dump_raw, load_raw
from .io_toml import dump_toml, load_toml
from .io_yaml import dump_yaml, load_yaml


__all__ = [
    "dump",
    "dump_conf",
    "dump_json",
    "dump_raw",
    "dump_toml",
    "dump_yaml",
    "load",
    "load_conf",
    "load_json",
    "load_raw",
    "load_toml",
    "load_yaml",
]


dumpers = {
    "cfg": dump_conf,
    "conf": dump_conf,
    "ini": dump_conf,
    "json": dump_json,
    "toml": dump_toml,
    "yaml": dump_yaml,
    "yml": dump_yaml,
}

loaders = {
    "cfg": load_conf,
    "conf": load_conf,
    "ini": load_conf,
    "json": load_json,
    "toml": load_toml,
    "yaml": load_yaml,
    "yml": load_yaml,
}


def dump(data, file_path, **settings):
    """Dump data based on the file extension"""

    # Avoid errors with Path objects
    file_path = fspath(file_path)

    # Normalize the file extension
    file_ext = file_path.rsplit(".", 1)[-1].lower()

    # Get the appropriate dumper based on file extension
    dump_data = dumpers.get(file_ext, dump_raw)

    return dump_data(data, file_path, **settings)


def load(file_path, **settings):
    """Load data based on the file extension"""

    # Avoid errors with Path objects
    file_path = fspath(file_path)

    # Normalize the file extension
    file_ext = file_path.rsplit(".", 1)[-1].lower()

    # Get the appropriate loader based on file extension
    load_data = loaders.get(file_ext, load_raw)

    return load_data(file_path, **settings)

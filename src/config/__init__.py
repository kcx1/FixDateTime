import pathlib
import os
from typing import Any

try:
    import tomllib  # Preferred lib
except ImportError as err:
    raise SystemExit(err)
except ModuleNotFoundError as err:  # ModuleNotFoundError
    raise SystemExit(err)


builtin_path = pathlib.Path(__file__).parent / "config.toml"

# Try to use XDG_CONFIG_HOME for config
default_path = pathlib.Path(os.environ.get("XDG_CONFIG_HOME", pathlib.Path.home())) / "FixDateTime.toml"


def import_config(config_path: pathlib.Path = default_path) -> dict[str, Any]:
    # Use config_path; if not provided, use default_path. 
    if not default_path.exists():
        # If default_path doesn't exist, copy builtin_path into it.
        default_path.touch()
        default_path.write_text(builtin_path.read_text())

    with config_path.open(mode="rb") as toml:
        config: dict[str, Any] = tomllib.load(toml)
        return config

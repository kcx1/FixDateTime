import pathlib
from typing import Any

try:
    import tomllib  # Preferred lib
except ImportError as err:
    raise SystemExit(err)
except ModuleNotFoundError as err:  # ModuleNotFoundError
    raise SystemExit(err)


builtin_path = pathlib.Path(__file__).parent / "config.toml"
default_path = pathlib.Path.home() / "config.toml"



def import_config(config_path: pathlib.Path = builtin_path) -> dict[str, Any]:
    # Use provided config, fallback to default, or fallback to built-in if the others do not exist.
    if config_path == builtin_path and default_path.exists():
        config_path = default_path

    with config_path.open(mode="rb") as toml:
        config: dict[str, Any] = tomllib.load(toml)
        return config

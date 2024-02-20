import pandas as pd
from datetime import datetime
from typing import Generator

import argparse
from pathlib import Path

from config import import_config

class TermColors:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    GRAY = "\033[90m"
    END = "\033[0m"


parser = argparse.ArgumentParser(
    prog="Fix Date / Time", 
    description="Command line tool to fix date/time in an excel file.",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

parser.add_argument(
    "files",
    nargs="+",
    action="store",
    type=Path,
    metavar="path/to/file.xlsx",
    help="Space separated list of files that you would like to fix date/time in. Tip: use quotes to help prevent splitting",
)

parser.add_argument(
    "--config",
    "-c",
    nargs="?",
    type=Path,
    action="store",
    help="Specify the path to a custom config file: config.toml",
)


args = parser.parse_args()


CONFIG = import_config()["config"]


def fix_date_time(value: str) -> str:
    """Fix the datetime format using the format declared in the config file"""
    try:
        date = datetime.strptime(value, CONFIG["in_format"])
        return date.strftime(CONFIG["out_format"])
    except ValueError as e:
        print(f"Oops, {e}! Not modifying the field.")
        return value


def iterate_files(files: list[Path]) -> Generator[Path, None, None]:
    """Iterate over command line provided files and yield them"""
    try:
        for file in files:
            yield file

    except FileNotFoundError as e:
        print(f"Oops, {e.filename} does not exist!")


def fix_column(df: pd.DataFrame) -> pd.DataFrame:
    """For each column, iterate over the rows and fix date/time and return the modified dataframe"""
    try:
        for col in CONFIG["columns"]:
            for row in range(len(df.index)):
                df.loc[row, col] = fix_date_time(df[col][row])
    except KeyError as e:
        print(f"Oops, The column: {e} does not exist!")

    return df


def main() -> None:
    for file in iterate_files(args.files):
        fix_column(pd.read_excel(file)).to_excel(file, index=False)
        print(f"{file} date/time fixed!")


if __name__ == "__main__":
    main()

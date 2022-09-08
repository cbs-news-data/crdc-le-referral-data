"""
Performs necessary transformations on CRDC data files

Transforms data from its original one-row-per-school format
to one row per category per school
"""

import argparse
import sys
from typing import Union
import pandas as pd
import yaml
import pandera as pa

# shared constants
INDEX_COLS = ["combokey", "lea_state", "lea_name", "sch_name", "jj"]
# dropping all LEP and 504 related columns because they don't
# have detailed enough data on those kids
DROP_COLS = ["tot_", "lea_state_name", "leaid", "schid", "lep", "504"]

RESERVE_CODES = {
    -3: "Skip logic failure",
    -5: "Action plan",
    -6: "Force certified",
    -8: "EDFacts missing data",
    -9: "Not applicable / skipped",
    -11: "Suppressed data",
}

REPLACE_VALUES = {
    "race": {
        "hi": "hispanic",
        "am": "american indian/alaskan native",
        "as": "asian",
        "hp": "native hawaiian/pacific islander",
        "bl": "black",
        "wh": "white",
        "tr": "two or more races",
    },
    "sex": {"f": "female", "m": "male"},
}

# from https://github.com/python/cpython/blob/main/Lib/distutils/util.py
def strtobool(val: any) -> bool:
    """
    Converts a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True

    if val in ("n", "no", "f", "false", "off", "0"):
        return False

    raise ValueError(f"invalid truth value {val}")


def load_yaml(path: str) -> Union[dict, list]:
    """loads data from yaml"""

    with open(path, "r", encoding="utf-8") as yaml_file:
        return yaml.load(yaml_file, Loader=yaml.CLoader)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
    )
    parser.add_argument(
        "variable_replace_values_yaml",
        type=str,
        help="path to yaml file containing values to replace variables with",
    )
    parser.add_argument(
        "value_col", type=str, help="name of column to rename values column to"
    )
    parser.add_argument(
        "--drop_cols_kwds_yaml",
        "-d",
        type=str,
        help="path to yaml file containing keywords to identify columns to drop",
        default=None,
    )
    parser.add_argument("--header", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    # setup schema based on provided column name
    schema = pa.DataFrameSchema(
        columns={
            "combokey": pa.Column(dtype=str),
            "lea_state": pa.Column(dtype=str),
            "lea_name": pa.Column(dtype=str),
            "sch_name": pa.Column(dtype=str),
            "jj": pa.Column(dtype=bool, nullable=False, unique=False),
            "variable": pa.Column(
                dtype=str,
                checks=[
                    pa.Check.isin(
                        [
                            "overall",
                            "without disabilities",
                            "idea",
                        ]
                    )
                ],
            ),
            "race": pa.Column(
                dtype=str,
                checks=[
                    pa.Check.isin(
                        [
                            "hispanic",
                            "american indian/alaskan native",
                            "asian",
                            "native hawaiian/pacific islander",
                            "black",
                            "white",
                            "two or more races",
                        ]
                    )
                ],
            ),
            "sex": pa.Column(dtype=str, checks=[pa.Check.isin(["female", "male"])]),
            args.value_col: pa.Column(
                dtype=int, checks=[pa.Check.greater_than_or_equal_to(0)]
            ),
        }
    )

    # load yaml files
    variable_replace_values = load_yaml(args.variable_replace_values_yaml)

    if args.drop_cols_kwds_yaml is None:
        drop_cols_kwds = {}
    else:
        drop_cols_kwds = load_yaml(args.drop_cols_kwds_yaml)

    print(
        pd.read_csv(args.infile, dtype={"COMBOKEY": str})
        .rename(columns=lambda col: col.lower())
        # parse "JJ" yes/no column to python boolean
        .assign(
            jj=lambda df: df.jj.apply(
                lambda val: bool(strtobool(val)) if pd.notna(val) else val
            )
        )
        # set index to shared columns and drop unwanted columns
        .set_index(INDEX_COLS)
        .pipe(
            lambda df: df.drop(
                [c for c in df.columns if any(kwd in c for kwd in DROP_COLS)], axis=1
            )
        )
        # drop total columns
        .pipe(
            lambda df: df.drop(
                [c for c in df.columns if any(kwd in c for kwd in drop_cols_kwds)],
                axis=1,
            )
        )
        # melt dataframe to one row per variable, preserving index
        .melt(ignore_index=False)
        # split the variable field on underscores
        .pipe(
            lambda df: df.variable.str.split("_", expand=True)
            .iloc[:, 1:]
            .rename(columns={1: "variable", 2: "race", 3: "sex"})
            .assign(value=lambda _: df.value)
        )
        # replace values from constants
        .replace(REPLACE_VALUES)
        # replace variables from yaml
        .replace({"variable": variable_replace_values})
        # drop any rows contianing reserve codes
        .pipe(lambda df: df[~(df.value.isin(RESERVE_CODES.keys()))])
        # rename value column from parameter
        .rename(columns={"value": args.value_col})
        .reset_index()
        .pipe(schema)
        .to_csv(index=False, line_terminator="\n", header=args.header)
    )

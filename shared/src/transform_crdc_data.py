"""
Performs necessary transformations on CRDC data files

Transforms data from its original one-row-per-school format
to one row per category per school
"""

import argparse
import sys
import pandas as pd

# import pandera as pa

# constants
RESERVE_CODES = {
    -3: "Skip logic failure",
    -5: "Action plan",
    -6: "Force certified",
    -8: "EDFacts missing data",
    -9: "Not applicable / skipped",
    -11: "Suppressed data",
}

REPLACE_VALUES = {
    "variable": {
        "enr": "overall",
        "lepenr": "limited_english_proficient",
        "lepprogenr": "enrolled_in_lep_program",
        "ideaenr": "idea",
        "504enr": "sec_504",
    }
}

DROP_COLS_PATTERNS = [r"^tot_", r"_psenr_"]

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
    )
    parser.add_argument(
        "value_col", type=str, help="name of column to rename values column to"
    )
    parser.add_argument(
        "outfile", nargs="?", type=argparse.FileType("w"), default=sys.stdout
    )
    args = parser.parse_args()

    # with open("hand/replace_vals", "r", encoding="utf-8") as yaml_file:
    #     replace_vals = yaml.load(yaml_file, Loader=yaml.CLoader)

    print(
        pd.read_csv(args.infile)
        .rename(columns=lambda col: col.lower())
        # parse "JJ" yes/no column to python boolean
        .assign(
            jj=lambda df: df.jj.apply(
                lambda val: bool(strtobool(val)) if pd.notna(val) else val
            )
        )
        # set index to shared columns and drop unwanted columns
        .set_index(["combokey", "lea_state", "lea_name", "sch_name", "jj"])
        .drop(["lea_state_name", "leaid", "schid"], axis=1)
        # drop total columns
        .pipe(
            lambda df: df.drop(
                # TODO: parametrize the columns to drop
                [c for c in df.columns if c.startswith("tot") or "psenr" in c],
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
        # .replace(REPLACE_VALUES)
        # drop any rows contianing reserve codes
        .pipe(lambda df: df[~(df.value.isin(RESERVE_CODES.keys()))])
        # rename value column from parameter
        .rename(columns={"value": args.value_col})
        .to_csv(line_terminator="\n")
    )

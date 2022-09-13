"""performs specific transformations on school characteristics file"""

import sys
import pandas as pd

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


def all_cols_to_bool(df: pd.DataFrame) -> pd.DataFrame:
    """applies strtobool to all columns"""
    for col in df.columns:
        df[col] = df[col].apply(strtobool)
    return df


print(
    pd.read_csv(sys.argv[1])
    .rename(columns=lambda col: col.lower())[
        [
            "combokey",
            "sch_name",
            "lea_name",
            "lea_state_name",
            "jj",
            "sch_grade_g01",
            "sch_grade_g02",
            "sch_grade_g03",
            "sch_grade_g04",
            "sch_grade_g05",
            "sch_grade_g06",
            "sch_grade_g07",
            "sch_grade_g08",
            "sch_grade_g09",
            "sch_grade_g10",
            "sch_grade_g11",
            "sch_grade_g12",
        ]
    ]
    # convert state names to title case
    .assign(lea_state_name=lambda df: df.lea_state_name.str.title())
    .set_index(
        [
            "combokey",
            "sch_name",
            "lea_name",
            "lea_state_name",
            "jj",
        ]
    )
    .pipe(all_cols_to_bool)
    .to_csv(line_terminator="\n")
)

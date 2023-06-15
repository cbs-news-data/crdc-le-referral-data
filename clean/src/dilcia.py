import argparse
import logging
import re
import numpy as np
import pandas as pd
from tqdm import tqdm
import constants

logging.basicConfig(
    filename="output/clean_crdc_data.log", filemode="w", level=logging.INFO
)


def drop_reserve_codes(df: pd.DataFrame) -> pd.DataFrame:
    """drops reserve codes from the dataframe"""
    return (
        df.set_index(constants.TEXT_COLS).pipe(lambda d: d.mask(d.lt(0))).reset_index()
    )  # is this where you mask the negative numbers?


# going through script line by line to make sure I understand the code & filters
def get_max_grade(df: pd.DataFrame) -> pd.DataFrame:
    """gets the max grade from the grade range"""

    def get_grade_for_row(row):
        true_cols = [
            (k, v) for k, v in row.items() if k in constants.GRADE_COLS and v == "Yes"
        ]
        if len(true_cols) == 0:
            return np.NaN
        return int(re.search(r"(?<=SCH_GRADE_G)\d{1,2}$", true_cols[-1][0]).group())

    return df.assign(max_grade=df.apply(get_grade_for_row, axis=1)).drop(
        constants.GRADE_COLS, axis=1
    )


def select_cols(df: pd.DataFrame) -> pd.DataFrame:
    """selects columns from the dataframe"""
    return df.set_index([c for c in df.columns if c in constants.TEXT_COLS])[
        [c for c in df.columns if c in constants.NUMERIC_COLS]
    ].reset_index()  # cols pulled from constants.py file


def preprocess_df(df: pd.DataFrame, year) -> pd.DataFrame:
    """preprocesses the dataframe"""
    return (
        df.pipe(select_cols)
        .pipe(drop_reserve_codes)
        .pipe(get_max_grade)
        # .pipe(drop_duplicates_keep_most_complete)
        # .assign(year=year)
    )


def read_stack_dfs(*filenames) -> pd.DataFrame:
    """reads and stacks the dataframes"""
    dfs = []
    counter = tqdm()
    for filename in filenames:
        counter.update(1)
        counter.set_description(f"Cleaning {filename}")

        match filename:
            case str():  # don't totally understand this line # is this to distinguish between reading in one file & reading in many?
                dfs.append(
                    preprocess_df(
                        # read_file(filename),
                        # get_school_year(filename),
                    )
                )

    #         case tuple() | list():
    #             dfs.append(
    #                 preprocess_df(
    #                     read_segmented_dfs(*filename), get_school_year(filename[0])
    #                 )
    #             )

    #         case _:
    #             raise ValueError(f"unknown filename type {type(filename)}")

    # return pd.concat(dfs)


def main(*input_files, output_file):
    (read_stack_dfs(*input_files))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year-files", "-f", nargs="+", action="append", required=True)
    parser.add_argument("--output-file", "-o", required=True)
    args = parser.parse_args()

    main(*args.year_files, output_file=args.output_file)

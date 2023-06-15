import argparse
import logging
import re
import numpy as np
import pandas as pd
from tqdm import tqdm
import constants

# going through script line by line to make sure I understand the code & filters


logging.basicConfig(
    filename="output/clean_crdc_data.log", filemode="w", level=logging.INFO
)


def read_file(file_path: str) -> pd.DataFrame:
    """Reads a file and returns a dataframe"""
    if file_path.endswith(".csv") or file_path.endswith(".csv.gz"):
        return pd.read_csv(file_path, encoding="latin-1", low_memory=False)
    if file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    raise ValueError("File type not supported")


def drop_reserve_codes(df: pd.DataFrame) -> pd.DataFrame:
    """drops reserve codes from the dataframe"""
    return (
        df.set_index(constants.TEXT_COLS).pipe(lambda d: d.mask(d.lt(0))).reset_index()
    )  # is this where you mask the negative numbers?


def get_school_year(school_year: str) -> int:
    """gets the year from the school year"""
    school_match = re.search(r"\d{4}-\d{2}", school_year)
    if school_match:
        return int(school_match.group()[:4])

    school_match = re.search(r"\d{4}", school_year)
    if school_match:
        return int("20" + school_match.group()[:2])

    raise ValueError(f"couldn't extract school year from {school_year}")


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


def drop_duplicates_keep_most_complete(df: pd.DataFrame) -> pd.DataFrame:
    """drops duplicates and keeps the most complete row"""
    return (
        df.assign(
            completeness_score=lambda df: df.apply(
                lambda row: sum(1 for key in row.index if pd.notna(row[key])), axis=1
            )
        )
        .sort_values("completeness_score", ascending=False)
        .drop_duplicates(subset=["LEAID", "SCHID"], keep="first")
        .drop("completeness_score", axis=1)
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
        .pipe(drop_duplicates_keep_most_complete)
        .assign(year=year)
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
                        read_file(filename),
                        get_school_year(filename),
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

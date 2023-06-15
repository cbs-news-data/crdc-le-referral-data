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

# going through script line by line to make sure I understand the code & filters


def main(*input_files, output_file):
    # some code
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year-files", "-f", nargs="+", action="append", required=True)
    parser.add_argument("--output-file", "-o", required=True)
    args = parser.parse_args()

    main(*args.year_files, output_file=args.output_file)

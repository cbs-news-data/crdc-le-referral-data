"""separates referral and arrest data so they can be handled separately"""

import sys
import pandas as pd
from transform_crdc_data import INDEX_COLS

REF = "--referrals" in sys.argv
ARR = "--arrests" in sys.argv

args = [REF is not False, ARR is not False]
assert any(args) and not all(args), "one of --referrals or --arrests must be provided"
KWD = "_REF_" if REF is True else "_ARR_"

print(
    pd.read_csv(sys.argv[1], encoding="latin")
    # select only the necessary columns
    .pipe(
        lambda df: df[
            [col for col in df.columns if col.lower() in INDEX_COLS or KWD in col]
        ]
    )
    # drop the keyword from each column
    .rename(columns=lambda col: col.replace(KWD, "_"))
    # drop "discwdis" so it's replaced with IDEA/504 indication
    .pipe(lambda df: df.rename(columns=lambda col: col.replace("_DISCWDIS_", "_")))
    # write output
    .to_csv(index=False, line_terminator="\n", encoding="utf-8")
)

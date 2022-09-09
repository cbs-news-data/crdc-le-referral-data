"""
fixes variable names for section 504 variables that
don't conform to the var_race_sex format
"""

import sys
import re
import pandas as pd

print(
    pd.read_csv(sys.stdin)
    .rename(
        columns=lambda col: re.sub(
            r"(?<=_504_)(?=[MF])",
            "_",
            col,
        )
    )
    .to_csv(index=False)
)

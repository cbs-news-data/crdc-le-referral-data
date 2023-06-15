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

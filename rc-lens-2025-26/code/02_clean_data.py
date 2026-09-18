"""
02_clean_data.py
Milestone 2 (Wk 2-3)

Load data/raw/, clean it (types, missing values, consistent team and
player names), and save match/team-level CSVs to data/processed/.
"""
from os import path

import numpy as np
import pandas as pd

# run scripts from the project root so these relative paths work
DATA_DIR = './data'
RAW_DIR = path.join(DATA_DIR, 'raw')
PROCESSED_DIR = path.join(DATA_DIR, 'processed')
FIG_DIR = './figures'

# TODO: write your code here (get it working simple first, then put it in functions)

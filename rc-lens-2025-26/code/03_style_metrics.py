"""
03_style_metrics.py
Milestone 2 (Wk 2-3)

Load data/processed/ and engineer the style-of-play metrics per team
(possession %, PPDA, directness, pressing). Also season avg/min/max.
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

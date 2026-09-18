"""
01_collect_data.py
Milestone 1 (Wk 1)

Pull RC Lens 2025-26 data (StatsBomb / FBref) and save it as CSVs in data/raw/.
Also define the style-of-play metrics you plan to calculate
(possession %, PPDA, directness, pressing).
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

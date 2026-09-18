"""
05_dashboard.py
Milestone 4 (Wk 5-6)

Team Performance dashboard (standings, avg stats, min/max), Style of Play
dashboard, and a post-match report view for one team.
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

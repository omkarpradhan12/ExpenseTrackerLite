import pandas as pd
import os
from pathlib import Path


paths = sorted(Path('../CSV').iterdir(), key=os.path.getmtime)
files = [os.path.basename(pth) for pth in paths]


def get_dfs():
    dfs = {}
    for f in files:
        dfs[f] = pd.read_csv('../CSV/'+f)
        dfs[f]['Category'] = dfs[f]['Category'].str.capitalize().str.strip()

    return [files,dfs]


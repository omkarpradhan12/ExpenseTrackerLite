import pandas as pd
import os
from pathlib import Path


folder_path = "../CSV"
paths = sorted(Path(folder_path).iterdir(), key=os.path.getmtime)
files = [os.path.basename(pth) for pth in paths]


def get_dfs():
    dfs = {}
    for f in files:
        try:
            dfs[f] = pd.read_csv(folder_path+f)
            dfs[f]['Category'] = dfs[f]['Category'].str.capitalize().str.strip()
        except Exception:
            print("Error reading file: " + f)

    return [files,dfs]


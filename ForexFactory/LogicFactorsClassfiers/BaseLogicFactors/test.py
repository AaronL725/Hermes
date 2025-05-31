import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from BaseLogicFactors.baselogicfactors import BaseLogicFactors


def load_HOLCVO(level):
    script_dir = os.path.dirname(__file__)
    relative_data_path = os.path.join(script_dir, f"../../FutureData/{level}")
    path = os.path.abspath(relative_data_path)
    high = pd.read_csv(os.path.join(path,"high.csv"),index_col=[0])
    open = pd.read_csv(os.path.join(path,"open.csv"),index_col=[0])
    low = pd.read_csv(os.path.join(path,"low.csv"),index_col=[0])
    close = pd.read_csv(os.path.join(path,"close.csv"),index_col=[0])
    vol = pd.read_csv(os.path.join(path,"vol.csv"),index_col=[0])
    oi = pd.read_csv(os.path.join(path,"oi.csv"),index_col=[0])
    return high,open,low,close,vol,oi


if __name__=='__main__':
    level = 'min60'

    high,open,low,close,vol,oi = load_HOLCVO(level)
    BaseLogicFactors.CMO(high.to_numpy(dtype='float64'),open.to_numpy(dtype='float64'),low.to_numpy(dtype='float64'),close.to_numpy(dtype='float64'),vol.to_numpy(dtype='float64'),oi.to_numpy(dtype='float64'))




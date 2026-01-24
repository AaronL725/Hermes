import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from BaseLogicFactors.baselogicfactors import BaseLogicFactors
from Mining.data_cache import load_HOLCVO_cached


def load_HOLCVO(level):
    return load_HOLCVO_cached(level)


if __name__=='__main__':
    level = 'min60'

    high,open,low,close,vol,oi = load_HOLCVO(level)
    BaseLogicFactors.CMO(high.to_numpy(dtype='float64'),open.to_numpy(dtype='float64'),low.to_numpy(dtype='float64'),close.to_numpy(dtype='float64'),vol.to_numpy(dtype='float64'),oi.to_numpy(dtype='float64'))




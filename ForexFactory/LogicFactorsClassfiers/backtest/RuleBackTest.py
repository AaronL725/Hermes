import numpy as np
import numba as nb
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



@nb.jit(nopython=True, fastmath=True, cache=True)
def RunRuleBackTest(close,pctchg,limit,opensignal,closesignal,ifdaychange,maxium_day_holding=5):
    CLOSE_BY_CLOSESIGNAL = 1
    CLOSE_BY_TIME = 2

    tdts,secs = close.shape
    Holding = []
    ClosedHolding = []
    PorfolioPctchg = []
    for ts in range(tdts):
        
        _PorfolioPctchg = 0
        _PorfolioPctchgNum = 0
        if len(Holding)>0:
            for _h in Holding:
                _sec = int(_h[0])  # 确保索引为整数类型
                if  pctchg[ts,_sec]== pctchg[ts,_sec]:
                    _PorfolioPctchgNum+=1
                    _PorfolioPctchg += pctchg[ts,_sec] 
                if ifdaychange[ts]==1:
                    _h[2] +=1
        if _PorfolioPctchgNum==0:
            PorfolioPctchg.append(np.nan)
        else:
            PorfolioPctchg.append(_PorfolioPctchg/_PorfolioPctchgNum)
        for sec in range(secs):


            _opensignal = opensignal[ts,sec]
            _closesignal = closesignal[ts,sec]
            if _opensignal == 1 and close[ts,sec]==close[ts,sec]:
                Holding.append([float(sec),float(ts),0.0])  # 统一使用float64类型

            elif _closesignal == 1 and close[ts,sec]==close[ts,sec]:
                # 使用倒序遍历避免在循环中修改列表导致的问题
                for i in range(len(Holding)-1, -1, -1):
                    _h = Holding[i]
                    if int(_h[0])==sec:  # 确保比较时类型一致
                        Holding.pop(i)
                        _h.append(float(ts))  # 统一使用float64类型
                        _h.append(close[ts,sec]/close[int(_h[1]),sec]-1)    
                        _h.append(float(CLOSE_BY_CLOSESIGNAL))  # 统一使用float64类型
                        ClosedHolding.append(_h)
                            
        # 使用倒序遍历处理超过最大持有天数的持仓
        for i in range(len(Holding)-1, -1, -1):
            _h = Holding[i]
            if _h[2]>=maxium_day_holding:
                _sec = int(_h[0])  # 确保索引为整数类型
                if close[ts,_sec] == close[ts,_sec]:
                    Holding.pop(i)
                    _h.append(float(ts))  # 统一使用float64类型
                    _h.append(close[ts,_sec]/close[int(_h[1]),_sec]-1)    
                    _h.append(float(CLOSE_BY_TIME))  # 统一使用float64类型
                    ClosedHolding.append(_h)

    return Holding,ClosedHolding,PorfolioPctchg
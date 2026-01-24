import numpy as np
import numba as nb
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



@nb.jit
def RunRuleBackTest(close,pctchg,limit,opensignal,closesignal,ifdaychange,maxium_day_holding=5):
    CLOSE_BY_CLOSESIGNAL = 1
    CLOSE_BY_TIME = 2

    tdts,secs = close.shape

    # Initialize lists with a template element to inform Numba of their type, then pop it.
    # This is necessary because Numba's type inference fails on empty lists in this context.
    Holding = [[0.0, 0.0, 0.0]]
    Holding.pop()
    
    # A closed holding has 6 elements: [sec, open_ts, holding_days, close_ts, pct_chg, close_type]
    ClosedHolding = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
    ClosedHolding.pop()

    # The portfolio percentage change is a single float.
    PorfolioPctchg = [0.0]
    PorfolioPctchg.pop()

    for ts in range(tdts):
        
        _PorfolioPctchg = 0
        _PorfolioPctchgNum = 0
        if len(Holding)>0:
            for _h in Holding:
                _sec = int(_h[0])
                if  pctchg[ts,_sec]== pctchg[ts,_sec]:
                    _PorfolioPctchgNum+=1
                    _PorfolioPctchg += pctchg[ts,_sec] 
                if ifdaychange[ts]==1:
                    _h[2] +=1
        if _PorfolioPctchgNum==0:
            PorfolioPctchg.append(np.nan)
        else:
            PorfolioPctchg.append(_PorfolioPctchg/_PorfolioPctchgNum)

        # --- Start of Refactored Section ---
        
        # Initialize with a template like the main 'Holding' list to ensure type stability
        _next_Holding = [[0.0, 0.0, 0.0]]
        _next_Holding.pop()
        
        # First, iterate through existing holdings to check for close signals or time-based exits.
        for _h in Holding:
            _sec = int(_h[0])
            is_closed = False

            # Check for signal-based close
            if closesignal[ts, _sec] == 1 and close[ts, _sec] == close[ts, _sec]:
                closed_item = _h + [float(ts), close[ts, _sec] / close[int(_h[1]), _sec] - 1, float(CLOSE_BY_CLOSESIGNAL)]
                ClosedHolding.append(closed_item)
                is_closed = True
            
            # Check for time-based close (only if not already closed by signal)
            if not is_closed and _h[2] >= maxium_day_holding:
                if close[ts, _sec] == close[ts, _sec]:
                    closed_item = _h + [float(ts), close[ts, _sec] / close[int(_h[1]), _sec] - 1, float(CLOSE_BY_TIME)]
                    ClosedHolding.append(closed_item)
                    is_closed = True

            # If the holding was not closed, carry it over to the next time step.
            if not is_closed:
                _next_Holding.append(_h)

        # Second, check for new open signals for the current time step and add them.
        for sec in range(secs):
            if opensignal[ts, sec] == 1 and close[ts, sec] == close[ts, sec]:
                _next_Holding.append([float(sec), float(ts), float(0)])
        
        # Replace the old Holding list with the newly constructed one.
        Holding = _next_Holding
        # --- End of Refactored Section ---

    return Holding,ClosedHolding,PorfolioPctchg

import numba as nb
import numpy as np
from operators import *

@nb.njit
def getavailabledata(target,length):
    new_target = [np.nan]*length
    new_index = 0
    for i in range(len(target)-1,-1,-1):
        if target[i]==target[i]:
            new_index+=1
            if new_index>length:
                break
            new_target[-new_index] = target[i]
    return np.array(new_target)


class BaseLogicFactors:

    __doc__ = '''
            deepseek生成的常用因子
            '''


    @staticmethod
    @nb.njit
    def BIAS(high,open,low,close,vol,oi,N=6):
        '''Bias Ratio (BIAS)，用于衡量收盘价与移动平均线之间的偏离程度，判断市场超买或超卖状态'''
        tdts, secs = high.shape
        Tfactors = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts <=N or close[ts,sec]!=close[ts,sec]:
                    continue

                
                _high = high[:ts + 1, sec]
                _open = open[:ts + 1, sec]
                _low = low[:ts + 1, sec]
                _close = close[:ts + 1, sec]
                _vol = vol[:ts + 1, sec]
                _oi = oi[:ts + 1, sec]

                myopen = getavailabledata(_open, N)
                myhigh = getavailabledata(_high, N)
                myclose = getavailabledata(_close, N)
                mylow = getavailabledata(_low, N)
                myvol = getavailabledata(_vol, N)
                myoi = getavailabledata(_oi,N+1)
                _maN = ROLLING_MEAN(myclose,N)
                
                _Tfactor = (myclose[-1] - _maN[-1])/_maN[-1]  * 100
                Tfactors[ts, sec] = _Tfactor
        return Tfactors


    @staticmethod
    @nb.njit
    def VolPriceCorr(high,open,low,close,vol,oi,N=20):
        '''Volume-Price Correlation (VolPriceCorr)，用于分析成交量与价格之间的相关性，判断量价配合程度'''
        tdts, secs = high.shape
        Tfactors = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts <=N or close[ts,sec]!=close[ts,sec]:
                    continue

                
                _high = high[:ts + 1, sec]
                _open = open[:ts + 1, sec]
                _low = low[:ts + 1, sec]
                _close = close[:ts + 1, sec]
                _vol = vol[:ts + 1, sec]
                _oi = oi[:ts + 1, sec]

                myopen = getavailabledata(_open, N)
                myhigh = getavailabledata(_high, N)
                myclose = getavailabledata(_close, N)
                mylow = getavailabledata(_low, N)
                myvol = getavailabledata(_vol, N)
                myoi = getavailabledata(_oi,N)
                
                _Tfactor = CORR(myclose,myvol)
                Tfactors[ts, sec] = _Tfactor
        return Tfactors


    @staticmethod
    @nb.njit
    def KDJ(high,open,low,close,vol,oi,N=9,m1=3,m2=3):
        '''Stochastic Oscillator (KDJ)，用于判断价格的超买或超卖状态'''
        tdts, secs = high.shape
        k = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        d = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        j = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts <=N or close[ts,sec]!=close[ts,sec]:
                    continue

                
                _high = high[:ts + 1, sec]
                _open = open[:ts + 1, sec]
                _low = low[:ts + 1, sec]
                _close = close[:ts + 1, sec]
                _vol = vol[:ts + 1, sec]
                _oi = oi[:ts + 1, sec]

                _N = N*3 if ts>=N*3 else ts

                myopen = getavailabledata(_open,_N)
                myhigh = getavailabledata(_high,_N)
                myclose = getavailabledata(_close, _N)
                mylow = getavailabledata(_low, _N)
                myvol = getavailabledata(_vol, _N)
                myoi = getavailabledata(_oi,_N)

                rsv = (myclose-TSMIN(mylow,N))/(TSMAX(myhigh,N)-TSMIN(mylow,N)) * 100
                _k = ROLLING_EWM(rsv,2/(m1+1))
                _d = ROLLING_EWM(_k,2/(m2+1))
                _j = 3*_k - 2*_d
                k[ts,sec] = _k [-1]
                d[ts,sec]  = _d[-1]
                j[ts,sec] = _j[-1]               
        return k,d,j
    
        
    @staticmethod
    @nb.njit
    def ADX2(high,open,low,close,vol,oi,N=14):
        '''Average Directional Index (ADX) - Alternative Implementation，用于衡量趋势的强弱'''
        tdts, secs = high.shape
        adx = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts <=N or close[ts,sec]!=close[ts,sec]:
                    continue
                _high = high[:ts + 1, sec]
                _open = open[:ts + 1, sec]
                _low = low[:ts + 1, sec]
                _close = close[:ts + 1, sec]
                _vol = vol[:ts + 1, sec]
                _oi = oi[:ts + 1, sec]

                _N = N*3 if ts>=N*3 else ts
                myopen = getavailabledata(_open,_N)
                myhigh = getavailabledata(_high,_N)
                myclose = getavailabledata(_close, _N)
                mylow = getavailabledata(_low, _N)
                myvol = getavailabledata(_vol,_N)
                myoi = getavailabledata(_oi,_N)
                
                tr1 = myhigh - mylow
                tr2 = ABS(myhigh - DELAY(myclose,1))
                tr3 = ABS(mylow - DELAY(myclose, 1))
                tr = TSMAX(TSMAX(tr1, tr2), tr3)

                prev_low = DELAY(mylow,1)
                prev_high = DELAY(myhigh, 1)
                dm_plus = myhigh - prev_high
                dm_minus = prev_low - mylow
                
                dm_plus_new = np.array([np.nan]*len(dm_plus))
                for i in range(len(dm_plus)):
                    cond1 = dm_plus[i] > np.abs(mylow[i]-prev_low[i])
                    cond2 = dm_plus[i] > 0
                    if cond1 and cond2:
                        dm_plus_new[i] = dm_plus[i]
                    else:
                        dm_plus_new[i] = 0
                dm_minus_new = np.array([np.nan]*len(dm_minus))
                for i in range(len(dm_minus)):
                    cond1 = dm_minus[i] > np.abs(myhigh[i]-prev_high[i])
                    cond2 = dm_minus[i] > 0
                    if cond1 and cond2:
                        dm_minus_new[i] = dm_minus[i]
                    else:
                        dm_minus_new[i] = 0

                tr_ewm = ROLLING_MEAN(tr,N)
                dm_plus_ewm = ROLLING_MEAN(dm_plus_new,N)
                dm_minus_ewm = ROLLING_MEAN(dm_minus_new,N)
                
                di_plus = dm_plus_ewm/tr_ewm * 100
                di_minus = dm_minus_ewm/tr_ewm * 100

                dx = (di_plus - di_minus)/(di_plus + di_minus) * 100
                _adx = ROLLING_MEAN(dx,N)[-1]

                adx[ts,sec] =_adx
        return   adx


    @staticmethod
    @nb.njit
    def AD(high, open, low, close, vol, oi):
        """
        AD - Chaikin A/D Line
        
        # AD指标（钱德动量摆动指标）是由Marc Chaikin开发的，用于衡量资金流入和流出的指标
        # 计算方法：((收盘价-最低价)-(最高价-收盘价))/(最高价-最低价) * 成交量，然后累加
        # 用途：判断价格趋势与交易量的关系，预测价格变动
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        
        for sec in range(secs):
            ad = 0.0
            for ts in range(tdts):
                if not np.isnan(high[ts,sec]) and not np.isnan(low[ts,sec]) and not np.isnan(close[ts,sec]) and not np.isnan(vol[ts,sec]):
                    # 直接使用当前值计算
                    tmp = high[ts,sec] - low[ts,sec]
                    if tmp > 0.0:
                        ad += (((close[ts,sec]-low[ts,sec])-(high[ts,sec]-close[ts,sec]))/tmp)*vol[ts,sec]
                result[ts,sec] = ad
        
        return result
    

    @staticmethod
    @nb.njit
    def ATR(high, open, low, close, vol, oi, timeperiod=14):
        """
        # ATR - Average True Range
        # 平均真实范围是以下三者中的最大值:
        # val1 = 当日最高价与当日最低价之差
        # val2 = 前一日收盘价与当日最高价之差的绝对值
        # val3 = 前一日收盘价与当日最低价之差的绝对值
        # 使用Wilder方法对指定周期内的这些值进行平均，该方法有一个与指数移动平均线(EMA)相当的不稳定期。
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        
        for sec in range(secs):
            # 精确模拟TA-Lib的数据处理方式
            
            # 步骤1: 创建有效数据的掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
            
            # 步骤2: 创建连续数据序列（没有NaN）
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
            valid_indices = np.where(valid_mask)[0]
            
            # 如果没有足够的有效数据，跳过
            if len(valid_high) <= timeperiod:
                continue
            
            # 步骤3: 计算所有TR值
            tr_values = np.zeros(len(valid_high))
            # 第一个点的TR只能用高-低
            tr_values[0] = valid_high[0] - valid_low[0]
            
            # 计算剩余点的TR
            for i in range(1, len(valid_high)):
                tr_1 = valid_high[i] - valid_low[i]
                tr_2 = abs(valid_close[i-1] - valid_high[i])
                tr_3 = abs(valid_close[i-1] - valid_low[i])
                tr_values[i] = max(tr_1, tr_2, tr_3)
            
            # 步骤4: 计算ATR
            atr_values = np.zeros(len(valid_high))
            # ATR的第一个值是前timeperiod个TR的简单平均
            if timeperiod <= 1:
                # 对于timeperiod=1的情况，ATR就是TR
                atr_values = tr_values
            else:
                # 计算第一个ATR（等于前timeperiod个TR的简单平均）
                first_atr = 0.0
                for i in range(timeperiod):
                    first_atr += tr_values[i]
                first_atr /= timeperiod
                atr_values[timeperiod-1] = first_atr
                
                # 使用Wilder平滑公式计算其余ATR值
                for i in range(timeperiod, len(tr_values)):
                    atr_values[i] = (atr_values[i-1] * (timeperiod-1) + tr_values[i]) / timeperiod
            
            # 步骤5: 将结果映射回原始数组
            # TA-Lib从第timeperiod个点开始输出ATR
            start_idx = timeperiod - 1 if timeperiod > 1 else 0
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = atr_values[i]
        
        return result
    

    @staticmethod
    @nb.njit
    def ADOSC(high, open, low, close, vol, oi, fast_period=3, slow_period=10):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)

        # Determine the slowest period for lookback
        if fast_period < slow_period:
            slowest_period = slow_period
        else:
            slowest_period = fast_period
            
        # Approximation of EMA lookback
        lookback_total = slowest_period - 1
        
        for sec in range(secs):
            # Check if we have enough valid data
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec] and
                    vol[i, sec] == vol[i, sec]):
                    valid_mask[i] = True
                    
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
                
            # Get valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
            valid_vol = vol[valid_mask, sec]
            
            # Initialize AD value and EMAs
            ad = 0.0
            fast_k = 2.0 / (fast_period + 1.0)
            one_minus_fast_k = 1.0 - fast_k
            slow_k = 2.0 / (slow_period + 1.0)
            one_minus_slow_k = 1.0 - slow_k
            
            # Calculate first AD value and initialize EMAs
            today = 0
            h = valid_high[today]
            l = valid_low[today]
            tmp = h - l
            c = valid_close[today]
            if tmp > 0.0:
                ad += (((c - l) - (h - c)) / tmp) * valid_vol[today]
            today += 1
            
            fast_ema = ad
            slow_ema = ad
            
            # Warm-up period calculation - calculate EMAs but don't output results
            while today < lookback_total:
                h = valid_high[today]
                l = valid_low[today]
                tmp = h - l
                c = valid_close[today]
                if tmp > 0.0:
                    ad += (((c - l) - (h - c)) / tmp) * valid_vol[today]
                
                fast_ema = (fast_k * ad) + (one_minus_fast_k * fast_ema)
                slow_ema = (slow_k * ad) + (one_minus_slow_k * slow_ema)
                today += 1
            
            # Main calculation loop - calculate and output results
            out_idx = 0
            while today < len(valid_high):
                h = valid_high[today]
                l = valid_low[today]
                tmp = h - l
                c = valid_close[today]
                if tmp > 0.0:
                    ad += (((c - l) - (h - c)) / tmp) * valid_vol[today]
                
                fast_ema = (fast_k * ad) + (one_minus_fast_k * fast_ema)
                slow_ema = (slow_k * ad) + (one_minus_slow_k * slow_ema)
                
                # Store result at original index position
                result[valid_indices[lookback_total + out_idx], sec] = fast_ema - slow_ema
                out_idx += 1
                today += 1

        return result
    

    @staticmethod
    @nb.njit
    def ADX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        
        # 使用TA-Lib默认的不稳定期参数，通常为25
        unstable_period = 25
        lookback_total = (2 * timeperiod) + unstable_period - 1

        for sec in range(secs):
            if tdts <= lookback_total:
                continue

            # 初始化变量
            prev_minus_dm = 0.0
            prev_plus_dm = 0.0
            prev_tr = 0.0
            
            # 设置起始日期
            today = lookback_total
            
            # 确保数据有效
            if (today < tdts and 
                high[today - lookback_total, sec] == high[today - lookback_total, sec] and
                low[today - lookback_total, sec] == low[today - lookback_total, sec] and
                close[today - lookback_total, sec] == close[today - lookback_total, sec]):
                
                prev_high = high[today - lookback_total, sec]
                prev_low = low[today - lookback_total, sec]
                prev_close = close[today - lookback_total, sec]
                
                # 第一个循环：初始化MinusDM、PlusDM和TR的累计值
                i = timeperiod - 1
                today_idx = today - lookback_total
                while i > 0 and today_idx + 1 < tdts:
                    today_idx += 1
                    
                    # 确保数据有效
                    if (high[today_idx, sec] != high[today_idx, sec] or
                        low[today_idx, sec] != low[today_idx, sec] or
                        close[today_idx, sec] != close[today_idx, sec]):
                        continue
                    
                    temp_real = high[today_idx, sec]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                    
                    temp_real = low[today_idx, sec]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                    
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
                    elif diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm += diff_p
                    
                    # True Range计算
                    tr = max(prev_high - prev_low, 
                            max(abs(prev_high - prev_close), abs(prev_low - prev_close)))
                    prev_tr += tr
                    prev_close = close[today_idx, sec]
                    i -= 1
                
                # 第二个循环：计算sumDX的初始值
                sum_dx = 0.0
                i = timeperiod
                while i > 0 and today_idx + 1 < tdts:
                    today_idx += 1
                    
                    # 确保数据有效
                    if (high[today_idx, sec] != high[today_idx, sec] or
                        low[today_idx, sec] != low[today_idx, sec] or
                        close[today_idx, sec] != close[today_idx, sec]):
                        continue
                    
                    temp_real = high[today_idx, sec]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                    
                    temp_real = low[today_idx, sec]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                    
                    prev_minus_dm -= prev_minus_dm / timeperiod
                    prev_plus_dm -= prev_plus_dm / timeperiod
                    
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
                    elif diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm += diff_p
                    
                    # True Range计算
                    tr = max(prev_high - prev_low, 
                            max(abs(prev_high - prev_close), abs(prev_low - prev_close)))
                    prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                    prev_close = close[today_idx, sec]
                    
                    # 注意：使用更精确的零值检测
                    if prev_tr > 1e-10:
                        minus_di = 100.0 * (prev_minus_dm / prev_tr)
                        plus_di = 100.0 * (prev_plus_dm / prev_tr)
                        temp_real = minus_di + plus_di
                        if temp_real > 1e-10:
                            sum_dx += 100.0 * (abs(minus_di - plus_di) / temp_real)
                    i -= 1
                
                # 计算初始ADX值
                prev_adx = sum_dx / timeperiod
                
                # 第三个循环：处理不稳定期
                i = unstable_period
                while i > 0 and today_idx + 1 < tdts:
                    today_idx += 1
                    
                    # 确保数据有效
                    if (high[today_idx, sec] != high[today_idx, sec] or
                        low[today_idx, sec] != low[today_idx, sec] or
                        close[today_idx, sec] != close[today_idx, sec]):
                        continue
                    
                    temp_real = high[today_idx, sec]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                    
                    temp_real = low[today_idx, sec]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                    
                    prev_minus_dm -= prev_minus_dm / timeperiod
                    prev_plus_dm -= prev_plus_dm / timeperiod
                    
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
                    elif diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm += diff_p
                    
                    # True Range计算
                    tr = max(prev_high - prev_low, 
                            max(abs(prev_high - prev_close), abs(prev_low - prev_close)))
                    prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                    prev_close = close[today_idx, sec]
                    
                    if prev_tr > 1e-10:
                        minus_di = 100.0 * (prev_minus_dm / prev_tr)
                        plus_di = 100.0 * (prev_plus_dm / prev_tr)
                        temp_real = minus_di + plus_di
                        if temp_real > 1e-10:
                            temp_real = 100.0 * (abs(minus_di - plus_di) / temp_real)
                            prev_adx = ((prev_adx * (timeperiod - 1)) + temp_real) / timeperiod
                    i -= 1
                
                # 记录第一个有效输出
                out_idx = today_idx
                if out_idx < tdts:
                    result[out_idx, sec] = prev_adx
                
                # 主循环：计算和记录剩余的ADX值
                while today_idx + 1 < tdts:
                    today_idx += 1
                    
                    # 确保数据有效
                    if (high[today_idx, sec] != high[today_idx, sec] or
                        low[today_idx, sec] != low[today_idx, sec] or
                        close[today_idx, sec] != close[today_idx, sec]):
                        continue
                    
                    temp_real = high[today_idx, sec]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                    
                    temp_real = low[today_idx, sec]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                    
                    prev_minus_dm -= prev_minus_dm / timeperiod
                    prev_plus_dm -= prev_plus_dm / timeperiod
                    
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
                    elif diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm += diff_p
                    
                    # True Range计算
                    tr = max(prev_high - prev_low, 
                            max(abs(prev_high - prev_close), abs(prev_low - prev_close)))
                    prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                    prev_close = close[today_idx, sec]
                    
                    if prev_tr > 1e-10:
                        minus_di = 100.0 * (prev_minus_dm / prev_tr)
                        plus_di = 100.0 * (prev_plus_dm / prev_tr)
                        temp_real = minus_di + plus_di
                        if temp_real > 1e-10:
                            temp_real = 100.0 * (abs(minus_di - plus_di) / temp_real)
                            prev_adx = ((prev_adx * (timeperiod - 1)) + temp_real) / timeperiod
                    
                    result[today_idx, sec] = prev_adx

        return result
    

    @staticmethod
    @nb.njit
    def ADXR(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
            
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= (2 * timeperiod) + 24:  # 需要足够数据(ADX lookback + timeperiod - 1)
                continue
                
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
            
            # 计算ADX (基于baselogicfactors中ADX函数逻辑)
            adx_values = np.zeros(len(valid_high))
            
            # 初始化变量
            prev_minus_dm = 0.0
            prev_plus_dm = 0.0
            prev_tr = 0.0
            prev_adx = 0.0
            unstable_period = 25  # TA-Lib默认不稳定期
            
            # 处理第一个点的初始化
            prev_high = valid_high[0]
            prev_low = valid_low[0]
            prev_close = valid_close[0]
            
            # 第一个循环：初始化MinusDM、PlusDM和TR的累计值
            sum_dm_plus = 0.0
            sum_dm_minus = 0.0
            sum_tr = 0.0
            
            for i in range(1, timeperiod):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                
                if diff_m > 0 and diff_p < diff_m:
                    sum_dm_minus += diff_m
                elif diff_p > 0 and diff_p > diff_m:
                    sum_dm_plus += diff_p
                
                # True Range计算
                tr = max(valid_high[i] - valid_low[i], 
                        max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                sum_tr += tr
                prev_close = valid_close[i]
            
            # 初始化EMA值
            prev_plus_dm = sum_dm_plus
            prev_minus_dm = sum_dm_minus
            prev_tr = sum_tr
            
            # 第二个循环：计算sumDX的初始值
            sum_dx = 0.0
            for i in range(timeperiod, 2*timeperiod):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                
                prev_minus_dm -= prev_minus_dm / timeperiod
                prev_plus_dm -= prev_plus_dm / timeperiod
                
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm += diff_m
                elif diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm += diff_p
                
                # True Range计算
                tr = max(valid_high[i] - valid_low[i], 
                        max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                prev_close = valid_close[i]
                
                # 注意：使用更精确的零值检测
                if prev_tr > 1e-10:
                    minus_di = 100.0 * (prev_minus_dm / prev_tr)
                    plus_di = 100.0 * (prev_plus_dm / prev_tr)
                    temp_real = minus_di + plus_di
                    if temp_real > 1e-10:
                        sum_dx += 100.0 * (abs(minus_di - plus_di) / temp_real)
            
            # 计算初始ADX值
            prev_adx = sum_dx / timeperiod
            
            # 第三个循环：处理不稳定期
            for i in range(2*timeperiod, 2*timeperiod + unstable_period):
                if i >= len(valid_high):
                    break
                    
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                
                prev_minus_dm -= prev_minus_dm / timeperiod
                prev_plus_dm -= prev_plus_dm / timeperiod
                
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm += diff_m
                elif diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm += diff_p
                
                # True Range计算
                tr = max(valid_high[i] - valid_low[i], 
                        max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                prev_close = valid_close[i]
                
                if prev_tr > 1e-10:
                    minus_di = 100.0 * (prev_minus_dm / prev_tr)
                    plus_di = 100.0 * (prev_plus_dm / prev_tr)
                    temp_real = minus_di + plus_di
                    if temp_real > 1e-10:
                        temp_real = 100.0 * (abs(minus_di - plus_di) / temp_real)
                        prev_adx = ((prev_adx * (timeperiod - 1)) + temp_real) / timeperiod
                
                adx_values[i] = prev_adx
            
            # 主循环：计算和记录剩余的ADX值
            start_idx = 2*timeperiod + unstable_period
            for i in range(start_idx, len(valid_high)):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                
                prev_minus_dm -= prev_minus_dm / timeperiod
                prev_plus_dm -= prev_plus_dm / timeperiod
                
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm += diff_m
                elif diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm += diff_p
                
                # True Range计算
                tr = max(valid_high[i] - valid_low[i], 
                        max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                prev_close = valid_close[i]
                
                if prev_tr > 1e-10:
                    minus_di = 100.0 * (prev_minus_dm / prev_tr)
                    plus_di = 100.0 * (prev_plus_dm / prev_tr)
                    temp_real = minus_di + plus_di
                    if temp_real > 1e-10:
                        temp_real = 100.0 * (abs(minus_di - plus_di) / temp_real)
                        prev_adx = ((prev_adx * (timeperiod - 1)) + temp_real) / timeperiod
                
                adx_values[i] = prev_adx
            
            # 计算ADXR值: (当前ADX + 前(timeperiod)日的ADX)/2
            adxr_values = np.zeros(len(valid_high))
            for i in range(timeperiod - 1, len(valid_high)):
                if i >= timeperiod + start_idx - 1:  # 确保有前期ADX值可用
                    adxr_values[i] = (adx_values[i] + adx_values[i - (timeperiod - 1)]) / 2.0
            
            # 映射结果回原始数组
            for i in range(len(valid_indices)):
                if i >= timeperiod + start_idx - 1:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = adxr_values[i]

        return result
    

    @staticmethod
    @nb.njit
    def APO(high, open, low, close, vol, oi, fastperiod=12, slowperiod=26, matype=0):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < max(fastperiod, slowperiod):
                continue
            
            # 提取有效数据
            valid_close = close[valid_mask, sec]
        
            # 确保fastperiod小于slowperiod，与C源码逻辑一致
            actual_fastperiod = fastperiod
            actual_slowperiod = slowperiod
            if slowperiod < fastperiod:
                actual_fastperiod = slowperiod
                actual_slowperiod = fastperiod
        
            # 计算快速移动平均
            fast_ma = np.zeros(len(valid_close))
            if matype == 0:  # SMA
                for i in range(actual_fastperiod - 1, len(valid_close)):
                    sum_val = 0.0
                    count = 0
                    for j in range(i - actual_fastperiod + 1, i + 1):
                        if valid_close[j] == valid_close[j]:
                            sum_val += valid_close[j]
                            count += 1
                    if count > 0:
                        fast_ma[i] = sum_val / actual_fastperiod
            else:
                # 其他MA类型可以扩展，这里默认使用SMA
                for i in range(actual_fastperiod - 1, len(valid_close)):
                    sum_val = 0.0
                    count = 0
                    for j in range(i - actual_fastperiod + 1, i + 1):
                        if valid_close[j] == valid_close[j]:
                            sum_val += valid_close[j]
                            count += 1
                    if count > 0:
                        fast_ma[i] = sum_val / actual_fastperiod
        
            # 计算慢速移动平均
            slow_ma = np.zeros(len(valid_close))
            if matype == 0:  # SMA
                for i in range(actual_slowperiod - 1, len(valid_close)):
                    sum_val = 0.0
                    count = 0
                    for j in range(i - actual_slowperiod + 1, i + 1):
                        if valid_close[j] == valid_close[j]:
                            sum_val += valid_close[j]
                            count += 1
                    if count > 0:
                        slow_ma[i] = sum_val / actual_slowperiod
            else:
                # 其他MA类型可以扩展，这里默认使用SMA
                for i in range(actual_slowperiod - 1, len(valid_close)):
                    sum_val = 0.0
                    count = 0
                    for j in range(i - actual_slowperiod + 1, i + 1):
                        if valid_close[j] == valid_close[j]:
                            sum_val += valid_close[j]
                            count += 1
                    if count > 0:
                        slow_ma[i] = sum_val / actual_slowperiod
        
            # 计算APO值：快速MA - 慢速MA
            apo_values = np.zeros(len(valid_close))
            start_idx = actual_slowperiod - 1
            for i in range(start_idx, len(valid_close)):
                if fast_ma[i] == fast_ma[i] and slow_ma[i] == slow_ma[i]:
                    apo_values[i] = fast_ma[i] - slow_ma[i]
                else:
                    apo_values[i] = np.nan
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = apo_values[i]
    
        return result


    @staticmethod
    @nb.njit
    def AROONOSC(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # 初始化输出数组
            aroon_osc_values = np.zeros(len(valid_high))
        
            # 设置起始索引和滑动窗口
            start_idx = timeperiod
            factor = 100.0 / timeperiod
        
            # 主计算循环
            for today in range(start_idx, len(valid_high)):
                trailing_idx = today - timeperiod
                lowest_idx = -1
                highest_idx = -1
                lowest = 0.0
                highest = 0.0
            
                # 寻找最低点
                tmp = valid_low[today]
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_low[lowest_idx]
                    for i in range(lowest_idx + 1, today + 1):
                        tmp = valid_low[i]
                        if tmp <= lowest:
                            lowest_idx = i
                            lowest = tmp
                elif tmp <= lowest:
                    lowest_idx = today
                    lowest = tmp
                
                # 寻找最高点
                tmp = valid_high[today]
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_high[highest_idx]
                    for i in range(highest_idx + 1, today + 1):
                        tmp = valid_high[i]
                        if tmp >= highest:
                            highest_idx = i
                            highest = tmp
                elif tmp >= highest:
                    highest_idx = today
                    highest = tmp
                
                # 计算Aroon Oscillator值
                aroon_osc = factor * (highest_idx - lowest_idx)
                aroon_osc_values[today] = aroon_osc
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = aroon_osc_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def AVGPRICE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) == 0:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 计算AVGPRICE
            for i in range(len(valid_high)):
                avg_price = (valid_high[i] + valid_low[i] + valid_close[i] + valid_open[i]) / 4.0
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = avg_price
    
        return result



    @staticmethod
    @nb.njit
    def BBANDS(high, open, low, close, vol, oi, timeperiod=20, nbdevup=2.0, nbdevdn=2.0, matype=0):
        tdts, secs = close.shape
        result_upper = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_middle = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_lower = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # 提取有效数据
            valid_close = close[valid_mask, sec]
        
            # 计算移动平均线 (Middle Band)
            middle_band = np.zeros(len(valid_close))
            if matype == 0:  # SMA
                for i in range(timeperiod - 1, len(valid_close)):
                    window = valid_close[i - timeperiod + 1:i + 1]
                    middle_band[i] = np.mean(window[window == window])
            else:
                # 其他MA类型可以使用通用MA函数，这里简化为SMA逻辑
                for i in range(timeperiod - 1, len(valid_close)):
                    window = valid_close[i - timeperiod + 1:i + 1]
                    middle_band[i] = np.mean(window[window == window])
        
            # 计算标准差 (用于Upper和Lower Band)
            std_dev = np.zeros(len(valid_close))
            if matype == 0:  # SMA情况下使用预计算的MA优化标准差
                for i in range(timeperiod - 1, len(valid_close)):
                    window = valid_close[i - timeperiod + 1:i + 1]
                    mean_val = middle_band[i]
                    squared_diff_sum = 0.0
                    count = 0
                    for val in window:
                        if val == val:
                            squared_diff_sum += (val - mean_val) * (val - mean_val)
                            count += 1
                    if count > 0:
                        std_dev[i] = np.sqrt(squared_diff_sum / count)
            else:
                for i in range(timeperiod - 1, len(valid_close)):
                    window = valid_close[i - timeperiod + 1:i + 1]
                    valid_window = window[window == window]
                    if len(valid_window) > 0:
                        std_dev[i] = np.std(valid_window)
        
            # 计算Upper和Lower Band
            upper_band = np.zeros(len(valid_close))
            lower_band = np.zeros(len(valid_close))
            if nbdevup == nbdevdn:
                if nbdevup == 1.0:
                    for i in range(timeperiod - 1, len(valid_close)):
                        upper_band[i] = middle_band[i] + std_dev[i]
                        lower_band[i] = middle_band[i] - std_dev[i]
                else:
                    for i in range(timeperiod - 1, len(valid_close)):
                        temp_real = std_dev[i] * nbdevup
                        upper_band[i] = middle_band[i] + temp_real
                        lower_band[i] = middle_band[i] - temp_real
            elif nbdevup == 1.0:
                for i in range(timeperiod - 1, len(valid_close)):
                    temp_real = std_dev[i]
                    upper_band[i] = middle_band[i] + temp_real
                    lower_band[i] = middle_band[i] - (temp_real * nbdevdn)
            elif nbdevdn == 1.0:
                for i in range(timeperiod - 1, len(valid_close)):
                    temp_real = std_dev[i]
                    lower_band[i] = middle_band[i] - temp_real
                    upper_band[i] = middle_band[i] + (temp_real * nbdevup)
            else:
                for i in range(timeperiod - 1, len(valid_close)):
                    temp_real = std_dev[i]
                    upper_band[i] = middle_band[i] + (temp_real * nbdevup)
                    lower_band[i] = middle_band[i] - (temp_real * nbdevdn)
        
            # 映射结果回原始数组
            for i in range(len(valid_indices)):
                if i >= timeperiod - 1:
                    orig_idx = valid_indices[i]
                    result_upper[orig_idx, sec] = upper_band[i]
                    result_middle[orig_idx, sec] = middle_band[i]
                    result_lower[orig_idx, sec] = lower_band[i]
    
        return result_upper, result_middle, result_lower


    @staticmethod
    @nb.njit
    def BOP(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) == 0:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Calculate BOP values
            bop_values = np.zeros(len(valid_high))
            for i in range(len(valid_high)):
                temp_real = valid_high[i] - valid_low[i]
                if temp_real <= 0.0:
                    bop_values[i] = 0.0
                else:
                    bop_values[i] = (valid_close[i] - valid_open[i]) / temp_real
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = bop_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def CCI(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize circular buffer simulation
            lookback_total = timeperiod - 1
            start_idx = lookback_total if timeperiod > 1 else 0
        
            # Warm-up period: Fill initial buffer
            circ_buffer = np.zeros(timeperiod)
            circ_idx = 0
        
            if timeperiod > 1:
                for i in range(start_idx):
                    typical_price = (valid_high[i] + valid_low[i] + valid_close[i]) / 3.0
                    circ_buffer[circ_idx] = typical_price
                    circ_idx = (circ_idx + 1) % timeperiod
        
            # Main calculation loop
            for i in range(start_idx, len(valid_high)):
                # Calculate typical price for current bar
                last_value = (valid_high[i] + valid_low[i] + valid_close[i]) / 3.0
                circ_buffer[circ_idx] = last_value
            
                # Calculate mean of buffer
                the_average = 0.0
                for j in range(timeperiod):
                    the_average += circ_buffer[j]
                the_average /= timeperiod
            
                # Calculate mean absolute deviation
                temp_real2 = 0.0
                for j in range(timeperiod):
                    temp_real2 += abs(circ_buffer[j] - the_average)
            
                # Calculate CCI
                temp_real = last_value - the_average
                if temp_real != 0.0 and temp_real2 != 0.0:
                    cci_value = temp_real / (0.015 * (temp_real2 / timeperiod))
                else:
                    cci_value = 0.0
            
                # Map result back to original array
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = cci_value
            
                # Update circular buffer index
                circ_idx = (circ_idx + 1) % timeperiod
    
        return result



    @staticmethod
    @nb.njit
    def CDL2CROWS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (2 days for pattern + additional for BodyLong average)
        lookback_total = 2
        body_long_period = 10  # Default period for BodyLong average as per TA-Lib
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookback_total + body_long_period:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output for valid data
            temp_result = np.zeros(len(valid_high))
        
            # Initialize BodyLongPeriodTotal for trailing average
            body_long_period_total = 0.0
            body_long_trailing_idx = 0
        
            # Calculate initial sum for BodyLong average
            for i in range(body_long_period):
                if i < len(valid_high):
                    body_long_period_total += abs(valid_open[i] - valid_close[i])
        
            # Start processing from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Calculate candle color (1 for white/up, -1 for black/down)
                color_i2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_i1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_i = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate real body for i-2
                real_body_i2 = abs(valid_close[i-2] - valid_open[i-2])
            
                # Calculate BodyLong average
                body_long_average = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
            
                # Check if real body at i-2 is long
                is_body_long_i2 = real_body_i2 > body_long_average
            
                # Check if there is a gap up between i-2 and i-1
                is_gap_up = valid_open[i-1] > valid_close[i-2]
            
                # Check conditions for Two Crows pattern
                if (color_i2 == 1 and  # First candle is white (up)
                    is_body_long_i2 and  # First candle has long body
                    color_i1 == -1 and  # Second candle is black (down)
                    is_gap_up and  # Gap up between first and second candle
                    color_i == -1 and  # Third candle is black (down)
                    valid_open[i] < valid_open[i-1] and  # Third opens below second's open
                    valid_open[i] > valid_close[i-1] and  # Third opens above second's close
                    valid_close[i] > valid_open[i-2] and  # Third closes above first's open
                    valid_close[i] < valid_close[i-2]):  # Third closes below first's close
                    temp_result[i] = -100
                else:
                    temp_result[i] = 0
                
                # Update trailing sum for BodyLong average
                if i - 2 >= 0:
                    body_long_period_total += abs(valid_close[i-2] - valid_open[i-2])
                if body_long_trailing_idx < len(valid_high):
                    body_long_period_total -= abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
                    body_long_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDL3BLACKCROWS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        lookback_total = 3  # Lookback period for 3 Black Crows pattern
        shadow_very_short_period = 3  # Period for calculating average shadow, as per TA-Lib default

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue

            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]

            # Initialize arrays for shadow calculations
            shadow_very_short_period_total = np.zeros(3)
            shadow_very_short_trailing_idx = 0
            start_idx = lookback_total

            # Warm-up period for shadow averages
            if start_idx > shadow_very_short_period:
                shadow_very_short_trailing_idx = start_idx - shadow_very_short_period
            else:
                shadow_very_short_trailing_idx = 0

            i = shadow_very_short_trailing_idx
            while i < start_idx and i < len(valid_high):
                if i >= 2:
                    shadow_very_short_period_total[2] += valid_high[i-2] - valid_low[i-2]
                if i >= 1:
                    shadow_very_short_period_total[1] += valid_high[i-1] - valid_low[i-1]
                shadow_very_short_period_total[0] += valid_high[i] - valid_low[i]
                i += 1

            i = start_idx
            while i < len(valid_high):
                # Calculate candle colors (1 for white, -1 for black)
                color_3 = 1 if valid_close[i-3] > valid_open[i-3] else -1
                color_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1

                # Calculate lower shadows
                lower_shadow_2 = valid_open[i-2] - valid_low[i-2] if color_2 == 1 else valid_close[i-2] - valid_low[i-2]
                lower_shadow_1 = valid_open[i-1] - valid_low[i-1] if color_1 == 1 else valid_close[i-1] - valid_low[i-1]
                lower_shadow_0 = valid_open[i] - valid_low[i] if color_0 == 1 else valid_close[i] - valid_low[i]

                # Calculate shadow averages
                shadow_avg_2 = shadow_very_short_period_total[2] / shadow_very_short_period if shadow_very_short_period > 0 else 0
                shadow_avg_1 = shadow_very_short_period_total[1] / shadow_very_short_period if shadow_very_short_period > 0 else 0
                shadow_avg_0 = shadow_very_short_period_total[0] / shadow_very_short_period if shadow_very_short_period > 0 else 0

                # Check 3 Black Crows pattern conditions
                if (color_3 == 1 and
                    color_2 == -1 and
                    lower_shadow_2 < shadow_avg_2 and
                    color_1 == -1 and
                    lower_shadow_1 < shadow_avg_1 and
                    color_0 == -1 and
                    lower_shadow_0 < shadow_avg_0 and
                    valid_open[i-1] < valid_open[i-2] and valid_open[i-1] > valid_close[i-2] and
                    valid_open[i] < valid_open[i-1] and valid_open[i] > valid_close[i-1] and
                    valid_high[i-3] > valid_close[i-2] and
                    valid_close[i-2] > valid_close[i-1] and
                    valid_close[i-1] > valid_close[i]):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0

                # Update shadow totals for next iteration
                for tot_idx in range(2, -1, -1):
                    if i - tot_idx >= 0:
                        shadow_very_short_period_total[tot_idx] += valid_high[i - tot_idx] - valid_low[i - tot_idx]
                    if shadow_very_short_trailing_idx - tot_idx >= 0:
                        shadow_very_short_period_total[tot_idx] -= valid_high[shadow_very_short_trailing_idx - tot_idx] - valid_low[shadow_very_short_trailing_idx - tot_idx]

                i += 1
                shadow_very_short_trailing_idx += 1

        return result



    @staticmethod
    @nb.njit
    def CDL3INSIDE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback period as per TA-Lib (2 days prior for pattern recognition)
        lookback_total = 2
        body_long_period = 3  # Default period for long body average as per TA-Lib
        body_short_period = 3  # Default period for short body average as per TA-Lib
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing indices for body averages
            body_long_trailing_idx = 0
            body_short_trailing_idx = 0
        
            # Initialize totals for body averages
            body_long_period_total = 0.0
            body_short_period_total = 0.0
        
            # Calculate initial totals for body long average (i-2)
            for i in range(body_long_trailing_idx, min(body_long_period, len(valid_high))):
                if i + 2 < len(valid_high):
                    body_long_period_total += abs(valid_close[i] - valid_open[i])
        
            # Calculate initial totals for body short average (i-1)
            for i in range(body_short_trailing_idx, min(body_short_period, len(valid_high))):
                if i + 1 < len(valid_high):
                    body_short_period_total += abs(valid_close[i] - valid_open[i])
        
            # Start processing from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Calculate real body for i-2 and i-1
                real_body_i2 = abs(valid_close[i-2] - valid_open[i-2])
                real_body_i1 = abs(valid_close[i-1] - valid_open[i-1])
            
                # Calculate candle color for i-2 and i
                color_i2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_i = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate body averages
                body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
                body_short_avg = body_short_period_total / body_short_period if body_short_period > 0 else 0.0
            
                # Check for 3 Inside pattern conditions
                if (real_body_i2 > body_long_avg and
                    real_body_i1 <= body_short_avg and
                    max(valid_close[i-1], valid_open[i-1]) < max(valid_close[i-2], valid_open[i-2]) and
                    min(valid_close[i-1], valid_open[i-1]) > min(valid_close[i-2], valid_open[i-2]) and
                    ((color_i2 == 1 and color_i == -1 and valid_close[i] < valid_open[i-2]) or
                     (color_i2 == -1 and color_i == 1 and valid_close[i] > valid_open[i-2]))):
                    result[valid_indices[i], sec] = -color_i2 * 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update body totals for next iteration
                if i - 2 >= body_long_trailing_idx and i - 2 < len(valid_high):
                    body_long_period_total += abs(valid_close[i-2] - valid_open[i-2])
                    if body_long_trailing_idx < len(valid_high):
                        body_long_period_total -= abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
                    body_long_trailing_idx += 1
                
                if i - 1 >= body_short_trailing_idx and i - 1 < len(valid_high):
                    body_short_period_total += abs(valid_close[i-1] - valid_open[i-1])
                    if body_short_trailing_idx < len(valid_high):
                        body_short_period_total -= abs(valid_close[body_short_trailing_idx] - valid_open[body_short_trailing_idx])
                    body_short_trailing_idx += 1
                
        return result



    @staticmethod
    @nb.njit
    def CDL3LINESTRIKE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (3 prior candles needed)
        lookback_total = 3
        # Near period for candle range averaging, typically 14 in TA-Lib
        near_period = 14
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize NearPeriodTotal for averaging candle ranges
            near_period_total_3 = 0.0
            near_period_total_2 = 0.0
            near_trailing_idx = lookback_total - near_period
        
            # Warm-up period for NearPeriodTotal calculation
            i = near_trailing_idx if near_trailing_idx >= 0 else 0
            while i < lookback_total and i < len(valid_high):
                if i - 3 >= 0:
                    near_period_total_3 += valid_high[i - 3] - valid_low[i - 3]
                if i - 2 >= 0:
                    near_period_total_2 += valid_high[i - 2] - valid_low[i - 2]
                i += 1
        
            # Main calculation loop starting from lookback_total
            out_idx = lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Determine candle colors (1 for bullish, -1 for bearish)
                color_3 = 1 if valid_close[i - 3] > valid_open[i - 3] else -1
                color_2 = 1 if valid_close[i - 2] > valid_open[i - 2] else -1
                color_1 = 1 if valid_close[i - 1] > valid_open[i - 1] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate averages for Near period
                near_avg_3 = near_period_total_3 / near_period if near_period > 0 else 0.0
                near_avg_2 = near_period_total_2 / near_period if near_period > 0 else 0.0
            
                # Check for 3 Line Strike pattern
                if (color_3 == color_2 and 
                    color_2 == color_1 and 
                    color_0 == -color_1):
                    # Check open price conditions within range of previous candles
                    min_3 = min(valid_open[i - 3], valid_close[i - 3])
                    max_3 = max(valid_open[i - 3], valid_close[i - 3])
                    min_2 = min(valid_open[i - 2], valid_close[i - 2])
                    max_2 = max(valid_open[i - 2], valid_close[i - 2])
                
                    open_cond_2 = (valid_open[i - 2] >= min_3 - near_avg_3 and 
                                  valid_open[i - 2] <= max_3 + near_avg_3)
                    open_cond_1 = (valid_open[i - 1] >= min_2 - near_avg_2 and 
                                  valid_open[i - 1] <= max_2 + near_avg_2)
                
                    if open_cond_2 and open_cond_1:
                        if (color_1 == 1 and 
                            valid_close[i - 1] > valid_close[i - 2] and 
                            valid_close[i - 2] > valid_close[i - 3] and 
                            valid_open[i] > valid_close[i - 1] and 
                            valid_close[i] < valid_open[i - 3]):
                            result[valid_indices[i], sec] = 100
                        elif (color_1 == -1 and 
                              valid_close[i - 1] < valid_close[i - 2] and 
                              valid_close[i - 2] < valid_close[i - 3] and 
                              valid_open[i] < valid_close[i - 1] and 
                              valid_close[i] > valid_open[i - 3]):
                            result[valid_indices[i], sec] = -100
                        else:
                            result[valid_indices[i], sec] = 0
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update NearPeriodTotal for next iteration
                if i - 3 >= 0:
                    near_period_total_3 += (valid_high[i - 3] - valid_low[i - 3])
                if i - 2 >= 0:
                    near_period_total_2 += (valid_high[i - 2] - valid_low[i - 2])
                if near_trailing_idx - 3 >= 0:
                    near_period_total_3 -= (valid_high[near_trailing_idx - 3] - valid_low[near_trailing_idx - 3])
                if near_trailing_idx - 2 >= 0:
                    near_period_total_2 -= (valid_high[near_trailing_idx - 2] - valid_low[near_trailing_idx - 2])
                near_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDL3STARSINSOUTH(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        BodyLongPeriod = 10
        ShadowLongPeriod = 10
        ShadowVeryShortPeriod = 3
        BodyShortPeriod = 10
        lookbackTotal = max(BodyLongPeriod, ShadowLongPeriod, ShadowVeryShortPeriod, BodyShortPeriod) + 2
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for averages
            BodyLongPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal_0 = 0.0
            ShadowVeryShortPeriodTotal_1 = 0.0
            BodyShortPeriodTotal = 0.0
        
            # Calculate initial totals for averages
            BodyLongTrailingIdx = lookbackTotal - BodyLongPeriod
            ShadowLongTrailingIdx = lookbackTotal - ShadowLongPeriod
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
            BodyShortTrailingIdx = lookbackTotal - BodyShortPeriod
        
            for i in range(BodyLongTrailingIdx, lookbackTotal):
                BodyLongPeriodTotal += abs(valid_close[i-2] - valid_open[i-2])
            for i in range(ShadowLongTrailingIdx, lookbackTotal):
                ShadowLongPeriodTotal += max(0.0, valid_close[i-2] - valid_low[i-2]) if valid_close[i-2] >= valid_open[i-2] else max(0.0, valid_open[i-2] - valid_low[i-2])
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                ShadowVeryShortPeriodTotal_1 += max(0.0, valid_close[i-1] - valid_low[i-1]) if valid_close[i-1] >= valid_open[i-1] else max(0.0, valid_open[i-1] - valid_low[i-1])
                ShadowVeryShortPeriodTotal_0 += max(0.0, valid_close[i] - valid_low[i]) if valid_close[i] >= valid_open[i] else max(0.0, valid_open[i] - valid_low[i])
            for i in range(BodyShortTrailingIdx, lookbackTotal):
                BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # Main calculation loop
            for i in range(lookbackTotal, len(valid_high)):
                # Check for 3 Stars in the South pattern
                if (valid_close[i-2] < valid_open[i-2] and  # Bearish first candle
                    valid_close[i-1] < valid_open[i-1] and  # Bearish second candle
                    valid_close[i] < valid_open[i] and      # Bearish third candle
                    abs(valid_close[i-2] - valid_open[i-2]) > (BodyLongPeriodTotal / BodyLongPeriod) and  # Long body first candle
                    (valid_close[i-2] - valid_low[i-2] if valid_close[i-2] >= valid_open[i-2] else valid_open[i-2] - valid_low[i-2]) > (ShadowLongPeriodTotal / ShadowLongPeriod) and  # Long lower shadow first candle
                    abs(valid_close[i-1] - valid_open[i-1]) < abs(valid_close[i-2] - valid_open[i-2]) and  # Smaller body second candle
                    valid_open[i-1] > valid_close[i-2] and valid_open[i-1] <= valid_high[i-2] and  # Second candle opens above first close
                    valid_low[i-1] < valid_close[i-2] and valid_low[i-1] >= valid_low[i-2] and  # Second candle low within first candle range
                    (valid_close[i-1] - valid_low[i-1] if valid_close[i-1] >= valid_open[i-1] else valid_open[i-1] - valid_low[i-1]) > (ShadowVeryShortPeriodTotal_1 / ShadowVeryShortPeriod) and  # Long lower shadow second candle
                    abs(valid_close[i] - valid_open[i]) < (BodyShortPeriodTotal / BodyShortPeriod) and  # Short body third candle
                    (valid_close[i] - valid_low[i] if valid_close[i] >= valid_open[i] else valid_open[i] - valid_low[i]) < (ShadowVeryShortPeriodTotal_0 / ShadowVeryShortPeriod) and  # Short lower shadow third candle
                    (valid_high[i] - valid_close[i] if valid_close[i] >= valid_open[i] else valid_high[i] - valid_open[i]) < (ShadowVeryShortPeriodTotal_0 / ShadowVeryShortPeriod) and  # Short upper shadow third candle
                    valid_low[i] > valid_low[i-1] and valid_high[i] < valid_high[i-1]):  # Third candle within second candle range
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update period totals
                BodyLongPeriodTotal += abs(valid_close[i-2] - valid_open[i-2]) - abs(valid_close[BodyLongTrailingIdx-2] - valid_open[BodyLongTrailingIdx-2])
                ShadowLongPeriodTotal += (max(0.0, valid_close[i-2] - valid_low[i-2]) if valid_close[i-2] >= valid_open[i-2] else max(0.0, valid_open[i-2] - valid_low[i-2])) - \
                                         (max(0.0, valid_close[ShadowLongTrailingIdx-2] - valid_low[ShadowLongTrailingIdx-2]) if valid_close[ShadowLongTrailingIdx-2] >= valid_open[ShadowLongTrailingIdx-2] else max(0.0, valid_open[ShadowLongTrailingIdx-2] - valid_low[ShadowLongTrailingIdx-2]))
                ShadowVeryShortPeriodTotal_1 += (max(0.0, valid_close[i-1] - valid_low[i-1]) if valid_close[i-1] >= valid_open[i-1] else max(0.0, valid_open[i-1] - valid_low[i-1])) - \
                                                (max(0.0, valid_close[ShadowVeryShortTrailingIdx-1] - valid_low[ShadowVeryShortTrailingIdx-1]) if valid_close[ShadowVeryShortTrailingIdx-1] >= valid_open[ShadowVeryShortTrailingIdx-1] else max(0.0, valid_open[ShadowVeryShortTrailingIdx-1] - valid_low[ShadowVeryShortTrailingIdx-1]))
                ShadowVeryShortPeriodTotal_0 += (max(0.0, valid_close[i] - valid_low[i]) if valid_close[i] >= valid_open[i] else max(0.0, valid_open[i] - valid_low[i])) - \
                                                (max(0.0, valid_close[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]) if valid_close[ShadowVeryShortTrailingIdx] >= valid_open[ShadowVeryShortTrailingIdx] else max(0.0, valid_open[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]))
                BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i]) - abs(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx])
            
                BodyLongTrailingIdx += 1
                ShadowLongTrailingIdx += 1
                ShadowVeryShortTrailingIdx += 1
                BodyShortTrailingIdx += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDL3WHITESOLDIERS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle ranges as per TA-Lib defaults
        ShadowVeryShortPeriod = 3
        NearPeriod = 3
        FarPeriod = 3
        BodyShortPeriod = 3
        lookbackTotal = max(ShadowVeryShortPeriod, NearPeriod, FarPeriod, BodyShortPeriod) + 2
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for moving averages
            ShadowVeryShortPeriodTotal = np.zeros(3)
            NearPeriodTotal = np.zeros(3)
            FarPeriodTotal = np.zeros(3)
            BodyShortPeriodTotal = 0.0
        
            # Initialize trailing indices
            start_idx = lookbackTotal
            ShadowVeryShortTrailingIdx = start_idx - ShadowVeryShortPeriod
            NearTrailingIdx = start_idx - NearPeriod
            FarTrailingIdx = start_idx - FarPeriod
            BodyShortTrailingIdx = start_idx - BodyShortPeriod
        
            # Calculate initial totals for ShadowVeryShort
            for i in range(ShadowVeryShortTrailingIdx, start_idx):
                ShadowVeryShortPeriodTotal[2] += max(valid_high[i-2] - valid_close[i-2], 0.0) if valid_close[i-2] > valid_open[i-2] else max(valid_open[i-2] - valid_high[i-2], 0.0)
                ShadowVeryShortPeriodTotal[1] += max(valid_high[i-1] - valid_close[i-1], 0.0) if valid_close[i-1] > valid_open[i-1] else max(valid_open[i-1] - valid_high[i-1], 0.0)
                ShadowVeryShortPeriodTotal[0] += max(valid_high[i] - valid_close[i], 0.0) if valid_close[i] > valid_open[i] else max(valid_open[i] - valid_high[i], 0.0)
        
            # Calculate initial totals for Near
            for i in range(NearTrailingIdx, start_idx):
                NearPeriodTotal[2] += valid_high[i-2] - valid_low[i-2]
                NearPeriodTotal[1] += valid_high[i-1] - valid_low[i-1]
        
            # Calculate initial totals for Far
            for i in range(FarTrailingIdx, start_idx):
                FarPeriodTotal[2] += valid_high[i-2] - valid_low[i-2]
                FarPeriodTotal[1] += valid_high[i-1] - valid_low[i-1]
        
            # Calculate initial totals for BodyShort
            for i in range(BodyShortTrailingIdx, start_idx):
                BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # Main calculation loop
            i = start_idx
            while i < len(valid_high):
                # Calculate averages
                ShadowVeryShortAvg2 = ShadowVeryShortPeriodTotal[2] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                ShadowVeryShortAvg1 = ShadowVeryShortPeriodTotal[1] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                ShadowVeryShortAvg0 = ShadowVeryShortPeriodTotal[0] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                NearAvg2 = NearPeriodTotal[2] / NearPeriod if NearPeriod > 0 else 0.0
                NearAvg1 = NearPeriodTotal[1] / NearPeriod if NearPeriod > 0 else 0.0
                FarAvg2 = FarPeriodTotal[2] / FarPeriod if FarPeriod > 0 else 0.0
                FarAvg1 = FarPeriodTotal[1] / FarPeriod if FarPeriod > 0 else 0.0
                BodyShortAvg = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check for 3 White Soldiers pattern
                if (valid_close[i-2] > valid_open[i-2] and  # First candle is white
                    (valid_high[i-2] - valid_close[i-2] if valid_close[i-2] > valid_open[i-2] else valid_open[i-2] - valid_high[i-2]) < ShadowVeryShortAvg2 and  # Short upper shadow
                    valid_close[i-1] > valid_open[i-1] and  # Second candle is white
                    (valid_high[i-1] - valid_close[i-1] if valid_close[i-1] > valid_open[i-1] else valid_open[i-1] - valid_high[i-1]) < ShadowVeryShortAvg1 and  # Short upper shadow
                    valid_close[i] > valid_open[i] and  # Third candle is white
                    (valid_high[i] - valid_close[i] if valid_close[i] > valid_open[i] else valid_open[i] - valid_high[i]) < ShadowVeryShortAvg0 and  # Short upper shadow
                    valid_close[i] > valid_close[i-1] and valid_close[i-1] > valid_close[i-2] and  # Increasing closes
                    valid_open[i-1] > valid_open[i-2] and  # Increasing opens
                    valid_open[i-1] <= valid_close[i-2] + NearAvg2 and  # Second open near first close
                    valid_open[i] > valid_open[i-1] and  # Increasing opens
                    valid_open[i] <= valid_close[i-1] + NearAvg1 and  # Third open near second close
                    abs(valid_close[i-1] - valid_open[i-1]) > abs(valid_close[i-2] - valid_open[i-2]) - FarAvg2 and  # Increasing body size
                    abs(valid_close[i] - valid_open[i]) > abs(valid_close[i-1] - valid_open[i-1]) - FarAvg1 and  # Increasing body size
                    abs(valid_close[i] - valid_open[i]) > BodyShortAvg):  # Significant body size
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = 100
                else:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = 0
            
                # Update totals for next iteration
                for totIdx in range(2, -1, -1):
                    if i - totIdx >= 0 and ShadowVeryShortTrailingIdx - totIdx >= 0:
                        ShadowVeryShortPeriodTotal[totIdx] += (max(valid_high[i-totIdx] - valid_close[i-totIdx], 0.0) if valid_close[i-totIdx] > valid_open[i-totIdx] else max(valid_open[i-totIdx] - valid_high[i-totIdx], 0.0))
                        ShadowVeryShortPeriodTotal[totIdx] -= (max(valid_high[ShadowVeryShortTrailingIdx-totIdx] - valid_close[ShadowVeryShortTrailingIdx-totIdx], 0.0) if valid_close[ShadowVeryShortTrailingIdx-totIdx] > valid_open[ShadowVeryShortTrailingIdx-totIdx] else max(valid_open[ShadowVeryShortTrailingIdx-totIdx] - valid_high[ShadowVeryShortTrailingIdx-totIdx], 0.0))
            
                for totIdx in range(2, 0, -1):
                    if i - totIdx >= 0 and FarTrailingIdx - totIdx >= 0:
                        FarPeriodTotal[totIdx] += (valid_high[i-totIdx] - valid_low[i-totIdx])
                        FarPeriodTotal[totIdx] -= (valid_high[FarTrailingIdx-totIdx] - valid_low[FarTrailingIdx-totIdx])
                    if i - totIdx >= 0 and NearTrailingIdx - totIdx >= 0:
                        NearPeriodTotal[totIdx] += (valid_high[i-totIdx] - valid_low[i-totIdx])
                        NearPeriodTotal[totIdx] -= (valid_high[NearTrailingIdx-totIdx] - valid_low[NearTrailingIdx-totIdx])
            
                if i >= 0 and BodyShortTrailingIdx >= 0:
                    BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
                    BodyShortPeriodTotal -= abs(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx])
            
                i += 1
                ShadowVeryShortTrailingIdx += 1
                NearTrailingIdx += 1
                FarTrailingIdx += 1
                BodyShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLABANDONEDBABY(high, open, low, close, vol, oi, penetration=0.3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle body types as per TA-Lib defaults
        body_long_period = 10  # Default for BodyLong in TA-Lib
        body_doji_period = 3   # Default for BodyDoji in TA-Lib
        body_short_period = 5  # Default for BodyShort in TA-Lib
    
        # Lookback total is 2 days prior data needed for pattern recognition
        lookback_total = 2
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookback_total:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing indices for rolling averages
            start_idx = lookback_total
            body_long_trailing_idx = 0
            body_doji_trailing_idx = 0
            body_short_trailing_idx = 0
        
            # Initialize period totals for body averages
            body_long_period_total = 0.0
            body_doji_period_total = 0.0
            body_short_period_total = 0.0
        
            # Warm-up period: Calculate initial totals for body averages
            for i in range(body_long_trailing_idx, min(start_idx - 2, len(valid_high))):
                if i >= 0 and i < len(valid_high) - 2:
                    body_long_period_total += abs(valid_close[i] - valid_open[i])
            for i in range(body_doji_trailing_idx, min(start_idx - 1, len(valid_high))):
                if i >= 0 and i < len(valid_high) - 1:
                    body_doji_period_total += abs(valid_close[i] - valid_open[i])
            for i in range(body_short_trailing_idx, min(start_idx, len(valid_high))):
                if i >= 0:
                    body_short_period_total += abs(valid_close[i] - valid_open[i])
        
            # Main calculation loop
            for i in range(start_idx, len(valid_high)):
                if i - 2 < 0 or i - 1 < 0:
                    continue
                
                # Calculate real body sizes
                real_body_2 = abs(valid_close[i-2] - valid_open[i-2])
                real_body_1 = abs(valid_close[i-1] - valid_open[i-1])
                real_body_0 = abs(valid_close[i] - valid_open[i])
            
                # Calculate candle colors (1 for bullish, -1 for bearish)
                color_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate averages for body comparisons
                body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
                body_doji_avg = body_doji_period_total / body_doji_period if body_doji_period > 0 else 0.0
                body_short_avg = body_short_period_total / body_short_period if body_short_period > 0 else 0.0
            
                # Check for gaps
                gap_up_1_2 = valid_low[i-1] > valid_high[i-2]
                gap_down_1_2 = valid_high[i-1] < valid_low[i-2]
                gap_up_0_1 = valid_low[i] > valid_high[i-1]
                gap_down_0_1 = valid_high[i] < valid_low[i-1]
            
                # Check Abandoned Baby pattern conditions
                is_abandoned_baby = False
                if (real_body_2 > body_long_avg and
                    real_body_1 <= body_doji_avg and
                    real_body_0 > body_short_avg):
                    if (color_2 == 1 and color_0 == -1 and
                        valid_close[i] < valid_close[i-2] - real_body_2 * penetration and
                        gap_up_1_2 and gap_down_0_1):
                        is_abandoned_baby = True
                    elif (color_2 == -1 and color_0 == 1 and
                          valid_close[i] > valid_close[i-2] + real_body_2 * penetration and
                          gap_down_1_2 and gap_up_0_1):
                        is_abandoned_baby = True
            
                # Set output value
                if is_abandoned_baby:
                    result[valid_indices[i], sec] = color_0 * 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update rolling totals for body averages
                if i - 2 >= 0:
                    body_long_period_total += abs(valid_close[i-2] - valid_open[i-2])
                    if body_long_trailing_idx < len(valid_high):
                        body_long_period_total -= abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
                    body_long_trailing_idx += 1
                
                if i - 1 >= 0:
                    body_doji_period_total += abs(valid_close[i-1] - valid_open[i-1])
                    if body_doji_trailing_idx < len(valid_high):
                        body_doji_period_total -= abs(valid_close[body_doji_trailing_idx] - valid_open[body_doji_trailing_idx])
                    body_doji_trailing_idx += 1
                
                body_short_period_total += abs(valid_close[i] - valid_open[i])
                if body_short_trailing_idx < len(valid_high):
                    body_short_period_total -= abs(valid_close[body_short_trailing_idx] - valid_open[body_short_trailing_idx])
                body_short_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLADVANCEBLOCK(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define candle average periods as per TA-Lib defaults
        ShadowShortPeriod = 5
        ShadowLongPeriod = 5
        NearPeriod = 5
        FarPeriod = 5
        BodyLongPeriod = 5
    
        # Lookback period as per TA-Lib (maximum of the periods + 2 for the pattern)
        lookbackTotal = max(ShadowShortPeriod, ShadowLongPeriod, NearPeriod, FarPeriod, BodyLongPeriod) + 2
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for averages
            ShadowShortPeriodTotal = np.zeros(3)
            ShadowLongPeriodTotal = np.zeros(2)
            NearPeriodTotal = np.zeros(3)
            FarPeriodTotal = np.zeros(3)
            BodyLongPeriodTotal = 0.0
        
            # Initialize trailing indices
            ShadowShortTrailingIdx = lookbackTotal - ShadowShortPeriod
            ShadowLongTrailingIdx = lookbackTotal - ShadowLongPeriod
            NearTrailingIdx = lookbackTotal - NearPeriod
            FarTrailingIdx = lookbackTotal - FarPeriod
            BodyLongTrailingIdx = lookbackTotal - BodyLongPeriod
        
            # Warm-up period: Calculate initial totals
            i = ShadowShortTrailingIdx
            while i < lookbackTotal:
                ShadowShortPeriodTotal[2] += max(valid_high[i-2] - valid_close[i-2], 0.0) if valid_close[i-2] > valid_open[i-2] else max(valid_open[i-2] - valid_close[i-2], 0.0)
                ShadowShortPeriodTotal[1] += max(valid_high[i-1] - valid_close[i-1], 0.0) if valid_close[i-1] > valid_open[i-1] else max(valid_open[i-1] - valid_close[i-1], 0.0)
                ShadowShortPeriodTotal[0] += max(valid_high[i] - valid_close[i], 0.0) if valid_close[i] > valid_open[i] else max(valid_open[i] - valid_close[i], 0.0)
                i += 1
            
            i = ShadowLongTrailingIdx
            while i < lookbackTotal:
                ShadowLongPeriodTotal[1] += max(valid_high[i-1] - valid_close[i-1], 0.0) if valid_close[i-1] > valid_open[i-1] else max(valid_open[i-1] - valid_close[i-1], 0.0)
                ShadowLongPeriodTotal[0] += max(valid_high[i] - valid_close[i], 0.0) if valid_close[i] > valid_open[i] else max(valid_open[i] - valid_close[i], 0.0)
                i += 1
            
            i = NearTrailingIdx
            while i < lookbackTotal:
                NearPeriodTotal[2] += valid_high[i-2] - valid_low[i-2]
                NearPeriodTotal[1] += valid_high[i-1] - valid_low[i-1]
                i += 1
            
            i = FarTrailingIdx
            while i < lookbackTotal:
                FarPeriodTotal[2] += valid_high[i-2] - valid_low[i-2]
                FarPeriodTotal[1] += valid_high[i-1] - valid_low[i-1]
                i += 1
            
            i = BodyLongTrailingIdx
            while i < lookbackTotal:
                BodyLongPeriodTotal += abs(valid_close[i-2] - valid_open[i-2])
                i += 1
            
            # Main calculation loop
            i = lookbackTotal
            while i < len(valid_high):
                # Calculate candle color (1 for bullish, -1 for bearish)
                color_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate real body sizes
                realbody_2 = abs(valid_close[i-2] - valid_open[i-2])
                realbody_1 = abs(valid_close[i-1] - valid_open[i-1])
                realbody_0 = abs(valid_close[i] - valid_open[i])
            
                # Calculate upper shadows
                uppershadow_2 = valid_high[i-2] - valid_close[i-2] if valid_close[i-2] > valid_open[i-2] else valid_high[i-2] - valid_open[i-2]
                uppershadow_1 = valid_high[i-1] - valid_close[i-1] if valid_close[i-1] > valid_open[i-1] else valid_high[i-1] - valid_open[i-1]
                uppershadow_0 = valid_high[i] - valid_close[i] if valid_close[i] > valid_open[i] else valid_high[i] - valid_open[i]
            
                # Calculate averages
                ShadowShortAvg_2 = ShadowShortPeriodTotal[2] / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
                ShadowShortAvg_1 = ShadowShortPeriodTotal[1] / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
                ShadowShortAvg_0 = ShadowShortPeriodTotal[0] / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
                ShadowLongAvg_0 = ShadowLongPeriodTotal[0] / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
                NearAvg_2 = NearPeriodTotal[2] / NearPeriod if NearPeriod > 0 else 0.0
                NearAvg_1 = NearPeriodTotal[1] / NearPeriod if NearPeriod > 0 else 0.0
                FarAvg_2 = FarPeriodTotal[2] / FarPeriod if FarPeriod > 0 else 0.0
                FarAvg_1 = FarPeriodTotal[1] / FarPeriod if FarPeriod > 0 else 0.0
                BodyLongAvg_2 = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
            
                # Check for Advance Block pattern
                if (color_2 == 1 and color_1 == 1 and color_0 == 1 and
                    valid_close[i] > valid_close[i-1] and valid_close[i-1] > valid_close[i-2] and
                    valid_open[i-1] > valid_open[i-2] and
                    valid_open[i-1] <= valid_close[i-2] + NearAvg_2 and
                    valid_open[i] > valid_open[i-1] and
                    valid_open[i] <= valid_close[i-1] + NearAvg_1 and
                    realbody_2 > BodyLongAvg_2 and
                    uppershadow_2 < ShadowShortAvg_2 and
                    ((realbody_1 < realbody_2 - FarAvg_2 and realbody_0 < realbody_1 + NearAvg_1) or
                     (realbody_0 < realbody_1 - FarAvg_1) or
                     (realbody_0 < realbody_1 and realbody_1 < realbody_2 and
                      (uppershadow_0 > ShadowShortAvg_0 or uppershadow_1 > ShadowShortAvg_1)) or
                     (realbody_0 < realbody_1 and uppershadow_0 > ShadowLongAvg_0))):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update period totals
                for totIdx in range(2, -1, -1):
                    curr_val = max(valid_high[i-totIdx] - valid_close[i-totIdx], 0.0) if valid_close[i-totIdx] > valid_open[i-totIdx] else max(valid_open[i-totIdx] - valid_close[i-totIdx], 0.0)
                    trail_val = max(valid_high[ShadowShortTrailingIdx-totIdx] - valid_close[ShadowShortTrailingIdx-totIdx], 0.0) if valid_close[ShadowShortTrailingIdx-totIdx] > valid_open[ShadowShortTrailingIdx-totIdx] else max(valid_open[ShadowShortTrailingIdx-totIdx] - valid_close[ShadowShortTrailingIdx-totIdx], 0.0)
                    ShadowShortPeriodTotal[totIdx] += curr_val - trail_val
                
                for totIdx in range(1, -1, -1):
                    curr_val = max(valid_high[i-totIdx] - valid_close[i-totIdx], 0.0) if valid_close[i-totIdx] > valid_open[i-totIdx] else max(valid_open[i-totIdx] - valid_close[i-totIdx], 0.0)
                    trail_val = max(valid_high[ShadowLongTrailingIdx-totIdx] - valid_close[ShadowLongTrailingIdx-totIdx], 0.0) if valid_close[ShadowLongTrailingIdx-totIdx] > valid_open[ShadowLongTrailingIdx-totIdx] else max(valid_open[ShadowLongTrailingIdx-totIdx] - valid_close[ShadowLongTrailingIdx-totIdx], 0.0)
                    ShadowLongPeriodTotal[totIdx] += curr_val - trail_val
                
                for totIdx in range(2, 0, -1):
                    curr_val_far = valid_high[i-totIdx] - valid_low[i-totIdx]
                    trail_val_far = valid_high[FarTrailingIdx-totIdx] - valid_low[FarTrailingIdx-totIdx]
                    FarPeriodTotal[totIdx] += curr_val_far - trail_val_far
                    curr_val_near = valid_high[i-totIdx] - valid_low[i-totIdx]
                    trail_val_near = valid_high[NearTrailingIdx-totIdx] - valid_low[NearTrailingIdx-totIdx]
                    NearPeriodTotal[totIdx] += curr_val_near - trail_val_near
                
                curr_val_body = abs(valid_close[i-2] - valid_open[i-2])
                trail_val_body = abs(valid_close[BodyLongTrailingIdx-2] - valid_open[BodyLongTrailingIdx-2])
                BodyLongPeriodTotal += curr_val_body - trail_val_body
            
                # Increment indices
                i += 1
                ShadowShortTrailingIdx += 1
                ShadowLongTrailingIdx += 1
                NearTrailingIdx += 1
                FarTrailingIdx += 1
                BodyLongTrailingIdx += 1
            
        return result


    @staticmethod
    @nb.njit
    def CDLBREAKAWAY(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as defined in TA-Lib for CDLBREAKAWAY (5 bars needed for pattern)
        lookback_total = 4
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            pattern_values = np.zeros(len(valid_high))
        
            # BodyLong period for averaging candle range (default from TA-Lib)
            body_long_period = 10
            start_idx = max(lookback_total, body_long_period)
        
            # Pre-calculate real body and candle range for efficiency
            real_body = np.abs(valid_close - valid_open)
            candle_range = valid_high - valid_low
        
            # Initialize trailing total for BodyLong average
            body_long_period_total = 0.0
            body_long_trailing_idx = start_idx - body_long_period
        
            # Calculate initial total for BodyLong average
            for i in range(body_long_trailing_idx, start_idx):
                if i >= 4:
                    body_long_period_total += candle_range[i - 4]
        
            # Main calculation loop starting from lookback period
            for i in range(start_idx, len(valid_high)):
                # Calculate BodyLong average
                body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
            
                # Check for Breakaway pattern conditions
                if i >= 4:
                    # Condition 1: First candle has long body
                    cond1 = real_body[i - 4] > body_long_avg
                
                    # Condition 2: First three candles have same color
                    color_i4 = 1 if valid_close[i - 4] > valid_open[i - 4] else -1
                    color_i3 = 1 if valid_close[i - 3] > valid_open[i - 3] else -1
                    color_i1 = 1 if valid_close[i - 1] > valid_open[i - 1] else -1
                    color_i = 1 if valid_close[i] > valid_open[i] else -1
                    cond2 = color_i4 == color_i3 and color_i3 == color_i1
                
                    # Condition 3: Last candle is opposite color of first three
                    cond3 = color_i1 == -color_i
                
                    # Condition 4: Specific pattern based on direction
                    if color_i4 == -1:  # Bearish first candle
                        cond4 = (valid_open[i - 3] < valid_close[i - 4] and  # Gap down
                                valid_high[i - 2] < valid_high[i - 3] and
                                valid_low[i - 2] < valid_low[i - 3] and
                                valid_high[i - 1] < valid_high[i - 2] and
                                valid_low[i - 1] < valid_low[i - 2] and
                                valid_close[i] > valid_open[i - 3] and
                                valid_close[i] < valid_close[i - 4])
                    else:  # Bullish first candle
                        cond4 = (valid_open[i - 3] > valid_close[i - 4] and  # Gap up
                                valid_high[i - 2] > valid_high[i - 3] and
                                valid_low[i - 2] > valid_low[i - 3] and
                                valid_high[i - 1] > valid_high[i - 2] and
                                valid_low[i - 1] > valid_low[i - 2] and
                                valid_close[i] < valid_open[i - 3] and
                                valid_close[i] > valid_close[i - 4])
                
                    # If all conditions are met, set the pattern value
                    if cond1 and cond2 and cond3 and cond4:
                        pattern_values[i] = color_i * 100
                    else:
                        pattern_values[i] = 0
            
                # Update trailing total for next iteration
                if i >= 4 and body_long_trailing_idx >= 4:
                    body_long_period_total += candle_range[i - 4] - candle_range[body_long_trailing_idx - 4]
                body_long_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if valid_indices[i] >= start_idx:
                    result[valid_indices[i], sec] = pattern_values[i]
    
        return result


    @staticmethod
    @nb.njit
    def CDLCONCEALBABYSWALL(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # ShadowVeryShort的平均周期，通常为3
        ShadowVeryShortPeriod = 3
        lookbackTotal = ShadowVeryShortPeriod + 3  # 需要前3根K线加上周期
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 初始化ShadowVeryShortPeriodTotal数组
            ShadowVeryShortPeriodTotal = np.zeros(3)
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
        
            # 预热期：计算初始的ShadowVeryShortPeriodTotal
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                ShadowVeryShortPeriodTotal[2] += max(valid_high[i-3] - valid_low[i-3], 0.0)
                ShadowVeryShortPeriodTotal[1] += max(valid_high[i-2] - valid_low[i-2], 0.0)
                ShadowVeryShortPeriodTotal[0] += max(valid_high[i-1] - valid_low[i-1], 0.0)
        
            # 主计算阶段
            for i in range(lookbackTotal, len(valid_high)):
                # 判断条件，与C源码逻辑完全一致
                if (valid_close[i-3] < valid_open[i-3] and  # 3根前为阴线
                    valid_close[i-2] < valid_open[i-2] and  # 2根前为阴线
                    valid_close[i-1] < valid_open[i-1] and  # 1根前为阴线
                    valid_close[i] < valid_open[i] and      # 当前为阴线
                    # 下影线小于平均值
                    (valid_open[i-3] - valid_low[i-3]) < (ShadowVeryShortPeriodTotal[2] / ShadowVeryShortPeriod) and
                    # 上影线小于平均值
                    (valid_high[i-3] - valid_close[i-3]) < (ShadowVeryShortPeriodTotal[2] / ShadowVeryShortPeriod) and
                    # 下影线小于平均值
                    (valid_open[i-2] - valid_low[i-2]) < (ShadowVeryShortPeriodTotal[1] / ShadowVeryShortPeriod) and
                    # 上影线小于平均值
                    (valid_high[i-2] - valid_close[i-2]) < (ShadowVeryShortPeriodTotal[1] / ShadowVeryShortPeriod) and
                    # 实体间有向下跳空
                    valid_open[i-1] < valid_close[i-2] and
                    # 上影线大于平均值
                    (valid_high[i-1] - valid_close[i-1]) > (ShadowVeryShortPeriodTotal[0] / ShadowVeryShortPeriod) and
                    valid_high[i-1] > valid_close[i-2] and
                    valid_high[i] > valid_high[i-1] and
                    valid_low[i] < valid_low[i-1]):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # 更新ShadowVeryShortPeriodTotal
                for totIdx in range(2, -1, -1):
                    curr_range = max(valid_high[i - totIdx] - valid_low[i - totIdx], 0.0)
                    trail_range = max(valid_high[ShadowVeryShortTrailingIdx - totIdx] - valid_low[ShadowVeryShortTrailingIdx - totIdx], 0.0)
                    ShadowVeryShortPeriodTotal[totIdx] += curr_range - trail_range
            
                ShadowVeryShortTrailingIdx += 1
    
        return result


    @staticmethod
    @nb.njit
    def CDLDARKCLOUDCOVER(high, open, low, close, vol, oi, penetration=0.5):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        BodyLongPeriod = 10  # TA-Lib default for BodyLong average period

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 2:  # Need at least 2 bars for pattern
                continue
            
            valid_high = high[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Lookback period as per TA-Lib (1 prior bar for pattern + BodyLongPeriod for average)
            lookback_total = BodyLongPeriod + 1
            if len(valid_indices) < lookback_total:
                continue
            
            # Initialize output array for valid data
            pattern_values = np.zeros(len(valid_high))
        
            # Calculate initial BodyLongPeriodTotal for the first window
            BodyLongPeriodTotal = 0.0
            for i in range(lookback_total - BodyLongPeriod, lookback_total):
                if i > 0:  # Need previous bar for real body calculation
                    real_body = abs(valid_close[i-1] - valid_open[i-1])
                    BodyLongPeriodTotal += real_body
        
            BodyLongTrailingIdx = lookback_total - BodyLongPeriod
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Check for Dark Cloud Cover pattern
                if i > 0:  # Need previous bar
                    # First bar must be bullish (white candle)
                    prev_color = 1 if valid_close[i-1] > valid_open[i-1] else -1
                    # Current bar must be bearish (black candle)
                    curr_color = 1 if valid_close[i] > valid_open[i] else -1
                    # Previous real body size
                    prev_real_body = abs(valid_close[i-1] - valid_open[i-1])
                    # Calculate average body length for comparison
                    BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                
                    if (prev_color == 1 and  # Previous bar is bullish
                        prev_real_body > BodyLongAverage and  # Previous body is long
                        curr_color == -1 and  # Current bar is bearish
                        valid_open[i] > valid_high[i-1] and  # Current opens above previous high
                        valid_close[i] > valid_open[i-1] and  # Current close above previous open
                        valid_close[i] < valid_close[i-1] - prev_real_body * penetration):  # Penetration condition
                        pattern_values[i] = -100
                    else:
                        pattern_values[i] = 0
            
                # Update BodyLongPeriodTotal for next iteration
                if i > 0 and BodyLongTrailingIdx > 0:
                    prev_real_body_new = abs(valid_close[i-1] - valid_open[i-1])
                    prev_real_body_old = abs(valid_close[BodyLongTrailingIdx-1] - valid_open[BodyLongTrailingIdx-1])
                    BodyLongPeriodTotal += prev_real_body_new - prev_real_body_old
                BodyLongTrailingIdx += 1
        
            # Map results back to original array
            start_idx = lookback_total
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = pattern_values[i]
    
        return result


    @staticmethod
    @nb.njit
    def CDLENGULFING(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as defined in TA-Lib for CDLENGULFING (needs 2 bars)
        lookback_total = 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output for valid data
            engulfing_values = np.zeros(len(valid_open))
        
            # Start processing from lookback_total index
            for i in range(lookback_total, len(valid_open)):
                # Determine candle color for current and previous bar
                current_color = 1 if valid_close[i] > valid_open[i] else -1
                prev_color = 1 if valid_close[i-1] > valid_open[i-1] else -1
            
                # Bullish Engulfing: Current is bullish, previous is bearish
                bullish_engulfing = (current_color == 1 and prev_color == -1 and
                                    ((valid_close[i] >= valid_open[i-1] and valid_open[i] < valid_close[i-1]) or
                                     (valid_close[i] > valid_open[i-1] and valid_open[i] <= valid_close[i-1])))
            
                # Bearish Engulfing: Current is bearish, previous is bullish
                bearish_engulfing = (current_color == -1 and prev_color == 1 and
                                    ((valid_open[i] >= valid_close[i-1] and valid_close[i] < valid_open[i-1]) or
                                     (valid_open[i] > valid_close[i-1] and valid_close[i] <= valid_open[i-1])))
            
                if bullish_engulfing or bearish_engulfing:
                    if valid_open[i] != valid_close[i-1] and valid_close[i] != valid_open[i-1]:
                        engulfing_values[i] = current_color * 100
                    else:
                        engulfing_values[i] = current_color * 80
                else:
                    engulfing_values[i] = 0
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = engulfing_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLEVENINGDOJISTAR(high, open, low, close, vol, oi, penetration=0.3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different body types as in TA-Lib
        BodyLongPeriod = 10
        BodyDojiPeriod = 3
        BodyShortPeriod = 5
        lookbackTotal = 2 + max(BodyLongPeriod, max(BodyDojiPeriod, BodyShortPeriod))
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing indices for rolling sums
            start_idx = lookbackTotal
            BodyLongTrailingIdx = start_idx - 2 - BodyLongPeriod
            BodyDojiTrailingIdx = start_idx - 1 - BodyDojiPeriod
            BodyShortTrailingIdx = start_idx - BodyShortPeriod
        
            # Initialize rolling sums for body averages
            BodyLongPeriodTotal = 0.0
            BodyDojiPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
        
            # Calculate initial sums for BodyLong
            i = BodyLongTrailingIdx
            while i < start_idx - 2:
                if i >= 0:
                    BodyLongPeriodTotal += valid_high[i] - valid_low[i]
                i += 1
            
            # Calculate initial sums for BodyDoji
            i = BodyDojiTrailingIdx
            while i < start_idx - 1:
                if i >= 0:
                    BodyDojiPeriodTotal += valid_high[i] - valid_low[i]
                i += 1
            
            # Calculate initial sums for BodyShort
            i = BodyShortTrailingIdx
            while i < start_idx:
                if i >= 0:
                    BodyShortPeriodTotal += valid_high[i] - valid_low[i]
                i += 1
            
            # Main calculation loop
            i = start_idx
            while i < len(valid_high):
                # Calculate real body sizes
                realbody_2 = abs(valid_close[i-2] - valid_open[i-2])
                realbody_1 = abs(valid_close[i-1] - valid_open[i-1])
                realbody_0 = abs(valid_close[i] - valid_open[i])
            
                # Calculate candle ranges for averages
                range_2 = valid_high[i-2] - valid_low[i-2]
                range_1 = valid_high[i-1] - valid_low[i-1]
                range_0 = valid_high[i] - valid_low[i]
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check for Evening Doji Star pattern
                if (realbody_2 > BodyLongAverage and  # First candle is long white
                    valid_close[i-2] > valid_open[i-2] and  # First candle color is white
                    realbody_1 <= BodyDojiAverage and  # Second candle is doji
                    valid_open[i-1] > valid_close[i-2] and  # Gap up between first and second
                    realbody_0 > BodyShortAverage and  # Third candle is long black
                    valid_close[i] < valid_open[i] and  # Third candle color is black
                    valid_close[i] < valid_close[i-2] - realbody_2 * penetration):  # Penetration check
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update rolling sums
                if i - 2 >= 0:
                    BodyLongPeriodTotal += range_2
                if BodyLongTrailingIdx >= 0:
                    BodyLongPeriodTotal -= valid_high[BodyLongTrailingIdx] - valid_low[BodyLongTrailingIdx]
                if i - 1 >= 0:
                    BodyDojiPeriodTotal += range_1
                if BodyDojiTrailingIdx >= 0:
                    BodyDojiPeriodTotal -= valid_high[BodyDojiTrailingIdx] - valid_low[BodyDojiTrailingIdx]
                if i >= 0:
                    BodyShortPeriodTotal += range_0
                if BodyShortTrailingIdx >= 0:
                    BodyShortPeriodTotal -= valid_high[BodyShortTrailingIdx] - valid_low[BodyShortTrailingIdx]
                
                i += 1
                BodyLongTrailingIdx += 1
                BodyDojiTrailingIdx += 1
                BodyShortTrailingIdx += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLEVENINGSTAR(high, open, low, close, vol, oi, penetration=0.3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyLong and BodyShort as per TA-Lib defaults
        BodyLongPeriod = 10
        BodyShortPeriod = 3
        lookbackTotal = 2 + max(BodyLongPeriod, BodyShortPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for body calculations
            BodyLongPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
            BodyShortPeriodTotal2 = 0.0
        
            # Calculate initial totals for BodyLong (i-2 candle)
            BodyLongTrailingIdx = 0
            for i in range(BodyLongPeriod):
                if i < len(valid_high) - 2:
                    BodyLongPeriodTotal += abs(valid_open[i] - valid_close[i])
        
            # Calculate initial totals for BodyShort (i-1 and i candles)
            BodyShortTrailingIdx = 0
            for i in range(BodyShortPeriod):
                if i < len(valid_high) - 1:
                    BodyShortPeriodTotal += abs(valid_open[i] - valid_close[i])
                if i < len(valid_high) - 2:
                    BodyShortPeriodTotal2 += abs(valid_open[i+1] - valid_close[i+1])
        
            # Start processing from lookbackTotal
            start_idx = lookbackTotal
            for i in range(start_idx, len(valid_high)):
                # Calculate real body for current and previous candles
                realbody_i2 = abs(valid_close[i-2] - valid_open[i-2])
                realbody_i1 = abs(valid_close[i-1] - valid_open[i-1])
                realbody_i = abs(valid_close[i] - valid_open[i])
            
                # Calculate candle color (1 for bullish, -1 for bearish)
                color_i2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_i = 1 if valid_close[i] > valid_open[i] else -1
            
                # Check for gap up between i-2 and i-1
                gap_up = min(valid_open[i-1], valid_close[i-1]) > max(valid_open[i-2], valid_close[i-2])
            
                # Calculate averages for comparison
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                BodyShortAverage2 = BodyShortPeriodTotal2 / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Evening Star pattern conditions
                if (realbody_i2 > BodyLongAverage and
                    color_i2 == 1 and
                    realbody_i1 <= BodyShortAverage and
                    gap_up and
                    realbody_i > BodyShortAverage2 and
                    color_i == -1 and
                    valid_close[i] < valid_close[i-2] - realbody_i2 * penetration):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update trailing totals
                if i - 2 >= BodyLongPeriod:
                    BodyLongPeriodTotal += abs(valid_close[i-2] - valid_open[i-2])
                    BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                    BodyLongTrailingIdx += 1
                
                if i - 1 >= BodyShortPeriod:
                    BodyShortPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
                    BodyShortPeriodTotal -= abs(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx])
                    BodyShortPeriodTotal2 += abs(valid_close[i] - valid_open[i])
                    if BodyShortTrailingIdx + 1 < len(valid_high):
                        BodyShortPeriodTotal2 -= abs(valid_close[BodyShortTrailingIdx+1] - valid_open[BodyShortTrailingIdx+1])
                    BodyShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLHANGINGMAN(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle characteristics as in TA-Lib
        BodyShortPeriod = 10
        ShadowLongPeriod = 10
        ShadowVeryShortPeriod = 10
        NearPeriod = 10
    
        # Total lookback period as per TA-Lib
        lookbackTotal = max(BodyShortPeriod, max(ShadowLongPeriod, max(ShadowVeryShortPeriod, NearPeriod + 1)))
    
        for sec in range(secs):
            # Initialize period totals for averaging
            BodyPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
            NearPeriodTotal = 0.0
        
            # Initialize trailing indices for rolling window calculation
            BodyTrailingIdx = lookbackTotal - BodyShortPeriod
            ShadowLongTrailingIdx = lookbackTotal - ShadowLongPeriod
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
            NearTrailingIdx = lookbackTotal - 1 - NearPeriod
        
            # Warm-up period: Calculate initial totals for averages
            for i in range(BodyTrailingIdx, lookbackTotal):
                if i < tdts and high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    BodyPeriodTotal += abs(close[i, sec] - open[i, sec])
        
            for i in range(ShadowLongTrailingIdx, lookbackTotal):
                if i < tdts and high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    ShadowLongPeriodTotal += min(close[i, sec], open[i, sec]) - low[i, sec]
        
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                if i < tdts and high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    ShadowVeryShortPeriodTotal += high[i, sec] - max(close[i, sec], open[i, sec])
        
            for i in range(NearTrailingIdx, lookbackTotal - 1):
                if i < tdts and high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec]:
                    NearPeriodTotal += high[i, sec] - low[i, sec]
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, tdts):
                if (high[i, sec] != high[i, sec] or low[i, sec] != low[i, sec] or 
                    open[i, sec] != open[i, sec] or close[i, sec] != close[i, sec] or
                    i - 1 < 0 or high[i-1, sec] != high[i-1, sec]):
                    result[i, sec] = 0
                    continue
                
                # Calculate real body and shadows for current candle
                real_body = abs(close[i, sec] - open[i, sec])
                lower_shadow = min(close[i, sec], open[i, sec]) - low[i, sec]
                upper_shadow = high[i, sec] - max(close[i, sec], open[i, sec])
            
                # Calculate averages for comparison
                BodyAverage = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                ShadowLongAverage = ShadowLongPeriodTotal / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                NearAverage = NearPeriodTotal / NearPeriod if NearPeriod > 0 and i - 1 >= 0 else 0.0
            
                # Hanging Man pattern conditions
                if (real_body < BodyAverage and
                    lower_shadow > ShadowLongAverage and
                    upper_shadow < ShadowVeryShortAverage and
                    min(close[i, sec], open[i, sec]) >= high[i-1, sec] - NearAverage):
                    result[i, sec] = -100
                else:
                    result[i, sec] = 0
            
                # Update rolling totals for next iteration
                if i < tdts:
                    # Add current values
                    BodyPeriodTotal += abs(close[i, sec] - open[i, sec])
                    ShadowLongPeriodTotal += min(close[i, sec], open[i, sec]) - low[i, sec]
                    ShadowVeryShortPeriodTotal += high[i, sec] - max(close[i, sec], open[i, sec])
                    if i - 1 >= 0:
                        NearPeriodTotal += high[i-1, sec] - low[i-1, sec]
                
                    # Subtract trailing values
                    if BodyTrailingIdx < tdts and BodyTrailingIdx >= 0:
                        BodyPeriodTotal -= abs(close[BodyTrailingIdx, sec] - open[BodyTrailingIdx, sec])
                    if ShadowLongTrailingIdx < tdts and ShadowLongTrailingIdx >= 0:
                        ShadowLongPeriodTotal -= min(close[ShadowLongTrailingIdx, sec], open[ShadowLongTrailingIdx, sec]) - low[ShadowLongTrailingIdx, sec]
                    if ShadowVeryShortTrailingIdx < tdts and ShadowVeryShortTrailingIdx >= 0:
                        ShadowVeryShortPeriodTotal -= high[ShadowVeryShortTrailingIdx, sec] - max(close[ShadowVeryShortTrailingIdx, sec], open[ShadowVeryShortTrailingIdx, sec])
                    if NearTrailingIdx < tdts and NearTrailingIdx >= 0:
                        NearPeriodTotal -= high[NearTrailingIdx, sec] - low[NearTrailingIdx, sec]
                
                    # Increment trailing indices
                    BodyTrailingIdx += 1
                    ShadowLongTrailingIdx += 1
                    ShadowVeryShortTrailingIdx += 1
                    NearTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLHARAMI(high, open, low, close, vol, oi, body_long_period=10, body_short_period=3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (1 day prior for Harami pattern)
        lookback_total = 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing indices for rolling averages
            body_long_trailing_idx = 0
            body_short_trailing_idx = 0
            body_long_period_total = 0.0
            body_short_period_total = 0.0
        
            # Pre-calculate initial totals for BodyLong and BodyShort averages
            for i in range(body_long_trailing_idx, min(body_long_period, len(valid_high))):
                body_long_period_total += abs(valid_close[i] - valid_open[i])
            for i in range(body_short_trailing_idx, min(body_short_period, len(valid_high))):
                body_short_period_total += abs(valid_close[i] - valid_open[i])
        
            # Start processing from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Calculate current and previous real body
                real_body_prev = abs(valid_close[i-1] - valid_open[i-1])
                real_body_curr = abs(valid_close[i] - valid_open[i])
            
                # Calculate averages for BodyLong and BodyShort
                body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
                body_short_avg = body_short_period_total / body_short_period if body_short_period > 0 else 0.0
            
                # Harami pattern logic as per TA-Lib
                if real_body_prev > body_long_avg and real_body_curr <= body_short_avg:
                    curr_max = max(valid_close[i], valid_open[i])
                    curr_min = min(valid_close[i], valid_open[i])
                    prev_max = max(valid_close[i-1], valid_open[i-1])
                    prev_min = min(valid_close[i-1], valid_open[i-1])
                
                    if curr_max < prev_max and curr_min > prev_min:
                        # Classic Harami pattern
                        candle_color = 1 if valid_close[i-1] > valid_open[i-1] else -1
                        result[valid_indices[i], sec] = -candle_color * 100
                    elif curr_max <= prev_max and curr_min >= prev_min:
                        # Less strict Harami pattern
                        candle_color = 1 if valid_close[i-1] > valid_open[i-1] else -1
                        result[valid_indices[i], sec] = -candle_color * 80
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals for next iteration
                if i < len(valid_high):
                    # Add new value for BodyLong
                    if i - 1 >= 0:
                        body_long_period_total += abs(valid_close[i-1] - valid_open[i-1])
                    # Remove old value for BodyLong
                    if body_long_trailing_idx < len(valid_high):
                        body_long_period_total -= abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
                    body_long_trailing_idx += 1
                
                    # Add new value for BodyShort
                    body_short_period_total += abs(valid_close[i] - valid_open[i])
                    # Remove old value for BodyShort
                    if body_short_trailing_idx < len(valid_high):
                        body_short_period_total -= abs(valid_close[body_short_trailing_idx] - valid_open[body_short_trailing_idx])
                    body_short_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLHARAMICROSS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyLong and BodyDoji as per TA-Lib defaults
        BodyLongPeriod = 10
        BodyDojiPeriod = 3
        lookbackTotal = max(BodyLongPeriod + 1, BodyDojiPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            out_values = np.zeros(len(valid_high))
        
            # Initialize trailing indices and period totals
            BodyLongTrailingIdx = 0
            BodyDojiTrailingIdx = 0
            BodyLongPeriodTotal = 0.0
            BodyDojiPeriodTotal = 0.0
        
            # Warm-up period for BodyLong
            for i in range(BodyLongTrailingIdx, min(lookbackTotal - 1, len(valid_high))):
                if i < BodyLongPeriod:
                    BodyLongPeriodTotal += abs(valid_open[i] - valid_close[i])
        
            # Warm-up period for BodyDoji
            for i in range(BodyDojiTrailingIdx, min(lookbackTotal, len(valid_high))):
                if i < BodyDojiPeriod:
                    BodyDojiPeriodTotal += abs(valid_open[i] - valid_close[i])
        
            # Main calculation loop
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body for previous and current candle
                realbody_prev = abs(valid_open[i-1] - valid_close[i-1])
                realbody_curr = abs(valid_open[i] - valid_close[i])
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
            
                # Harami Cross pattern logic
                if realbody_prev > BodyLongAverage and realbody_curr <= BodyDojiAverage:
                    max_curr = max(valid_close[i], valid_open[i])
                    min_curr = min(valid_close[i], valid_open[i])
                    max_prev = max(valid_close[i-1], valid_open[i-1])
                    min_prev = min(valid_close[i-1], valid_open[i-1])
                
                    if max_curr < max_prev and min_curr > min_prev:
                        # Full Harami Cross pattern
                        candle_color = 1 if valid_close[i-1] > valid_open[i-1] else -1
                        out_values[i] = -candle_color * 100
                    elif max_curr <= max_prev and min_curr >= min_prev:
                        # Partial match (still within previous candle range)
                        candle_color = 1 if valid_close[i-1] > valid_open[i-1] else -1
                        out_values[i] = -candle_color * 80
                    else:
                        out_values[i] = 0
                else:
                    out_values[i] = 0
            
                # Update period totals for next iteration
                if i - 1 >= BodyLongTrailingIdx:
                    BodyLongPeriodTotal += abs(valid_open[i-1] - valid_close[i-1])
                    if BodyLongTrailingIdx < len(valid_high):
                        BodyLongPeriodTotal -= abs(valid_open[BodyLongTrailingIdx] - valid_close[BodyLongTrailingIdx])
                    BodyLongTrailingIdx += 1
            
                if i >= BodyDojiTrailingIdx:
                    BodyDojiPeriodTotal += abs(valid_open[i] - valid_close[i])
                    if BodyDojiTrailingIdx < len(valid_high):
                        BodyDojiPeriodTotal -= abs(valid_open[BodyDojiTrailingIdx] - valid_close[BodyDojiTrailingIdx])
                    BodyDojiTrailingIdx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookbackTotal:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = out_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLHIGHWAVE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        BodyShortPeriod = 10  # Default period for BodyShort in TA-Lib
        ShadowVeryLongPeriod = 10  # Default period for ShadowVeryLong in TA-Lib
        lookbackTotal = max(BodyShortPeriod, ShadowVeryLongPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for averaging
            BodyPeriodTotal = 0.0
            ShadowPeriodTotal = 0.0
        
            # Calculate initial totals for BodyShort and ShadowVeryLong
            BodyTrailingIdx = 0
            ShadowTrailingIdx = 0
            for i in range(lookbackTotal):
                # Body range for BodyShort (real body size)
                body_range = abs(valid_close[i] - valid_open[i])
                BodyPeriodTotal += body_range
            
                # Shadow range for ShadowVeryLong (high - low)
                shadow_range = valid_high[i] - valid_low[i]
                ShadowPeriodTotal += shadow_range
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body and shadows
                real_body = abs(valid_close[i] - valid_open[i])
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Calculate averages
                BodyAverage = BodyPeriodTotal / BodyShortPeriod
                ShadowAverage = ShadowPeriodTotal / ShadowVeryLongPeriod
            
                # Check High Wave conditions
                if (real_body < BodyAverage and 
                    upper_shadow > ShadowAverage and 
                    lower_shadow > ShadowAverage):
                    result[valid_indices[i], sec] = 100 if valid_close[i] > valid_open[i] else -100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update trailing totals
                # Remove oldest value and add newest value for Body
                oldest_body_range = abs(valid_close[BodyTrailingIdx] - valid_open[BodyTrailingIdx])
                BodyPeriodTotal += real_body - oldest_body_range
                BodyTrailingIdx += 1
            
                # Remove oldest value and add newest value for Shadow
                oldest_shadow_range = valid_high[ShadowTrailingIdx] - valid_low[ShadowTrailingIdx]
                ShadowPeriodTotal += (valid_high[i] - valid_low[i]) - oldest_shadow_range
                ShadowTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLHIKKAKE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 3:  # Need at least 3 data points for pattern recognition
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            temp_result = np.zeros(len(valid_high))
        
            # Lookback period as per TA-Lib (3 bars for Hikkake pattern)
            lookback_total = 3
            start_idx = lookback_total
        
            if len(valid_high) <= start_idx:
                continue
            
            # Initialize pattern tracking variables
            pattern_idx = 0
            pattern_result = 0
        
            # Warm-up period processing (before start_idx)
            i = start_idx - 3
            while i < start_idx and i < len(valid_high):
                if i >= 2:  # Need at least 2 previous bars
                    if (valid_high[i-1] < valid_high[i-2] and 
                        valid_low[i-1] > valid_low[i-2] and
                        ((valid_high[i] < valid_high[i-1] and valid_low[i] < valid_low[i-1]) or
                         (valid_high[i] > valid_high[i-1] and valid_low[i] > valid_low[i-1]))):
                        pattern_result = 100 * (1 if valid_high[i] < valid_high[i-1] else -1)
                        pattern_idx = i
                    elif (i <= pattern_idx + 3 and
                          ((pattern_result > 0 and valid_close[i] > valid_high[pattern_idx-1]) or
                           (pattern_result < 0 and valid_close[i] < valid_low[pattern_idx-1]))):
                        pattern_idx = 0
                i += 1
        
            # Main calculation loop
            for i in range(start_idx, len(valid_high)):
                if i >= 2:  # Need at least 2 previous bars
                    if (valid_high[i-1] < valid_high[i-2] and 
                        valid_low[i-1] > valid_low[i-2] and
                        ((valid_high[i] < valid_high[i-1] and valid_low[i] < valid_low[i-1]) or
                         (valid_high[i] > valid_high[i-1] and valid_low[i] > valid_low[i-1]))):
                        pattern_result = 100 * (1 if valid_high[i] < valid_high[i-1] else -1)
                        pattern_idx = i
                        temp_result[i] = pattern_result
                    elif (i <= pattern_idx + 3 and
                          ((pattern_result > 0 and valid_close[i] > valid_high[pattern_idx-1]) or
                           (pattern_result < 0 and valid_close[i] < valid_low[pattern_idx-1]))):
                        temp_result[i] = pattern_result + 100 * (1 if pattern_result > 0 else -1)
                        pattern_idx = 0
                    else:
                        temp_result[i] = 0
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= start_idx:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLHIKKAKEMOD(high, open, low, close, vol, oi, near_period=3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib
        lookback_total = near_period + 3
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            temp_result = np.zeros(len(valid_high))
            pattern_idx = 0
            pattern_result = 0
        
            # Pre-calculate NearPeriodTotal for the lookback period
            near_period_total = 0.0
            near_trailing_idx = 0
            if lookback_total - 3 < len(valid_high):
                for i in range(near_trailing_idx, lookback_total - 3):
                    near_period_total += valid_high[i] - valid_low[i]
                near_trailing_idx = lookback_total - 3 - near_period
        
            # Process data before start index (lookback period)
            i = lookback_total - 3
            while i < lookback_total and i < len(valid_high):
                if i >= 2:
                    if (valid_high[i-2] < valid_high[i-3] and valid_low[i-2] > valid_low[i-3] and
                        valid_high[i-1] < valid_high[i-2] and valid_low[i-1] > valid_low[i-2] and
                        ((valid_high[i] < valid_high[i-1] and valid_low[i] < valid_low[i-1] and
                          valid_close[i-2] <= valid_low[i-2] + (near_period_total / near_period))
                         or
                         (valid_high[i] > valid_high[i-1] and valid_low[i] > valid_low[i-1] and
                          valid_close[i-2] >= valid_high[i-2] - (near_period_total / near_period)))):
                        pattern_result = 100 * (1 if valid_high[i] < valid_high[i-1] else -1)
                        pattern_idx = i
                    elif i <= pattern_idx + 3 and (
                        (pattern_result > 0 and valid_close[i] > valid_high[pattern_idx-1]) or
                        (pattern_result < 0 and valid_close[i] < valid_low[pattern_idx-1])):
                        pattern_idx = 0
                
                    if i >= 2 and near_trailing_idx >= 0 and near_trailing_idx < len(valid_high):
                        near_period_total += (valid_high[i-2] - valid_low[i-2]) - (valid_high[near_trailing_idx-2] - valid_low[near_trailing_idx-2]) if near_trailing_idx >= 2 else 0
                        near_trailing_idx += 1
                i += 1
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                if i >= 2:
                    if (valid_high[i-2] < valid_high[i-3] and valid_low[i-2] > valid_low[i-3] and
                        valid_high[i-1] < valid_high[i-2] and valid_low[i-1] > valid_low[i-2] and
                        ((valid_high[i] < valid_high[i-1] and valid_low[i] < valid_low[i-1] and
                          valid_close[i-2] <= valid_low[i-2] + (near_period_total / near_period))
                         or
                         (valid_high[i] > valid_high[i-1] and valid_low[i] > valid_low[i-1] and
                          valid_close[i-2] >= valid_high[i-2] - (near_period_total / near_period)))):
                        pattern_result = 100 * (1 if valid_high[i] < valid_high[i-1] else -1)
                        pattern_idx = i
                        temp_result[i] = pattern_result
                    elif i <= pattern_idx + 3 and (
                        (pattern_result > 0 and valid_close[i] > valid_high[pattern_idx-1]) or
                        (pattern_result < 0 and valid_close[i] < valid_low[pattern_idx-1])):
                        temp_result[i] = pattern_result + 100 * (1 if pattern_result > 0 else -1)
                        pattern_idx = 0
                    else:
                        temp_result[i] = 0
                
                    if i >= 2 and near_trailing_idx >= 0 and near_trailing_idx < len(valid_high):
                        near_period_total += (valid_high[i-2] - valid_low[i-2]) - (valid_high[near_trailing_idx-2] - valid_low[near_trailing_idx-2]) if near_trailing_idx >= 2 else 0
                        near_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLHOMINGPIGEON(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback period as per TA-Lib (2 days for pattern + additional for averages)
        lookback_total = 2
        body_long_period = 10  # Default period for long body average as per TA-Lib
        body_short_period = 10  # Default period for short body average as per TA-Lib
    
        for sec in range(secs):
            # Initialize variables for body averages
            body_long_period_total = 0.0
            body_short_period_total = 0.0
        
            # Calculate initial totals for body averages before start index
            body_long_trailing_idx = lookback_total - body_long_period
            body_short_trailing_idx = lookback_total - body_short_period
        
            for i in range(body_long_trailing_idx, lookback_total):
                if i >= 0:
                    body_long_period_total += abs(open[i, sec] - close[i, sec])
        
            for i in range(body_short_trailing_idx, lookback_total):
                if i >= 0:
                    body_short_period_total += abs(open[i, sec] - close[i, sec])
        
            # Main loop starting from lookback_total
            for i in range(lookback_total, tdts):
                # Check data validity
                if (open[i, sec] != open[i, sec] or close[i, sec] != close[i, sec] or
                    open[i-1, sec] != open[i-1, sec] or close[i-1, sec] != close[i-1, sec]):
                    result[i, sec] = 0
                    continue
            
                # Calculate candle colors (negative for bearish)
                color_prev = -1 if close[i-1, sec] < open[i-1, sec] else 1
                color_curr = -1 if close[i, sec] < open[i, sec] else 1
            
                # Calculate real body sizes
                real_body_prev = abs(close[i-1, sec] - open[i-1, sec])
                real_body_curr = abs(close[i, sec] - open[i, sec])
            
                # Calculate averages for body comparison
                body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0
                body_short_avg = body_short_period_total / body_short_period if body_short_period > 0 else 0
            
                # Check Homing Pigeon pattern conditions
                if (color_prev == -1 and color_curr == -1 and
                    real_body_prev > body_long_avg and
                    real_body_curr <= body_short_avg and
                    open[i, sec] < open[i-1, sec] and
                    close[i, sec] > close[i-1, sec]):
                    result[i, sec] = 100
                else:
                    result[i, sec] = 0
            
                # Update trailing totals for next iteration
                if i - body_long_period >= 0:
                    body_long_period_total += abs(close[i-1, sec] - open[i-1, sec])
                    body_long_period_total -= abs(close[i - body_long_period - 1, sec] - open[i - body_long_period - 1, sec])
                else:
                    body_long_period_total += abs(close[i-1, sec] - open[i-1, sec])
                
                body_short_period_total += abs(close[i, sec] - open[i, sec])
                if i - body_short_period >= 0:
                    body_short_period_total -= abs(close[i - body_short_period, sec] - open[i - body_short_period, sec])
    
        return result



    @staticmethod
    @nb.njit
    def CDLIDENTICAL3CROWS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (3 days for pattern recognition)
        lookback_total = 3
        shadow_very_short_period = 3  # Default period for ShadowVeryShort as per TA-Lib
        equal_period = 3  # Default period for Equal as per TA-Lib
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize arrays for rolling totals
            shadow_very_short_total = np.zeros(3)
            equal_total = np.zeros(3)
        
            # Calculate initial totals for ShadowVeryShort
            shadow_very_short_trailing_idx = 0
            if shadow_very_short_period > 0:
                shadow_very_short_trailing_idx = lookback_total - shadow_very_short_period
                if shadow_very_short_trailing_idx < 0:
                    shadow_very_short_trailing_idx = 0
                
            equal_trailing_idx = 0
            if equal_period > 0:
                equal_trailing_idx = lookback_total - equal_period
                if equal_trailing_idx < 0:
                    equal_trailing_idx = 0
                
            # Initialize ShadowVeryShort totals
            for i in range(shadow_very_short_trailing_idx, lookback_total):
                for tot_idx in range(3):
                    if i - tot_idx >= 0:
                        shadow_very_short_total[tot_idx] += max(valid_high[i - tot_idx] - valid_low[i - tot_idx], 0.0)
        
            # Initialize Equal totals
            for i in range(equal_trailing_idx, lookback_total):
                for tot_idx in range(2, 0, -1):  # Only for indices 2 and 1 as per C code
                    if i - tot_idx >= 0:
                        equal_total[tot_idx] += max(valid_high[i - tot_idx] - valid_low[i - tot_idx], 0.0)
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Calculate candle color (negative for bearish)
                color_2 = -1 if valid_close[i-2] < valid_open[i-2] else 1
                color_1 = -1 if valid_close[i-1] < valid_open[i-1] else 1
                color_0 = -1 if valid_close[i] < valid_open[i] else 1
            
                # Calculate lower shadow
                lower_shadow_2 = valid_open[i-2] - valid_low[i-2] if color_2 == -1 else valid_close[i-2] - valid_low[i-2]
                lower_shadow_1 = valid_open[i-1] - valid_low[i-1] if color_1 == -1 else valid_close[i-1] - valid_low[i-1]
                lower_shadow_0 = valid_open[i] - valid_low[i] if color_0 == -1 else valid_close[i] - valid_low[i]
            
                # Calculate averages for comparison
                shadow_avg_2 = shadow_very_short_total[2] / shadow_very_short_period if shadow_very_short_period > 0 else 0.0
                shadow_avg_1 = shadow_very_short_total[1] / shadow_very_short_period if shadow_very_short_period > 0 else 0.0
                shadow_avg_0 = shadow_very_short_total[0] / shadow_very_short_period if shadow_very_short_period > 0 else 0.0
            
                equal_avg_2 = equal_total[2] / equal_period if equal_period > 0 else 0.0
                equal_avg_1 = equal_total[1] / equal_period if equal_period > 0 else 0.0
            
                # Check conditions for Identical Three Crows pattern
                if (color_2 == -1 and lower_shadow_2 < shadow_avg_2 and
                    color_1 == -1 and lower_shadow_1 < shadow_avg_1 and
                    color_0 == -1 and lower_shadow_0 < shadow_avg_0 and
                    valid_close[i-2] > valid_close[i-1] and
                    valid_close[i-1] > valid_close[i] and
                    valid_open[i-1] <= valid_close[i-2] + equal_avg_2 and
                    valid_open[i-1] >= valid_close[i-2] - equal_avg_2 and
                    valid_open[i] <= valid_close[i-1] + equal_avg_1 and
                    valid_open[i] >= valid_close[i-1] - equal_avg_1):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals for ShadowVeryShort
                for tot_idx in range(2, -1, -1):
                    current_range = max(valid_high[i - tot_idx] - valid_low[i - tot_idx], 0.0) if i - tot_idx >= 0 else 0.0
                    trailing_range = max(valid_high[shadow_very_short_trailing_idx - tot_idx] - valid_low[shadow_very_short_trailing_idx - tot_idx], 0.0) if shadow_very_short_trailing_idx - tot_idx >= 0 else 0.0
                    shadow_very_short_total[tot_idx] += current_range - trailing_range
            
                # Update rolling totals for Equal
                for tot_idx in range(2, 0, -1):
                    current_range = max(valid_high[i - tot_idx] - valid_low[i - tot_idx], 0.0) if i - tot_idx >= 0 else 0.0
                    trailing_range = max(valid_high[equal_trailing_idx - tot_idx] - valid_low[equal_trailing_idx - tot_idx], 0.0) if equal_trailing_idx - tot_idx >= 0 else 0.0
                    equal_total[tot_idx] += current_range - trailing_range
            
                shadow_very_short_trailing_idx += 1
                equal_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLINNECK(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for lookback periods as per TA-Lib defaults
        EqualPeriod = 10
        BodyLongPeriod = 10
        lookbackTotal = max(EqualPeriod, BodyLongPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for Equal and BodyLong ranges
            EqualPeriodTotal = 0.0
            BodyLongPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            EqualTrailingIdx = 0
            BodyLongTrailingIdx = 0
        
            for i in range(lookbackTotal):
                if i < EqualPeriod:
                    EqualPeriodTotal += abs(valid_close[i] - valid_open[i])
                if i < BodyLongPeriod:
                    BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # Main calculation loop
            outIdx = lookbackTotal
            i = lookbackTotal
            while i < len(valid_high):
                if i >= 1:
                    # Check for In Neck pattern
                    # Condition 1: Previous candle is black (bearish)
                    prev_color = -1 if valid_close[i-1] < valid_open[i-1] else 1
                    # Condition 2: Previous candle has long body
                    prev_body = abs(valid_close[i-1] - valid_open[i-1])
                    body_long_avg = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0
                    # Condition 3: Current candle is white (bullish)
                    curr_color = 1 if valid_close[i] > valid_open[i] else -1
                    # Condition 4: Current open below previous low
                    # Condition 5 & 6: Current close between previous close and previous close + equal average
                    equal_avg = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0
                
                    if (prev_color == -1 and 
                        prev_body > body_long_avg and 
                        curr_color == 1 and 
                        valid_open[i] < valid_low[i-1] and 
                        valid_close[i] <= valid_close[i-1] + equal_avg and 
                        valid_close[i] >= valid_close[i-1]):
                        result[valid_indices[i], sec] = -100
                    else:
                        result[valid_indices[i], sec] = 0
                
                    # Update totals for next iteration
                    if i >= EqualPeriod:
                        EqualPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
                        EqualPeriodTotal -= abs(valid_close[EqualTrailingIdx] - valid_open[EqualTrailingIdx])
                        EqualTrailingIdx += 1
                
                    if i >= BodyLongPeriod:
                        BodyLongPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
                        BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                        BodyLongTrailingIdx += 1
            
                i += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLKICKING(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # TA-Lib中定义的lookback周期，BodyLong和ShadowVeryShort的平均周期
        BodyLongPeriod = 10
        ShadowVeryShortPeriod = 3
        lookbackTotal = max(BodyLongPeriod, ShadowVeryShortPeriod)
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 初始化结果数组
            temp_result = np.zeros(len(valid_high))
        
            # 初始化滑动窗口总和
            ShadowVeryShortPeriodTotal = np.zeros(2)
            BodyLongPeriodTotal = np.zeros(2)
        
            # 计算初始的滑动窗口总和
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
            BodyLongTrailingIdx = lookbackTotal - BodyLongPeriod
        
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                ShadowVeryShortPeriodTotal[1] += max(valid_high[i-1] - valid_low[i-1], 0.0) if i > 0 else 0.0
                ShadowVeryShortPeriodTotal[0] += max(valid_high[i] - valid_low[i], 0.0)
        
            for i in range(BodyLongTrailingIdx, lookbackTotal):
                BodyLongPeriodTotal[1] += abs(valid_close[i-1] - valid_open[i-1]) if i > 0 else 0.0
                BodyLongPeriodTotal[0] += abs(valid_close[i] - valid_open[i])
        
            # 主计算循环
            i = lookbackTotal
            while i < len(valid_high):
                # 计算Kicking形态条件
                if i > 0:
                    # 颜色相反
                    color_prev = 1 if valid_close[i-1] > valid_open[i-1] else -1
                    color_curr = 1 if valid_close[i] > valid_open[i] else -1
                
                    # 计算平均值
                    BodyLongAverage1 = BodyLongPeriodTotal[1] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                    BodyLongAverage0 = BodyLongPeriodTotal[0] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                    ShadowVeryShortAverage1 = ShadowVeryShortPeriodTotal[1] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                    ShadowVeryShortAverage0 = ShadowVeryShortPeriodTotal[0] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                
                    # 实体和影线条件
                    realbody_prev = abs(valid_close[i-1] - valid_open[i-1])
                    realbody_curr = abs(valid_close[i] - valid_open[i])
                    uppershadow_prev = valid_high[i-1] - max(valid_close[i-1], valid_open[i-1])
                    lowershadow_prev = min(valid_close[i-1], valid_open[i-1]) - valid_low[i-1]
                    uppershadow_curr = valid_high[i] - max(valid_close[i], valid_open[i])
                    lowershadow_curr = min(valid_close[i], valid_open[i]) - valid_low[i]
                
                    # 跳空条件
                    gap_up = valid_low[i] > valid_high[i-1]
                    gap_down = valid_high[i] < valid_low[i-1]
                
                    if (color_prev == -color_curr and
                        realbody_prev > BodyLongAverage1 and
                        uppershadow_prev < ShadowVeryShortAverage1 and
                        lowershadow_prev < ShadowVeryShortAverage1 and
                        realbody_curr > BodyLongAverage0 and
                        uppershadow_curr < ShadowVeryShortAverage0 and
                        lowershadow_curr < ShadowVeryShortAverage0 and
                        ((color_prev == -1 and gap_up) or (color_prev == 1 and gap_down))):
                        temp_result[i] = color_curr * 100
                    else:
                        temp_result[i] = 0
                else:
                    temp_result[i] = 0
            
                # 更新滑动窗口总和
                for totIdx in range(1, -1, -1):
                    if i - totIdx >= 0:
                        BodyLongPeriodTotal[totIdx] += abs(valid_close[i-totIdx] - valid_open[i-totIdx])
                        if BodyLongTrailingIdx - totIdx >= 0:
                            BodyLongPeriodTotal[totIdx] -= abs(valid_close[BodyLongTrailingIdx-totIdx] - valid_open[BodyLongTrailingIdx-totIdx])
                        ShadowVeryShortPeriodTotal[totIdx] += max(valid_high[i-totIdx] - valid_low[i-totIdx], 0.0)
                        if ShadowVeryShortTrailingIdx - totIdx >= 0:
                            ShadowVeryShortPeriodTotal[totIdx] -= max(valid_high[ShadowVeryShortTrailingIdx-totIdx] - valid_low[ShadowVeryShortTrailingIdx-totIdx], 0.0)
            
                i += 1
                ShadowVeryShortTrailingIdx += 1
                BodyLongTrailingIdx += 1
        
            # 映射结果回原始数组
            for i in range(len(valid_indices)):
                if i >= lookbackTotal:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLKICKINGBYLENGTH(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for averages as per TA-Lib defaults
        ShadowVeryShortPeriod = 2
        BodyLongPeriod = 10
        lookbackTotal = max(ShadowVeryShortPeriod, BodyLongPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize arrays for storing running totals
            ShadowVeryShortPeriodTotal = np.zeros(2)
            BodyLongPeriodTotal = np.zeros(2)
        
            # Initialize trailing indices for rolling window
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
            BodyLongTrailingIdx = lookbackTotal - BodyLongPeriod
        
            # Warm-up period: Calculate initial totals for averages
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                ShadowVeryShortPeriodTotal[1] += max(valid_high[i-1] - valid_close[i-1], valid_open[i-1] - valid_low[i-1]) if i > 0 else 0
                ShadowVeryShortPeriodTotal[0] += max(valid_high[i] - valid_close[i], valid_open[i] - valid_low[i])
        
            for i in range(BodyLongTrailingIdx, lookbackTotal):
                BodyLongPeriodTotal[1] += abs(valid_close[i-1] - valid_open[i-1]) if i > 0 else 0
                BodyLongPeriodTotal[0] += abs(valid_close[i] - valid_open[i])
        
            # Main calculation loop
            i = lookbackTotal
            while i < len(valid_high):
                # Calculate candle properties
                color_i = 1 if valid_close[i] > valid_open[i] else -1
                color_i1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
            
                realbody_i = abs(valid_close[i] - valid_open[i])
                realbody_i1 = abs(valid_close[i-1] - valid_open[i-1])
            
                uppershadow_i = valid_high[i] - max(valid_close[i], valid_open[i])
                lowershadow_i = min(valid_close[i], valid_open[i]) - valid_low[i]
                uppershadow_i1 = valid_high[i-1] - max(valid_close[i-1], valid_open[i-1])
                lowershadow_i1 = min(valid_close[i-1], valid_open[i-1]) - valid_low[i-1]
            
                # Calculate averages
                body_long_avg_i = BodyLongPeriodTotal[0] / BodyLongPeriod if BodyLongPeriod > 0 else 0
                body_long_avg_i1 = BodyLongPeriodTotal[1] / BodyLongPeriod if BodyLongPeriod > 0 else 0
                shadow_short_avg_i = ShadowVeryShortPeriodTotal[0] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0
                shadow_short_avg_i1 = ShadowVeryShortPeriodTotal[1] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0
            
                # Check for kicking pattern conditions
                gap_condition = (color_i1 == -1 and valid_low[i] > valid_high[i-1]) or (color_i1 == 1 and valid_high[i] < valid_low[i-1])
                if (color_i1 == -color_i and
                    realbody_i1 > body_long_avg_i1 and
                    uppershadow_i1 < shadow_short_avg_i1 and
                    lowershadow_i1 < shadow_short_avg_i1 and
                    realbody_i > body_long_avg_i and
                    uppershadow_i < shadow_short_avg_i and
                    lowershadow_i < shadow_short_avg_i and
                    gap_condition):
                    stronger_candle = i if realbody_i > realbody_i1 else i-1
                    stronger_color = 1 if valid_close[stronger_candle] > valid_open[stronger_candle] else -1
                    result[valid_indices[i], sec] = stronger_color * 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update running totals for averages
                for totIdx in range(1, -1, -1):
                    if i - totIdx >= 0 and BodyLongTrailingIdx - totIdx >= 0:
                        BodyLongPeriodTotal[totIdx] += abs(valid_close[i-totIdx] - valid_open[i-totIdx])
                        BodyLongPeriodTotal[totIdx] -= abs(valid_close[BodyLongTrailingIdx-totIdx] - valid_open[BodyLongTrailingIdx-totIdx])
                    if i - totIdx >= 0 and ShadowVeryShortTrailingIdx - totIdx >= 0:
                        ShadowVeryShortPeriodTotal[totIdx] += max(valid_high[i-totIdx] - valid_close[i-totIdx], valid_open[i-totIdx] - valid_low[i-totIdx])
                        ShadowVeryShortPeriodTotal[totIdx] -= max(valid_high[ShadowVeryShortTrailingIdx-totIdx] - valid_close[ShadowVeryShortTrailingIdx-totIdx], valid_open[ShadowVeryShortTrailingIdx-totIdx] - valid_low[ShadowVeryShortTrailingIdx-totIdx])
            
                i += 1
                ShadowVeryShortTrailingIdx += 1
                BodyLongTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLLADDERBOTTOM(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as defined in TA-Lib (4 prior candles + current)
        lookback_total = 4
        shadow_very_short_period = 3  # Default period for shadow calculation as per TA-Lib
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize shadow calculation
            shadow_very_short_total = 0.0
            shadow_trailing_idx = 0
        
            # Warm-up period for shadow calculation
            for i in range(shadow_very_short_period):
                if i < len(valid_high):
                    shadow_very_short_total += valid_high[i] - valid_low[i]
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Calculate candle colors (1 for white, -1 for black)
                color_4 = 1 if valid_close[i-4] > valid_open[i-4] else -1
                color_3 = 1 if valid_close[i-3] > valid_open[i-3] else -1
                color_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate upper shadow for i-1
                upper_shadow_1 = valid_high[i-1] - max(valid_open[i-1], valid_close[i-1])
            
                # Calculate shadow average
                shadow_avg = shadow_very_short_total / shadow_very_short_period if shadow_very_short_period > 0 else 0.0
            
                # Ladder Bottom pattern conditions
                if (color_4 == -1 and color_3 == -1 and color_2 == -1 and  # Three black candles
                    valid_open[i-4] > valid_open[i-3] and valid_open[i-3] > valid_open[i-2] and  # Decreasing opens
                    valid_close[i-4] > valid_close[i-3] and valid_close[i-3] > valid_close[i-2] and  # Decreasing closes
                    color_1 == -1 and  # Fourth black candle
                    upper_shadow_1 > shadow_avg and  # Long upper shadow on fourth candle
                    color_0 == 1 and  # White candle on current day
                    valid_open[i] > valid_open[i-1] and  # Current open above previous open
                    valid_close[i] > valid_high[i-1]):  # Current close above previous high
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update shadow total for next iteration
                if i < len(valid_high):
                    shadow_very_short_total += (valid_high[i] - valid_low[i])
                    if shadow_trailing_idx < len(valid_high):
                        shadow_very_short_total -= (valid_high[shadow_trailing_idx] - valid_low[shadow_trailing_idx])
                    shadow_trailing_idx += 1
                
        return result



    @staticmethod
    @nb.njit
    def CDLMARUBOZU(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyLong and ShadowVeryShort as per TA-Lib defaults
        BodyLongPeriod = 10
        ShadowVeryShortPeriod = 10
        lookbackTotal = max(BodyLongPeriod, ShadowVeryShortPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for rolling averages
            BodyLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for BodyLong and ShadowVeryShort
            BodyLongTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
            startIdx = lookbackTotal
        
            for i in range(BodyLongTrailingIdx, startIdx):
                if i < len(valid_high):
                    # BodyLong range is typically the real body size
                    real_body = abs(valid_close[i] - valid_open[i])
                    BodyLongPeriodTotal += real_body
        
            for i in range(ShadowVeryShortTrailingIdx, startIdx):
                if i < len(valid_high):
                    # ShadowVeryShort range is typically the shadow size
                    upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                    lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
                    ShadowVeryShortPeriodTotal += min(upper_shadow, lower_shadow)
        
            # Main calculation loop
            outIdx = startIdx
            while outIdx < len(valid_high):
                # Calculate real body and shadows for current candle
                real_body = abs(valid_close[outIdx] - valid_open[outIdx])
                upper_shadow = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx])
                lower_shadow = min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
                candle_color = 1 if valid_close[outIdx] > valid_open[outIdx] else -1
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Marubozu condition: long body and very short shadows
                if (real_body > BodyLongAverage and 
                    upper_shadow < ShadowVeryShortAverage and 
                    lower_shadow < ShadowVeryShortAverage):
                    result[valid_indices[outIdx], sec] = candle_color * 100
                else:
                    result[valid_indices[outIdx], sec] = 0
            
                # Update rolling totals
                if outIdx + 1 < len(valid_high):
                    # Add new values
                    new_real_body = abs(valid_close[outIdx] - valid_open[outIdx])
                    new_upper_shadow = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx])
                    new_lower_shadow = min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
                    new_shadow = min(new_upper_shadow, new_lower_shadow)
                
                    BodyLongPeriodTotal += new_real_body
                    ShadowVeryShortPeriodTotal += new_shadow
                
                    # Subtract trailing values
                    if BodyLongTrailingIdx < len(valid_high):
                        old_real_body = abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                        BodyLongPeriodTotal -= old_real_body
                
                    if ShadowVeryShortTrailingIdx < len(valid_high):
                        old_upper_shadow = valid_high[ShadowVeryShortTrailingIdx] - max(valid_open[ShadowVeryShortTrailingIdx], valid_close[ShadowVeryShortTrailingIdx])
                        old_lower_shadow = min(valid_open[ShadowVeryShortTrailingIdx], valid_close[ShadowVeryShortTrailingIdx]) - valid_low[ShadowVeryShortTrailingIdx]
                        old_shadow = min(old_upper_shadow, old_lower_shadow)
                        ShadowVeryShortPeriodTotal -= old_shadow
                
                    BodyLongTrailingIdx += 1
                    ShadowVeryShortTrailingIdx += 1
            
                outIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLMATHOLD(high, open, low, close, vol, oi, penetration=0.5):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for body periods as in TA-Lib
        BODY_SHORT_PERIOD = 5
        BODY_LONG_PERIOD = 5
    
        # Lookback period as per TA-Lib (4 prior candles needed for pattern)
        lookback_total = 4
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize body period totals for short and long
            body_period_total = np.zeros(5)
            body_short_trailing_idx = 0
            body_long_trailing_idx = 0
        
            # Initialize output index
            out_idx = lookback_total
        
            # Pre-calculate initial body totals for short and long periods
            if out_idx >= BODY_SHORT_PERIOD:
                body_short_trailing_idx = out_idx - BODY_SHORT_PERIOD
                for i in range(body_short_trailing_idx, out_idx):
                    body_period_total[3] += abs(valid_close[i-3] - valid_open[i-3]) if i >= 3 else 0.0
                    body_period_total[2] += abs(valid_close[i-2] - valid_open[i-2]) if i >= 2 else 0.0
                    body_period_total[1] += abs(valid_close[i-1] - valid_open[i-1]) if i >= 1 else 0.0
        
            if out_idx >= BODY_LONG_PERIOD:
                body_long_trailing_idx = out_idx - BODY_LONG_PERIOD
                for i in range(body_long_trailing_idx, out_idx):
                    body_period_total[4] += abs(valid_close[i-4] - valid_open[i-4]) if i >= 4 else 0.0
        
            # Main loop for pattern detection
            for i in range(out_idx, len(valid_high)):
                # Calculate real body for comparison
                real_body_4 = abs(valid_close[i-4] - valid_open[i-4]) if i >= 4 else 0.0
                real_body_3 = abs(valid_close[i-3] - valid_open[i-3]) if i >= 3 else 0.0
                real_body_2 = abs(valid_close[i-2] - valid_open[i-2]) if i >= 2 else 0.0
                real_body_1 = abs(valid_close[i-1] - valid_open[i-1]) if i >= 1 else 0.0
            
                # Calculate candle averages
                body_long_avg = body_period_total[4] / BODY_LONG_PERIOD if BODY_LONG_PERIOD > 0 else 0.0
                body_short_avg_3 = body_period_total[3] / BODY_SHORT_PERIOD if BODY_SHORT_PERIOD > 0 else 0.0
                body_short_avg_2 = body_period_total[2] / BODY_SHORT_PERIOD if BODY_SHORT_PERIOD > 0 else 0.0
                body_short_avg_1 = body_period_total[1] / BODY_SHORT_PERIOD if BODY_SHORT_PERIOD > 0 else 0.0
            
                # Check candle colors (1 for bullish, -1 for bearish)
                color_4 = 1 if valid_close[i-4] > valid_open[i-4] else -1 if i >= 4 else 0
                color_3 = 1 if valid_close[i-3] > valid_open[i-3] else -1 if i >= 3 else 0
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Check for gap up between i-4 and i-3
                gap_up_3_4 = valid_open[i-3] > valid_close[i-4] if i >= 4 else False
            
                # Pattern conditions for Mat Hold
                if (real_body_4 > body_long_avg and
                    real_body_3 < body_short_avg_3 and
                    real_body_2 < body_short_avg_2 and
                    real_body_1 < body_short_avg_1 and
                    color_4 == 1 and
                    color_3 == -1 and
                    color_0 == 1 and
                    gap_up_3_4 and
                    min(valid_open[i-2], valid_close[i-2]) < valid_close[i-4] and
                    min(valid_open[i-1], valid_close[i-1]) < valid_close[i-4] and
                    min(valid_open[i-2], valid_close[i-2]) > valid_close[i-4] - real_body_4 * penetration and
                    min(valid_open[i-1], valid_close[i-1]) > valid_close[i-4] - real_body_4 * penetration and
                    max(valid_close[i-2], valid_open[i-2]) < valid_open[i-3] and
                    max(valid_close[i-1], valid_open[i-1]) < max(valid_close[i-2], valid_open[i-2]) and
                    valid_open[i] > valid_close[i-1] and
                    valid_close[i] > max(max(valid_high[i-3], valid_high[i-2]), valid_high[i-1])):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update body period totals
                if i >= 4:
                    body_period_total[4] += abs(valid_close[i-4] - valid_open[i-4])
                    if body_long_trailing_idx < len(valid_high) - 4:
                        body_period_total[4] -= abs(valid_close[body_long_trailing_idx-4] - valid_open[body_long_trailing_idx-4]) if body_long_trailing_idx >= 4 else 0.0
                for tot_idx in range(3, 0, -1):
                    if i >= tot_idx:
                        body_period_total[tot_idx] += abs(valid_close[i-tot_idx] - valid_open[i-tot_idx])
                        if body_short_trailing_idx < len(valid_high) - tot_idx:
                            body_period_total[tot_idx] -= abs(valid_close[body_short_trailing_idx-tot_idx] - valid_open[body_short_trailing_idx-tot_idx]) if body_short_trailing_idx >= tot_idx else 0.0
            
                body_short_trailing_idx += 1
                body_long_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLMORNINGDOJISTAR(high, open, low, close, vol, oi, optInPenetration=0.3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different body types as in TA-Lib
        BodyLongPeriod = 5
        BodyDojiPeriod = 3
        BodyShortPeriod = 5
        lookbackTotal = 2  # Need 3 candles for pattern (i-2, i-1, i)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal + max(BodyLongPeriod, BodyDojiPeriod, BodyShortPeriod):
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for body averages
            BodyLongPeriodTotal = 0.0
            BodyDojiPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
        
            # Calculate initial totals for body ranges
            start_idx = lookbackTotal
            BodyLongTrailingIdx = start_idx - 2 - BodyLongPeriod
            BodyDojiTrailingIdx = start_idx - 1 - BodyDojiPeriod
            BodyShortTrailingIdx = start_idx - BodyShortPeriod
        
            # Initialize totals for BodyLong (i-2)
            i = BodyLongTrailingIdx if BodyLongTrailingIdx >= 0 else 0
            while i < start_idx - 2:
                if i >= 0:
                    BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
                i += 1
            
            # Initialize totals for BodyDoji (i-1)
            i = BodyDojiTrailingIdx if BodyDojiTrailingIdx >= 0 else 0
            while i < start_idx - 1:
                if i >= 0:
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                i += 1
            
            # Initialize totals for BodyShort (i)
            i = BodyShortTrailingIdx if BodyShortTrailingIdx >= 0 else 0
            while i < start_idx:
                if i >= 0:
                    BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
                i += 1
        
            # Main loop for pattern detection
            i = start_idx
            while i < len(valid_high):
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check for Morning Doji Star pattern
                if i >= 2:
                    # First candle (i-2): Long black body
                    realbody2 = abs(valid_close[i-2] - valid_open[i-2])
                    color2 = -1 if valid_close[i-2] < valid_open[i-2] else 1
                
                    # Second candle (i-1): Doji with gap down
                    realbody1 = abs(valid_close[i-1] - valid_open[i-1])
                    gapdown = max(valid_open[i-1], valid_close[i-1]) < min(valid_open[i-2], valid_close[i-2])
                
                    # Third candle (i): White body
                    realbody0 = abs(valid_close[i] - valid_open[i])
                    color0 = 1 if valid_close[i] > valid_open[i] else -1
                
                    # Pattern conditions
                    if (realbody2 > BodyLongAverage and
                        color2 == -1 and
                        realbody1 <= BodyDojiAverage and
                        gapdown and
                        realbody0 > BodyShortAverage and
                        color0 == 1 and
                        valid_close[i] > valid_close[i-2] + realbody2 * optInPenetration):
                        result[valid_indices[i], sec] = 100
                    else:
                        result[valid_indices[i], sec] = 0
            
                # Update totals for next iteration
                if i >= 2:
                    BodyLongPeriodTotal += abs(valid_close[i-2] - valid_open[i-2])
                    if BodyLongTrailingIdx >= 0:
                        BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                    BodyLongTrailingIdx += 1
                
                if i >= 1:
                    BodyDojiPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
                    if BodyDojiTrailingIdx >= 0:
                        BodyDojiPeriodTotal -= abs(valid_close[BodyDojiTrailingIdx] - valid_open[BodyDojiTrailingIdx])
                    BodyDojiTrailingIdx += 1
                
                BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
                if BodyShortTrailingIdx >= 0:
                    BodyShortPeriodTotal -= abs(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx])
                BodyShortTrailingIdx += 1
            
                i += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLMORNINGSTAR(high, open, low, close, vol, oi, penetration=0.3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyLong and BodyShort as per TA-Lib defaults
        BodyLongPeriod = 10
        BodyShortPeriod = 3
        lookbackTotal = 2 + max(BodyLongPeriod, BodyShortPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for body calculations
            BodyLongPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
            BodyShortPeriodTotal2 = 0.0
        
            # Calculate initial totals for BodyLong (i-2 candle)
            BodyLongTrailingIdx = 0
            for i in range(BodyLongTrailingIdx, min(BodyLongPeriod, len(valid_close) - 2)):
                if valid_close[i + 2] == valid_close[i + 2]:
                    BodyLongPeriodTotal += abs(valid_close[i + 2] - valid_open[i + 2])
        
            # Calculate initial totals for BodyShort (i-1 candle and i candle)
            BodyShortTrailingIdx = 0
            for i in range(BodyShortTrailingIdx, min(BodyShortPeriod, len(valid_close) - 1)):
                if valid_close[i + 1] == valid_close[i + 1]:
                    BodyShortPeriodTotal += abs(valid_close[i + 1] - valid_open[i + 1])
                if i < len(valid_close) and valid_close[i] == valid_close[i]:
                    BodyShortPeriodTotal2 += abs(valid_close[i] - valid_open[i])
        
            # Start processing from lookbackTotal
            start_idx = lookbackTotal
            for i in range(start_idx, len(valid_close)):
                # Calculate real body sizes
                realbody_i_2 = abs(valid_close[i - 2] - valid_open[i - 2])
                realbody_i_1 = abs(valid_close[i - 1] - valid_open[i - 1])
                realbody_i = abs(valid_close[i] - valid_open[i])
            
                # Calculate candle colors
                color_i_2 = 1 if valid_close[i - 2] > valid_open[i - 2] else -1
                color_i = 1 if valid_close[i] > valid_open[i] else -1
            
                # Check for gap down between i-2 and i-1
                gap_down = valid_open[i - 1] < valid_close[i - 2] if color_i_2 == -1 else False
            
                # Calculate averages for comparison
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                BodyShortAverage2 = BodyShortPeriodTotal2 / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Morning Star pattern conditions
                if (realbody_i_2 > BodyLongAverage and
                    color_i_2 == -1 and
                    realbody_i_1 <= BodyShortAverage and
                    gap_down and
                    realbody_i > BodyShortAverage2 and
                    color_i == 1 and
                    valid_close[i] > valid_close[i - 2] + realbody_i_2 * penetration):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update trailing totals
                if i - 2 >= BodyLongTrailingIdx + BodyLongPeriod:
                    old_body_long = abs(valid_close[i - 2 - BodyLongPeriod] - valid_open[i - 2 - BodyLongPeriod])
                    new_body_long = abs(valid_close[i - 2] - valid_open[i - 2])
                    BodyLongPeriodTotal += new_body_long - old_body_long
                    BodyLongTrailingIdx += 1
            
                if i - 1 >= BodyShortTrailingIdx + BodyShortPeriod:
                    old_body_short = abs(valid_close[i - 1 - BodyShortPeriod] - valid_open[i - 1 - BodyShortPeriod])
                    new_body_short = abs(valid_close[i - 1] - valid_open[i - 1])
                    BodyShortPeriodTotal += new_body_short - old_body_short
                
                    old_body_short2 = abs(valid_close[i - BodyShortPeriod] - valid_open[i - BodyShortPeriod])
                    new_body_short2 = abs(valid_close[i] - valid_open[i])
                    BodyShortPeriodTotal2 += new_body_short2 - old_body_short2
                    BodyShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLONNECK(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for lookback periods as per TA-Lib defaults
        EqualPeriod = 5  # Default period for Equal candlestick range
        BodyLongPeriod = 10  # Default period for BodyLong candlestick range
        lookbackTotal = max(EqualPeriod, BodyLongPeriod) - 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for moving averages
            EqualPeriodTotal = 0.0
            BodyLongPeriodTotal = 0.0
        
            # Calculate initial totals for Equal and BodyLong ranges
            EqualTrailingIdx = 0
            BodyLongTrailingIdx = 0
        
            for i in range(EqualPeriod - 1):
                if i < len(valid_high) - 1:
                    EqualPeriodTotal += abs(valid_close[i + 1] - valid_open[i + 1])
        
            for i in range(BodyLongPeriod - 1):
                if i < len(valid_high) - 1:
                    BodyLongPeriodTotal += abs(valid_close[i + 1] - valid_open[i + 1])
        
            # Start processing from lookbackTotal
            start_idx = lookbackTotal
            for i in range(start_idx, len(valid_high)):
                # Check if previous day was black (bearish) candle
                prev_color = -1 if valid_close[i - 1] < valid_open[i - 1] else 1
            
                # Calculate real body of previous day
                prev_realbody = abs(valid_close[i - 1] - valid_open[i - 1])
            
                # Calculate current day color (white/bullish)
                curr_color = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate averages
                EqualAverage = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0.0
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
            
                # Check On-Neck pattern conditions
                if (prev_color == -1 and
                    prev_realbody > BodyLongAverage and
                    curr_color == 1 and
                    valid_open[i] < valid_low[i - 1] and
                    valid_close[i] <= valid_low[i - 1] + EqualAverage and
                    valid_close[i] >= valid_low[i - 1] - EqualAverage):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update totals for next iteration
                if i < len(valid_high) - 1:
                    # Add new value and subtract oldest value for Equal
                    if EqualTrailingIdx < len(valid_high) - 1:
                        EqualPeriodTotal += abs(valid_close[i] - valid_open[i])
                        if EqualTrailingIdx < len(valid_high) - EqualPeriod:
                            EqualPeriodTotal -= abs(valid_close[EqualTrailingIdx] - valid_open[EqualTrailingIdx])
                        EqualTrailingIdx += 1
                
                    # Add new value and subtract oldest value for BodyLong
                    if BodyLongTrailingIdx < len(valid_high) - 1:
                        BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
                        if BodyLongTrailingIdx < len(valid_high) - BodyLongPeriod:
                            BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                        BodyLongTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLPIERCING(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # BodyLong period as defined in TA-Lib, typically 10
        BodyLongPeriod = 10
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < BodyLongPeriod:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            piercing_values = np.zeros(len(valid_high))
        
            # Initialize BodyLongPeriodTotal for two periods (current and previous day)
            BodyLongPeriodTotal = np.zeros(2)
            BodyLongTrailingIdx = 0
        
            # Lookback period as per TA-Lib (start after BodyLongPeriod)
            lookbackTotal = BodyLongPeriod
        
            # Initialize trailing sums for BodyLong averages
            if len(valid_high) > lookbackTotal:
                for i in range(BodyLongTrailingIdx, lookbackTotal):
                    BodyLongPeriodTotal[1] += abs(valid_close[i-1] - valid_open[i-1]) if i > 0 else 0
                    BodyLongPeriodTotal[0] += abs(valid_close[i] - valid_open[i])
                BodyLongTrailingIdx = lookbackTotal - BodyLongPeriod
            
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body for current and previous candle
                realbody_prev = abs(valid_close[i-1] - valid_open[i-1])
                realbody_curr = abs(valid_close[i] - valid_open[i])
            
                # Calculate BodyLong averages
                BodyLongAverage_prev = BodyLongPeriodTotal[1] / BodyLongPeriod if BodyLongPeriod > 0 else 0
                BodyLongAverage_curr = BodyLongPeriodTotal[0] / BodyLongPeriod if BodyLongPeriod > 0 else 0
            
                # Piercing pattern conditions
                if (valid_close[i-1] < valid_open[i-1] and  # Bearish previous candle
                    realbody_prev > BodyLongAverage_prev and  # Long body previous
                    valid_close[i] > valid_open[i] and  # Bullish current candle
                    realbody_curr > BodyLongAverage_curr and  # Long body current
                    valid_open[i] < valid_low[i-1] and  # Current opens below previous low
                    valid_close[i] < valid_open[i-1] and  # Current closes below previous open
                    valid_close[i] > valid_close[i-1] + realbody_prev * 0.5):  # Current closes above midpoint of previous body
                    piercing_values[i] = 100
                else:
                    piercing_values[i] = 0
                
                # Update trailing sums for BodyLongPeriodTotal
                for totIdx in range(1, -1, -1):
                    curr_range = abs(valid_close[i-totIdx] - valid_open[i-totIdx])
                    trail_range = abs(valid_close[BodyLongTrailingIdx-totIdx] - valid_open[BodyLongTrailingIdx-totIdx]) if BodyLongTrailingIdx-totIdx >= 0 else 0
                    BodyLongPeriodTotal[totIdx] += curr_range - trail_range
            
                BodyLongTrailingIdx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookbackTotal:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = piercing_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLRISEFALL3METHODS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback period as per TA-Lib (4 periods for the pattern + additional for averages)
        lookback_total = 4 + 5  # 4 for pattern, 5 for BodyLong/BodyShort averages
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize arrays for body period totals (5 periods as in C code)
            body_period_total = np.zeros(5, dtype=np.float64)
            body_short_period = 3  # TA_CANDLEAVGPERIOD(BodyShort)
            body_long_period = 5   # TA_CANDLEAVGPERIOD(BodyLong)
        
            # Calculate initial BodyPeriodTotal for short and long
            body_short_trailing_idx = lookback_total - body_short_period
            body_long_trailing_idx = lookback_total - body_long_period
        
            # Initialize BodyPeriodTotal for short periods (indices 1-3)
            for i in range(body_short_trailing_idx, lookback_total):
                body_period_total[3] += abs(valid_close[i-3] - valid_open[i-3])
                body_period_total[2] += abs(valid_close[i-2] - valid_open[i-2])
                body_period_total[1] += abs(valid_close[i-1] - valid_open[i-1])
        
            # Initialize BodyPeriodTotal for long periods (indices 0 and 4)
            for i in range(body_long_trailing_idx, lookback_total):
                body_period_total[4] += abs(valid_close[i-4] - valid_open[i-4])
                body_period_total[0] += abs(valid_close[i] - valid_open[i])
        
            # Main calculation loop starting from lookback_total
            out_idx = lookback_total
            i = lookback_total
        
            while i < len(valid_high):
                # Calculate real body sizes
                real_body_4 = abs(valid_close[i-4] - valid_open[i-4])
                real_body_3 = abs(valid_close[i-3] - valid_open[i-3])
                real_body_2 = abs(valid_close[i-2] - valid_open[i-2])
                real_body_1 = abs(valid_close[i-1] - valid_open[i-1])
                real_body_0 = abs(valid_close[i] - valid_open[i])
            
                # Calculate candle averages
                avg_body_long_4 = body_period_total[4] / body_long_period if body_long_period > 0 else 0
                avg_body_short_3 = body_period_total[3] / body_short_period if body_short_period > 0 else 0
                avg_body_short_2 = body_period_total[2] / body_short_period if body_short_period > 0 else 0
                avg_body_short_1 = body_period_total[1] / body_short_period if body_short_period > 0 else 0
                avg_body_long_0 = body_period_total[0] / body_long_period if body_long_period > 0 else 0
            
                # Determine candle colors (1 for bullish, -1 for bearish)
                color_4 = 1 if valid_close[i-4] > valid_open[i-4] else -1
                color_3 = 1 if valid_close[i-3] > valid_open[i-3] else -1
                color_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Check pattern conditions as per C code
                if (real_body_4 > avg_body_long_4 and
                    real_body_3 < avg_body_short_3 and
                    real_body_2 < avg_body_short_2 and
                    real_body_1 < avg_body_short_1 and
                    real_body_0 > avg_body_long_0 and
                    color_4 == -color_3 and
                    color_3 == color_2 and
                    color_2 == color_1 and
                    color_1 == -color_0 and
                    min(valid_open[i-3], valid_close[i-3]) < valid_high[i-4] and
                    max(valid_open[i-3], valid_close[i-3]) > valid_low[i-4] and
                    min(valid_open[i-2], valid_close[i-2]) < valid_high[i-4] and
                    max(valid_open[i-2], valid_close[i-2]) > valid_low[i-4] and
                    min(valid_open[i-1], valid_close[i-1]) < valid_high[i-4] and
                    max(valid_open[i-1], valid_close[i-1]) > valid_low[i-4] and
                    valid_close[i-2] * color_4 < valid_close[i-3] * color_4 and
                    valid_close[i-1] * color_4 < valid_close[i-2] * color_4 and
                    valid_open[i] * color_4 > valid_close[i-1] * color_4 and
                    valid_close[i] * color_4 > valid_close[i-4] * color_4):
                    result[valid_indices[i], sec] = 100 * color_4
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update BodyPeriodTotal for next iteration
                body_period_total[4] += abs(valid_close[i-4] - valid_open[i-4]) - abs(valid_close[body_long_trailing_idx-4] - valid_open[body_long_trailing_idx-4])
                body_period_total[3] += abs(valid_close[i-3] - valid_open[i-3]) - abs(valid_close[body_short_trailing_idx-3] - valid_open[body_short_trailing_idx-3])
                body_period_total[2] += abs(valid_close[i-2] - valid_open[i-2]) - abs(valid_close[body_short_trailing_idx-2] - valid_open[body_short_trailing_idx-2])
                body_period_total[1] += abs(valid_close[i-1] - valid_open[i-1]) - abs(valid_close[body_short_trailing_idx-1] - valid_open[body_short_trailing_idx-1])
                body_period_total[0] += abs(valid_close[i] - valid_open[i]) - abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
            
                i += 1
                body_short_trailing_idx += 1
                body_long_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLSEPARATINGLINES(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle characteristics as in TA-Lib
        ShadowVeryShortPeriod = 10
        BodyLongPeriod = 10
        EqualPeriod = 10
        lookbackTotal = max(ShadowVeryShortPeriod, max(BodyLongPeriod, EqualPeriod))
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for averaging
            ShadowVeryShortPeriodTotal = 0.0
            BodyLongPeriodTotal = 0.0
            EqualPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            for i in range(lookbackTotal):
                if i < len(valid_high):
                    # ShadowVeryShort range (high - low for simplicity as in TA-Lib)
                    ShadowVeryShortPeriodTotal += valid_high[i] - valid_low[i]
                    # BodyLong range (absolute body size)
                    BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
                    # Equal range (for open price comparison, using body size of previous candle)
                    if i > 0:
                        EqualPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
        
            # Start processing from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate candle color (1 for bullish, -1 for bearish)
                color_current = 1 if valid_close[i] > valid_open[i] else -1
                color_prev = 1 if valid_close[i-1] > valid_open[i-1] else -1
            
                # Calculate averages
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod
                EqualAverage = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0.0
            
                # Calculate real body and shadows
                real_body_current = abs(valid_close[i] - valid_open[i])
                lower_shadow_current = valid_open[i] - valid_low[i] if color_current == 1 else valid_close[i] - valid_low[i]
                upper_shadow_current = valid_high[i] - valid_close[i] if color_current == 1 else valid_high[i] - valid_open[i]
            
                # Check Separating Lines pattern conditions
                if (color_prev == -color_current and  # Opposite colors
                    valid_open[i] <= valid_open[i-1] + EqualAverage and  # Open prices are close
                    valid_open[i] >= valid_open[i-1] - EqualAverage and
                    real_body_current > BodyLongAverage and  # Current candle has long body
                    ((color_current == 1 and lower_shadow_current < ShadowVeryShortAverage) or  # Bullish with short lower shadow
                     (color_current == -1 and upper_shadow_current < ShadowVeryShortAverage))):  # Bearish with short upper shadow
                    result[valid_indices[i], sec] = color_current * 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update totals for next iteration
                if i < len(valid_high):
                    new_shadow_very_short = valid_high[i] - valid_low[i]
                    new_body_long = abs(valid_close[i] - valid_open[i])
                    new_equal = abs(valid_close[i-1] - valid_open[i-1]) if i > 0 else 0.0
                
                    old_shadow_very_short_idx = i - ShadowVeryShortPeriod
                    old_body_long_idx = i - BodyLongPeriod
                    old_equal_idx = i - EqualPeriod
                
                    old_shadow_very_short = valid_high[old_shadow_very_short_idx] - valid_low[old_shadow_very_short_idx] if old_shadow_very_short_idx >= 0 else 0.0
                    old_body_long = abs(valid_close[old_body_long_idx] - valid_open[old_body_long_idx]) if old_body_long_idx >= 0 else 0.0
                    old_equal = abs(valid_close[old_equal_idx-1] - valid_open[old_equal_idx-1]) if old_equal_idx > 0 else 0.0
                
                    ShadowVeryShortPeriodTotal += new_shadow_very_short - old_shadow_very_short
                    BodyLongPeriodTotal += new_body_long - old_body_long
                    EqualPeriodTotal += new_equal - old_equal
    
        return result



    @staticmethod
    @nb.njit
    def CDLSHOOTINGSTAR(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle components as per TA-Lib defaults
        BodyShortPeriod = 10
        ShadowLongPeriod = 10
        ShadowVeryShortPeriod = 10
        lookbackTotal = max(BodyShortPeriod, ShadowLongPeriod, ShadowVeryShortPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for averaging
            BodyPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyTrailingIdx = 0
            ShadowLongTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
        
            for i in range(lookbackTotal):
                # BodyShort range (real body)
                BodyPeriodTotal += abs(valid_close[i] - valid_open[i])
                # ShadowLong range (upper shadow)
                if valid_close[i] >= valid_open[i]:
                    ShadowLongPeriodTotal += valid_high[i] - valid_close[i]
                else:
                    ShadowLongPeriodTotal += valid_high[i] - valid_open[i]
                # ShadowVeryShort range (lower shadow)
                if valid_close[i] >= valid_open[i]:
                    ShadowVeryShortPeriodTotal += valid_open[i] - valid_low[i]
                else:
                    ShadowVeryShortPeriodTotal += valid_close[i] - valid_low[i]
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
                # Calculate upper shadow
                if valid_close[i] >= valid_open[i]:
                    upper_shadow = valid_high[i] - valid_close[i]
                else:
                    upper_shadow = valid_high[i] - valid_open[i]
                # Calculate lower shadow
                if valid_close[i] >= valid_open[i]:
                    lower_shadow = valid_open[i] - valid_low[i]
                else:
                    lower_shadow = valid_close[i] - valid_low[i]
                # Calculate averages
                body_avg = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                shadow_long_avg = ShadowLongPeriodTotal / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
                shadow_short_avg = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Check for Shooting Star pattern
                if i > 0:
                    # Real body gap up condition
                    real_body_gap_up = min(valid_open[i], valid_close[i]) > max(valid_open[i-1], valid_close[i-1])
                    if (real_body < body_avg and 
                        upper_shadow > shadow_long_avg and 
                        lower_shadow < shadow_short_avg and 
                        real_body_gap_up):
                        result[valid_indices[i], sec] = -100.0
                    else:
                        result[valid_indices[i], sec] = 0.0
                else:
                    result[valid_indices[i], sec] = 0.0
                
                # Update period totals by adding current and subtracting trailing
                # BodyShort update
                BodyPeriodTotal += abs(valid_close[i] - valid_open[i])
                BodyPeriodTotal -= abs(valid_close[BodyTrailingIdx] - valid_open[BodyTrailingIdx])
                BodyTrailingIdx += 1
            
                # ShadowLong update
                if valid_close[i] >= valid_open[i]:
                    ShadowLongPeriodTotal += valid_high[i] - valid_close[i]
                else:
                    ShadowLongPeriodTotal += valid_high[i] - valid_open[i]
                if valid_close[ShadowLongTrailingIdx] >= valid_open[ShadowLongTrailingIdx]:
                    ShadowLongPeriodTotal -= valid_high[ShadowLongTrailingIdx] - valid_close[ShadowLongTrailingIdx]
                else:
                    ShadowLongPeriodTotal -= valid_high[ShadowLongTrailingIdx] - valid_open[ShadowLongTrailingIdx]
                ShadowLongTrailingIdx += 1
            
                # ShadowVeryShort update
                if valid_close[i] >= valid_open[i]:
                    ShadowVeryShortPeriodTotal += valid_open[i] - valid_low[i]
                else:
                    ShadowVeryShortPeriodTotal += valid_close[i] - valid_low[i]
                if valid_close[ShadowVeryShortTrailingIdx] >= valid_open[ShadowVeryShortTrailingIdx]:
                    ShadowVeryShortPeriodTotal -= valid_open[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]
                else:
                    ShadowVeryShortPeriodTotal -= valid_close[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]
                ShadowVeryShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLSPINNINGTOP(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # BodyShort average period as defined in TA-Lib, typically 5
        BodyShortPeriod = 5
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < BodyShortPeriod:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize BodyPeriodTotal for the first window
            BodyPeriodTotal = 0.0
            for i in range(BodyShortPeriod):
                if i < len(valid_high):
                    BodyPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # Start processing from lookback period
            start_idx = BodyShortPeriod
            for i in range(start_idx, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
            
                # Calculate average body size over the period
                BodyAverage = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Calculate upper and lower shadows
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Spinning Top condition:
                # 1. Real body is small (less than average body size)
                # 2. Upper shadow is larger than real body
                # 3. Lower shadow is larger than real body
                if (real_body < BodyAverage and 
                    upper_shadow > real_body and 
                    lower_shadow > real_body):
                    # Determine candle color (positive for bullish, negative for bearish)
                    candle_color = 1 if valid_close[i] > valid_open[i] else -1
                    result[valid_indices[i], sec] = candle_color * 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update BodyPeriodTotal for next iteration
                if i + 1 < len(valid_high):
                    BodyPeriodTotal += abs(valid_close[i] - valid_open[i])
                    BodyPeriodTotal -= abs(valid_close[i - BodyShortPeriod] - valid_open[i - BodyShortPeriod])
    
        return result



    @staticmethod
    @nb.njit
    def CDLSTALLEDPATTERN(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        BodyLongPeriod = 10
        BodyShortPeriod = 5
        ShadowVeryShortPeriod = 7
        NearPeriod = 7
        lookbackTotal = max(BodyLongPeriod, BodyShortPeriod, ShadowVeryShortPeriod, NearPeriod) + 2
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing totals for averaging
            BodyLongPeriodTotal = np.zeros(3)
            NearPeriodTotal = np.zeros(3)
            BodyShortPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Initialize trailing indices
            start_idx = lookbackTotal
            BodyLongTrailingIdx = start_idx - BodyLongPeriod
            BodyShortTrailingIdx = start_idx - BodyShortPeriod
            ShadowVeryShortTrailingIdx = start_idx - ShadowVeryShortPeriod
            NearTrailingIdx = start_idx - NearPeriod
        
            # Warm-up period: Calculate initial totals for averages
            for i in range(BodyLongTrailingIdx, start_idx):
                BodyLongPeriodTotal[2] += abs(valid_close[i-2] - valid_open[i-2]) if i >= 2 else 0.0
                BodyLongPeriodTotal[1] += abs(valid_close[i-1] - valid_open[i-1]) if i >= 1 else 0.0
        
            for i in range(BodyShortTrailingIdx, start_idx):
                BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            for i in range(ShadowVeryShortTrailingIdx, start_idx):
                ShadowVeryShortPeriodTotal += valid_high[i-1] - valid_close[i-1] if valid_close[i-1] > valid_open[i-1] else valid_open[i-1] - valid_close[i-1] if i >= 1 else 0.0
        
            for i in range(NearTrailingIdx, start_idx):
                NearPeriodTotal[2] += abs(valid_close[i-2] - valid_open[i-2]) if i >= 2 else 0.0
                NearPeriodTotal[1] += abs(valid_close[i-1] - valid_open[i-1]) if i >= 1 else 0.0
        
            # Main calculation loop
            i = start_idx
            while i < len(valid_high):
                # Stalled Pattern conditions
                if (valid_close[i-2] > valid_open[i-2] and  # White candle 2 days ago
                    valid_close[i-1] > valid_open[i-1] and  # White candle 1 day ago
                    valid_close[i] > valid_open[i] and      # White candle today
                    valid_close[i] > valid_close[i-1] and valid_close[i-1] > valid_close[i-2] and  # Upward trend
                    abs(valid_close[i-2] - valid_open[i-2]) > BodyLongPeriodTotal[2] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0 and  # Long body 2 days ago
                    abs(valid_close[i-1] - valid_open[i-1]) > BodyLongPeriodTotal[1] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0 and  # Long body 1 day ago
                    (valid_high[i-1] - valid_close[i-1] if valid_close[i-1] > valid_open[i-1] else valid_open[i-1] - valid_close[i-1]) < ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0 and  # Short upper shadow yesterday
                    valid_open[i-1] > valid_open[i-2] and
                    valid_open[i-1] <= valid_close[i-2] + (NearPeriodTotal[2] / NearPeriod if NearPeriod > 0 else 0.0) and
                    abs(valid_close[i] - valid_open[i]) < BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0 and  # Short body today
                    valid_open[i] >= valid_close[i-1] - abs(valid_close[i] - valid_open[i]) - (NearPeriodTotal[1] / NearPeriod if NearPeriod > 0 else 0.0)):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update trailing totals
                for totIdx in range(2, 0, -1):
                    if i - totIdx >= 0 and BodyLongTrailingIdx - totIdx >= 0:
                        BodyLongPeriodTotal[totIdx] += abs(valid_close[i-totIdx] - valid_open[i-totIdx])
                        BodyLongPeriodTotal[totIdx] -= abs(valid_close[BodyLongTrailingIdx-totIdx] - valid_open[BodyLongTrailingIdx-totIdx])
                    if i - totIdx >= 0 and NearTrailingIdx - totIdx >= 0:
                        NearPeriodTotal[totIdx] += abs(valid_close[i-totIdx] - valid_open[i-totIdx])
                        NearPeriodTotal[totIdx] -= abs(valid_close[NearTrailingIdx-totIdx] - valid_open[NearTrailingIdx-totIdx])
            
                if i >= 0 and BodyShortTrailingIdx >= 0:
                    BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
                    BodyShortPeriodTotal -= abs(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx])
            
                if i - 1 >= 0 and ShadowVeryShortTrailingIdx - 1 >= 0:
                    current_shadow = valid_high[i-1] - valid_close[i-1] if valid_close[i-1] > valid_open[i-1] else valid_open[i-1] - valid_close[i-1]
                    trailing_shadow = valid_high[ShadowVeryShortTrailingIdx-1] - valid_close[ShadowVeryShortTrailingIdx-1] if valid_close[ShadowVeryShortTrailingIdx-1] > valid_open[ShadowVeryShortTrailingIdx-1] else valid_open[ShadowVeryShortTrailingIdx-1] - valid_close[ShadowVeryShortTrailingIdx-1]
                    ShadowVeryShortPeriodTotal += current_shadow
                    ShadowVeryShortPeriodTotal -= trailing_shadow
            
                i += 1
                BodyLongTrailingIdx += 1
                BodyShortTrailingIdx += 1
                ShadowVeryShortTrailingIdx += 1
                NearTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLSTICKSANDWICH(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        lookback_total = 2  # As per TA-Lib, lookback for CDLSTICKSANDWICH is 2
        equal_period = 3    # Default period for Equal average as per TA-Lib

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            temp_result = np.zeros(len(valid_high))
        
            # Calculate initial EqualPeriodTotal for the first window
            equal_period_total = 0.0
            equal_trailing_idx = 0
            start_idx = lookback_total
        
            if start_idx < len(valid_high):
                for i in range(equal_trailing_idx, start_idx):
                    if i >= 2:
                        equal_period_total += valid_high[i-2] - valid_low[i-2]
                equal_trailing_idx = start_idx - equal_period
            
                # Main calculation loop
                for i in range(start_idx, len(valid_high)):
                    # Check for Stick Sandwich pattern
                    if i >= 2:
                        # Candle colors: -1 for bearish, 1 for bullish
                        color_2 = -1 if valid_close[i-2] < valid_open[i-2] else 1
                        color_1 = -1 if valid_close[i-1] < valid_open[i-1] else 1
                        color_0 = -1 if valid_close[i] < valid_open[i] else 1
                    
                        # Calculate Equal average
                        equal_avg = equal_period_total / equal_period if equal_period > 0 else 0.0
                    
                        # Pattern conditions
                        if (color_2 == -1 and 
                            color_1 == 1 and 
                            color_0 == -1 and 
                            valid_low[i-1] > valid_close[i-2] and
                            valid_close[i] <= valid_close[i-2] + equal_avg and
                            valid_close[i] >= valid_close[i-2] - equal_avg):
                            temp_result[i] = 100
                        else:
                            temp_result[i] = 0
                    
                        # Update EqualPeriodTotal for next iteration
                        if i < len(valid_high):
                            equal_period_total += (valid_high[i-2] - valid_low[i-2]) if i >= 2 else 0.0
                            equal_period_total -= (valid_high[equal_trailing_idx-2] - valid_low[equal_trailing_idx-2]) if equal_trailing_idx >= 2 else 0.0
                        equal_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= start_idx:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLTASUKIGAP(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as defined in TA-Lib (2 days for pattern recognition)
        lookback_total = 2
        # Near period for averaging candle range, typically 14 in TA-Lib
        near_period = 14
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookback_total:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize NearPeriodTotal for averaging candle range
            near_period_total = 0.0
            near_trailing_idx = 0
            start_idx = lookback_total
        
            # Calculate initial NearPeriodTotal for the first window
            if start_idx >= near_period:
                near_trailing_idx = start_idx - near_period
                for i in range(near_trailing_idx, start_idx):
                    near_period_total += valid_high[i] - valid_low[i]
        
            out_idx = start_idx
            i = start_idx
        
            while i < len(valid_high):
                # Calculate candle color (1 for bullish, -1 for bearish)
                def candle_color(idx):
                    return 1 if valid_close[idx] > valid_open[idx] else -1
            
                # Calculate real body size
                def real_body(idx):
                    return abs(valid_close[idx] - valid_open[idx])
            
                # Calculate candle range
                def candle_range(idx):
                    return valid_high[idx] - valid_low[idx]
            
                # Calculate average for Near period
                near_average = near_period_total / near_period if near_period > 0 else 0.0
            
                # Check for Tasuki Gap pattern
                if i >= 2:
                    # Bullish Tasuki Gap (Upward gap followed by bearish candle)
                    bullish_condition = (
                        valid_open[i-1] > valid_close[i-2] and  # Gap up
                        candle_color(i-1) == 1 and  # Bullish candle on day 1
                        candle_color(i) == -1 and  # Bearish candle on day 2
                        valid_open[i] < valid_close[i-1] and valid_open[i] > valid_open[i-1] and  # Open within previous body
                        valid_close[i] < valid_open[i-1] and  # Close below previous open
                        valid_close[i] > max(valid_close[i-2], valid_open[i-2]) and  # Close above gap
                        abs(real_body(i-1) - real_body(i)) < near_average  # Similar body sizes
                    )
                
                    # Bearish Tasuki Gap (Downward gap followed by bullish candle)
                    bearish_condition = (
                        valid_open[i-1] < valid_close[i-2] and  # Gap down
                        candle_color(i-1) == -1 and  # Bearish candle on day 1
                        candle_color(i) == 1 and  # Bullish candle on day 2
                        valid_open[i] < valid_open[i-1] and valid_open[i] > valid_close[i-1] and  # Open within previous body
                        valid_close[i] > valid_open[i-1] and  # Close above previous open
                        valid_close[i] < min(valid_close[i-2], valid_open[i-2]) and  # Close below gap
                        abs(real_body(i-1) - real_body(i)) < near_average  # Similar body sizes
                    )
                
                    if bullish_condition or bearish_condition:
                        result[valid_indices[i], sec] = candle_color(i-1) * 100
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update NearPeriodTotal for next iteration
                if i + 1 < len(valid_high):
                    near_period_total += candle_range(i) - (candle_range(near_trailing_idx) if near_trailing_idx < len(valid_high) else 0)
                    near_trailing_idx += 1
            
                i += 1
        
        return result



    @staticmethod
    @nb.njit
    def CDLTHRUSTING(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for lookback periods as per TA-Lib
        EqualPeriod = 3
        BodyLongPeriod = 5
        lookbackTotal = max(EqualPeriod, BodyLongPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for Equal and BodyLong periods
            EqualPeriodTotal = 0.0
            BodyLongPeriodTotal = 0.0
        
            # Calculate initial totals for Equal period (range is typically high-low for candlestick)
            EqualTrailingIdx = 0
            for i in range(EqualTrailingIdx, min(EqualPeriod, len(valid_high))):
                if i > 0:
                    EqualPeriodTotal += (valid_high[i-1] - valid_low[i-1])
        
            # Calculate initial totals for BodyLong period (range is typically close-open absolute)
            BodyLongTrailingIdx = 0
            for i in range(BodyLongTrailingIdx, min(BodyLongPeriod, len(valid_high))):
                if i > 0:
                    BodyLongPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
        
            # Start processing from lookbackTotal
            outIdx = lookbackTotal
            i = outIdx
        
            while i < len(valid_high):
                # Calculate candle color and real body for previous day (i-1)
                if i > 0:
                    prev_color = 1 if valid_close[i-1] >= valid_open[i-1] else -1
                    curr_color = 1 if valid_close[i] >= valid_open[i] else -1
                    prev_realbody = abs(valid_close[i-1] - valid_open[i-1])
                    # Calculate averages
                    EqualAverage = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0.0
                    BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                
                    # Thrusting pattern conditions
                    if (prev_color == -1 and
                        prev_realbody > BodyLongAverage and
                        curr_color == 1 and
                        valid_open[i] < valid_low[i-1] and
                        valid_close[i] > valid_close[i-1] + EqualAverage and
                        valid_close[i] <= valid_close[i-1] + prev_realbody * 0.5):
                        result[valid_indices[i], sec] = -100
                    else:
                        result[valid_indices[i], sec] = 0
                
                    # Update totals for next iteration
                    if i >= EqualPeriod:
                        EqualPeriodTotal += (valid_high[i-1] - valid_low[i-1])
                        EqualPeriodTotal -= (valid_high[EqualTrailingIdx-1] - valid_low[EqualTrailingIdx-1]) if EqualTrailingIdx > 0 else 0.0
                        EqualTrailingIdx += 1
                
                    if i >= BodyLongPeriod:
                        BodyLongPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
                        BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx-1] - valid_open[BodyLongTrailingIdx-1]) if BodyLongTrailingIdx > 0 else 0.0
                        BodyLongTrailingIdx += 1
            
                i += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLUNIQUE3RIVER(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback period as per TA-Lib (2 days prior data needed)
        lookback_total = 2
    
        # Define candle body periods as per TA-Lib defaults
        body_long_period = 10
        body_short_period = 10
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing indices for body averages
            start_idx = lookback_total
            body_long_trailing_idx = start_idx - 2 - body_long_period
            body_short_trailing_idx = start_idx - body_short_period
        
            # Initialize period totals for body averages
            body_long_period_total = 0.0
            body_short_period_total = 0.0
        
            # Calculate initial totals for BodyLong
            i = body_long_trailing_idx if body_long_trailing_idx >= 0 else 0
            while i < start_idx - 2 and i < len(valid_high):
                if i >= 0:
                    body_long_period_total += abs(valid_close[i] - valid_open[i])
                i += 1
            
            # Calculate initial totals for BodyShort
            i = body_short_trailing_idx if body_short_trailing_idx >= 0 else 0
            while i < start_idx and i < len(valid_high):
                if i >= 0:
                    body_short_period_total += abs(valid_close[i] - valid_open[i])
                i += 1
            
            # Main calculation loop
            for i in range(start_idx, len(valid_high)):
                # Calculate real body for current and previous candles
                real_body_i_2 = abs(valid_close[i-2] - valid_open[i-2]) if i-2 >= 0 else 0.0
                real_body_i = abs(valid_close[i] - valid_open[i])
            
                # Calculate candle color (1 for bullish, -1 for bearish)
                color_i_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1 if i-2 >= 0 else 0
                color_i_1 = 1 if valid_close[i-1] > valid_open[i-1] else -1 if i-1 >= 0 else 0
                color_i = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate body averages
                body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
                body_short_avg = body_short_period_total / body_short_period if body_short_period > 0 else 0.0
            
                # Check Unique 3 River pattern conditions
                if (real_body_i_2 > body_long_avg and
                    color_i_2 == -1 and
                    color_i_1 == -1 and
                    valid_close[i-1] > valid_close[i-2] and
                    valid_open[i-1] <= valid_open[i-2] and
                    valid_low[i-1] < valid_low[i-2] and
                    real_body_i < body_short_avg and
                    color_i == 1 and
                    valid_open[i] > valid_low[i-1]):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update trailing totals for next iteration
                if i-2 >= 0 and body_long_trailing_idx >= 0 and body_long_trailing_idx < len(valid_high):
                    body_long_period_total += abs(valid_close[i-2] - valid_open[i-2])
                    body_long_period_total -= abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
                if body_short_trailing_idx >= 0 and body_short_trailing_idx < len(valid_high):
                    body_short_period_total += abs(valid_close[i] - valid_open[i])
                    body_short_period_total -= abs(valid_close[body_short_trailing_idx] - valid_open[body_short_trailing_idx])
                
                body_long_trailing_idx += 1
                body_short_trailing_idx += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLUPSIDEGAP2CROWS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyLong and BodyShort as per TA-Lib defaults
        BodyLongPeriod = 10
        BodyShortPeriod = 10
        lookbackTotal = 2  # Need at least 2 previous candles for pattern recognition
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for BodyLong and BodyShort averages
            BodyLongPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
        
            # Calculate initial totals for BodyLong (2 candles back)
            BodyLongTrailingIdx = 0
            if len(valid_close) >= BodyLongPeriod + 2:
                for i in range(BodyLongTrailingIdx, BodyLongPeriod):
                    BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
                BodyLongTrailingIdx = 0
        
            # Calculate initial totals for BodyShort (1 candle back)
            BodyShortTrailingIdx = 0
            if len(valid_close) >= BodyShortPeriod + 1:
                for i in range(BodyShortTrailingIdx, BodyShortPeriod):
                    BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
                BodyShortTrailingIdx = 0
        
            # Start processing from lookbackTotal
            for i in range(lookbackTotal, len(valid_close)):
                # Calculate BodyLong and BodyShort averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check for Upside Gap Two Crows pattern
                if (
                    # First candle (i-2) is white (bullish)
                    valid_close[i-2] > valid_open[i-2] and
                    # First candle has long body
                    abs(valid_close[i-2] - valid_open[i-2]) > BodyLongAverage and
                    # Second candle (i-1) is black (bearish)
                    valid_close[i-1] < valid_open[i-1] and
                    # Second candle has short body
                    abs(valid_close[i-1] - valid_open[i-1]) <= BodyShortAverage and
                    # Gap up between first and second candle
                    valid_open[i-1] > valid_close[i-2] and
                    # Third candle (i) is black (bearish)
                    valid_close[i] < valid_open[i] and
                    # Third candle opens above second candle's open
                    valid_open[i] > valid_open[i-1] and
                    # Third candle closes below second candle's close
                    valid_close[i] < valid_close[i-1] and
                    # Third candle closes above first candle's close
                    valid_close[i] > valid_close[i-2]
                ):
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = -100
                else:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = 0
            
                # Update trailing totals for next iteration
                if i - 2 >= 0 and BodyLongTrailingIdx < len(valid_close):
                    BodyLongPeriodTotal += abs(valid_close[i-2] - valid_open[i-2])
                    if BodyLongTrailingIdx + BodyLongPeriod < len(valid_close):
                        BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                    BodyLongTrailingIdx += 1
            
                if i - 1 >= 0 and BodyShortTrailingIdx < len(valid_close):
                    BodyShortPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
                    if BodyShortTrailingIdx + BodyShortPeriod < len(valid_close):
                        BodyShortPeriodTotal -= abs(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx])
                    BodyShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLXSIDEGAP3METHODS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        lookbackTotal = 2  # As per C code, need 2 previous candles for calculation
    
        for sec in range(secs):
            for ts in range(lookbackTotal, tdts):
                # Data validation: ensure current and previous 2 candles have valid data
                if (high[ts, sec] != high[ts, sec] or
                    open[ts, sec] != open[ts, sec] or
                    low[ts, sec] != low[ts, sec] or
                    close[ts, sec] != close[ts, sec] or
                    high[ts-1, sec] != high[ts-1, sec] or
                    open[ts-1, sec] != open[ts-1, sec] or
                    low[ts-1, sec] != low[ts-1, sec] or
                    close[ts-1, sec] != close[ts-1, sec] or
                    high[ts-2, sec] != high[ts-2, sec] or
                    open[ts-2, sec] != open[ts-2, sec] or
                    low[ts-2, sec] != low[ts-2, sec] or
                    close[ts-2, sec] != close[ts-2, sec]):
                    continue
            
                # Calculate candle colors (1 for bullish, -1 for bearish)
                color_i_2 = 1 if close[ts-2, sec] > open[ts-2, sec] else -1
                color_i_1 = 1 if close[ts-1, sec] > open[ts-1, sec] else -1
                color_i = 1 if close[ts, sec] > open[ts, sec] else -1
            
                # Check if first two candles have same color and third is opposite
                if color_i_2 == color_i_1 and color_i_1 == -color_i:
                    # Check if current open is between previous candle's open and close
                    prev_max = max(close[ts-1, sec], open[ts-1, sec])
                    prev_min = min(close[ts-1, sec], open[ts-1, sec])
                    if open[ts, sec] < prev_max and open[ts, sec] > prev_min:
                        # Check if current close is between candle from 2 periods ago's open and close
                        prev2_max = max(close[ts-2, sec], open[ts-2, sec])
                        prev2_min = min(close[ts-2, sec], open[ts-2, sec])
                        if close[ts, sec] < prev2_max and close[ts, sec] > prev2_min:
                            # Check for gap conditions based on color of first candle
                            if color_i_2 == 1:
                                # For bullish first candle, check for gap up between i-2 and i-1
                                gap_up = min(open[ts-1, sec], close[ts-1, sec]) > max(open[ts-2, sec], close[ts-2, sec])
                                if gap_up:
                                    result[ts, sec] = color_i_2 * 100
                                else:
                                    result[ts, sec] = 0
                            else:
                                # For bearish first candle, check for gap down between i-2 and i-1
                                gap_down = max(open[ts-1, sec], close[ts-1, sec]) < min(open[ts-2, sec], close[ts-2, sec])
                                if gap_down:
                                    result[ts, sec] = color_i_2 * 100
                                else:
                                    result[ts, sec] = 0
                        else:
                            result[ts, sec] = 0
                    else:
                        result[ts, sec] = 0
                else:
                    result[ts, sec] = 0
    
        return result



    @staticmethod
    @nb.njit
    def DX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            # Lookback total includes timeperiod and unstable period (25 as per TA-Lib)
            lookback_total = timeperiod + 25 if timeperiod > 1 else 2
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for DX values
            dx_values = np.zeros(len(valid_high))
        
            # Initialize variables
            prev_minus_dm = 0.0
            prev_plus_dm = 0.0
            prev_tr = 0.0
            prev_high = valid_high[0]
            prev_low = valid_low[0]
            prev_close = valid_close[0]
        
            # First loop: Warm-up period to accumulate initial sums (timeperiod-1 iterations)
            for i in range(1, timeperiod):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
            
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
            
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm += diff_m
                elif diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm += diff_p
            
                # True Range calculation
                tr = max(valid_high[i] - valid_low[i], 
                         max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr += tr
                prev_close = valid_close[i]
        
            # Second loop: Unstable period processing (26 iterations as per TA-Lib)
            unstable_period = 25 + 1
            for i in range(timeperiod, timeperiod + unstable_period):
                if i >= len(valid_high):
                    break
                
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
            
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
            
                prev_minus_dm -= prev_minus_dm / timeperiod
                prev_plus_dm -= prev_plus_dm / timeperiod
            
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm += diff_m
                elif diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm += diff_p
            
                # True Range calculation
                tr = max(valid_high[i] - valid_low[i], 
                         max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                prev_close = valid_close[i]
        
            # Calculate first DX value after warm-up and unstable period
            start_idx = timeperiod + unstable_period - 1
            if start_idx < len(valid_high):
                if prev_tr > 1e-10:
                    minus_di = 100.0 * (prev_minus_dm / prev_tr)
                    plus_di = 100.0 * (prev_plus_dm / prev_tr)
                    temp_real = minus_di + plus_di
                    if temp_real > 1e-10:
                        dx_values[start_idx] = 100.0 * (abs(minus_di - plus_di) / temp_real)
                    else:
                        dx_values[start_idx] = 0.0
                else:
                    dx_values[start_idx] = 0.0
        
            # Main loop: Calculate remaining DX values
            for i in range(start_idx + 1, len(valid_high)):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
            
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
            
                prev_minus_dm -= prev_minus_dm / timeperiod
                prev_plus_dm -= prev_plus_dm / timeperiod
            
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm += diff_m
                elif diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm += diff_p
            
                # True Range calculation
                tr = max(valid_high[i] - valid_low[i], 
                         max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                prev_close = valid_close[i]
            
                if prev_tr > 1e-10:
                    minus_di = 100.0 * (prev_minus_dm / prev_tr)
                    plus_di = 100.0 * (prev_plus_dm / prev_tr)
                    temp_real = minus_di + plus_di
                    if temp_real > 1e-10:
                        dx_values[i] = 100.0 * (abs(minus_di - plus_di) / temp_real)
                    else:
                        dx_values[i] = dx_values[i-1]
                else:
                    dx_values[i] = dx_values[i-1]
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = dx_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def HT_TRENDLINE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        lookback_total = 63  # As defined in C code with unstable period
        smooth_price_size = 64  # Size for circular buffer simulation
    
        for sec in range(secs):
            # Data validation mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            valid_close = close[valid_mask, sec]
            output = np.array([np.float64(np.nan)] * len(valid_close))
        
            # Initialize variables for WMA calculation
            trailing_wma_idx = 0
            today = trailing_wma_idx
            period_wma_sub = 0.0
            period_wma_sum = 0.0
            trailing_wma_value = 0.0
        
            # Initial WMA setup for first 3 points
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub = temp_real
                period_wma_sum = temp_real
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sum += temp_real * 2.0
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sum += temp_real * 3.0
        
            # WMA for next 34 points as in C code
            for i in range(34):
                if today < len(valid_close):
                    temp_real = valid_close[today]
                    today += 1
                    period_wma_sub += temp_real
                    period_wma_sub -= trailing_wma_value
                    period_wma_sum += temp_real * 4.0
                    if trailing_wma_idx < len(valid_close):
                        trailing_wma_value = valid_close[trailing_wma_idx]
                        trailing_wma_idx += 1
                    smoothed_value = period_wma_sum * 0.1
                    period_wma_sum -= period_wma_sub
        
            # Hilbert Transform variables
            hilbert_idx = 0
            detrender_even = np.zeros(3)
            detrender_odd = np.zeros(3)
            q1_even = np.zeros(3)
            q1_odd = np.zeros(3)
            ji_even = np.zeros(3)
            ji_odd = np.zeros(3)
            jq_even = np.zeros(3)
            jq_odd = np.zeros(3)
        
            period = 0.0
            smooth_period = 0.0
            prev_i2 = 0.0
            prev_q2 = 0.0
            re = 0.0
            im = 0.0
            i1_for_odd_prev3 = 0.0
            i1_for_odd_prev2 = 0.0
            i1_for_even_prev3 = 0.0
            i1_for_even_prev2 = 0.0
        
            # Circular buffer for smooth price
            smooth_price = np.zeros(smooth_price_size)
            smooth_price_idx = 0
        
            rad2deg = 45.0 / np.arctan(1.0)
            i_trend1 = 0.0
            i_trend2 = 0.0
            i_trend3 = 0.0
        
            out_idx = 0
        
            while today <= len(valid_close) - 1:
                if today < len(valid_close):
                    today_value = valid_close[today]
                    period_wma_sub += today_value
                    period_wma_sub -= trailing_wma_value
                    period_wma_sum += today_value * 4.0
                    if trailing_wma_idx < len(valid_close):
                        trailing_wma_value = valid_close[trailing_wma_idx]
                        trailing_wma_idx += 1
                    smoothed_value = period_wma_sum * 0.1
                    period_wma_sum -= period_wma_sub
                
                    smooth_price[smooth_price_idx] = smoothed_value
                
                    adjusted_prev_period = (0.075 * period) + 0.54
                
                    if today % 2 == 0:
                        # Even index processing
                        detrender = (0.0962 * smoothed_value + 0.5769 * detrender_even[2] - 0.5769 * detrender_even[0] - 0.0962 * detrender_even[1])
                        q1 = (0.0962 * detrender + 0.5769 * q1_even[2] - 0.5769 * q1_even[0] - 0.0962 * q1_even[1])
                        ji = (0.0962 * i1_for_even_prev3 + 0.5769 * ji_even[2] - 0.5769 * ji_even[0] - 0.0962 * ji_even[1])
                        jq = (0.0962 * q1 + 0.5769 * jq_even[2] - 0.5769 * jq_even[0] - 0.0962 * jq_even[1])
                    
                        detrender_even[0] = detrender_even[1]
                        detrender_even[1] = detrender_even[2]
                        detrender_even[2] = detrender
                    
                        q1_even[0] = q1_even[1]
                        q1_even[1] = q1_even[2]
                        q1_even[2] = q1
                    
                        ji_even[0] = ji_even[1]
                        ji_even[1] = ji_even[2]
                        ji_even[2] = ji
                    
                        jq_even[0] = jq_even[1]
                        jq_even[1] = jq_even[2]
                        jq_even[2] = jq
                    
                        hilbert_idx += 1
                        if hilbert_idx == 3:
                            hilbert_idx = 0
                        
                        q2 = (0.2 * (q1 + ji)) + (0.8 * prev_q2)
                        i2 = (0.2 * (i1_for_even_prev3 - jq)) + (0.8 * prev_i2)
                        i1_for_odd_prev3 = i1_for_odd_prev2
                        i1_for_odd_prev2 = detrender
                    else:
                        # Odd index processing
                        detrender = (-0.091 * smoothed_value + 0.369 * detrender_odd[2] + 0.7199 * detrender_odd[1] - 0.369 * detrender_odd[0])
                        q1 = (-0.091 * detrender + 0.369 * q1_odd[2] + 0.7199 * q1_odd[1] - 0.369 * q1_odd[0])
                        ji = (-0.091 * i1_for_odd_prev3 + 0.369 * ji_odd[2] + 0.7199 * ji_odd[1] - 0.369 * ji_odd[0])
                        jq = (-0.091 * q1 + 0.369 * jq_odd[2] + 0.7199 * jq_odd[1] - 0.369 * jq_odd[0])
                    
                        detrender_odd[0] = detrender_odd[1]
                        detrender_odd[1] = detrender_odd[2]
                        detrender_odd[2] = detrender
                    
                        q1_odd[0] = q1_odd[1]
                        q1_odd[1] = q1_odd[2]
                        q1_odd[2] = q1
                    
                        ji_odd[0] = ji_odd[1]
                        ji_odd[1] = ji_odd[2]
                        ji_odd[2] = ji
                    
                        jq_odd[0] = jq_odd[1]
                        jq_odd[1] = jq_odd[2]
                        jq_odd[2] = jq
                    
                        q2 = (0.2 * (q1 + ji)) + (0.8 * prev_q2)
                        i2 = (0.2 * (i1_for_odd_prev3 - jq)) + (0.8 * prev_i2)
                        i1_for_even_prev3 = i1_for_even_prev2
                        i1_for_even_prev2 = detrender
                
                    re = (0.2 * ((i2 * prev_i2) + (q2 * prev_q2))) + (0.8 * re)
                    im = (0.2 * ((i2 * prev_q2) - (q2 * prev_i2))) + (0.8 * im)
                    prev_q2 = q2
                    prev_i2 = i2
                
                    temp_real = period
                    if im != 0.0 and re != 0.0:
                        period = 360.0 / (np.arctan(im / re) * rad2deg)
                    temp_real2 = 1.5 * temp_real
                    if period > temp_real2:
                        period = temp_real2
                    temp_real2 = 0.67 * temp_real
                    if period < temp_real2:
                        period = temp_real2
                    if period < 6:
                        period = 6
                    elif period > 50:
                        period = 50
                    period = (0.2 * period) + (0.8 * temp_real)
                    smooth_period = (0.33 * period) + (0.67 * smooth_period)
                
                    dc_period = smooth_period + 0.5
                    dc_period_int = int(dc_period)
                    idx = today
                    temp_real = 0.0
                    for i in range(dc_period_int):
                        if idx - i >= 0:
                            temp_real += valid_close[idx - i]
                    if dc_period_int > 0:
                        temp_real = temp_real / dc_period_int
                
                    temp_real2 = (4.0 * temp_real + 3.0 * i_trend1 + 2.0 * i_trend2 + i_trend3) / 10.0
                    i_trend3 = i_trend2
                    i_trend2 = i_trend1
                    i_trend1 = temp_real
                
                    if today >= lookback_total:
                        output[out_idx] = temp_real2
                        out_idx += 1
                
                    smooth_price_idx = (smooth_price_idx + 1) % smooth_price_size
                    today += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total and i - lookback_total < len(output):
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = output[i - lookback_total]
    
        return result



    @staticmethod
    @nb.njit
    def LINEARREG(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Precompute constants for linear regression
            SumX = timeperiod * (timeperiod - 1) * 0.5
            SumXSqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            Divisor = SumX * SumX - timeperiod * SumXSqr
        
            # Calculate linear regression for each valid position
            start_idx = timeperiod - 1
            for i in range(start_idx, len(valid_close)):
                SumXY = 0.0
                SumY = 0.0
                for j in range(timeperiod):
                    temp_value = valid_close[i - j]
                    SumY += temp_value
                    SumXY += j * temp_value
            
                # Calculate slope (m) and intercept (b)
                m = (timeperiod * SumXY - SumX * SumY) / Divisor
                b = (SumY - m * SumX) / timeperiod
            
                # Calculate the regression value at the last point of the window
                reg_value = b + m * (timeperiod - 1)
            
                # Map back to original index
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = reg_value
    
        return result



    @staticmethod
    @nb.njit
    def LINEARREG_ANGLE(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        PI = 3.141592653589793
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Pre-calculate constants for linear regression
            SumX = timeperiod * (timeperiod - 1) * 0.5
            SumXSqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            Divisor = SumX * SumX - timeperiod * SumXSqr
        
            # Start index matches TA-Lib lookback
            start_idx = timeperiod - 1
        
            # Calculate linear regression angle
            for i in range(start_idx, len(valid_close)):
                SumXY = 0.0
                SumY = 0.0
            
                # Calculate sums for current window
                for j in range(timeperiod):
                    temp_value = valid_close[i - j]
                    SumY += temp_value
                    SumXY += j * temp_value
            
                # Calculate slope (m)
                if Divisor != 0:
                    m = (timeperiod * SumXY - SumX * SumY) / Divisor
                    # Convert slope to angle in degrees
                    angle = np.arctan(m) * (180.0 / PI)
                else:
                    angle = 0.0
                
                # Map result back to original array
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = angle
    
        return result



    @staticmethod
    @nb.njit
    def LINEARREG_INTERCEPT(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Pre-calculate constants for linear regression
            SumX = timeperiod * (timeperiod - 1) * 0.5
            SumXSqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            Divisor = SumX * SumX - timeperiod * SumXSqr
        
            # Start index for output (matches TA-Lib lookback)
            start_idx = timeperiod - 1
            if start_idx >= len(valid_close):
                continue
            
            # Main calculation loop
            for today in range(start_idx, len(valid_close)):
                SumXY = 0.0
                SumY = 0.0
            
                # Calculate sums for current window
                for i in range(timeperiod):
                    tempValue = valid_close[today - i]
                    SumY += tempValue
                    SumXY += i * tempValue
            
                # Calculate slope (m)
                m = (timeperiod * SumXY - SumX * SumY) / Divisor
            
                # Calculate intercept
                intercept = (SumY - m * SumX) / timeperiod
            
                # Map result back to original array
                orig_idx = valid_indices[today]
                result[orig_idx, sec] = intercept
    
        return result



    @staticmethod
    @nb.njit
    def LINEARREG_SLOPE(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Pre-calculate constants as per C code
            SumX = timeperiod * (timeperiod - 1) * 0.5
            SumXSqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            Divisor = SumX * SumX - timeperiod * SumXSqr
        
            # Calculate linear regression slope
            slope_values = np.zeros(len(valid_close))
            start_idx = timeperiod - 1
        
            for today in range(start_idx, len(valid_close)):
                SumXY = 0.0
                SumY = 0.0
                for i in range(timeperiod):
                    tempValue = valid_close[today - i]
                    SumY += tempValue
                    SumXY += i * tempValue
                slope_values[today] = (timeperiod * SumXY - SumX * SumY) / Divisor
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = slope_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MAXINDEX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if high[i, sec] == high[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
        
            # Initialize output array for max index values
            maxindex_values = np.zeros(len(valid_high))
        
            # Set lookback period as per C code
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed if nb_initial_element_needed < len(valid_high) else len(valid_high) - 1
        
            if start_idx >= len(valid_high):
                continue
            
            out_idx = 0
            today = start_idx
            trailing_idx = today - nb_initial_element_needed
            highest_idx = -1
            highest = 0.0
        
            while today < len(valid_high):
                tmp = valid_high[today]
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_high[highest_idx]
                    i = highest_idx
                    while i < today + 1:
                        tmp_val = valid_high[i]
                        if tmp_val > highest:
                            highest_idx = i
                            highest = tmp_val
                        i += 1
                elif tmp >= highest:
                    highest_idx = today
                    highest = tmp
                
                if out_idx < len(maxindex_values):
                    maxindex_values[out_idx] = highest_idx
                    out_idx += 1
                
                trailing_idx += 1
                today += 1
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                if i - start_idx < len(maxindex_values):
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = maxindex_values[i - start_idx]
    
        return result



    @staticmethod
    @nb.njit
    def MEDPRICE(high, open, low, close, vol, oi):
        """
        MEDPRICE - Median Price
        Calculates the median price as the average of high and low prices for each period.
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create a mask for valid data
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            # Get valid data indices
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) == 0:
                continue
            
            # Extract valid high and low data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Calculate median price as (high + low) / 2
            medprice_values = np.zeros(len(valid_high))
            for i in range(len(valid_high)):
                medprice_values[i] = (valid_high[i] + valid_low[i]) / 2.0
        
            # Map results back to the original array
            for i in range(len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = medprice_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MFI(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        unstable_period = 25  # TA-Lib default unstable period for MFI
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec] and
                    vol[i, sec] == vol[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod + unstable_period:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
            valid_vol = vol[valid_mask, sec]
        
            # Initialize output array for MFI values
            mfi_values = np.zeros(len(valid_high))
        
            # Initialize circular buffer simulation for positive and negative money flow
            pos_mf_buffer = np.zeros(timeperiod)
            neg_mf_buffer = np.zeros(timeperiod)
            buffer_idx = 0
        
            # Initialize sums for positive and negative money flow
            pos_sum_mf = 0.0
            neg_sum_mf = 0.0
        
            # Calculate lookback total as in TA-Lib
            lookback_total = timeperiod + unstable_period
            start_idx = lookback_total
        
            # Initialize previous typical price
            today = 0
            prev_value = (valid_high[today] + valid_low[today] + valid_close[today]) / 3.0
            today += 1
        
            # Warm-up period: First timeperiod points
            for i in range(timeperiod):
                temp_value1 = (valid_high[today] + valid_low[today] + valid_close[today]) / 3.0
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                temp_value1 *= valid_vol[today]
                today += 1
            
                if temp_value2 < 0:
                    neg_mf_buffer[buffer_idx] = temp_value1
                    pos_mf_buffer[buffer_idx] = 0.0
                    neg_sum_mf += temp_value1
                elif temp_value2 > 0:
                    pos_mf_buffer[buffer_idx] = temp_value1
                    neg_mf_buffer[buffer_idx] = 0.0
                    pos_sum_mf += temp_value1
                else:
                    pos_mf_buffer[buffer_idx] = 0.0
                    neg_mf_buffer[buffer_idx] = 0.0
                
                buffer_idx = (buffer_idx + 1) % timeperiod
        
            # Process until start_idx (unstable period)
            while today < start_idx:
                pos_sum_mf -= pos_mf_buffer[buffer_idx]
                neg_sum_mf -= neg_mf_buffer[buffer_idx]
            
                temp_value1 = (valid_high[today] + valid_low[today] + valid_close[today]) / 3.0
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                temp_value1 *= valid_vol[today]
                today += 1
            
                if temp_value2 < 0:
                    neg_mf_buffer[buffer_idx] = temp_value1
                    pos_mf_buffer[buffer_idx] = 0.0
                    neg_sum_mf += temp_value1
                elif temp_value2 > 0:
                    pos_mf_buffer[buffer_idx] = temp_value1
                    neg_mf_buffer[buffer_idx] = 0.0
                    pos_sum_mf += temp_value1
                else:
                    pos_mf_buffer[buffer_idx] = 0.0
                    neg_mf_buffer[buffer_idx] = 0.0
                
                buffer_idx = (buffer_idx + 1) % timeperiod
        
            # Main calculation loop
            out_idx = start_idx
            while today < len(valid_high):
                pos_sum_mf -= pos_mf_buffer[buffer_idx]
                neg_sum_mf -= neg_mf_buffer[buffer_idx]
            
                temp_value1 = (valid_high[today] + valid_low[today] + valid_close[today]) / 3.0
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                temp_value1 *= valid_vol[today]
                today += 1
            
                if temp_value2 < 0:
                    neg_mf_buffer[buffer_idx] = temp_value1
                    pos_mf_buffer[buffer_idx] = 0.0
                    neg_sum_mf += temp_value1
                elif temp_value2 > 0:
                    pos_mf_buffer[buffer_idx] = temp_value1
                    neg_mf_buffer[buffer_idx] = 0.0
                    pos_sum_mf += temp_value1
                else:
                    pos_mf_buffer[buffer_idx] = 0.0
                    neg_mf_buffer[buffer_idx] = 0.0
                
                temp_total = pos_sum_mf + neg_sum_mf
                if temp_total < 1.0:
                    mfi_values[out_idx] = 0.0
                else:
                    mfi_values[out_idx] = 100.0 * (pos_sum_mf / temp_total)
                
                buffer_idx = (buffer_idx + 1) % timeperiod
                out_idx += 1
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = mfi_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MIDPOINT(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Calculate MIDPOINT
            midpoint_values = np.zeros(len(valid_close))
            nb_initial_element_needed = timeperiod - 1
        
            for today in range(nb_initial_element_needed, len(valid_close)):
                trailing_idx = today - nb_initial_element_needed
                lowest = valid_close[trailing_idx]
                highest = lowest
                for i in range(trailing_idx + 1, today + 1):
                    tmp = valid_close[i]
                    if tmp < lowest:
                        lowest = tmp
                    elif tmp > highest:
                        highest = tmp
                midpoint_values[today] = (highest + lowest) / 2.0
        
            # Map results back to original array
            start_idx = nb_initial_element_needed
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = midpoint_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MIDPRICE(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Initialize output array for valid data
            midprice_values = np.zeros(len(valid_high))
        
            # Set lookback period as per C code
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed
        
            # Main calculation loop
            out_idx = 0
            today = start_idx
            while today < len(valid_high):
                trailing_idx = today - nb_initial_element_needed
                lowest = valid_low[trailing_idx]
                highest = valid_high[trailing_idx]
                trailing_idx += 1
            
                for i in range(trailing_idx, today + 1):
                    tmp_low = valid_low[i]
                    if tmp_low < lowest:
                        lowest = tmp_low
                    tmp_high = valid_high[i]
                    if tmp_high > highest:
                        highest = tmp_high
            
                midprice_values[today] = (highest + lowest) / 2.0
                out_idx += 1
                today += 1
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = midprice_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MININDEX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if low[i, sec] == low[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_low = low[valid_mask, sec]
        
            # Initialize variables for MININDEX calculation
            nb_initial_needed = timeperiod - 1
            start_idx = nb_initial_needed if nb_initial_needed < len(valid_low) else len(valid_low) - 1
            out_idx = 0
            today = start_idx
            trailing_idx = today - nb_initial_needed
            lowest_idx = -1
            lowest = 0.0
            minindex_values = np.zeros(len(valid_low))
        
            while today < len(valid_low):
                tmp = valid_low[today]
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_low[lowest_idx]
                    i = lowest_idx
                    while i <= today:
                        tmp_val = valid_low[i]
                        if tmp_val < lowest:
                            lowest_idx = i
                            lowest = tmp_val
                        i += 1
                elif tmp <= lowest:
                    lowest_idx = today
                    lowest = tmp
                
                minindex_values[today] = lowest_idx
                trailing_idx += 1
                today += 1
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = minindex_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MINMAXINDEX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result_max = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_min = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize output arrays for max and min indices
            out_max_idx = np.zeros(len(valid_close))
            out_min_idx = np.zeros(len(valid_close))
        
            # Set initial lookback period
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed if nb_initial_element_needed < len(valid_close) else len(valid_close) - 1
        
            if start_idx >= len(valid_close):
                continue
            
            out_idx = 0
            today = start_idx
            trailing_idx = start_idx - nb_initial_element_needed
            highest_idx = -1
            highest = 0.0
            lowest_idx = -1
            lowest = 0.0
        
            while today < len(valid_close):
                tmp_low = valid_close[today]
                tmp_high = valid_close[today]
            
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_close[highest_idx]
                    i = highest_idx
                    while i <= today:
                        tmp_high = valid_close[i]
                        if tmp_high > highest:
                            highest_idx = i
                            highest = tmp_high
                        i += 1
                elif tmp_high >= highest:
                    highest_idx = today
                    highest = tmp_high
                
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_close[lowest_idx]
                    i = lowest_idx
                    while i <= today:
                        tmp_low = valid_close[i]
                        if tmp_low < lowest:
                            lowest_idx = i
                            lowest = tmp_low
                        i += 1
                elif tmp_low <= lowest:
                    lowest_idx = today
                    lowest = tmp_low
                
                if out_idx < len(out_max_idx):
                    out_max_idx[out_idx] = valid_indices[highest_idx] if highest_idx >= 0 else np.nan
                    out_min_idx[out_idx] = valid_indices[lowest_idx] if lowest_idx >= 0 else np.nan
                out_idx += 1
                trailing_idx += 1
                today += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= start_idx:
                    orig_idx = valid_indices[i]
                    result_max[orig_idx, sec] = out_max_idx[i - start_idx]
                    result_min[orig_idx, sec] = out_min_idx[i - start_idx]
    
        return result_max, result_min



    @staticmethod
    @nb.njit
    def MINUS_DI(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        unstable_period = 25  # TA-Lib default unstable period for MINUS_DI
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod + unstable_period:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for this security
            minus_di_values = np.zeros(len(valid_high))
        
            # Handle special case when timeperiod <= 1
            if timeperiod <= 1:
                prev_high = valid_high[0]
                prev_low = valid_low[0]
                prev_close = valid_close[0]
                for i in range(1, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                    if diff_m > 0 and diff_p < diff_m:
                        tr = max(valid_high[i] - valid_low[i], 
                                max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                        if tr > 1e-10:
                            minus_di_values[i] = diff_m / tr
                        else:
                            minus_di_values[i] = 0.0
                    else:
                        minus_di_values[i] = 0.0
                    prev_close = valid_close[i]
            else:
                # Initialize variables
                prev_minus_dm = 0.0
                prev_tr = 0.0
                prev_high = valid_high[0]
                prev_low = valid_low[0]
                prev_close = valid_close[0]
            
                # First loop: Warm-up period to accumulate initial sums
                for i in range(1, timeperiod):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
                    tr = max(valid_high[i] - valid_low[i], 
                            max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                    prev_tr += tr
                    prev_close = valid_close[i]
            
                # Second loop: Unstable period processing
                for i in range(timeperiod, timeperiod + unstable_period):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                    prev_minus_dm = prev_minus_dm - (prev_minus_dm / timeperiod)
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
                    tr = max(valid_high[i] - valid_low[i], 
                            max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                    prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                    prev_close = valid_close[i]
            
                # Set first output value after unstable period
                if prev_tr > 1e-10:
                    minus_di_values[timeperiod + unstable_period - 1] = 100.0 * (prev_minus_dm / prev_tr)
                else:
                    minus_di_values[timeperiod + unstable_period - 1] = 0.0
            
                # Main loop: Calculate remaining values
                for i in range(timeperiod + unstable_period, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                    prev_minus_dm = prev_minus_dm - (prev_minus_dm / timeperiod)
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
                    tr = max(valid_high[i] - valid_low[i], 
                            max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                    prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                    prev_close = valid_close[i]
                    if prev_tr > 1e-10:
                        minus_di_values[i] = 100.0 * (prev_minus_dm / prev_tr)
                    else:
                        minus_di_values[i] = 0.0
        
            # Map results back to original array
            start_idx = timeperiod + unstable_period - 1 if timeperiod > 1 else 1
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = minus_di_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MINUS_DM(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        unstable_period = 25  # TA-Lib default unstable period for MINUS_DM
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod + unstable_period - 1:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Initialize output array for valid data
            minus_dm_values = np.zeros(len(valid_high))
        
            # Handle special case when timeperiod <= 1
            if timeperiod <= 1:
                prev_high = valid_high[0]
                prev_low = valid_low[0]
                for i in range(1, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    if diff_m > 0 and diff_p < diff_m:
                        minus_dm_values[i] = diff_m
                    else:
                        minus_dm_values[i] = 0
                start_idx = 1
            else:
                # Initialize variables
                prev_minus_dm = 0.0
                prev_high = valid_high[0]
                prev_low = valid_low[0]
            
                # First loop: Sum up initial Minus DM values for first timeperiod-1 periods
                for i in range(1, timeperiod):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
            
                # Second loop: Handle unstable period
                for i in range(timeperiod, timeperiod + unstable_period):
                    if i >= len(valid_high):
                        break
                    
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    prev_minus_dm -= prev_minus_dm / timeperiod
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
            
                # Set the first output value after unstable period
                start_idx = timeperiod + unstable_period - 1
                if start_idx < len(valid_high):
                    minus_dm_values[start_idx] = prev_minus_dm
            
                # Main loop: Calculate remaining Minus DM values
                for i in range(start_idx + 1, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    prev_minus_dm -= prev_minus_dm / timeperiod
                    if diff_m > 0 and diff_p < diff_m:
                        prev_minus_dm += diff_m
                    
                    minus_dm_values[i] = prev_minus_dm
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = minus_dm_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MOM(high, open, low, close, vol, oi, timeperiod=10):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Calculate MOM
            mom_values = np.zeros(len(valid_close))
            for i in range(timeperiod, len(valid_close)):
                mom_values[i] = valid_close[i] - valid_close[i - timeperiod]
        
            # Map results back to original array
            start_idx = timeperiod
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = mom_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def NATR(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Calculate True Range (TR)
            tr_values = np.zeros(len(valid_high))
            tr_values[0] = valid_high[0] - valid_low[0]
            for i in range(1, len(valid_high)):
                tr_1 = valid_high[i] - valid_low[i]
                tr_2 = abs(valid_close[i-1] - valid_high[i])
                tr_3 = abs(valid_close[i-1] - valid_low[i])
                tr_values[i] = max(tr_1, tr_2, tr_3)
        
            # Handle special case when timeperiod <= 1
            if timeperiod <= 1:
                for i in range(len(valid_indices)):
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = tr_values[i] * 100.0 / valid_close[i] if valid_close[i] > 1e-10 else 0.0
                continue
        
            # Calculate ATR using Wilder smoothing
            atr_values = np.zeros(len(valid_high))
            first_atr = 0.0
            for i in range(timeperiod):
                first_atr += tr_values[i]
            first_atr /= timeperiod
            atr_values[timeperiod-1] = first_atr
        
            # Unstable period handling as per TA-Lib
            unstable_period = 25  # TA_GLOBALS_UNSTABLE_PERIOD for NATR
            for i in range(timeperiod, timeperiod + unstable_period):
                if i < len(tr_values):
                    atr_values[i] = (atr_values[i-1] * (timeperiod - 1) + tr_values[i]) / timeperiod
        
            # Main calculation loop for ATR
            for i in range(timeperiod + unstable_period, len(tr_values)):
                atr_values[i] = (atr_values[i-1] * (timeperiod - 1) + tr_values[i]) / timeperiod
        
            # Calculate NATR = (ATR / Close) * 100
            start_idx = timeperiod - 1
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                if valid_close[i] > 1e-10:
                    result[orig_idx, sec] = (atr_values[i] / valid_close[i]) * 100.0
                else:
                    result[orig_idx, sec] = 0.0
    
        return result



    @staticmethod
    @nb.njit
    def OBV(high, open, low, close, vol, oi):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (close[i, sec] == close[i, sec] and 
                    vol[i, sec] == vol[i, sec]):
                    valid_mask[i] = True
        
            # Get valid indices and data
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 1:
                continue
            
            valid_close = close[valid_mask, sec]
            valid_vol = vol[valid_mask, sec]
        
            # Initialize OBV calculation
            obv_values = np.zeros(len(valid_close))
            prev_obv = valid_vol[0]
            prev_close = valid_close[0]
            obv_values[0] = prev_obv
        
            # Calculate OBV for each valid data point
            for i in range(1, len(valid_close)):
                current_close = valid_close[i]
                if current_close > prev_close:
                    prev_obv += valid_vol[i]
                elif current_close < prev_close:
                    prev_obv -= valid_vol[i]
                obv_values[i] = prev_obv
                prev_close = current_close
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = obv_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def PLUS_DI(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        unstable_period = 25  # TA-Lib default unstable period for PLUS_DI
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod + unstable_period:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize variables
            prev_plus_dm = 0.0
            prev_tr = 0.0
            prev_high = valid_high[0]
            prev_low = valid_low[0]
            prev_close = valid_close[0]
        
            # Handle timeperiod <= 1 case
            if timeperiod <= 1:
                for i in range(1, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    # True Range calculation
                    tr = max(valid_high[i] - valid_low[i], 
                             max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                    prev_close = valid_close[i]
                
                    if (diff_p > 0) and (diff_p > diff_m):
                        if tr > 1e-10:
                            result[valid_indices[i], sec] = diff_p / tr
                        else:
                            result[valid_indices[i], sec] = 0.0
                    else:
                        result[valid_indices[i], sec] = 0.0
                continue
        
            # First loop: Initialize PlusDM and TR sums for first timeperiod-1 points
            sum_plus_dm = 0.0
            sum_tr = 0.0
            for i in range(1, timeperiod):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
            
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
            
                if (diff_p > 0) and (diff_p > diff_m):
                    sum_plus_dm += diff_p
                
                # True Range calculation
                tr = max(valid_high[i] - valid_low[i], 
                         max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                sum_tr += tr
                prev_close = valid_close[i]
        
            # Set initial smoothed values
            prev_plus_dm = sum_plus_dm
            prev_tr = sum_tr
        
            # Second loop: Handle unstable period
            for i in range(timeperiod, timeperiod + unstable_period):
                if i >= len(valid_high):
                    break
                
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
            
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
            
                prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod)
                if (diff_p > 0) and (diff_p > diff_m):
                    prev_plus_dm += diff_p
                
                # True Range calculation
                tr = max(valid_high[i] - valid_low[i], 
                         max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                prev_close = valid_close[i]
        
            # Set first output value after unstable period
            start_idx = timeperiod + unstable_period - 1
            if start_idx < len(valid_high):
                if prev_tr > 1e-10:
                    result[valid_indices[start_idx], sec] = 100.0 * (prev_plus_dm / prev_tr)
                else:
                    result[valid_indices[start_idx], sec] = 0.0
        
            # Main loop: Calculate remaining PLUS_DI values
            for i in range(start_idx + 1, len(valid_high)):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
            
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
            
                prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod)
                if (diff_p > 0) and (diff_p > diff_m):
                    prev_plus_dm += diff_p
                
                # True Range calculation
                tr = max(valid_high[i] - valid_low[i], 
                         max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                prev_close = valid_close[i]
            
                if prev_tr > 1e-10:
                    result[valid_indices[i], sec] = 100.0 * (prev_plus_dm / prev_tr)
                else:
                    result[valid_indices[i], sec] = 0.0
    
        return result



    @staticmethod
    @nb.njit
    def PLUS_DM(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        unstable_period = 25  # TA-Lib default unstable period for PLUS_DM
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod + unstable_period - 1:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Initialize output array for this security
            plus_dm_values = np.zeros(len(valid_high))
        
            # Handle lookback and start index as per TA-Lib
            lookback_total = timeperiod + unstable_period - 1 if timeperiod > 1 else 1
            start_idx = lookback_total if timeperiod > 1 else 0
        
            # Case for timeperiod <= 1
            if timeperiod <= 1:
                prev_high = valid_high[0]
                prev_low = valid_low[0]
                for i in range(1, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    if diff_p > 0 and diff_p > diff_m:
                        plus_dm_values[i] = diff_p
                    else:
                        plus_dm_values[i] = 0
            else:
                # Initialize variables
                prev_plus_dm = 0.0
                prev_high = valid_high[0]
                prev_low = valid_low[0]
            
                # First loop: Sum up PlusDM for the first timeperiod-1 periods
                for i in range(1, timeperiod):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    if diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm += diff_p
            
                # Second loop: Handle unstable period
                for i in range(timeperiod, timeperiod + unstable_period):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    prev_plus_dm -= prev_plus_dm / timeperiod
                    if diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm += diff_p
            
                # Set the first output value after lookback
                if timeperiod + unstable_period - 1 < len(valid_high):
                    plus_dm_values[timeperiod + unstable_period - 1] = prev_plus_dm
            
                # Main loop: Calculate remaining PlusDM values
                for i in range(timeperiod + unstable_period, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    prev_plus_dm -= prev_plus_dm / timeperiod
                    if diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm += diff_p
                    
                    plus_dm_values[i] = prev_plus_dm
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = plus_dm_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def ROC(high, open, low, close, vol, oi, timeperiod=10):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Calculate ROC
            roc_values = np.zeros(len(valid_close))
            start_idx = timeperiod
        
            for i in range(start_idx, len(valid_close)):
                trailing_idx = i - timeperiod
                temp_real = valid_close[trailing_idx]
                if temp_real != 0.0:
                    roc_values[i] = ((valid_close[i] / temp_real) - 1.0) * 100.0
                else:
                    roc_values[i] = 0.0
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = roc_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def ROCP(high, open, low, close, vol, oi, timeperiod=10):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for this security
            roc_values = np.zeros(len(valid_close))
        
            # Set start index based on timeperiod
            start_idx = timeperiod
            if start_idx >= len(valid_close):
                continue
            
            # Calculate ROCP
            for i in range(start_idx, len(valid_close)):
                trailing_idx = i - timeperiod
                temp_real = valid_close[trailing_idx]
                if temp_real != 0.0:
                    roc_values[i] = (valid_close[i] - temp_real) / temp_real
                else:
                    roc_values[i] = 0.0
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = roc_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def ROCR(high, open, low, close, vol, oi, timeperiod=10):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create mask for valid data
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid close data
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            rocr_values = np.zeros(len(valid_close))
        
            # Calculate ROCR starting from timeperiod
            start_idx = timeperiod
            for i in range(start_idx, len(valid_close)):
                trailing_idx = i - timeperiod
                temp_real = valid_close[trailing_idx]
                if temp_real != 0.0:
                    rocr_values[i] = valid_close[i] / temp_real
                else:
                    rocr_values[i] = 0.0
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = rocr_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def ROCR100(high, open, low, close, vol, oi, timeperiod=10):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            rocr100_values = np.zeros(len(valid_close))
        
            # Set start index based on timeperiod
            start_idx = timeperiod
            if start_idx >= len(valid_close):
                continue
            
            # Calculate ROCR100
            out_idx = start_idx
            trailing_idx = 0
        
            while out_idx < len(valid_close):
                temp_real = valid_close[trailing_idx]
                if temp_real != 0.0:
                    rocr100_values[out_idx] = (valid_close[out_idx] / temp_real) * 100.0
                else:
                    rocr100_values[out_idx] = 0.0
                out_idx += 1
                trailing_idx += 1
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = rocr100_values[i]
    
        return result


    @staticmethod
    @nb.njit
    def RSI(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize variables
            lookback_total = timeperiod
            start_idx = lookback_total if timeperiod > 1 else 0
        
            if len(valid_close) <= start_idx:
                continue
            
            # Special case for timeperiod = 1
            if timeperiod == 1:
                for i in range(start_idx, len(valid_close)):
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = valid_close[i]
                continue
            
            # Initialize variables for RSI calculation
            today = 0
            prev_value = valid_close[today]
            prev_gain = 0.0
            prev_loss = 0.0
        
            # First loop: Calculate initial gains and losses
            today += 1
            for i in range(timeperiod):
                temp_value1 = valid_close[today]
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                if temp_value2 < 0:
                    prev_loss -= temp_value2
                else:
                    prev_gain += temp_value2
                today += 1
        
            # Calculate initial averages
            prev_loss /= timeperiod
            prev_gain /= timeperiod
        
            # Handle data before start_idx (warm-up period)
            while today < start_idx and today < len(valid_close):
                temp_value1 = valid_close[today]
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                prev_loss *= (timeperiod - 1)
                prev_gain *= (timeperiod - 1)
                if temp_value2 < 0:
                    prev_loss -= temp_value2
                else:
                    prev_gain += temp_value2
                prev_loss /= timeperiod
                prev_gain /= timeperiod
                today += 1
        
            # Main calculation loop
            for i in range(today, len(valid_close)):
                temp_value1 = valid_close[i]
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                prev_loss *= (timeperiod - 1)
                prev_gain *= (timeperiod - 1)
                if temp_value2 < 0:
                    prev_loss -= temp_value2
                else:
                    prev_gain += temp_value2
                prev_loss /= timeperiod
                prev_gain /= timeperiod
            
                temp_value1 = prev_gain + prev_loss
                rsi_value = 0.0
                if temp_value1 > 1e-10:
                    rsi_value = 100.0 * (prev_gain / temp_value1)
            
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = rsi_value
    
        return result



    @staticmethod
    @nb.njit
    def SAREXT(high, open, low, close, vol, oi, startvalue=0.0, offsetonreverse=0.0, 
               accelerationinitlong=0.02, accelerationlong=0.02, accelerationmaxlong=0.2,
               accelerationinitshort=0.02, accelerationshort=0.02, accelerationmaxshort=0.2):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 2:  # Need at least 2 points to start
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Initialize parameters
            af_long = accelerationinitlong
            af_short = accelerationinitshort
            if af_long > accelerationmaxlong:
                af_long = accelerationinitlong = accelerationmaxlong
            if accelerationlong > accelerationmaxlong:
                accelerationlong = accelerationmaxlong
            if af_short > accelerationmaxshort:
                af_short = accelerationinitshort = accelerationmaxshort
            if accelerationshort > accelerationmaxshort:
                accelerationshort = accelerationmaxshort
            
            # Determine initial direction
            is_long = 0
            if startvalue == 0.0:
                if valid_high[1] - valid_low[1] > 0:
                    is_long = 0
                else:
                    is_long = 1
            elif startvalue > 0:
                is_long = 1
            else:
                is_long = 0
            
            # Initialize SAR and EP
            today_idx = 1
            new_high = valid_high[0]
            new_low = valid_low[0]
        
            if startvalue == 0.0:
                if is_long == 1:
                    ep = valid_high[today_idx]
                    sar = new_low
                else:
                    ep = valid_low[today_idx]
                    sar = new_high
            elif startvalue > 0:
                ep = valid_high[today_idx]
                sar = startvalue
            else:
                ep = valid_low[today_idx]
                sar = abs(startvalue)
            
            new_low = valid_low[today_idx]
            new_high = valid_high[today_idx]
            sar_values = np.zeros(len(valid_high))
        
            # Main calculation loop
            out_idx = 0
            while today_idx < len(valid_high):
                prev_low = new_low
                prev_high = new_high
                new_low = valid_low[today_idx]
                new_high = valid_high[today_idx]
                today_idx += 1
            
                if is_long == 1:
                    if new_low <= sar:
                        is_long = 0
                        sar = ep
                        if sar < prev_high:
                            sar = prev_high
                        if sar < new_high:
                            sar = new_high
                        if offsetonreverse != 0.0:
                            sar += sar * offsetonreverse
                        sar_values[out_idx] = -sar
                        out_idx += 1
                        af_short = accelerationinitshort
                        ep = new_low
                        sar = sar + af_short * (ep - sar)
                        if sar < prev_high:
                            sar = prev_high
                        if sar < new_high:
                            sar = new_high
                    else:
                        sar_values[out_idx] = sar
                        out_idx += 1
                        if new_high > ep:
                            ep = new_high
                            af_long += accelerationlong
                            if af_long > accelerationmaxlong:
                                af_long = accelerationmaxlong
                        sar = sar + af_long * (ep - sar)
                        if sar > prev_low:
                            sar = prev_low
                        if sar > new_low:
                            sar = new_low
                else:
                    if new_high >= sar:
                        is_long = 1
                        sar = ep
                        if sar > prev_low:
                            sar = prev_low
                        if sar > new_low:
                            sar = new_low
                        if offsetonreverse != 0.0:
                            sar -= sar * offsetonreverse
                        sar_values[out_idx] = sar
                        out_idx += 1
                        af_long = accelerationinitlong
                        ep = new_high
                        sar = sar + af_long * (ep - sar)
                        if sar > prev_low:
                            sar = prev_low
                        if sar > new_low:
                            sar = new_low
                    else:
                        sar_values[out_idx] = -sar
                        out_idx += 1
                        if new_low < ep:
                            ep = new_low
                            af_short += accelerationshort
                            if af_short > accelerationmaxshort:
                                af_short = accelerationmaxshort
                        sar = sar + af_short * (ep - sar)
                        if sar < prev_high:
                            sar = prev_high
                        if sar < new_high:
                            sar = new_high
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i > 0:  # Start from second point as per TA-Lib
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = sar_values[i-1]
    
        return result



    @staticmethod
    @nb.njit
    def STDDEV(high, open, low, close, vol, oi, timeperiod=5, nbdev=1.0):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Calculate moving average for valid data
            mov_avg = np.zeros(len(valid_close))
            for i in range(timeperiod - 1, len(valid_close)):
                sum_val = 0.0
                for j in range(i - timeperiod + 1, i + 1):
                    sum_val += valid_close[j]
                mov_avg[i] = sum_val / timeperiod
        
            # Calculate standard deviation using precalculated moving average
            stddev_values = np.zeros(len(valid_close))
            for out_idx in range(timeperiod - 1, len(valid_close)):
                start_sum = out_idx - timeperiod + 1
                end_sum = out_idx
                period_total2 = 0.0
            
                # Calculate sum of squared values for the current window
                for k in range(start_sum, end_sum + 1):
                    temp_real = valid_close[k]
                    period_total2 += temp_real * temp_real
            
                mean_value2 = period_total2 / timeperiod
                temp_real = mov_avg[out_idx]
                mean_value2 -= temp_real * temp_real
            
                if mean_value2 > 1e-10:
                    stddev_values[out_idx] = np.sqrt(mean_value2)
                    if nbdev != 1.0:
                        stddev_values[out_idx] *= nbdev
                else:
                    stddev_values[out_idx] = 0.0
        
            # Map results back to original array
            for i in range(timeperiod - 1, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = stddev_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def TRANGE(high, open, low, close, vol, oi):
        """
        TRANGE - True Range
        True Range is the greatest of the following:
        - High of the current period minus low of the current period
        - Absolute value of high of the current period minus close of the previous period
        - Absolute value of low of the current period minus close of the previous period
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 1:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Calculate True Range values
            tr_values = np.zeros(len(valid_high))
            for i in range(1, len(valid_high)):
                temp_lt = valid_low[i]
                temp_ht = valid_high[i]
                temp_cy = valid_close[i-1]
                greatest = temp_ht - temp_lt
                val2 = abs(temp_cy - temp_ht)
                if val2 > greatest:
                    greatest = val2
                val3 = abs(temp_cy - temp_lt)
                if val3 > greatest:
                    greatest = val3
                tr_values[i] = greatest
        
            # Map results back to original array
            for i in range(1, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = tr_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def TRIX(high, open, low, close, vol, oi, timeperiod=30):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Calculate lookback periods as per TA-Lib
        ema_lookback = timeperiod - 1
        roc_lookback = 1
        total_lookback = (ema_lookback * 3) + roc_lookback
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= total_lookback:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Calculate EMA smoothing factor
            k = 2.0 / (timeperiod + 1.0)
        
            # First EMA
            temp_buffer = np.zeros(len(valid_close))
            for i in range(len(valid_close)):
                if i == 0:
                    temp_buffer[i] = valid_close[i]
                else:
                    temp_buffer[i] = temp_buffer[i-1] + k * (valid_close[i] - temp_buffer[i-1])
        
            # Second EMA
            temp_buffer2 = np.zeros(len(valid_close))
            for i in range(len(valid_close)):
                if i == 0:
                    temp_buffer2[i] = temp_buffer[i]
                else:
                    temp_buffer2[i] = temp_buffer2[i-1] + k * (temp_buffer[i] - temp_buffer2[i-1])
        
            # Third EMA
            temp_buffer3 = np.zeros(len(valid_close))
            for i in range(len(valid_close)):
                if i == 0:
                    temp_buffer3[i] = temp_buffer2[i]
                else:
                    temp_buffer3[i] = temp_buffer3[i-1] + k * (temp_buffer2[i] - temp_buffer3[i-1])
        
            # Calculate ROC (Rate of Change) on triple EMA
            trix_values = np.zeros(len(valid_close))
            for i in range(1, len(valid_close)):
                if temp_buffer3[i-1] > 1e-10:
                    trix_values[i] = 100.0 * (temp_buffer3[i] - temp_buffer3[i-1]) / temp_buffer3[i-1]
                else:
                    trix_values[i] = 0.0
        
            # Map results back to original array
            start_idx = total_lookback
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = trix_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def TSF(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for this security
            tsf_values = np.zeros(len(valid_close))
        
            # Calculate lookback period (start index)
            lookback_total = timeperiod - 1
            start_idx = lookback_total
        
            # Pre-calculate constants for linear regression
            sum_x = timeperiod * (timeperiod - 1) * 0.5
            sum_x_sqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            divisor = sum_x * sum_x - timeperiod * sum_x_sqr
        
            # Main calculation loop
            for today in range(start_idx, len(valid_close)):
                sum_xy = 0.0
                sum_y = 0.0
            
                # Calculate sums for linear regression
                for i in range(timeperiod):
                    temp_value = valid_close[today - i]
                    sum_y += temp_value
                    sum_xy += i * temp_value
            
                # Calculate slope (m) and intercept (b)
                m = (timeperiod * sum_xy - sum_x * sum_y) / divisor
                b = (sum_y - m * sum_x) / timeperiod
            
                # Calculate forecast value
                tsf_values[today] = b + m * timeperiod
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = tsf_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def TYPPRICE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create a mask for valid data
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            # Get valid data indices
            valid_indices = np.where(valid_mask)[0]
        
            # Skip if no valid data
            if len(valid_indices) == 0:
                continue
        
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Calculate TYPPRICE for valid data
            typprice_values = np.zeros(len(valid_high))
            for i in range(len(valid_high)):
                typprice_values[i] = (valid_high[i] + valid_low[i] + valid_close[i]) / 3.0
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = typprice_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def VAR(high, open, low, close, vol, oi, timeperiod=5):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize variables for calculation
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed if nb_initial_element_needed < len(valid_close) else len(valid_close) - 1
        
            if start_idx >= len(valid_close):
                continue
            
            # Initialize period totals for warm-up
            period_total1 = 0.0
            period_total2 = 0.0
            trailing_idx = start_idx - nb_initial_element_needed
        
            # Warm-up period: calculate initial sums
            i = trailing_idx
            while i < start_idx and i < len(valid_close):
                temp_real = valid_close[i]
                period_total1 += temp_real
                period_total2 += temp_real * temp_real
                i += 1
        
            # Main calculation loop
            out_idx = start_idx
            while out_idx < len(valid_close):
                temp_real = valid_close[out_idx]
                period_total1 += temp_real
                period_total2 += temp_real * temp_real
            
                mean_value1 = period_total1 / timeperiod
                mean_value2 = period_total2 / timeperiod
            
                # Subtract the oldest value for sliding window
                if trailing_idx < len(valid_close):
                    temp_real = valid_close[trailing_idx]
                    period_total1 -= temp_real
                    period_total2 -= temp_real * temp_real
                    trailing_idx += 1
            
                # Calculate variance
                variance = mean_value2 - mean_value1 * mean_value1
                if out_idx < len(valid_indices):
                    orig_idx = valid_indices[out_idx]
                    result[orig_idx, sec] = variance
            
                out_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def WCLPRICE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) == 0:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Calculate WCLPRICE for valid data
            wclprice_values = np.zeros(len(valid_high))
            for i in range(len(valid_high)):
                wclprice_values[i] = (valid_high[i] + valid_low[i] + (valid_close[i] * 2.0)) / 4.0
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = wclprice_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def WILLR(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            willr_values = np.zeros(len(valid_high))
            nb_initial_needed = timeperiod - 1
            start_idx = nb_initial_needed if nb_initial_needed < len(valid_high) else len(valid_high) - 1
        
            if start_idx >= len(valid_high):
                continue
            
            out_idx = 0
            today = start_idx
            trailing_idx = today - nb_initial_needed
            lowest_idx = -1
            highest_idx = -1
            diff = 0.0
            highest = 0.0
            lowest = 0.0
        
            while today < len(valid_high):
                # Handle lowest value update
                tmp = valid_low[today]
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_low[lowest_idx]
                    i = lowest_idx
                    while i < today + 1:
                        tmp = valid_low[i]
                        if tmp < lowest:
                            lowest_idx = i
                            lowest = tmp
                        i += 1
                    diff = (highest - lowest) / (-100.0)
                elif tmp <= lowest:
                    lowest_idx = today
                    lowest = tmp
                    diff = (highest - lowest) / (-100.0)
                
                # Handle highest value update
                tmp = valid_high[today]
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_high[highest_idx]
                    i = highest_idx
                    while i < today + 1:
                        tmp = valid_high[i]
                        if tmp > highest:
                            highest_idx = i
                            highest = tmp
                        i += 1
                    diff = (highest - lowest) / (-100.0)
                elif tmp >= highest:
                    highest_idx = today
                    highest = tmp
                    diff = (highest - lowest) / (-100.0)
                
                # Calculate WILLR value
                if diff != 0.0:
                    willr_values[today] = (highest - valid_close[today]) / diff
                else:
                    willr_values[today] = 0.0
                
                trailing_idx += 1
                today += 1
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = willr_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def AROON(high, open, low, close, vol, oi, timeperiod=25):
        tdts, secs = high.shape
        result_up = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_down = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Initialize output arrays for Aroon Up and Down
            aroon_up = np.zeros(len(valid_high))
            aroon_down = np.zeros(len(valid_high))
        
            # Set start index as per TA-Lib logic
            start_idx = timeperiod
            out_idx = 0
            today = start_idx
            trailing_idx = start_idx - timeperiod
            lowest_idx = -1
            highest_idx = -1
            lowest = 0.0
            highest = 0.0
            factor = 100.0 / timeperiod
        
            while today < len(valid_high):
                # Process lowest for Aroon Down
                tmp = valid_low[today]
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_low[lowest_idx]
                    i = lowest_idx
                    while i <= today:
                        tmp = valid_low[i]
                        if tmp <= lowest:
                            lowest_idx = i
                            lowest = tmp
                        i += 1
                elif tmp <= lowest:
                    lowest_idx = today
                    lowest = tmp
            
                # Process highest for Aroon Up
                tmp = valid_high[today]
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_high[highest_idx]
                    i = highest_idx
                    while i <= today:
                        tmp = valid_high[i]
                        if tmp >= highest:
                            highest_idx = i
                            highest = tmp
                        i += 1
                elif tmp >= highest:
                    highest_idx = today
                    highest = tmp
            
                # Calculate Aroon Up and Down
                aroon_up[today] = factor * (timeperiod - (today - highest_idx))
                aroon_down[today] = factor * (timeperiod - (today - lowest_idx))
            
                out_idx += 1
                trailing_idx += 1
                today += 1
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result_up[orig_idx, sec] = aroon_up[i]
                result_down[orig_idx, sec] = aroon_down[i]
    
        return result_up, result_down



    @staticmethod
    @nb.njit
    def CDLHAMMER(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        BodyShortPeriod = 5
        ShadowLongPeriod = 5
        ShadowVeryShortPeriod = 5
        NearPeriod = 5
    
        # Total lookback period for starting index
        lookbackTotal = max(BodyShortPeriod, ShadowLongPeriod, ShadowVeryShortPeriod, NearPeriod + 1)
    
        for sec in range(secs):
            # Initialize period totals for averages
            BodyPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
            NearPeriodTotal = 0.0
        
            # Trailing indices for rolling window calculations
            BodyTrailingIdx = lookbackTotal - BodyShortPeriod
            ShadowLongTrailingIdx = lookbackTotal - ShadowLongPeriod
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
            NearTrailingIdx = lookbackTotal - 1 - NearPeriod
        
            # Warm-up period: Calculate initial totals for averages
            for i in range(BodyTrailingIdx, lookbackTotal):
                if i >= 0 and i < tdts:
                    # BodyShort range (Close - Open)
                    if close[i, sec] == close[i, sec] and open[i, sec] == open[i, sec]:
                        BodyPeriodTotal += abs(close[i, sec] - open[i, sec])
        
            for i in range(ShadowLongTrailingIdx, lookbackTotal):
                if i >= 0 and i < tdts:
                    # ShadowLong range (typically lower shadow)
                    if low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                        ShadowLongPeriodTotal += min(open[i, sec], close[i, sec]) - low[i, sec]
        
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                if i >= 0 and i < tdts:
                    # ShadowVeryShort range (typically upper shadow)
                    if high[i, sec] == high[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                        ShadowVeryShortPeriodTotal += high[i, sec] - max(open[i, sec], close[i, sec])
        
            for i in range(NearTrailingIdx, lookbackTotal - 1):
                if i >= 0 and i < tdts:
                    # Near range (typically high - low of previous candle)
                    if high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec]:
                        NearPeriodTotal += high[i, sec] - low[i, sec]
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, tdts):
                # Check data validity
                if (high[i, sec] != high[i, sec] or low[i, sec] != low[i, sec] or 
                    open[i, sec] != open[i, sec] or close[i, sec] != close[i, sec] or
                    i - 1 < 0 or high[i - 1, sec] != high[i - 1, sec] or low[i - 1, sec] != low[i - 1, sec]):
                    result[i, sec] = 0
                    continue
            
                # Calculate real body
                real_body = abs(close[i, sec] - open[i, sec])
                # Calculate averages
                body_avg = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                shadow_long_avg = ShadowLongPeriodTotal / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
                shadow_short_avg = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                near_avg = NearPeriodTotal / NearPeriod if NearPeriod > 0 else 0.0
            
                # Hammer pattern conditions
                if (real_body < body_avg and
                    (min(open[i, sec], close[i, sec]) - low[i, sec]) > shadow_long_avg and
                    (high[i, sec] - max(open[i, sec], close[i, sec])) < shadow_short_avg and
                    min(close[i, sec], open[i, sec]) <= low[i - 1, sec] + near_avg):
                    result[i, sec] = 100
                else:
                    result[i, sec] = 0
            
                # Update rolling totals for next iteration
                if i + 1 < tdts:
                    # Update BodyPeriodTotal
                    if close[i, sec] == close[i, sec] and open[i, sec] == open[i, sec]:
                        BodyPeriodTotal += abs(close[i, sec] - open[i, sec])
                    if BodyTrailingIdx >= 0 and close[BodyTrailingIdx, sec] == close[BodyTrailingIdx, sec] and open[BodyTrailingIdx, sec] == open[BodyTrailingIdx, sec]:
                        BodyPeriodTotal -= abs(close[BodyTrailingIdx, sec] - open[BodyTrailingIdx, sec])
                
                    # Update ShadowLongPeriodTotal
                    if low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                        ShadowLongPeriodTotal += min(open[i, sec], close[i, sec]) - low[i, sec]
                    if ShadowLongTrailingIdx >= 0 and low[ShadowLongTrailingIdx, sec] == low[ShadowLongTrailingIdx, sec] and open[ShadowLongTrailingIdx, sec] == open[ShadowLongTrailingIdx, sec] and close[ShadowLongTrailingIdx, sec] == close[ShadowLongTrailingIdx, sec]:
                        ShadowLongPeriodTotal -= min(open[ShadowLongTrailingIdx, sec], close[ShadowLongTrailingIdx, sec]) - low[ShadowLongTrailingIdx, sec]
                
                    # Update ShadowVeryShortPeriodTotal
                    if high[i, sec] == high[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                        ShadowVeryShortPeriodTotal += high[i, sec] - max(open[i, sec], close[i, sec])
                    if ShadowVeryShortTrailingIdx >= 0 and high[ShadowVeryShortTrailingIdx, sec] == high[ShadowVeryShortTrailingIdx, sec] and open[ShadowVeryShortTrailingIdx, sec] == open[ShadowVeryShortTrailingIdx, sec] and close[ShadowVeryShortTrailingIdx, sec] == close[ShadowVeryShortTrailingIdx, sec]:
                        ShadowVeryShortPeriodTotal -= high[ShadowVeryShortTrailingIdx, sec] - max(open[ShadowVeryShortTrailingIdx, sec], close[ShadowVeryShortTrailingIdx, sec])
                
                    # Update NearPeriodTotal
                    if i - 1 >= 0 and high[i - 1, sec] == high[i - 1, sec] and low[i - 1, sec] == low[i - 1, sec]:
                        NearPeriodTotal += high[i - 1, sec] - low[i - 1, sec]
                    if NearTrailingIdx >= 0 and high[NearTrailingIdx, sec] == high[NearTrailingIdx, sec] and low[NearTrailingIdx, sec] == low[NearTrailingIdx, sec]:
                        NearPeriodTotal -= high[NearTrailingIdx, sec] - low[NearTrailingIdx, sec]
                
                    BodyTrailingIdx += 1
                    ShadowLongTrailingIdx += 1
                    ShadowVeryShortTrailingIdx += 1
                    NearTrailingIdx += 1
    
        return result






### end here

    @staticmethod
    @nb.njit
    def BETA(high, open, low, close, vol, oi, timeperiod=5):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask for close and open (used as inReal0 and inReal1 in C code)
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (close[i, sec] == close[i, sec] and 
                    open[i, sec] == open[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]  # inReal0 in C code
            valid_open = open[valid_mask, sec]    # inReal1 in C code
        
            # Initialize variables as per C code
            nb_initial_element_needed = timeperiod
            start_idx = nb_initial_element_needed if nb_initial_element_needed > 0 else 0
        
            if start_idx >= len(valid_close):
                continue
            
            trailing_idx = start_idx - nb_initial_element_needed
            last_price_x = trailing_last_price_x = valid_close[trailing_idx] if trailing_idx >= 0 else 0.0
            last_price_y = trailing_last_price_y = valid_open[trailing_idx] if trailing_idx >= 0 else 0.0
        
            # Initialize summation variables
            S_xx = 0.0
            S_xy = 0.0
            S_x = 0.0
            S_y = 0.0
        
            # Warm-up period: calculate initial sums
            i = trailing_idx + 1 if trailing_idx + 1 < start_idx else start_idx
            while i < start_idx and i < len(valid_close):
                tmp_real = valid_close[i]
                if last_price_x != 0.0:
                    x = (tmp_real - last_price_x) / last_price_x
                else:
                    x = 0.0
                last_price_x = tmp_real
            
                tmp_real = valid_open[i]
                if last_price_y != 0.0:
                    y = (tmp_real - last_price_y) / last_price_y
                else:
                    y = 0.0
                last_price_y = tmp_real
            
                S_xx += x * x
                S_xy += x * y
                S_x += x
                S_y += y
                i += 1
        
            # Main calculation loop
            out_idx = start_idx
            n = float(timeperiod)
            trailing_idx = start_idx - nb_initial_element_needed
        
            while i < len(valid_close):
                tmp_real = valid_close[i]
                if last_price_x != 0.0:
                    x = (tmp_real - last_price_x) / last_price_x
                else:
                    x = 0.0
                last_price_x = tmp_real
            
                tmp_real = valid_open[i]
                if last_price_y != 0.0:
                    y = (tmp_real - last_price_y) / last_price_y
                else:
                    y = 0.0
                last_price_y = tmp_real
            
                S_xx += x * x
                S_xy += x * y
                S_x += x
                S_y += y
            
                # Subtract trailing value
                if trailing_idx < len(valid_close):
                    tmp_real = valid_close[trailing_idx]
                    if trailing_last_price_x != 0.0:
                        x = (tmp_real - trailing_last_price_x) / trailing_last_price_x
                    else:
                        x = 0.0
                    trailing_last_price_x = tmp_real
                
                    tmp_real = valid_open[trailing_idx]
                    if trailing_last_price_y != 0.0:
                        y = (tmp_real - trailing_last_price_y) / trailing_last_price_y
                    else:
                        y = 0.0
                    trailing_last_price_y = tmp_real
                
                    S_xx -= x * x
                    S_xy -= x * y
                    S_x -= x
                    S_y -= y
            
                # Calculate BETA
                tmp_real = (n * S_xx) - (S_x * S_x)
                if tmp_real != 0.0:
                    beta_value = ((n * S_xy) - (S_x * S_y)) / tmp_real
                else:
                    beta_value = 0.0
            
                if out_idx < len(valid_close):
                    orig_idx = valid_indices[out_idx]
                    result[orig_idx, sec] = beta_value
            
                trailing_idx += 1
                i += 1
                out_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLBELTHOLD(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults for BodyLong and ShadowVeryShort
        BodyLongPeriod = 5
        ShadowVeryShortPeriod = 5
        lookbackTotal = max(BodyLongPeriod, ShadowVeryShortPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing totals for moving averages
            BodyLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyLongTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
        
            for i in range(lookbackTotal):
                # BodyLong range is typically close-open difference for real body
                BodyLongRange = abs(valid_close[i] - valid_open[i])
                BodyLongPeriodTotal += BodyLongRange
            
                # ShadowVeryShort range for shadows
                if valid_close[i] > valid_open[i]:
                    ShadowRange = valid_high[i] - valid_close[i]
                else:
                    ShadowRange = valid_open[i] - valid_low[i]
                ShadowVeryShortPeriodTotal += ShadowRange
        
            # Start processing from lookbackTotal onwards
            outIdx = lookbackTotal
            while outIdx < len(valid_high):
                # Calculate real body
                realBody = abs(valid_close[outIdx] - valid_open[outIdx])
            
                # Calculate candle color (1 for bullish, -1 for bearish)
                candleColor = 1 if valid_close[outIdx] > valid_open[outIdx] else -1
            
                # Calculate shadows
                upperShadow = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx])
                lowerShadow = min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod
            
                # Belt Hold pattern logic
                if realBody > BodyLongAverage:
                    if candleColor == 1 and lowerShadow < ShadowVeryShortAverage:
                        result[valid_indices[outIdx], sec] = 100
                    elif candleColor == -1 and upperShadow < ShadowVeryShortAverage:
                        result[valid_indices[outIdx], sec] = -100
                    else:
                        result[valid_indices[outIdx], sec] = 0
                else:
                    result[valid_indices[outIdx], sec] = 0
            
                # Update trailing totals
                # Remove oldest value
                oldBodyLongRange = abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                BodyLongPeriodTotal -= oldBodyLongRange
            
                oldShadowRange = valid_high[ShadowVeryShortTrailingIdx] - max(valid_open[ShadowVeryShortTrailingIdx], valid_close[ShadowVeryShortTrailingIdx]) if valid_close[ShadowVeryShortTrailingIdx] > valid_open[ShadowVeryShortTrailingIdx] else min(valid_open[ShadowVeryShortTrailingIdx], valid_close[ShadowVeryShortTrailingIdx]) - valid_low[ShadowVeryShortTrailingIdx]
                ShadowVeryShortPeriodTotal -= oldShadowRange
            
                # Add newest value
                newBodyLongRange = abs(valid_close[outIdx] - valid_open[outIdx])
                BodyLongPeriodTotal += newBodyLongRange
            
                newShadowRange = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx]) if valid_close[outIdx] > valid_open[outIdx] else min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
                ShadowVeryShortPeriodTotal += newShadowRange
            
                # Increment indices
                BodyLongTrailingIdx += 1
                ShadowVeryShortTrailingIdx += 1
                outIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLCLOSINGMARUBOZU(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyLong and ShadowVeryShort as per TA-Lib defaults
        BodyLongPeriod = 10
        ShadowVeryShortPeriod = 10
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < max(BodyLongPeriod, ShadowVeryShortPeriod):
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            temp_result = np.zeros(len(valid_high))
        
            # Calculate lookback total as per TA-Lib
            lookback_total = max(BodyLongPeriod, ShadowVeryShortPeriod)
            start_idx = lookback_total if lookback_total < len(valid_high) else len(valid_high) - 1
        
            if start_idx >= len(valid_high):
                continue
            
            # Initialize totals for BodyLong and ShadowVeryShort
            BodyLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyLongTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
        
            for i in range(start_idx):
                # BodyLong range is typically close - open (real body)
                BodyLongRange = abs(valid_close[i] - valid_open[i])
                BodyLongPeriodTotal += BodyLongRange
            
                # ShadowVeryShort range is typically high - low for shadow calculation
                ShadowVeryShortRange = valid_high[i] - valid_low[i]
                ShadowVeryShortPeriodTotal += ShadowVeryShortRange
        
            # Main calculation loop
            for i in range(start_idx, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
            
                # Calculate candle color (1 for bullish, -1 for bearish)
                candle_color = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate upper and lower shadows
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Check for Closing Marubozu pattern
                if real_body > BodyLongAverage:
                    if candle_color == 1 and upper_shadow < ShadowVeryShortAverage:
                        temp_result[i] = 100
                    elif candle_color == -1 and lower_shadow < ShadowVeryShortAverage:
                        temp_result[i] = -100
                    else:
                        temp_result[i] = 0
                else:
                    temp_result[i] = 0
            
                # Update totals for next iteration
                if i + 1 < len(valid_high):
                    # Add current range
                    new_body_range = abs(valid_close[i] - valid_open[i])
                    new_shadow_range = valid_high[i] - valid_low[i]
                
                    BodyLongPeriodTotal += new_body_range
                    ShadowVeryShortPeriodTotal += new_shadow_range
                
                    # Subtract trailing range if within bounds
                    if BodyLongTrailingIdx < len(valid_high):
                        old_body_range = abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                        BodyLongPeriodTotal -= old_body_range
                        BodyLongTrailingIdx += 1
                
                    if ShadowVeryShortTrailingIdx < len(valid_high):
                        old_shadow_range = valid_high[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]
                        ShadowVeryShortPeriodTotal -= old_shadow_range
                        ShadowVeryShortTrailingIdx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= start_idx:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLCOUNTERATTACK(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        EqualPeriod = 2
        BodyLongPeriod = 10
        lookbackTotal = max(EqualPeriod, BodyLongPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for Equal and BodyLong periods
            EqualPeriodTotal = 0.0
            BodyLongPeriodTotal = np.zeros(2, dtype=np.float64)
            EqualTrailingIdx = 0
            BodyLongTrailingIdx = 0
        
            # Warm-up period for Equal
            for i in range(EqualTrailingIdx, lookbackTotal):
                if i < EqualPeriod:
                    EqualPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # Warm-up period for BodyLong
            for i in range(BodyLongTrailingIdx, lookbackTotal):
                if i < BodyLongPeriod:
                    BodyLongPeriodTotal[1] += abs(valid_close[i] - valid_open[i])
                    if i + 1 < len(valid_close):
                        BodyLongPeriodTotal[0] += abs(valid_close[i + 1] - valid_open[i + 1])
        
            # Main calculation loop
            for i in range(lookbackTotal, len(valid_close)):
                # Calculate candle color for current and previous day
                color_prev = 1 if valid_close[i - 1] > valid_open[i - 1] else -1
                color_curr = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate real body for current and previous day
                realbody_prev = abs(valid_close[i - 1] - valid_open[i - 1])
                realbody_curr = abs(valid_close[i] - valid_open[i])
            
                # Calculate averages
                EqualAverage = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0.0
                BodyLongAverage_prev = BodyLongPeriodTotal[1] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyLongAverage_curr = BodyLongPeriodTotal[0] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
            
                # Counterattack pattern logic
                if (color_prev == -color_curr and
                    realbody_prev > BodyLongAverage_prev and
                    realbody_curr > BodyLongAverage_curr and
                    valid_close[i] <= valid_close[i - 1] + EqualAverage and
                    valid_close[i] >= valid_close[i - 1] - EqualAverage):
                    result[valid_indices[i], sec] = color_curr * 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update totals for next iteration
                if i - EqualPeriod >= 0:
                    EqualPeriodTotal += abs(valid_close[i - 1] - valid_open[i - 1])
                    EqualPeriodTotal -= abs(valid_close[i - EqualPeriod - 1] - valid_open[i - EqualPeriod - 1])
            
                for totIdx in range(1, -1, -1):
                    if i - totIdx >= 0 and i - totIdx - BodyLongPeriod >= 0:
                        BodyLongPeriodTotal[totIdx] += abs(valid_close[i - totIdx] - valid_open[i - totIdx])
                        BodyLongPeriodTotal[totIdx] -= abs(valid_close[i - totIdx - BodyLongPeriod] - valid_open[i - totIdx - BodyLongPeriod])
    
        return result



    @staticmethod
    @nb.njit
    def CDLDOJISTAR(high, open, low, close, vol, oi):
        """
        CDLDOJISTAR - Candlestick Doji Star Pattern
    
        Identifies a Doji Star pattern where a Doji appears after a long body candle
        with a gap between them, indicating potential reversal.
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for averaging candle body sizes as per TA-Lib defaults
        BodyLongPeriod = 10
        BodyDojiPeriod = 3
    
        # Lookback period as per TA-Lib (maximum of the two periods + 1 for previous candle)
        lookbackTotal = max(BodyLongPeriod, BodyDojiPeriod) + 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            out_values = np.zeros(len(valid_high))
        
            # Initialize trailing totals for body averages
            BodyLongPeriodTotal = 0.0
            BodyDojiPeriodTotal = 0.0
        
            # Calculate initial totals for BodyLong
            BodyLongTrailingIdx = lookbackTotal - 1 - BodyLongPeriod
            if BodyLongTrailingIdx < 0:
                BodyLongTrailingIdx = 0
            for i in range(BodyLongTrailingIdx, lookbackTotal - 1):
                BodyLongPeriodTotal += abs(valid_open[i] - valid_close[i])
        
            # Calculate initial totals for BodyDoji
            BodyDojiTrailingIdx = lookbackTotal - BodyDojiPeriod
            if BodyDojiTrailingIdx < 0:
                BodyDojiTrailingIdx = 0
            for i in range(BodyDojiTrailingIdx, lookbackTotal):
                BodyDojiPeriodTotal += abs(valid_open[i] - valid_close[i])
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate BodyLong average
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
            
                # Calculate BodyDoji average
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
            
                # Calculate real body for current and previous candle
                realbody_prev = abs(valid_open[i-1] - valid_close[i-1])
                realbody_curr = abs(valid_open[i] - valid_close[i])
            
                # Determine candle color for previous day (1 for bullish, -1 for bearish)
                candle_color_prev = 1 if valid_close[i-1] > valid_open[i-1] else -1
            
                # Check for gap up or gap down
                gap_up = valid_open[i] > valid_close[i-1] if candle_color_prev == 1 else False
                gap_down = valid_open[i] < valid_close[i-1] if candle_color_prev == -1 else False
            
                # Check Doji Star conditions
                if (realbody_prev > BodyLongAverage and  # Previous candle has long body
                    realbody_curr <= BodyDojiAverage and  # Current candle is Doji
                    ((candle_color_prev == 1 and gap_up) or  # Bullish with gap up
                     (candle_color_prev == -1 and gap_down))):  # Bearish with gap down
                    out_values[i] = -candle_color_prev * 100
                else:
                    out_values[i] = 0
                
                # Update trailing totals for next iteration
                BodyLongPeriodTotal += abs(valid_open[i-1] - valid_close[i-1])
                BodyLongPeriodTotal -= abs(valid_open[BodyLongTrailingIdx] - valid_close[BodyLongTrailingIdx])
                BodyDojiPeriodTotal += abs(valid_open[i] - valid_close[i])
                BodyDojiPeriodTotal -= abs(valid_open[BodyDojiTrailingIdx] - valid_close[BodyDojiTrailingIdx])
            
                BodyLongTrailingIdx += 1
                BodyDojiTrailingIdx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookbackTotal:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = out_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLDRAGONFLYDOJI(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for averaging periods as in TA-Lib
        BodyDojiPeriod = 3
        ShadowVeryShortPeriod = 3
    
        # Lookback period as per TA-Lib
        lookbackTotal = max(BodyDojiPeriod, ShadowVeryShortPeriod)
    
        for sec in range(secs):
            # Initialize variables for trailing totals
            BodyDojiPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Initialize trailing indices
            BodyDojiTrailingIdx = lookbackTotal - BodyDojiPeriod
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
        
            # Warm-up period: Calculate initial totals for averages
            for i in range(BodyDojiTrailingIdx, lookbackTotal):
                if high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    BodyDojiPeriodTotal += abs(close[i, sec] - open[i, sec])
        
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                if high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    ShadowVeryShortPeriodTotal += high[i, sec] - low[i, sec]
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, tdts):
                if high[i, sec] != high[i, sec] or low[i, sec] != low[i, sec] or open[i, sec] != open[i, sec] or close[i, sec] != close[i, sec]:
                    result[i, sec] = 0
                    continue
                
                # Calculate real body and shadows
                real_body = abs(close[i, sec] - open[i, sec])
                upper_shadow = high[i, sec] - max(open[i, sec], close[i, sec])
                lower_shadow = min(open[i, sec], close[i, sec]) - low[i, sec]
            
                # Calculate averages for comparison
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Dragonfly Doji conditions:
                # 1. Real body is very small (less than or equal to average body)
                # 2. Upper shadow is very short (less than average shadow)
                # 3. Lower shadow is long (greater than average shadow)
                if (real_body <= BodyDojiAverage and
                    upper_shadow < ShadowVeryShortAverage and
                    lower_shadow > ShadowVeryShortAverage):
                    result[i, sec] = 100
                else:
                    result[i, sec] = 0
            
                # Update trailing totals for next iteration
                if i + 1 < tdts:
                    # Add current candle range to totals
                    if high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                        BodyDojiPeriodTotal += abs(close[i, sec] - open[i, sec])
                        ShadowVeryShortPeriodTotal += high[i, sec] - low[i, sec]
                
                    # Subtract trailing candle range from totals
                    if BodyDojiTrailingIdx < tdts and high[BodyDojiTrailingIdx, sec] == high[BodyDojiTrailingIdx, sec]:
                        BodyDojiPeriodTotal -= abs(close[BodyDojiTrailingIdx, sec] - open[BodyDojiTrailingIdx, sec])
                    if ShadowVeryShortTrailingIdx < tdts and high[ShadowVeryShortTrailingIdx, sec] == high[ShadowVeryShortTrailingIdx, sec]:
                        ShadowVeryShortPeriodTotal -= high[ShadowVeryShortTrailingIdx, sec] - low[ShadowVeryShortTrailingIdx, sec]
                
                    # Increment trailing indices
                    BodyDojiTrailingIdx += 1
                    ShadowVeryShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLGAPSIDESIDEWHITE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback period as per TA-Lib (2 days for pattern recognition)
        lookback_total = 2
    
        # Define periods for Near and Equal averages as per TA-Lib defaults
        near_period = 14
        equal_period = 14
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookback_total:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for Near and Equal periods
            near_period_total = 0.0
            equal_period_total = 0.0
        
            # Calculate initial totals for Near and Equal ranges
            start_idx = lookback_total
            near_trailing_idx = start_idx - near_period
            equal_trailing_idx = start_idx - equal_period
        
            if near_trailing_idx < 0:
                near_trailing_idx = 0
            if equal_trailing_idx < 0:
                equal_trailing_idx = 0
            
            for i in range(near_trailing_idx, start_idx):
                if i < len(valid_high):
                    near_period_total += valid_high[i] - valid_low[i]
                
            for i in range(equal_trailing_idx, start_idx):
                if i < len(valid_high):
                    equal_period_total += valid_high[i] - valid_low[i]
        
            # Main calculation loop
            out_idx = start_idx
            i = start_idx
            while i < len(valid_high):
                if i >= 2:  # Need at least 2 previous candles for pattern
                    # Check for gap up or gap down conditions
                    realbody_gapup_1 = valid_close[i-1] > valid_open[i-2]
                    realbody_gapup_2 = valid_close[i] > valid_open[i-2]
                    realbody_gapdown_1 = valid_close[i-1] < valid_open[i-2]
                    realbody_gapdown_2 = valid_close[i] < valid_open[i-2]
                
                    # Check candle colors (white candles for both)
                    color_1 = valid_close[i-1] > valid_open[i-1]
                    color_2 = valid_close[i] > valid_open[i]
                
                    # Calculate real body sizes
                    realbody_1 = abs(valid_close[i-1] - valid_open[i-1])
                    realbody_2 = abs(valid_close[i] - valid_open[i])
                
                    # Calculate averages for comparison
                    near_avg = near_period_total / near_period if near_period > 0 else 0.0
                    equal_avg = equal_period_total / equal_period if equal_period > 0 else 0.0
                
                    # Check all conditions for Side-by-Side White Lines pattern
                    if ((realbody_gapup_1 and realbody_gapup_2) or (realbody_gapdown_1 and realbody_gapdown_2)) and \
                       color_1 and color_2 and \
                       realbody_2 >= realbody_1 - near_avg and \
                       realbody_2 <= realbody_1 + near_avg and \
                       valid_open[i] >= valid_open[i-1] - equal_avg and \
                       valid_open[i] <= valid_open[i-1] + equal_avg:
                        result[valid_indices[i], sec] = 100 if realbody_gapup_1 else -100
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update trailing totals
                if i < len(valid_high):
                    current_near_range = valid_high[i] - valid_low[i]
                    current_equal_range = valid_high[i] - valid_low[i]
                
                    if near_trailing_idx < len(valid_high):
                        old_near_range = valid_high[near_trailing_idx] - valid_low[near_trailing_idx]
                        near_period_total += current_near_range - old_near_range
                    else:
                        near_period_total += current_near_range
                    
                    if equal_trailing_idx < len(valid_high):
                        old_equal_range = valid_high[equal_trailing_idx] - valid_low[equal_trailing_idx]
                        equal_period_total += current_equal_range - old_equal_range
                    else:
                        equal_period_total += current_equal_range
                    
                i += 1
                near_trailing_idx += 1
                equal_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLGRAVESTONEDOJI(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        BodyDojiPeriod = 3
        ShadowVeryShortPeriod = 3
        lookbackTotal = max(BodyDojiPeriod, ShadowVeryShortPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for averaging
            BodyDojiPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for BodyDoji and ShadowVeryShort
            BodyDojiTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
        
            for i in range(lookbackTotal):
                # BodyDoji range is typically the real body size
                BodyDojiRange = abs(valid_close[i] - valid_open[i])
                BodyDojiPeriodTotal += BodyDojiRange
            
                # ShadowVeryShort range is typically the high-low range
                ShadowVeryShortRange = valid_high[i] - valid_low[i]
                ShadowVeryShortPeriodTotal += ShadowVeryShortRange
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body and shadows
                real_body = abs(valid_close[i] - valid_open[i])
                lower_shadow = valid_open[i] - valid_low[i] if valid_close[i] >= valid_open[i] else valid_close[i] - valid_low[i]
                upper_shadow = valid_high[i] - valid_open[i] if valid_close[i] >= valid_open[i] else valid_high[i] - valid_close[i]
            
                # Calculate averages
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod
            
                # Gravestone Doji conditions:
                # 1. Real body is very small compared to average
                # 2. Lower shadow is very short compared to average
                # 3. Upper shadow is long compared to average
                if (real_body <= BodyDojiAverage and
                    lower_shadow < ShadowVeryShortAverage and
                    upper_shadow > ShadowVeryShortAverage):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update trailing totals
                # Remove oldest value and add newest value for BodyDoji
                oldest_body_range = abs(valid_close[BodyDojiTrailingIdx] - valid_open[BodyDojiTrailingIdx])
                newest_body_range = abs(valid_close[i] - valid_open[i])
                BodyDojiPeriodTotal += newest_body_range - oldest_body_range
                BodyDojiTrailingIdx += 1
            
                # Remove oldest value and add newest value for ShadowVeryShort
                oldest_shadow_range = valid_high[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]
                newest_shadow_range = valid_high[i] - valid_low[i]
                ShadowVeryShortPeriodTotal += newest_shadow_range - oldest_shadow_range
                ShadowVeryShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLINVERTEDHAMMER(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle components as in TA-Lib
        BodyShortPeriod = 10
        ShadowLongPeriod = 10
        ShadowVeryShortPeriod = 10
        lookbackTotal = max(BodyShortPeriod, max(ShadowLongPeriod, ShadowVeryShortPeriod))
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for averaging
            BodyPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            for i in range(lookbackTotal):
                # BodyShort range (real body)
                BodyPeriodTotal += abs(valid_close[i] - valid_open[i])
                # ShadowLong range (upper shadow)
                ShadowLongPeriodTotal += max(valid_high[i] - max(valid_open[i], valid_close[i]), 0.0)
                # ShadowVeryShort range (lower shadow)
                ShadowVeryShortPeriodTotal += max(min(valid_open[i], valid_close[i]) - valid_low[i], 0.0)
        
            # Start processing from lookbackTotal
            BodyTrailingIdx = 0
            ShadowLongTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
        
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
                # Calculate upper shadow
                upper_shadow = max(valid_high[i] - max(valid_open[i], valid_close[i]), 0.0)
                # Calculate lower shadow
                lower_shadow = max(min(valid_open[i], valid_close[i]) - valid_low[i], 0.0)
                # Calculate body gap down condition
                gap_down = 1 if i > 0 and min(valid_open[i-1], valid_close[i-1]) > max(valid_open[i], valid_close[i]) else 0
            
                # Calculate averages
                BodyAverage = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                ShadowLongAverage = ShadowLongPeriodTotal / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Check Inverted Hammer conditions
                if (real_body < BodyAverage and 
                    upper_shadow > ShadowLongAverage and 
                    lower_shadow < ShadowVeryShortAverage and 
                    gap_down == 1):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update totals by adding current and removing trailing
                BodyPeriodTotal += abs(valid_close[i] - valid_open[i])
                ShadowLongPeriodTotal += max(valid_high[i] - max(valid_open[i], valid_close[i]), 0.0)
                ShadowVeryShortPeriodTotal += max(min(valid_open[i], valid_close[i]) - valid_low[i], 0.0)
            
                if BodyTrailingIdx < len(valid_high):
                    BodyPeriodTotal -= abs(valid_close[BodyTrailingIdx] - valid_open[BodyTrailingIdx])
                if ShadowLongTrailingIdx < len(valid_high):
                    ShadowLongPeriodTotal -= max(valid_high[ShadowLongTrailingIdx] - max(valid_open[ShadowLongTrailingIdx], valid_close[ShadowLongTrailingIdx]), 0.0)
                if ShadowVeryShortTrailingIdx < len(valid_high):
                    ShadowVeryShortPeriodTotal -= max(min(valid_open[ShadowVeryShortTrailingIdx], valid_close[ShadowVeryShortTrailingIdx]) - valid_low[ShadowVeryShortTrailingIdx], 0.0)
                
                BodyTrailingIdx += 1
                ShadowLongTrailingIdx += 1
                ShadowVeryShortTrailingIdx += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLLONGLEGGEDDOJI(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for averaging as per TA-Lib defaults
        BodyDojiPeriod = 3
        ShadowLongPeriod = 3
        lookbackTotal = max(BodyDojiPeriod, ShadowLongPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for averaging
            BodyDojiPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
        
            # Calculate initial totals for BodyDoji and ShadowLong
            BodyDojiTrailingIdx = 0
            ShadowLongTrailingIdx = 0
            startIdx = lookbackTotal
        
            for i in range(BodyDojiTrailingIdx, startIdx):
                if i < len(valid_high):
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            for i in range(ShadowLongTrailingIdx, startIdx):
                if i < len(valid_high):
                    ShadowLongPeriodTotal += max(valid_high[i] - valid_low[i], 0.0)
        
            # Main calculation loop
            outIdx = startIdx
            i = startIdx
            while i < len(valid_high):
                # Calculate real body and shadows
                realBody = abs(valid_close[i] - valid_open[i])
                upperShadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lowerShadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Calculate averages
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                ShadowLongAverage = ShadowLongPeriodTotal / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
            
                # Long Legged Doji condition
                if (realBody <= BodyDojiAverage and
                    (lowerShadow > ShadowLongAverage or upperShadow > ShadowLongAverage)):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update totals for next iteration
                if i + 1 < len(valid_high):
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                    if BodyDojiTrailingIdx < len(valid_high):
                        BodyDojiPeriodTotal -= abs(valid_close[BodyDojiTrailingIdx] - valid_open[BodyDojiTrailingIdx])
                    ShadowLongPeriodTotal += max(valid_high[i] - valid_low[i], 0.0)
                    if ShadowLongTrailingIdx < len(valid_high):
                        ShadowLongPeriodTotal -= max(valid_high[ShadowLongTrailingIdx] - valid_low[ShadowLongTrailingIdx], 0.0)
            
                i += 1
                BodyDojiTrailingIdx += 1
                ShadowLongTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLLONGLINE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        BodyLongPeriod = 5
        ShadowShortPeriod = 5
        lookbackTotal = max(BodyLongPeriod, ShadowShortPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for BodyLong and ShadowShort
            BodyPeriodTotal = 0.0
            ShadowPeriodTotal = 0.0
        
            # Calculate initial totals for BodyLong and ShadowShort ranges
            BodyTrailingIdx = 0
            ShadowTrailingIdx = 0
        
            for i in range(lookbackTotal):
                if i < BodyLongPeriod:
                    BodyPeriodTotal += abs(valid_close[i] - valid_open[i])
                if i < ShadowShortPeriod:
                    ShadowPeriodTotal += max(valid_high[i] - valid_open[i], valid_close[i] - valid_low[i]) if valid_close[i] >= valid_open[i] else max(valid_open[i] - valid_low[i], valid_high[i] - valid_close[i])
        
            # Main calculation loop
            outIdx = lookbackTotal
            i = lookbackTotal
            while i < len(valid_high):
                # Calculate real body and shadows
                real_body = abs(valid_close[i] - valid_open[i])
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Calculate averages
                BodyAverage = BodyPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                ShadowAverage = ShadowPeriodTotal / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
            
                # Check for Long Line pattern
                if real_body > BodyAverage and upper_shadow < ShadowAverage and lower_shadow < ShadowAverage:
                    candle_color = 1 if valid_close[i] > valid_open[i] else -1
                    result[valid_indices[i], sec] = candle_color * 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update period totals by subtracting oldest value and adding newest
                if i >= BodyLongPeriod:
                    BodyPeriodTotal += abs(valid_close[i] - valid_open[i]) - abs(valid_close[BodyTrailingIdx] - valid_open[BodyTrailingIdx])
                    BodyTrailingIdx += 1
                
                if i >= ShadowShortPeriod:
                    new_shadow = max(valid_high[i] - valid_open[i], valid_close[i] - valid_low[i]) if valid_close[i] >= valid_open[i] else max(valid_open[i] - valid_low[i], valid_high[i] - valid_close[i])
                    old_shadow = max(valid_high[ShadowTrailingIdx] - valid_open[ShadowTrailingIdx], valid_close[ShadowTrailingIdx] - valid_low[ShadowTrailingIdx]) if valid_close[ShadowTrailingIdx] >= valid_open[ShadowTrailingIdx] else max(valid_open[ShadowTrailingIdx] - valid_low[ShadowTrailingIdx], valid_high[ShadowTrailingIdx] - valid_close[ShadowTrailingIdx])
                    ShadowPeriodTotal += new_shadow - old_shadow
                    ShadowTrailingIdx += 1
                
                i += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLMATCHINGLOW(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        EqualPeriod = 14  # Default period for Equal average as per TA-Lib

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 2:  # Need at least 2 points for pattern recognition
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Lookback period as per TA-Lib (1 day for pattern + EqualPeriod for averaging)
            lookback_total = 1 + EqualPeriod
            if len(valid_indices) < lookback_total:
                continue
            
            # Initialize EqualPeriodTotal for averaging candle range
            EqualPeriodTotal = 0.0
            EqualTrailingIdx = 0
        
            # Warm-up period: Calculate initial EqualPeriodTotal
            for i in range(EqualTrailingIdx, lookback_total - 1):
                EqualPeriodTotal += valid_high[i] - valid_low[i]
        
            out_idx = lookback_total - 1
            while out_idx < len(valid_high):
                # Check for Matching Low pattern
                if out_idx >= 1:
                    # Candle color check: both should be black (bearish)
                    color1 = -1 if valid_close[out_idx - 1] < valid_open[out_idx - 1] else 1
                    color2 = -1 if valid_close[out_idx] < valid_open[out_idx] else 1
                
                    if color1 == -1 and color2 == -1:
                        # Calculate Equal Average for range comparison
                        EqualAverage = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0.0
                        if (valid_close[out_idx] <= valid_close[out_idx - 1] + EqualAverage and
                            valid_close[out_idx] >= valid_close[out_idx - 1] - EqualAverage):
                            result[valid_indices[out_idx], sec] = 100
                        else:
                            result[valid_indices[out_idx], sec] = 0
                    else:
                        result[valid_indices[out_idx], sec] = 0
                    
                    # Update EqualPeriodTotal for next iteration
                    if out_idx < len(valid_high):
                        EqualPeriodTotal += (valid_high[out_idx] - valid_low[out_idx])
                    if EqualTrailingIdx < len(valid_high):
                        EqualPeriodTotal -= (valid_high[EqualTrailingIdx] - valid_low[EqualTrailingIdx])
                        EqualTrailingIdx += 1
                    
                out_idx += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLRICKSHAWMAN(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle components as per TA-Lib defaults
        BodyDojiPeriod = 3
        ShadowLongPeriod = 3
        NearPeriod = 3
        lookbackTotal = max(BodyDojiPeriod, ShadowLongPeriod, NearPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for averaging
            BodyDojiPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            NearPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            for i in range(lookbackTotal):
                # BodyDoji range (real body size)
                BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                # ShadowLong range (high-low range for shadow calculation)
                ShadowLongPeriodTotal += valid_high[i] - valid_low[i]
                # Near range (high-low range for near calculation)
                NearPeriodTotal += valid_high[i] - valid_low[i]
        
            # Start processing from lookbackTotal index
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
                # Calculate lower shadow
                lower_shadow = valid_open[i] if valid_close[i] >= valid_open[i] else valid_close[i]
                lower_shadow = lower_shadow - valid_low[i]
                # Calculate upper shadow
                upper_shadow = valid_high[i] - (valid_close[i] if valid_close[i] >= valid_open[i] else valid_open[i])
                # Calculate high-low range
                high_low_range = valid_high[i] - valid_low[i]
            
                # Calculate averages
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod
                ShadowLongAverage = ShadowLongPeriodTotal / ShadowLongPeriod
                NearAverage = NearPeriodTotal / NearPeriod
            
                # Rickshaw Man conditions
                if (real_body <= BodyDojiAverage and
                    lower_shadow > ShadowLongAverage and
                    upper_shadow > ShadowLongAverage and
                    min(valid_open[i], valid_close[i]) <= valid_low[i] + high_low_range / 2 + NearAverage and
                    max(valid_open[i], valid_close[i]) >= valid_low[i] + high_low_range / 2 - NearAverage):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals
                if i + 1 < len(valid_high):
                    # Remove oldest value and add newest for next iteration
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i]) - abs(valid_close[i - BodyDojiPeriod] - valid_open[i - BodyDojiPeriod])
                    ShadowLongPeriodTotal += (valid_high[i] - valid_low[i]) - (valid_high[i - ShadowLongPeriod] - valid_low[i - ShadowLongPeriod])
                    NearPeriodTotal += (valid_high[i] - valid_low[i]) - (valid_high[i - NearPeriod] - valid_low[i - NearPeriod])
    
        return result



    @staticmethod
    @nb.njit
    def CDLSHORTLINE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for candle average periods as per TA-Lib defaults
        BodyShortPeriod = 5
        ShadowShortPeriod = 5
    
        # Lookback period as per TA-Lib (maximum of the periods used)
        lookbackTotal = max(BodyShortPeriod, ShadowShortPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for body and shadow
            BodyPeriodTotal = 0.0
            ShadowPeriodTotal = 0.0
        
            # Calculate initial totals for body and shadow ranges
            BodyTrailingIdx = 0
            ShadowTrailingIdx = 0
        
            for i in range(lookbackTotal):
                # Body range for BodyShort (typically close - open)
                body_range = abs(valid_close[i] - valid_open[i])
                BodyPeriodTotal += body_range
            
                # Shadow range for ShadowShort (typically high - low for total candle height)
                shadow_range = valid_high[i] - valid_low[i]
                ShadowPeriodTotal += shadow_range
        
            # Start processing from lookbackTotal onwards
            outIdx = lookbackTotal
            while outIdx < len(valid_high):
                # Calculate real body size
                real_body = abs(valid_close[outIdx] - valid_open[outIdx])
            
                # Calculate upper and lower shadows
                upper_shadow = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx])
                lower_shadow = min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
            
                # Calculate averages
                BodyAverage = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                ShadowAverage = ShadowPeriodTotal / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
            
                # Check if current candle matches ShortLine pattern
                if (real_body < BodyAverage and 
                    upper_shadow < ShadowAverage and 
                    lower_shadow < ShadowAverage):
                    # Determine candle color (1 for bullish, -1 for bearish) and multiply by 100
                    candle_color = 1 if valid_close[outIdx] > valid_open[outIdx] else -1
                    result[valid_indices[outIdx], sec] = candle_color * 100
                else:
                    result[valid_indices[outIdx], sec] = 0
                
                # Update period totals by removing oldest and adding newest
                if outIdx - BodyShortPeriod >= 0:
                    old_body_range = abs(valid_close[BodyTrailingIdx] - valid_open[BodyTrailingIdx])
                    new_body_range = abs(valid_close[outIdx] - valid_open[outIdx])
                    BodyPeriodTotal += new_body_range - old_body_range
                    BodyTrailingIdx += 1
                
                if outIdx - ShadowShortPeriod >= 0:
                    old_shadow_range = valid_high[ShadowTrailingIdx] - valid_low[ShadowTrailingIdx]
                    new_shadow_range = valid_high[outIdx] - valid_low[outIdx]
                    ShadowPeriodTotal += new_shadow_range - old_shadow_range
                    ShadowTrailingIdx += 1
                
                outIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLTAKURI(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle parts as in TA-Lib
        BodyDojiPeriod = 3
        ShadowVeryShortPeriod = 3
        ShadowVeryLongPeriod = 3
        lookbackTotal = max(BodyDojiPeriod, ShadowVeryShortPeriod, ShadowVeryLongPeriod)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for averaging
            BodyDojiPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
            ShadowVeryLongPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            for i in range(lookbackTotal):
                # BodyDoji range (real body size)
                BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                # ShadowVeryShort range (upper shadow)
                ShadowVeryShortPeriodTotal += max(valid_high[i] - max(valid_open[i], valid_close[i]), 0.0)
                # ShadowVeryLong range (lower shadow)
                ShadowVeryLongPeriodTotal += max(min(valid_open[i], valid_close[i]) - valid_low[i], 0.0)
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate averages for comparison
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod
                ShadowVeryLongAverage = ShadowVeryLongPeriodTotal / ShadowVeryLongPeriod
            
                # Calculate current candle metrics
                real_body = abs(valid_close[i] - valid_open[i])
                upper_shadow = max(valid_high[i] - max(valid_open[i], valid_close[i]), 0.0)
                lower_shadow = max(min(valid_open[i], valid_close[i]) - valid_low[i], 0.0)
            
                # Check if current candle matches Takuri pattern
                if (real_body <= BodyDojiAverage and
                    upper_shadow < ShadowVeryShortAverage and
                    lower_shadow > ShadowVeryLongAverage):
                    result[valid_indices[i], sec] = 100.0
                else:
                    result[valid_indices[i], sec] = 0.0
            
                # Update rolling totals by adding current and subtracting trailing
                if i - BodyDojiPeriod >= 0:
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                    BodyDojiPeriodTotal -= abs(valid_close[i - BodyDojiPeriod] - valid_open[i - BodyDojiPeriod])
                
                if i - ShadowVeryShortPeriod >= 0:
                    ShadowVeryShortPeriodTotal += max(valid_high[i] - max(valid_open[i], valid_close[i]), 0.0)
                    ShadowVeryShortPeriodTotal -= max(valid_high[i - ShadowVeryShortPeriod] - max(valid_open[i - ShadowVeryShortPeriod], valid_close[i - ShadowVeryShortPeriod]), 0.0)
                
                if i - ShadowVeryLongPeriod >= 0:
                    ShadowVeryLongPeriodTotal += max(min(valid_open[i], valid_close[i]) - valid_low[i], 0.0)
                    ShadowVeryLongPeriodTotal -= max(min(valid_open[i - ShadowVeryLongPeriod], valid_close[i - ShadowVeryLongPeriod]) - valid_low[i - ShadowVeryLongPeriod], 0.0)
    
        return result



    @staticmethod
    @nb.njit
    def CDLTRISTAR(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        BodyDojiPeriod = 3  # Default period for BodyDoji average as per TA-Lib

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 3:  # Need at least 3 candles for Tristar pattern
                continue

            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]

            # Initialize output array for valid data
            temp_result = np.zeros(len(valid_high))

            # Lookback total as per C code (2 prior candles needed)
            lookback_total = 2
            start_idx = lookback_total

            if start_idx >= len(valid_high):
                continue

            # Initialize BodyPeriodTotal for trailing average calculation
            BodyPeriodTotal = 0.0
            BodyTrailingIdx = 0

            # Calculate initial BodyPeriodTotal for the first valid window
            for i in range(BodyTrailingIdx, start_idx):
                if i < len(valid_high):
                    candle_range = valid_high[i] - valid_low[i]
                    if candle_range == candle_range:  # Check for NaN
                        BodyPeriodTotal += candle_range

            # Main loop starting from start_idx
            for i in range(start_idx, len(valid_high)):
                # Calculate real body for current and previous two candles
                realbody_2 = abs(valid_close[i-2] - valid_open[i-2])
                realbody_1 = abs(valid_close[i-1] - valid_open[i-1])
                realbody_0 = abs(valid_close[i] - valid_open[i])

                # Calculate average body range for comparison (based on i-2 as in C code)
                BodyDojiAverage = BodyPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0

                # Check if all three candles are Doji-like (small body compared to average range)
                if (realbody_2 <= BodyDojiAverage and 
                    realbody_1 <= BodyDojiAverage and 
                    realbody_0 <= BodyDojiAverage):
                    temp_result[i] = 0

                    # Check for bullish Tristar (gap up between first and second candle)
                    if (min(valid_open[i-1], valid_close[i-1]) > max(valid_open[i-2], valid_close[i-2]) and
                        max(valid_open[i], valid_close[i]) < max(valid_open[i-1], valid_close[i-1])):
                        temp_result[i] = -100

                    # Check for bearish Tristar (gap down between first and second candle)
                    if (max(valid_open[i-1], valid_close[i-1]) < min(valid_open[i-2], valid_close[i-2]) and
                        min(valid_open[i], valid_close[i]) > min(valid_open[i-1], valid_close[i-1])):
                        temp_result[i] = 100
                else:
                    temp_result[i] = 0

                # Update BodyPeriodTotal for next iteration (add new, remove old)
                if i + 1 < len(valid_high):
                    new_range = valid_high[i-2] - valid_low[i-2]
                    old_range = valid_high[BodyTrailingIdx] - valid_low[BodyTrailingIdx]
                    if new_range == new_range:  # Check for NaN
                        BodyPeriodTotal += new_range
                    if old_range == old_range:  # Check for NaN
                        BodyPeriodTotal -= old_range
                    BodyTrailingIdx += 1

            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = temp_result[i]

        return result



    @staticmethod
    @nb.njit
    def CMO(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize variables
            lookback_total = timeperiod - 1 if timeperiod > 1 else 0
            start_idx = lookback_total
        
            # Handle special case when timeperiod is 1
            if timeperiod == 1:
                for i in range(len(valid_indices)):
                    if i >= start_idx:
                        orig_idx = valid_indices[i]
                        result[orig_idx, sec] = valid_close[i]
                continue
            
            # Initialize variables for CMO calculation
            today = 0
            prev_value = valid_close[today]
            prev_gain = 0.0
            prev_loss = 0.0
        
            # First loop: Calculate initial sums for gains and losses
            today += 1
            for i in range(timeperiod):
                temp_value1 = valid_close[today]
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                if temp_value2 < 0:
                    prev_loss -= temp_value2
                else:
                    prev_gain += temp_value2
                today += 1
        
            # Calculate initial averages
            prev_loss /= timeperiod
            prev_gain /= timeperiod
        
            # Handle data before start_idx
            while today < start_idx and today < len(valid_close):
                temp_value1 = valid_close[today]
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                prev_loss *= (timeperiod - 1)
                prev_gain *= (timeperiod - 1)
                if temp_value2 < 0:
                    prev_loss -= temp_value2
                else:
                    prev_gain += temp_value2
                prev_loss /= timeperiod
                prev_gain /= timeperiod
                today += 1
        
            # Main calculation loop
            out_idx = 0
            while today < len(valid_close):
                if today >= start_idx:
                    temp_value1 = prev_gain + prev_loss
                    if temp_value1 > 1e-10:
                        result[valid_indices[today], sec] = 100.0 * ((prev_gain - prev_loss) / temp_value1)
                    else:
                        result[valid_indices[today], sec] = 0.0
                    out_idx += 1
            
                temp_value1 = valid_close[today]
                temp_value2 = temp_value1 - prev_value
                prev_value = temp_value1
                prev_loss *= (timeperiod - 1)
                prev_gain *= (timeperiod - 1)
                if temp_value2 < 0:
                    prev_loss -= temp_value2
                else:
                    prev_gain += temp_value2
                prev_loss /= timeperiod
                prev_gain /= timeperiod
                today += 1
    
        return result



    @staticmethod
    @nb.njit
    def CORREL(high, open, low, close, vol, oi, timeperiod=30):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask for close and vol (used as inputs for correlation)
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (close[i, sec] == close[i, sec] and 
                    vol[i, sec] == vol[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
            valid_vol = vol[valid_mask, sec]
        
            # Initialize lookback period as per C code
            lookback_total = timeperiod - 1
            start_idx = lookback_total if lookback_total < len(valid_close) else len(valid_close) - 1
        
            if start_idx >= len(valid_close):
                continue
            
            # Initialize variables for sliding window sums
            sum_x = 0.0
            sum_y = 0.0
            sum_xy = 0.0
            sum_x2 = 0.0
            sum_y2 = 0.0
        
            # Initial sum calculation for the first window
            trailing_idx = start_idx - lookback_total
            for today in range(trailing_idx, start_idx + 1):
                x = valid_close[today]
                y = valid_vol[today]
                sum_x += x
                sum_y += y
                sum_xy += x * y
                sum_x2 += x * x
                sum_y2 += y * y
        
            # Calculate first correlation value
            trailing_x = valid_close[trailing_idx]
            trailing_y = valid_vol[trailing_idx]
            temp_real = (sum_x2 - ((sum_x * sum_x) / timeperiod)) * (sum_y2 - ((sum_y * sum_y) / timeperiod))
            correl_values = np.zeros(len(valid_close))
            if temp_real > 1e-10:
                correl_values[start_idx] = (sum_xy - ((sum_x * sum_y) / timeperiod)) / np.sqrt(temp_real)
            else:
                correl_values[start_idx] = 0.0
        
            # Main loop for remaining points using sliding window
            for today in range(start_idx + 1, len(valid_close)):
                # Remove trailing values
                sum_x -= trailing_x
                sum_y -= trailing_y
                sum_xy -= trailing_x * trailing_y
                sum_x2 -= trailing_x * trailing_x
                sum_y2 -= trailing_y * trailing_y
            
                # Add new values
                x = valid_close[today]
                y = valid_vol[today]
                sum_x += x
                sum_y += y
                sum_xy += x * y
                sum_x2 += x * x
                sum_y2 += y * y
            
                # Update trailing values for next iteration
                trailing_idx += 1
                trailing_x = valid_close[trailing_idx]
                trailing_y = valid_vol[trailing_idx]
            
                # Calculate correlation
                temp_real = (sum_x2 - ((sum_x * sum_x) / timeperiod)) * (sum_y2 - ((sum_y * sum_y) / timeperiod))
                if temp_real > 1e-10:
                    correl_values[today] = (sum_xy - ((sum_x * sum_y) / timeperiod)) / np.sqrt(temp_real)
                else:
                    correl_values[today] = 0.0
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = correl_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def HT_DCPERIOD(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        lookback_total = 32  # As per C code, lookback total is 32 + unstable period, but we handle it as 32 for start index
        rad2deg = 180.0 / (4.0 * np.arctan(1.0))

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True

            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue

            # Extract valid close data
            valid_close = close[valid_mask, sec]

            # Initialize variables for WMA calculation
            trailing_wma_idx = 0
            today = trailing_wma_idx
            period_wma_sub = 0.0
            period_wma_sum = 0.0
            trailing_wma_value = 0.0

            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub = temp_real
                period_wma_sum = temp_real

            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sum += temp_real * 2.0

            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sum += temp_real * 3.0

            # WMA for remaining initial points
            i = 9
            while i > 0 and today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sub -= trailing_wma_value
                period_wma_sum += temp_real * 4.0
                trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
                i -= 1

            # Hilbert Transform variables
            hilbert_idx = 0
            detrender_even = np.zeros(3)
            detrender_odd = np.zeros(3)
            q1_even = np.zeros(3)
            q1_odd = np.zeros(3)
            ji_even = np.zeros(3)
            ji_odd = np.zeros(3)
            jq_even = np.zeros(3)
            jq_odd = np.zeros(3)

            period = 0.0
            prev_i2 = 0.0
            prev_q2 = 0.0
            re = 0.0
            im = 0.0
            i1_for_odd_prev3 = 0.0
            i1_for_odd_prev2 = 0.0
            i1_for_even_prev3 = 0.0
            i1_for_even_prev2 = 0.0
            smooth_period = 0.0

            while today < len(valid_close):
                adjusted_prev_period = (0.075 * period) + 0.54
                today_value = valid_close[today]

                # WMA calculation
                if today < len(valid_close):
                    period_wma_sub += today_value
                    period_wma_sub -= trailing_wma_value
                    period_wma_sum += today_value * 4.0
                    trailing_wma_value = valid_close[trailing_wma_idx]
                    trailing_wma_idx += 1
                    smoothed_value = period_wma_sum * 0.1
                    period_wma_sum -= period_wma_sub

                # Hilbert Transform logic
                if (today % 2) == 0:
                    # Even index processing
                    detrender_even[hilbert_idx] = (0.0962 * smoothed_value) + (0.5769 * detrender_even[(hilbert_idx - 2) % 3]) - (0.5769 * detrender_even[hilbert_idx]) - (0.0962 * detrender_even[(hilbert_idx - 1) % 3])
                    q1_even[hilbert_idx] = (0.0962 * detrender_even[hilbert_idx]) + (0.5769 * q1_even[(hilbert_idx - 2) % 3]) - (0.5769 * q1_even[hilbert_idx]) - (0.0962 * q1_even[(hilbert_idx - 1) % 3])
                    ji_even[hilbert_idx] = (0.0962 * i1_for_even_prev3) + (0.5769 * ji_even[(hilbert_idx - 2) % 3]) - (0.5769 * ji_even[hilbert_idx]) - (0.0962 * ji_even[(hilbert_idx - 1) % 3])
                    jq_even[hilbert_idx] = (0.0962 * q1_even[hilbert_idx]) + (0.5769 * jq_even[(hilbert_idx - 2) % 3]) - (0.5769 * jq_even[hilbert_idx]) - (0.0962 * jq_even[(hilbert_idx - 1) % 3])
                    hilbert_idx = (hilbert_idx + 1) % 3
                    q2 = (0.2 * (q1_even[(hilbert_idx - 1) % 3] + ji_even[(hilbert_idx - 1) % 3])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_even_prev3 - jq_even[(hilbert_idx - 1) % 3])) + (0.8 * prev_i2)
                    i1_for_odd_prev3 = i1_for_odd_prev2
                    i1_for_odd_prev2 = detrender_even[(hilbert_idx - 1) % 3]
                else:
                    # Odd index processing
                    detrender_odd[hilbert_idx] = (0.0962 * smoothed_value) + (0.5769 * detrender_odd[(hilbert_idx - 2) % 3]) - (0.5769 * detrender_odd[hilbert_idx]) - (0.0962 * detrender_odd[(hilbert_idx - 1) % 3])
                    q1_odd[hilbert_idx] = (0.0962 * detrender_odd[hilbert_idx]) + (0.5769 * q1_odd[(hilbert_idx - 2) % 3]) - (0.5769 * q1_odd[hilbert_idx]) - (0.0962 * q1_odd[(hilbert_idx - 1) % 3])
                    ji_odd[hilbert_idx] = (0.0962 * i1_for_odd_prev3) + (0.5769 * ji_odd[(hilbert_idx - 2) % 3]) - (0.5769 * ji_odd[hilbert_idx]) - (0.0962 * ji_odd[(hilbert_idx - 1) % 3])
                    jq_odd[hilbert_idx] = (0.0962 * q1_odd[hilbert_idx]) + (0.5769 * jq_odd[(hilbert_idx - 2) % 3]) - (0.5769 * jq_odd[hilbert_idx]) - (0.0962 * jq_odd[(hilbert_idx - 1) % 3])
                    q2 = (0.2 * (q1_odd[(hilbert_idx - 1) % 3] + ji_odd[(hilbert_idx - 1) % 3])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_odd_prev3 - jq_odd[(hilbert_idx - 1) % 3])) + (0.8 * prev_i2)
                    i1_for_even_prev3 = i1_for_even_prev2
                    i1_for_even_prev2 = detrender_odd[(hilbert_idx - 1) % 3]

                re = (0.2 * ((i2 * prev_i2) + (q2 * prev_q2))) + (0.8 * re)
                im = (0.2 * ((i2 * prev_q2) - (q2 * prev_i2))) + (0.8 * im)
                prev_q2 = q2
                prev_i2 = i2

                temp_real = period
                if im != 0.0 and re != 0.0:
                    period = 360.0 / (np.arctan(im / re) * rad2deg)
                temp_real2 = 1.5 * temp_real
                if period > temp_real2:
                    period = temp_real2
                temp_real2 = 0.67 * temp_real
                if period < temp_real2:
                    period = temp_real2
                if period < 6:
                    period = 6
                elif period > 50:
                    period = 50
                period = (0.2 * period) + (0.8 * temp_real)
                smooth_period = (0.33 * period) + (0.67 * smooth_period)

                if today >= lookback_total:
                    orig_idx = valid_indices[today]
                    result[orig_idx, sec] = smooth_period

                today += 1

        return result



    @staticmethod
    @nb.njit
    def HT_DCPHASE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 63:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize constants
            temp_real = np.arctan(1.0)
            rad2deg = 45.0 / temp_real
            const_deg2rad_by_360 = temp_real * 8.0
            lookback_total = 63
        
            # Check if enough data after lookback
            if len(valid_close) <= lookback_total:
                continue
            
            # Initialize WMA variables
            trailing_wma_idx = 0
            today = trailing_wma_idx
            period_wma_sub = 0.0
            period_wma_sum = 0.0
            trailing_wma_value = 0.0
        
            # Initial WMA calculation for first 3 points
            temp_real = valid_close[today]
            today += 1
            period_wma_sub = temp_real
            period_wma_sum = temp_real
        
            temp_real = valid_close[today]
            today += 1
            period_wma_sub += temp_real
            period_wma_sum += temp_real * 2.0
        
            temp_real = valid_close[today]
            today += 1
            period_wma_sub += temp_real
            period_wma_sum += temp_real * 3.0
        
            # Calculate WMA for next 34 points
            for i in range(34):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sub -= trailing_wma_value
                period_wma_sum += temp_real * 4.0
                trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
        
            # Initialize Hilbert Transform variables
            hilbert_idx = 0
            detrender_even = np.zeros(3)
            detrender_odd = np.zeros(3)
            q1_even = np.zeros(3)
            q1_odd = np.zeros(3)
            ji_even = np.zeros(3)
            ji_odd = np.zeros(3)
            jq_even = np.zeros(3)
            jq_odd = np.zeros(3)
        
            period = 0.0
            prev_i2 = 0.0
            prev_q2 = 0.0
            re = 0.0
            im = 0.0
            i1_for_odd_prev3 = 0.0
            i1_for_odd_prev2 = 0.0
            i1_for_even_prev3 = 0.0
            i1_for_even_prev2 = 0.0
            smooth_period = 0.0
        
            # Circular buffer for smooth price
            smooth_price_size = 64
            smooth_price = np.zeros(smooth_price_size)
            smooth_price_idx = 0
        
            dc_phase = 0.0
            out_idx = 0
        
            while today < len(valid_close):
                adjusted_prev_period = (0.075 * period) + 0.54
                today_value = valid_close[today]
            
                # Update WMA
                period_wma_sub += today_value
                period_wma_sub -= trailing_wma_value
                period_wma_sum += today_value * 4.0
                trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
            
                # Store smoothed value in circular buffer
                smooth_price[smooth_price_idx] = smoothed_value
            
                # Hilbert Transform calculations
                if today % 2 == 0:
                    # Even index processing
                    detrender = (0.0962 * smoothed_value + 0.5769 * detrender_even[2] - 0.5769 * detrender_even[0] - 0.0962 * detrender_even[1]) * adjusted_prev_period
                    q1 = (0.0962 * detrender + 0.5769 * q1_even[2] - 0.5769 * q1_even[0] - 0.0962 * q1_even[1]) * adjusted_prev_period
                    ji = (0.0962 * i1_for_even_prev3 + 0.5769 * ji_even[2] - 0.5769 * ji_even[0] - 0.0962 * ji_even[1]) * adjusted_prev_period
                    jq = (0.0962 * q1 + 0.5769 * jq_even[2] - 0.5769 * jq_even[0] - 0.0962 * jq_even[1]) * adjusted_prev_period
                
                    hilbert_idx += 1
                    if hilbert_idx == 3:
                        hilbert_idx = 0
                    
                    q2 = (0.2 * (q1 + ji)) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_even_prev3 - jq)) + (0.8 * prev_i2)
                    i1_for_odd_prev3 = i1_for_odd_prev2
                    i1_for_odd_prev2 = detrender
                
                    # Update even arrays
                    detrender_even[0] = detrender_even[1]
                    detrender_even[1] = detrender_even[2]
                    detrender_even[2] = detrender
                    q1_even[0] = q1_even[1]
                    q1_even[1] = q1_even[2]
                    q1_even[2] = q1
                    ji_even[0] = ji_even[1]
                    ji_even[1] = ji_even[2]
                    ji_even[2] = ji
                    jq_even[0] = jq_even[1]
                    jq_even[1] = jq_even[2]
                    jq_even[2] = jq
                else:
                    # Odd index processing
                    detrender = (0.0962 * smoothed_value + 0.5769 * detrender_odd[2] - 0.5769 * detrender_odd[0] - 0.0962 * detrender_odd[1]) * adjusted_prev_period
                    q1 = (0.0962 * detrender + 0.5769 * q1_odd[2] - 0.5769 * q1_odd[0] - 0.0962 * q1_odd[1]) * adjusted_prev_period
                    ji = (0.0962 * i1_for_odd_prev3 + 0.5769 * ji_odd[2] - 0.5769 * ji_odd[0] - 0.0962 * ji_odd[1]) * adjusted_prev_period
                    jq = (0.0962 * q1 + 0.5769 * jq_odd[2] - 0.5769 * jq_odd[0] - 0.0962 * jq_odd[1]) * adjusted_prev_period
                
                    q2 = (0.2 * (q1 + ji)) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_odd_prev3 - jq)) + (0.8 * prev_i2)
                    i1_for_even_prev3 = i1_for_even_prev2
                    i1_for_even_prev2 = detrender
                
                    # Update odd arrays
                    detrender_odd[0] = detrender_odd[1]
                    detrender_odd[1] = detrender_odd[2]
                    detrender_odd[2] = detrender
                    q1_odd[0] = q1_odd[1]
                    q1_odd[1] = q1_odd[2]
                    q1_odd[2] = q1
                    ji_odd[0] = ji_odd[1]
                    ji_odd[1] = ji_odd[2]
                    ji_odd[2] = ji
                    jq_odd[0] = jq_odd[1]
                    jq_odd[1] = jq_odd[2]
                    jq_odd[2] = jq
            
                # Update Re and Im
                re = (0.2 * ((i2 * prev_i2) + (q2 * prev_q2))) + (0.8 * re)
                im = (0.2 * ((i2 * prev_q2) - (q2 * prev_i2))) + (0.8 * im)
                prev_q2 = q2
                prev_i2 = i2
            
                # Calculate period
                temp_real = period
                if im != 0.0 and re != 0.0:
                    period = 360.0 / (np.arctan(im / re) * rad2deg)
                temp_real2 = 1.5 * temp_real
                if period > temp_real2:
                    period = temp_real2
                temp_real2 = 0.67 * temp_real
                if period < temp_real2:
                    period = temp_real2
                if period < 6:
                    period = 6
                elif period > 50:
                    period = 50
                period = (0.2 * period) + (0.8 * temp_real)
                smooth_period = (0.33 * period) + (0.67 * smooth_period)
            
                # Calculate DC Period and Phase
                dc_period = smooth_period + 0.5
                dc_period_int = int(dc_period)
                real_part = 0.0
                imag_part = 0.0
                idx = smooth_price_idx
            
                for i in range(dc_period_int):
                    temp_real = (i * const_deg2rad_by_360) / dc_period_int
                    temp_real2 = smooth_price[idx]
                    real_part += np.sin(temp_real) * temp_real2
                    imag_part += np.cos(temp_real) * temp_real2
                    if idx == 0:
                        idx = smooth_price_size - 1
                    else:
                        idx -= 1
            
                temp_real = np.abs(imag_part)
                if temp_real > 0.0:
                    dc_phase = np.arctan(real_part / imag_part) * rad2deg
                elif temp_real <= 0.01:
                    if real_part < 0.0:
                        dc_phase -= 90.0
                    elif real_part > 0.0:
                        dc_phase += 90.0
            
                dc_phase += 90.0
                dc_phase += 360.0 / smooth_period
                if imag_part < 0.0:
                    dc_phase += 180.0
                if dc_phase > 315.0:
                    dc_phase -= 360.0
            
                # Store result if past start index
                if today >= lookback_total:
                    orig_idx = valid_indices[today]
                    result[orig_idx, sec] = dc_phase
            
                # Update circular buffer index
                smooth_price_idx += 1
                if smooth_price_idx >= smooth_price_size:
                    smooth_price_idx = 0
                
                today += 1
    
        return result



    @staticmethod
    @nb.njit
    def HT_PHASOR(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result_inphase = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_quadrature = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        rad2Deg = 180.0 / (4.0 * np.arctan(1.0))
        lookbackTotal = 32

        for sec in range(secs):
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True

            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookbackTotal:
                continue

            valid_close = close[valid_mask, sec]
            trailingWMAIdx = 0
            today = trailingWMAIdx
            tempReal = valid_close[today]
            today += 1
            periodWMASub = tempReal
            periodWMASum = tempReal
            tempReal = valid_close[today]
            today += 1
            periodWMASub += tempReal
            periodWMASum += tempReal * 2.0
            tempReal = valid_close[today]
            today += 1
            periodWMASub += tempReal
            periodWMASum += tempReal * 3.0
            trailingWMAValue = 0.0

            i = 9
            while i > 0:
                tempReal = valid_close[today]
                today += 1
                periodWMASub += tempReal
                periodWMASub -= trailingWMAValue
                periodWMASum += tempReal * 4.0
                trailingWMAValue = valid_close[trailingWMAIdx]
                trailingWMAIdx += 1
                smoothedValue = periodWMASum * 0.1
                periodWMASum -= periodWMASub
                i -= 1

            hilbertIdx = 0
            detrender = np.zeros(3)
            Q1 = np.zeros(3)
            jI = np.zeros(3)
            jQ = np.zeros(3)
            period = 0.0
            outIdx = 0
            prevI2 = 0.0
            prevQ2 = 0.0
            Re = 0.0
            Im = 0.0
            I1ForOddPrev3 = 0.0
            I1ForEvenPrev3 = 0.0
            I1ForOddPrev2 = 0.0
            I1ForEvenPrev2 = 0.0

            while today <= len(valid_close) - 1:
                adjustedPrevPeriod = (0.075 * period) + 0.54
                todayValue = valid_close[today]
                periodWMASub += todayValue
                periodWMASub -= trailingWMAValue
                periodWMASum += todayValue * 4.0
                trailingWMAValue = valid_close[trailingWMAIdx]
                trailingWMAIdx += 1
                smoothedValue = periodWMASum * 0.1
                periodWMASum -= periodWMASub

                if (today % 2) == 0:
                    detrender[hilbertIdx] = (0.0962 * smoothedValue) + (0.5769 * detrender[(hilbertIdx - 2) % 3]) - (0.5769 * detrender[hilbertIdx]) - (0.0962 * detrender[(hilbertIdx - 1) % 3])
                    Q1[hilbertIdx] = (0.0962 * detrender[hilbertIdx]) + (0.5769 * Q1[(hilbertIdx - 2) % 3]) - (0.5769 * Q1[hilbertIdx]) - (0.0962 * Q1[(hilbertIdx - 1) % 3])
                    if today >= lookbackTotal:
                        if outIdx < tdts:
                            orig_idx = valid_indices[today]
                            result_quadrature[orig_idx, sec] = Q1[hilbertIdx]
                            result_inphase[orig_idx, sec] = I1ForEvenPrev3
                            outIdx += 1
                    jI[hilbertIdx] = (0.0962 * I1ForEvenPrev3) + (0.5769 * jI[(hilbertIdx - 2) % 3]) - (0.5769 * jI[hilbertIdx]) - (0.0962 * jI[(hilbertIdx - 1) % 3])
                    jQ[hilbertIdx] = (0.0962 * Q1[hilbertIdx]) + (0.5769 * jQ[(hilbertIdx - 2) % 3]) - (0.5769 * jQ[hilbertIdx]) - (0.0962 * jQ[(hilbertIdx - 1) % 3])
                    if hilbertIdx + 1 == 3:
                        hilbertIdx = 0
                    else:
                        hilbertIdx += 1
                    Q2 = (0.2 * (Q1[(hilbertIdx - 1) % 3] + jI[(hilbertIdx - 1) % 3])) + (0.8 * prevQ2)
                    I2 = (0.2 * (I1ForEvenPrev3 - jQ[(hilbertIdx - 1) % 3])) + (0.8 * prevI2)
                    I1ForOddPrev3 = I1ForOddPrev2
                    I1ForOddPrev2 = detrender[(hilbertIdx - 1) % 3]
                else:
                    detrender[hilbertIdx] = (0.091 * smoothedValue) + (0.822 * detrender[(hilbertIdx - 2) % 3]) - (0.411 * detrender[hilbertIdx]) - (0.091 * detrender[(hilbertIdx - 1) % 3])
                    Q1[hilbertIdx] = (0.091 * detrender[hilbertIdx]) + (0.822 * Q1[(hilbertIdx - 2) % 3]) - (0.411 * Q1[hilbertIdx]) - (0.091 * Q1[(hilbertIdx - 1) % 3])
                    if today >= lookbackTotal:
                        if outIdx < tdts:
                            orig_idx = valid_indices[today]
                            result_quadrature[orig_idx, sec] = Q1[hilbertIdx]
                            result_inphase[orig_idx, sec] = I1ForOddPrev3
                            outIdx += 1
                    jI[hilbertIdx] = (0.091 * I1ForOddPrev3) + (0.822 * jI[(hilbertIdx - 2) % 3]) - (0.411 * jI[hilbertIdx]) - (0.091 * jI[(hilbertIdx - 1) % 3])
                    jQ[hilbertIdx] = (0.091 * Q1[hilbertIdx]) + (0.822 * jQ[(hilbertIdx - 2) % 3]) - (0.411 * jQ[hilbertIdx]) - (0.091 * jQ[(hilbertIdx - 1) % 3])
                    Q2 = (0.2 * (Q1[(hilbertIdx - 1) % 3] + jI[(hilbertIdx - 1) % 3])) + (0.8 * prevQ2)
                    I2 = (0.2 * (I1ForOddPrev3 - jQ[(hilbertIdx - 1) % 3])) + (0.8 * prevI2)
                    I1ForEvenPrev3 = I1ForEvenPrev2
                    I1ForEvenPrev2 = detrender[(hilbertIdx - 1) % 3]

                Re = (0.2 * ((I2 * prevI2) + (Q2 * prevQ2))) + (0.8 * Re)
                Im = (0.2 * ((I2 * prevQ2) - (Q2 * prevI2))) + (0.8 * Im)
                prevQ2 = Q2
                prevI2 = I2
                tempReal = period
                if Im != 0.0 and Re != 0.0:
                    period = 360.0 / (np.arctan(Im / Re) * rad2Deg)
                tempReal2 = 1.5 * tempReal
                if period > tempReal2:
                    period = tempReal2
                tempReal2 = 0.67 * tempReal
                if period < tempReal2:
                    period = tempReal2
                if period < 6:
                    period = 6
                elif period > 50:
                    period = 50
                period = (0.2 * period) + (0.8 * tempReal)
                today += 1

        return result_inphase, result_quadrature



    @staticmethod
    @nb.njit
    def HT_SINE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result_sine = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_lead_sine = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 63:
                continue
            
            valid_close = close[valid_mask, sec]
            lookback_total = 63
        
            # Initialize constants
            temp_real = np.arctan(1.0)
            rad2deg = 45.0 / temp_real
            deg2rad = 1.0 / rad2deg
            const_deg2rad_by_360 = temp_real * 8.0
        
            # Initialize WMA variables
            trailing_wma_idx = 0
            today = trailing_wma_idx
            period_wma_sub = 0.0
            period_wma_sum = 0.0
            trailing_wma_value = 0.0
        
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub = temp_real
                period_wma_sum = temp_real
        
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sum += temp_real * 2.0
        
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sum += temp_real * 3.0
        
            # WMA calculation for initial 34 periods
            i = 34
            while i > 0 and today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sub -= trailing_wma_value
                period_wma_sum += temp_real * 4.0
                if trailing_wma_idx < len(valid_close):
                    trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
                i -= 1
        
            # Initialize Hilbert Transform variables
            hilbert_idx = 0
            detrender_even = np.zeros(3)
            detrender_odd = np.zeros(3)
            q1_even = np.zeros(3)
            q1_odd = np.zeros(3)
            ji_even = np.zeros(3)
            ji_odd = np.zeros(3)
            jq_even = np.zeros(3)
            jq_odd = np.zeros(3)
        
            period = 0.0
            prev_i2 = 0.0
            prev_q2 = 0.0
            re = 0.0
            im = 0.0
            i1_for_odd_prev3 = 0.0
            i1_for_odd_prev2 = 0.0
            i1_for_even_prev3 = 0.0
            i1_for_even_prev2 = 0.0
            smooth_period = 0.0
        
            # Circular buffer for smooth price
            smooth_price_size = 64
            smooth_price = np.zeros(smooth_price_size)
            smooth_price_idx = 0
        
            dc_phase = 0.0
            out_idx = 0
        
            while today < len(valid_close):
                adjusted_prev_period = (0.075 * period) + 0.54
                today_value = valid_close[today]
            
                # WMA update
                period_wma_sub += today_value
                period_wma_sub -= trailing_wma_value
                period_wma_sum += today_value * 4.0
                if trailing_wma_idx < len(valid_close):
                    trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
            
                smooth_price[smooth_price_idx] = smoothed_value
            
                if (today % 2) == 0:
                    # Even Hilbert Transform
                    detrender_even[hilbert_idx] = (0.0962 * smoothed_value) + (0.5769 * detrender_even[(hilbert_idx - 2) % 3]) - (0.5769 * detrender_even[hilbert_idx]) - (0.0962 * detrender_even[(hilbert_idx - 1) % 3])
                    q1_even[hilbert_idx] = (0.0962 * detrender_even[hilbert_idx]) + (0.5769 * q1_even[(hilbert_idx - 2) % 3]) - (0.5769 * q1_even[hilbert_idx]) - (0.0962 * q1_even[(hilbert_idx - 1) % 3])
                    ji_even[hilbert_idx] = (0.0962 * i1_for_even_prev3) + (0.5769 * ji_even[(hilbert_idx - 2) % 3]) - (0.5769 * ji_even[hilbert_idx]) - (0.0962 * ji_even[(hilbert_idx - 1) % 3])
                    jq_even[hilbert_idx] = (0.0962 * q1_even[hilbert_idx]) + (0.5769 * jq_even[(hilbert_idx - 2) % 3]) - (0.5769 * jq_even[hilbert_idx]) - (0.0962 * jq_even[(hilbert_idx - 1) % 3])
                
                    if hilbert_idx == 2:
                        hilbert_idx = 0
                    else:
                        hilbert_idx += 1
                
                    q2 = (0.2 * (q1_even[(hilbert_idx - 1) % 3] + ji_even[(hilbert_idx - 1) % 3])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_even_prev3 - jq_even[(hilbert_idx - 1) % 3])) + (0.8 * prev_i2)
                    i1_for_odd_prev3 = i1_for_odd_prev2
                    i1_for_odd_prev2 = detrender_even[(hilbert_idx - 1) % 3]
                else:
                    # Odd Hilbert Transform
                    detrender_odd[hilbert_idx] = (0.091 * smoothed_value) + (0.822 * detrender_odd[(hilbert_idx - 2) % 3]) - (0.822 * detrender_odd[hilbert_idx]) - (0.091 * detrender_odd[(hilbert_idx - 1) % 3])
                    q1_odd[hilbert_idx] = (0.091 * detrender_odd[hilbert_idx]) + (0.822 * q1_odd[(hilbert_idx - 2) % 3]) - (0.822 * q1_odd[hilbert_idx]) - (0.091 * q1_odd[(hilbert_idx - 1) % 3])
                    ji_odd[hilbert_idx] = (0.091 * i1_for_odd_prev3) + (0.822 * ji_odd[(hilbert_idx - 2) % 3]) - (0.822 * ji_odd[hilbert_idx]) - (0.091 * ji_odd[(hilbert_idx - 1) % 3])
                    jq_odd[hilbert_idx] = (0.091 * q1_odd[hilbert_idx]) + (0.822 * jq_odd[(hilbert_idx - 2) % 3]) - (0.822 * jq_odd[hilbert_idx]) - (0.091 * jq_odd[(hilbert_idx - 1) % 3])
                
                    q2 = (0.2 * (q1_odd[(hilbert_idx - 1) % 3] + ji_odd[(hilbert_idx - 1) % 3])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_odd_prev3 - jq_odd[(hilbert_idx - 1) % 3])) + (0.8 * prev_i2)
                    i1_for_even_prev3 = i1_for_even_prev2
                    i1_for_even_prev2 = detrender_odd[(hilbert_idx - 1) % 3]
            
                re = (0.2 * ((i2 * prev_i2) + (q2 * prev_q2))) + (0.8 * re)
                im = (0.2 * ((i2 * prev_q2) - (q2 * prev_i2))) + (0.8 * im)
                prev_q2 = q2
                prev_i2 = i2
            
                temp_real = period
                if im != 0.0 and re != 0.0:
                    period = 360.0 / (np.arctan(im / re) * rad2deg)
            
                temp_real2 = 1.5 * temp_real
                if period > temp_real2:
                    period = temp_real2
                temp_real2 = 0.67 * temp_real
                if period < temp_real2:
                    period = temp_real2
                if period < 6:
                    period = 6
                elif period > 50:
                    period = 50
                period = (0.2 * period) + (0.8 * temp_real)
                smooth_period = (0.33 * period) + (0.67 * smooth_period)
            
                dc_period = smooth_period + 0.5
                dc_period_int = int(dc_period)
                real_part = 0.0
                imag_part = 0.0
                idx = smooth_price_idx
            
                for i in range(dc_period_int):
                    if idx >= 0 and idx < smooth_price_size:
                        temp_real = (float(i) * const_deg2rad_by_360) / float(dc_period_int)
                        temp_real2 = smooth_price[idx]
                        real_part += np.sin(temp_real) * temp_real2
                        imag_part += np.cos(temp_real) * temp_real2
                    if idx == 0:
                        idx = smooth_price_size - 1
                    else:
                        idx -= 1
            
                temp_real = np.abs(imag_part)
                if temp_real > 0.0:
                    dc_phase = np.arctan(real_part / imag_part) * rad2deg
                elif temp_real <= 0.01:
                    if real_part < 0.0:
                        dc_phase -= 90.0
                    elif real_part > 0.0:
                        dc_phase += 90.0
            
                dc_phase += 90.0
                dc_phase += 360.0 / smooth_period
                if imag_part < 0.0:
                    dc_phase += 180.0
                if dc_phase > 315.0:
                    dc_phase -= 360.0
            
                if today >= lookback_total:
                    if out_idx < len(valid_indices):
                        orig_idx = valid_indices[out_idx]
                        result_sine[orig_idx, sec] = np.sin(dc_phase * deg2rad)
                        result_lead_sine[orig_idx, sec] = np.sin((dc_phase + 45) * deg2rad)
                    out_idx += 1
            
                smooth_price_idx = (smooth_price_idx + 1) % smooth_price_size
                today += 1
    
        return result_sine



    @staticmethod
    @nb.njit
    def HT_TRENDMODE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 63:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
            lookback_total = 63
        
            # Initialize variables
            temp_real = np.arctan(1.0)
            rad2deg = 45.0 / temp_real
            deg2rad = 1.0 / rad2deg
            const_deg2rad_by_360 = temp_real * 8.0
        
            # WMA initialization
            trailing_wma_idx = 0
            today = trailing_wma_idx
            period_wma_sub = 0.0
            period_wma_sum = 0.0
            trailing_wma_value = 0.0
        
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub = temp_real
                period_wma_sum = temp_real
        
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sum += temp_real * 2.0
        
            if today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sum += temp_real * 3.0
        
            # WMA for initial 34 periods
            i = 34
            smoothed_value = 0.0
            while i > 0 and today < len(valid_close):
                temp_real = valid_close[today]
                today += 1
                period_wma_sub += temp_real
                period_wma_sub -= trailing_wma_value
                period_wma_sum += temp_real * 4.0
                if trailing_wma_idx < len(valid_close):
                    trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
                i -= 1
        
            # Hilbert Transform variables
            hilbert_idx = 0
            detrender_even = np.zeros(3)
            detrender_odd = np.zeros(3)
            q1_even = np.zeros(3)
            q1_odd = np.zeros(3)
            ji_even = np.zeros(3)
            ji_odd = np.zeros(3)
            jq_even = np.zeros(3)
            jq_odd = np.zeros(3)
        
            period = 0.0
            prev_i2 = 0.0
            prev_q2 = 0.0
            re = 0.0
            im = 0.0
            i1_for_odd_prev3 = 0.0
            i1_for_even_prev3 = 0.0
            i1_for_odd_prev2 = 0.0
            i1_for_even_prev2 = 0.0
            smooth_period = 0.0
        
            # Circular buffer for smooth price
            smooth_price_size = 64
            smooth_price = np.zeros(smooth_price_size)
            smooth_price_idx = 0
        
            dc_phase = 0.0
            prev_dc_phase = 0.0
            prev_sine = 0.0
            sine = 0.0
            prev_lead_sine = 0.0
            lead_sine = 0.0
            i_trend1 = 0.0
            i_trend2 = 0.0
            i_trend3 = 0.0
            days_in_trend = 0
        
            out_idx = 0
            start_idx = lookback_total if lookback_total < len(valid_indices) else len(valid_indices) - 1
        
            while today < len(valid_close):
                adjusted_prev_period = (0.075 * period) + 0.54
                today_value = valid_close[today]
            
                # WMA calculation
                period_wma_sub += today_value
                period_wma_sub -= trailing_wma_value
                period_wma_sum += today_value * 4.0
                if trailing_wma_idx < len(valid_close):
                    trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
            
                smooth_price[smooth_price_idx] = smoothed_value
            
                # Hilbert Transform calculations
                if today % 2 == 0:
                    # Even index calculations
                    detrender_even[hilbert_idx] = (0.33 * smoothed_value) + (0.67 * detrender_even[(hilbert_idx + 2) % 3])
                    q1_even[hilbert_idx] = (0.33 * detrender_even[hilbert_idx]) + (0.67 * q1_even[(hilbert_idx + 2) % 3])
                    ji_even[hilbert_idx] = (0.33 * i1_for_even_prev3) + (0.67 * ji_even[(hilbert_idx + 2) % 3])
                    jq_even[hilbert_idx] = (0.33 * q1_even[hilbert_idx]) + (0.67 * jq_even[(hilbert_idx + 2) % 3])
                
                    hilbert_idx = (hilbert_idx + 1) % 3
                    q2 = (0.2 * (q1_even[(hilbert_idx + 2) % 3] + ji_even[(hilbert_idx + 2) % 3])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_even_prev3 - jq_even[(hilbert_idx + 2) % 3])) + (0.8 * prev_i2)
                    i1_for_odd_prev3 = i1_for_odd_prev2
                    i1_for_odd_prev2 = detrender_even[(hilbert_idx + 2) % 3]
                else:
                    # Odd index calculations
                    detrender_odd[hilbert_idx] = (0.33 * smoothed_value) + (0.67 * detrender_odd[(hilbert_idx + 2) % 3])
                    q1_odd[hilbert_idx] = (0.33 * detrender_odd[hilbert_idx]) + (0.67 * q1_odd[(hilbert_idx + 2) % 3])
                    ji_odd[hilbert_idx] = (0.33 * i1_for_odd_prev3) + (0.67 * ji_odd[(hilbert_idx + 2) % 3])
                    jq_odd[hilbert_idx] = (0.33 * q1_odd[hilbert_idx]) + (0.67 * jq_odd[(hilbert_idx + 2) % 3])
                
                    q2 = (0.2 * (q1_odd[(hilbert_idx + 2) % 3] + ji_odd[(hilbert_idx + 2) % 3])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_odd_prev3 - jq_odd[(hilbert_idx + 2) % 3])) + (0.8 * prev_i2)
                    i1_for_even_prev3 = i1_for_even_prev2
                    i1_for_even_prev2 = detrender_odd[(hilbert_idx + 2) % 3]
            
                re = (0.2 * ((i2 * prev_i2) + (q2 * prev_q2))) + (0.8 * re)
                im = (0.2 * ((i2 * prev_q2) - (q2 * prev_i2))) + (0.8 * im)
                prev_q2 = q2
                prev_i2 = i2
            
                temp_real = period
                if im != 0.0 and re != 0.0:
                    period = 360.0 / (np.arctan(im / re) * rad2deg)
                temp_real2 = 1.5 * temp_real
                if period > temp_real2:
                    period = temp_real2
                temp_real2 = 0.67 * temp_real
                if period < temp_real2:
                    period = temp_real2
                if period < 6:
                    period = 6
                elif period > 50:
                    period = 50
                period = (0.2 * period) + (0.8 * temp_real)
                smooth_period = (0.33 * period) + (0.67 * smooth_period)
            
                prev_dc_phase = dc_phase
                dc_period = smooth_period + 0.5
                dc_period_int = int(dc_period)
                real_part = 0.0
                imag_part = 0.0
                idx = smooth_price_idx
            
                for i in range(dc_period_int):
                    if idx < 0:
                        idx = smooth_price_size - 1
                    temp_real_val = (i * const_deg2rad_by_360) / dc_period_int
                    temp_real2 = smooth_price[idx]
                    real_part += np.sin(temp_real_val) * temp_real2
                    imag_part += np.cos(temp_real_val) * temp_real2
                    idx -= 1
            
                temp_real = np.abs(imag_part)
                if temp_real > 0.0:
                    dc_phase = np.arctan(real_part / imag_part) * rad2deg
                elif temp_real <= 0.01:
                    if real_part < 0.0:
                        dc_phase -= 90.0
                    elif real_part > 0.0:
                        dc_phase += 90.0
            
                dc_phase += 90.0
                dc_phase += 360.0 / smooth_period
                if imag_part < 0.0:
                    dc_phase += 180.0
                if dc_phase > 315.0:
                    dc_phase -= 360.0
            
                prev_sine = sine
                prev_lead_sine = lead_sine
                sine = np.sin(dc_phase * deg2rad)
                lead_sine = np.sin((dc_phase + 45) * deg2rad)
            
                # Trendline calculation
                dc_period = smooth_period + 0.5
                dc_period_int = int(dc_period)
                idx = today
                temp_real = 0.0
                for i in range(dc_period_int):
                    if idx >= 0:
                        temp_real += valid_close[idx]
                    idx -= 1
                if dc_period_int > 0:
                    temp_real = temp_real / dc_period_int
            
                trendline = (4.0 * temp_real + 3.0 * i_trend1 + 2.0 * i_trend2 + i_trend3) / 10.0
                i_trend3 = i_trend2
                i_trend2 = i_trend1
                i_trend1 = temp_real
            
                trend = 1
                if ((sine > lead_sine) and (prev_sine <= prev_lead_sine)) or ((sine < lead_sine) and (prev_sine >= prev_lead_sine)):
                    days_in_trend = 0
                    trend = 0
                days_in_trend += 1
                if days_in_trend < (0.5 * smooth_period):
                    trend = 0
            
                temp_real = dc_phase - prev_dc_phase
                if smooth_period != 0.0 and (temp_real > (0.67 * 360.0 / smooth_period)) and (temp_real < (1.5 * 360.0 / smooth_period)):
                    trend = 0
            
                temp_real = smooth_price[smooth_price_idx]
                if trendline != 0.0 and np.abs((temp_real - trendline) / trendline) >= 0.015:
                    trend = 1
            
                if today >= start_idx:
                    orig_idx = valid_indices[today]
                    result[orig_idx, sec] = trend
            
                smooth_price_idx = (smooth_price_idx + 1) % smooth_price_size
                today += 1
    
        return result



    @staticmethod
    @nb.njit
    def MACDEXT(high, open, low, close, vol, oi, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
        tdts, secs = close.shape
        result_macd = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_signal = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_hist = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True

            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) == 0:
                continue

            # Extract valid data
            valid_close = close[valid_mask, sec]

            # Swap periods and matypes if slowperiod < fastperiod
            if slowperiod < fastperiod:
                temp_period = slowperiod
                slowperiod = fastperiod
                fastperiod = temp_period
                temp_matype = slowmatype
                slowmatype = fastmatype
                fastmatype = temp_matype

            # Calculate lookback periods for MA functions (simplified as direct periods)
            lookback_fast = fastperiod - 1 if fastperiod > 1 else 0
            lookback_slow = slowperiod - 1 if slowperiod > 1 else 0
            lookback_largest = max(lookback_fast, lookback_slow)
            lookback_signal = signalperiod - 1 if signalperiod > 1 else 0
            lookback_total = lookback_signal + lookback_largest

            if len(valid_close) <= lookback_total:
                continue

            # Allocate temporary buffers for fast and slow MAs
            temp_size = len(valid_close) - lookback_signal
            fast_ma_buffer = np.zeros(temp_size)
            slow_ma_buffer = np.zeros(temp_size)

            # Calculate Fast MA
            if fastmatype == 0:  # SMA
                for i in range(fastperiod - 1, temp_size):
                    sum_val = 0.0
                    for j in range(i - fastperiod + 1, i + 1):
                        sum_val += valid_close[j]
                    fast_ma_buffer[i] = sum_val / fastperiod
            else:  # Simplified EMA for other matypes
                alpha = 2.0 / (fastperiod + 1)
                fast_ma_buffer[fastperiod - 1] = valid_close[fastperiod - 1]
                for i in range(fastperiod, temp_size):
                    fast_ma_buffer[i] = alpha * valid_close[i] + (1 - alpha) * fast_ma_buffer[i - 1]

            # Calculate Slow MA
            if slowmatype == 0:  # SMA
                for i in range(slowperiod - 1, temp_size):
                    sum_val = 0.0
                    for j in range(i - slowperiod + 1, i + 1):
                        sum_val += valid_close[j]
                    slow_ma_buffer[i] = sum_val / slowperiod
            else:  # Simplified EMA for other matypes
                alpha = 2.0 / (slowperiod + 1)
                slow_ma_buffer[slowperiod - 1] = valid_close[slowperiod - 1]
                for i in range(slowperiod, temp_size):
                    slow_ma_buffer[i] = alpha * valid_close[i] + (1 - alpha) * slow_ma_buffer[i - 1]

            # Calculate MACD Line (Fast MA - Slow MA)
            macd_buffer = np.zeros(temp_size)
            for i in range(max(fastperiod, slowperiod) - 1, temp_size):
                macd_buffer[i] = fast_ma_buffer[i] - slow_ma_buffer[i]

            # Calculate Signal Line
            signal_buffer = np.zeros(temp_size)
            if signalmatype == 0:  # SMA
                for i in range(signalperiod - 1 + lookback_largest, temp_size):
                    sum_val = 0.0
                    for j in range(i - signalperiod + 1, i + 1):
                        sum_val += macd_buffer[j]
                    signal_buffer[i] = sum_val / signalperiod
            else:  # Simplified EMA for other matypes
                alpha = 2.0 / (signalperiod + 1)
                start_idx = lookback_largest
                if start_idx < temp_size:
                    signal_buffer[start_idx] = macd_buffer[start_idx]
                    for i in range(start_idx + 1, temp_size):
                        signal_buffer[i] = alpha * macd_buffer[i] + (1 - alpha) * signal_buffer[i - 1]

            # Calculate Histogram
            hist_buffer = np.zeros(temp_size)
            for i in range(lookback_total, temp_size):
                hist_buffer[i] = macd_buffer[i] - signal_buffer[i]

            # Map results back to original array
            for i in range(lookback_total, temp_size):
                orig_idx = valid_indices[i]
                result_macd[orig_idx, sec] = macd_buffer[i]
                result_signal[orig_idx, sec] = signal_buffer[i]
                result_hist[orig_idx, sec] = hist_buffer[i]

        return result_macd, result_signal, result_hist



    @staticmethod
    @nb.njit
    def MACDFIX(high, open, low, close, vol, oi, signalperiod=9):
        tdts, secs = close.shape
        result_macd = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_signal = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_hist = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 26 + signalperiod - 1:  # Need enough data for MACD and signal
                continue
        
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize arrays for MACD calculation
            macd_values = np.zeros(len(valid_close))
            signal_values = np.zeros(len(valid_close))
            hist_values = np.zeros(len(valid_close))
        
            # MACD FIX uses fixed 12 and 26 periods for EMA
            fast_period = 12
            slow_period = 26
        
            # Calculate EMA for fast and slow periods
            fast_ema = np.zeros(len(valid_close))
            slow_ema = np.zeros(len(valid_close))
        
            # EMA multipliers
            fast_multiplier = 2.0 / (fast_period + 1)
            slow_multiplier = 2.0 / (slow_period + 1)
        
            # Initialize first EMA values
            if len(valid_close) >= fast_period:
                fast_ema[fast_period - 1] = np.mean(valid_close[:fast_period])
            if len(valid_close) >= slow_period:
                slow_ema[slow_period - 1] = np.mean(valid_close[:slow_period])
        
            # Calculate subsequent EMA values for fast
            for i in range(fast_period, len(valid_close)):
                fast_ema[i] = (valid_close[i] - fast_ema[i - 1]) * fast_multiplier + fast_ema[i - 1]
        
            # Calculate subsequent EMA values for slow
            for i in range(slow_period, len(valid_close)):
                slow_ema[i] = (valid_close[i] - slow_ema[i - 1]) * slow_multiplier + slow_ema[i - 1]
        
            # Calculate MACD Line (difference between fast and slow EMA)
            for i in range(slow_period - 1, len(valid_close)):
                macd_values[i] = fast_ema[i] - slow_ema[i]
        
            # Calculate Signal Line (EMA of MACD Line)
            signal_multiplier = 2.0 / (signalperiod + 1)
            if len(valid_close) >= slow_period - 1 + signalperiod:
                signal_values[slow_period - 2 + signalperiod] = np.mean(macd_values[slow_period - 1:slow_period - 1 + signalperiod])
        
            for i in range(slow_period - 1 + signalperiod, len(valid_close)):
                signal_values[i] = (macd_values[i] - signal_values[i - 1]) * signal_multiplier + signal_values[i - 1]
        
            # Calculate Histogram (difference between MACD and Signal)
            for i in range(slow_period - 1 + signalperiod - 1, len(valid_close)):
                hist_values[i] = macd_values[i] - signal_values[i]
        
            # Map results back to original array
            start_idx = slow_period - 1 + signalperiod - 1
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result_macd[orig_idx, sec] = macd_values[i]
                result_signal[orig_idx, sec] = signal_values[i]
                result_hist[orig_idx, sec] = hist_values[i]
    
        return result_macd, result_signal, result_hist



    @staticmethod
    @nb.njit
    def MINMAX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result_max = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_min = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize output arrays for this security
            out_max = np.zeros(len(valid_close))
            out_min = np.zeros(len(valid_close))
        
            # Set initial lookback period as per C code
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed if nb_initial_element_needed < len(valid_close) else len(valid_close) - 1
        
            if start_idx >= len(valid_close):
                continue
            
            out_idx = 0
            today = start_idx
            trailing_idx = start_idx - nb_initial_element_needed
        
            while today < len(valid_close):
                tmp_high = valid_close[today]
                tmp_low = valid_close[today]
                highest_idx = -1
                highest = 0.0
                lowest_idx = -1
                lowest = 0.0
            
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_close[highest_idx]
                    i = highest_idx
                    while i <= today:
                        tmp_high = valid_close[i]
                        if tmp_high > highest:
                            highest_idx = i
                            highest = tmp_high
                        i += 1
                elif tmp_high >= highest:
                    highest_idx = today
                    highest = tmp_high
                
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_close[lowest_idx]
                    i = lowest_idx
                    while i <= today:
                        tmp_low = valid_close[i]
                        if tmp_low < lowest:
                            lowest_idx = i
                            lowest = tmp_low
                        i += 1
                elif tmp_low <= lowest:
                    lowest_idx = today
                    lowest = tmp_low
                
                if out_idx < len(out_max):
                    out_max[out_idx] = highest
                    out_min[out_idx] = lowest
                out_idx += 1
                trailing_idx += 1
                today += 1
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                if i - start_idx < out_idx:
                    orig_idx = valid_indices[i]
                    result_max[orig_idx, sec] = out_max[i - start_idx]
                    result_min[orig_idx, sec] = out_min[i - start_idx]
    
        return result_max, result_min



    @staticmethod
    @nb.njit
    def PPO(high, open, low, close, vol, oi, fastperiod=12, slowperiod=26, matype=0):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < max(fastperiod, slowperiod):
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Calculate fast and slow moving averages based on matype
            fast_ma = np.zeros(len(valid_close))
            slow_ma = np.zeros(len(valid_close))
        
            if matype == 0:  # SMA
                for i in range(fastperiod - 1, len(valid_close)):
                    fast_ma[i] = np.mean(valid_close[max(0, i - fastperiod + 1):i + 1])
                for i in range(slowperiod - 1, len(valid_close)):
                    slow_ma[i] = np.mean(valid_close[max(0, i - slowperiod + 1):i + 1])
            else:  # EMA as default fallback (simplified for numba compatibility)
                alpha_fast = 2.0 / (fastperiod + 1)
                alpha_slow = 2.0 / (slowperiod + 1)
                for i in range(len(valid_close)):
                    if i == 0:
                        fast_ma[i] = valid_close[i]
                        slow_ma[i] = valid_close[i]
                    else:
                        fast_ma[i] = alpha_fast * valid_close[i] + (1 - alpha_fast) * fast_ma[i - 1]
                        slow_ma[i] = alpha_slow * valid_close[i] + (1 - alpha_slow) * slow_ma[i - 1]
        
            # Calculate PPO
            ppo_values = np.zeros(len(valid_close))
            start_idx = max(fastperiod, slowperiod) - 1
            for i in range(start_idx, len(valid_close)):
                if slow_ma[i] > 1e-10:  # Avoid division by zero
                    ppo_values[i] = ((fast_ma[i] - slow_ma[i]) / slow_ma[i]) * 100.0
                else:
                    ppo_values[i] = 0.0
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = ppo_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def SAR(high, open, low, close, vol, oi, acceleration=0.02, maximum=0.2):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 2:  # Need at least 2 points to start
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Initialize parameters
            af = acceleration
            if af > maximum:
                af = acceleration = maximum
            
            # Determine initial position (long or short)
            is_long = 1 if valid_high[1] > valid_low[1] else 0
        
            # Initialize variables
            today_idx = 1
            out_idx = 0
            sar_values = np.zeros(len(valid_high))
            new_high = valid_high[0]
            new_low = valid_low[0]
        
            if is_long == 1:
                ep = valid_high[today_idx]
                sar = new_low
            else:
                ep = valid_low[today_idx]
                sar = new_high
            
            new_low = valid_low[today_idx]
            new_high = valid_high[today_idx]
        
            # Main calculation loop
            while today_idx < len(valid_high):
                prev_low = new_low
                prev_high = new_high
                new_low = valid_low[today_idx]
                new_high = valid_high[today_idx]
                today_idx += 1
            
                if is_long == 1:
                    if new_low <= sar:
                        is_long = 0
                        sar = ep
                        if sar < prev_high:
                            sar = prev_high
                        if sar < new_high:
                            sar = new_high
                        sar_values[out_idx] = sar
                        out_idx += 1
                        af = acceleration
                        ep = new_low
                        sar = sar + af * (ep - sar)
                        if sar < prev_high:
                            sar = prev_high
                        if sar < new_high:
                            sar = new_high
                    else:
                        sar_values[out_idx] = sar
                        out_idx += 1
                        if new_high > ep:
                            ep = new_high
                            af += acceleration
                            if af > maximum:
                                af = maximum
                        sar = sar + af * (ep - sar)
                        if sar > prev_low:
                            sar = prev_low
                        if sar > new_low:
                            sar = new_low
                else:
                    if new_high >= sar:
                        is_long = 1
                        sar = ep
                        if sar > prev_low:
                            sar = prev_low
                        if sar > new_low:
                            sar = new_low
                        sar_values[out_idx] = sar
                        out_idx += 1
                        af = acceleration
                        ep = new_high
                        sar = sar + af * (ep - sar)
                        if sar > prev_low:
                            sar = prev_low
                        if sar > new_low:
                            sar = new_low
                    else:
                        sar_values[out_idx] = sar
                        out_idx += 1
                        if new_low < ep:
                            ep = new_low
                            af += acceleration
                            if af > maximum:
                                af = maximum
                        sar = sar + af * (ep - sar)
                        if sar < prev_high:
                            sar = prev_high
                        if sar < new_high:
                            sar = new_high
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i > 0:  # Output starts from second point
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = sar_values[i - 1]
    
        return result



    @staticmethod
    @nb.njit
    def STOCH(high, open, low, close, vol, oi, fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
        tdts, secs = high.shape
        result_slowk = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_slowd = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Calculate lookback periods based on TA-Lib logic
        lookback_k = fastk_period - 1
        lookback_kslow = slowk_period - 1 if slowk_matype == 0 else slowk_period - 1
        lookback_dslow = slowd_period - 1 if slowd_matype == 0 else slowd_period - 1
        lookback_total = lookback_k + lookback_kslow + lookback_dslow
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize temporary buffer for Fast %K calculation
            temp_buffer = np.zeros(len(valid_high))
            out_idx = 0
            trailing_idx = lookback_total if lookback_total < len(valid_high) else 0
            today = trailing_idx + lookback_k if trailing_idx + lookback_k < len(valid_high) else trailing_idx
        
            lowest_idx = -1
            highest_idx = -1
            lowest = 0.0
            highest = 0.0
            diff = 0.0
        
            while today < len(valid_high):
                tmp_low = valid_low[today]
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_low[lowest_idx]
                    i = lowest_idx
                    while i <= today:
                        tmp = valid_low[i]
                        if tmp < lowest:
                            lowest_idx = i
                            lowest = tmp
                        i += 1
                    diff = (highest - lowest) / 100.0
                elif tmp_low <= lowest:
                    lowest_idx = today
                    lowest = tmp_low
                    diff = (highest - lowest) / 100.0
                
                tmp_high = valid_high[today]
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_high[highest_idx]
                    i = highest_idx
                    while i <= today:
                        tmp = valid_high[i]
                        if tmp > highest:
                            highest_idx = i
                            highest = tmp
                        i += 1
                    diff = (highest - lowest) / 100.0
                elif tmp_high >= highest:
                    highest_idx = today
                    highest = tmp_high
                    diff = (highest - lowest) / 100.0
                
                if diff != 0.0:
                    temp_buffer[out_idx] = (valid_close[today] - lowest) / diff
                else:
                    temp_buffer[out_idx] = 0.0
                
                out_idx += 1
                trailing_idx += 1
                today += 1
        
            # Calculate Slow %K using MA
            slowk_values = np.zeros(len(valid_high))
            if slowk_matype == 0:  # SMA
                for i in range(slowk_period - 1, out_idx):
                    sum_val = 0.0
                    count = 0
                    for j in range(i - slowk_period + 1, i + 1):
                        if j >= 0:
                            sum_val += temp_buffer[j]
                            count += 1
                    if count > 0:
                        slowk_values[i] = sum_val / slowk_period
        
            # Calculate Slow %D using MA on Slow %K
            slowd_values = np.zeros(len(valid_high))
            if slowd_matype == 0:  # SMA
                for i in range(slowk_period - 1 + slowd_period - 1, out_idx):
                    sum_val = 0.0
                    count = 0
                    for j in range(i - slowd_period + 1, i + 1):
                        if j >= slowk_period - 1:
                            sum_val += slowk_values[j]
                            count += 1
                    if count > 0:
                        slowd_values[i] = sum_val / slowd_period
        
            # Map results back to original array
            start_idx = lookback_total
            for i in range(start_idx, len(valid_indices)):
                if i - start_idx < out_idx:
                    orig_idx = valid_indices[i]
                    result_slowk[orig_idx, sec] = slowk_values[i - start_idx + lookback_dslow]
                    result_slowd[orig_idx, sec] = slowd_values[i - start_idx]
    
        return result_slowk, result_slowd



    @staticmethod
    @nb.njit
    def STOCHF(high, open, low, close, vol, oi, fastk_period=5, fastd_period=3, fastd_matype=0):
        tdts, secs = high.shape
        result_fastk = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_fastd = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback calculation as per TA-Lib
        lookback_k = fastk_period - 1
        # Simplified lookback for MA calculation (assuming SMA for matype=0)
        lookback_fastd = fastd_period - 1 if fastd_matype == 0 else fastd_period - 1
        lookback_total = lookback_k + lookback_fastd
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize temporary buffer for FastK calculation
            temp_buffer = np.zeros(len(valid_high))
            out_idx = 0
            trailing_idx = 0
            today = lookback_k
        
            while today < len(valid_high):
                lowest_idx = -1
                highest_idx = -1
                lowest = 0.0
                highest = 0.0
                diff = 0.0
            
                # Calculate lowest
                tmp = valid_low[today]
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_low[lowest_idx]
                    for i in range(lowest_idx + 1, today + 1):
                        tmp = valid_low[i]
                        if tmp < lowest:
                            lowest_idx = i
                            lowest = tmp
                    diff = (highest - lowest) / 100.0
                elif tmp <= lowest:
                    lowest_idx = today
                    lowest = tmp
                    diff = (highest - lowest) / 100.0
            
                # Calculate highest
                tmp = valid_high[today]
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_high[highest_idx]
                    for i in range(highest_idx + 1, today + 1):
                        tmp = valid_high[i]
                        if tmp > highest:
                            highest_idx = i
                            highest = tmp
                    diff = (highest - lowest) / 100.0
                elif tmp >= highest:
                    highest_idx = today
                    highest = tmp
                    diff = (highest - lowest) / 100.0
            
                if diff != 0.0:
                    temp_buffer[out_idx] = (valid_close[today] - lowest) / diff
                else:
                    temp_buffer[out_idx] = 0.0
                
                out_idx += 1
                trailing_idx += 1
                today += 1
        
            # Calculate FastD using MA (simplified as SMA for matype=0)
            fastd_values = np.zeros(len(valid_high))
            for i in range(fastd_period - 1, out_idx):
                if i >= fastd_period - 1:
                    sum_val = 0.0
                    count = 0
                    for j in range(i - (fastd_period - 1), i + 1):
                        if temp_buffer[j] == temp_buffer[j]:  # Check for NaN
                            sum_val += temp_buffer[j]
                            count += 1
                    if count > 0:
                        fastd_values[i] = sum_val / fastd_period
        
            # Map results back to original array
            start_idx = lookback_total
            for i in range(start_idx, len(valid_indices)):
                if i - lookback_fastd < out_idx:
                    orig_idx = valid_indices[i]
                    result_fastk[orig_idx, sec] = temp_buffer[i - lookback_fastd]
                    result_fastd[orig_idx, sec] = fastd_values[i - lookback_fastd]
    
        return result_fastk, result_fastd



    @staticmethod
    @nb.njit
    def STOCHRSI(high, open, low, close, vol, oi, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
        tdts, secs = close.shape
        result_fastk = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_fastd = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod + fastk_period + fastd_period - 2:
                continue
        
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Step 1: Calculate RSI
            rsi_values = np.zeros(len(valid_close))
            up_avg = 0.0
            down_avg = 0.0
        
            # Initialize first period for RSI
            for i in range(1, timeperiod + 1):
                delta = valid_close[i] - valid_close[i-1]
                if delta > 0:
                    up_avg += delta
                else:
                    down_avg += abs(delta)
        
            if timeperiod > 0:
                up_avg = up_avg / timeperiod
                down_avg = down_avg / timeperiod
        
            # Calculate first RSI value
            if down_avg > 1e-10:
                rs = up_avg / down_avg
                rsi_values[timeperiod] = 100.0 - (100.0 / (1.0 + rs))
            else:
                rsi_values[timeperiod] = 100.0 if up_avg > 0 else 0.0
        
            # Calculate remaining RSI values using Wilder smoothing
            for i in range(timeperiod + 1, len(valid_close)):
                delta = valid_close[i] - valid_close[i-1]
                up_val = delta if delta > 0 else 0.0
                down_val = abs(delta) if delta < 0 else 0.0
                up_avg = ((up_avg * (timeperiod - 1)) + up_val) / timeperiod
                down_avg = ((down_avg * (timeperiod - 1)) + down_val) / timeperiod
                if down_avg > 1e-10:
                    rs = up_avg / down_avg
                    rsi_values[i] = 100.0 - (100.0 / (1.0 + rs))
                else:
                    rsi_values[i] = 100.0 if up_avg > 0 else 0.0
        
            # Step 2: Calculate Stochastic FastK and FastD from RSI
            fastk_values = np.zeros(len(valid_close))
            fastd_values = np.zeros(len(valid_close))
        
            # Calculate FastK
            for i in range(fastk_period - 1, len(valid_close)):
                # Get the window of RSI values for FastK calculation
                window_start = max(0, i - fastk_period + 1)
                window_rsi = rsi_values[window_start:i + 1]
                window_high = np.nanmax(window_rsi)
                window_low = np.nanmin(window_rsi)
            
                if window_high - window_low > 1e-10:
                    fastk_values[i] = 100.0 * (rsi_values[i] - window_low) / (window_high - window_low)
                else:
                    fastk_values[i] = 0.0
        
            # Calculate FastD based on matype (0 for SMA)
            if fastd_matype == 0:  # Simple Moving Average
                for i in range(fastk_period + fastd_period - 2, len(valid_close)):
                    window_start = max(0, i - fastd_period + 1)
                    window_fastk = fastk_values[window_start:i + 1]
                    valid_window = window_fastk[~np.isnan(window_fastk)]
                    if len(valid_window) > 0:
                        fastd_values[i] = np.mean(valid_window)
        
            # Map results back to original array
            lookback_total = timeperiod + fastk_period + fastd_period - 2
            for i in range(lookback_total, len(valid_indices)):
                orig_idx = valid_indices[i]
                result_fastk[orig_idx, sec] = fastk_values[i]
                result_fastd[orig_idx, sec] = fastd_values[i]
    
        return result_fastd  # Returning FastD as primary output per common usage



    @staticmethod
    @nb.njit
    def SUM(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Initialize variables for SUM calculation
            lookback_total = timeperiod - 1
            start_idx = lookback_total if lookback_total < len(valid_close) else len(valid_close) - 1
            if start_idx >= len(valid_close):
                continue
            
            # Initialize period total for the first window
            period_total = 0.0
            trailing_idx = start_idx - lookback_total
        
            # Warm-up period: sum the first window of data
            if timeperiod > 1:
                for i in range(trailing_idx, start_idx):
                    period_total += valid_close[i]
        
            # Main calculation loop
            out_idx = start_idx
            i = start_idx
            while i < len(valid_close):
                period_total += valid_close[i]
                temp_real = period_total
                if trailing_idx < len(valid_close):
                    period_total -= valid_close[trailing_idx]
                trailing_idx += 1
                if out_idx < len(valid_close):
                    result[valid_indices[out_idx], sec] = temp_real
                out_idx += 1
                i += 1
    
        return result



    @staticmethod
    @nb.njit
    def ULTOSC(high, open, low, close, vol, oi, timeperiod1=7, timeperiod2=14, timeperiod3=28):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Sort periods in descending order as in C code
        periods = np.array([timeperiod1, timeperiod2, timeperiod3])
        sorted_periods = np.sort(periods)[::-1]
        timeperiod1 = sorted_periods[0]
        timeperiod2 = sorted_periods[1]
        timeperiod3 = sorted_periods[2]
    
        # Calculate lookback total as per TA-Lib
        lookback_total = timeperiod1 - 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for each period
            a1_total = 0.0
            a2_total = 0.0
            a3_total = 0.0
            b1_total = 0.0
            b2_total = 0.0
            b3_total = 0.0
        
            # Prime the totals for each period as in C code
            for i in range(lookback_total - timeperiod1 + 1, lookback_total):
                if i >= 0:
                    temp_lt = valid_low[i]
                    temp_ht = valid_high[i]
                    temp_cy = valid_close[i-1] if i > 0 else valid_close[0]
                    true_low = min(temp_lt, temp_cy)
                    close_minus_true_low = valid_close[i] - true_low
                    true_range = temp_ht - temp_lt
                    temp_double = abs(temp_cy - temp_ht)
                    if temp_double > true_range:
                        true_range = temp_double
                    temp_double = abs(temp_cy - temp_lt)
                    if temp_double > true_range:
                        true_range = temp_double
                    a1_total += close_minus_true_low
                    b1_total += true_range
        
            for i in range(lookback_total - timeperiod2 + 1, lookback_total):
                if i >= 0:
                    temp_lt = valid_low[i]
                    temp_ht = valid_high[i]
                    temp_cy = valid_close[i-1] if i > 0 else valid_close[0]
                    true_low = min(temp_lt, temp_cy)
                    close_minus_true_low = valid_close[i] - true_low
                    true_range = temp_ht - temp_lt
                    temp_double = abs(temp_cy - temp_ht)
                    if temp_double > true_range:
                        true_range = temp_double
                    temp_double = abs(temp_cy - temp_lt)
                    if temp_double > true_range:
                        true_range = temp_double
                    a2_total += close_minus_true_low
                    b2_total += true_range
        
            for i in range(lookback_total - timeperiod3 + 1, lookback_total):
                if i >= 0:
                    temp_lt = valid_low[i]
                    temp_ht = valid_high[i]
                    temp_cy = valid_close[i-1] if i > 0 else valid_close[0]
                    true_low = min(temp_lt, temp_cy)
                    close_minus_true_low = valid_close[i] - true_low
                    true_range = temp_ht - temp_lt
                    temp_double = abs(temp_cy - temp_ht)
                    if temp_double > true_range:
                        true_range = temp_double
                    temp_double = abs(temp_cy - temp_lt)
                    if temp_double > true_range:
                        true_range = temp_double
                    a3_total += close_minus_true_low
                    b3_total += true_range
        
            # Main calculation loop
            today = lookback_total
            out_idx = lookback_total
            trailing_idx1 = today - timeperiod1 + 1
            trailing_idx2 = today - timeperiod2 + 1
            trailing_idx3 = today - timeperiod3 + 1
        
            while today < len(valid_high):
                # Calculate terms for current day
                temp_lt = valid_low[today]
                temp_ht = valid_high[today]
                temp_cy = valid_close[today-1] if today > 0 else valid_close[0]
                true_low = min(temp_lt, temp_cy)
                close_minus_true_low = valid_close[today] - true_low
                true_range = temp_ht - temp_lt
                temp_double = abs(temp_cy - temp_ht)
                if temp_double > true_range:
                    true_range = temp_double
                temp_double = abs(temp_cy - temp_lt)
                if temp_double > true_range:
                    true_range = temp_double
            
                # Update totals
                a1_total += close_minus_true_low
                a2_total += close_minus_true_low
                a3_total += close_minus_true_low
                b1_total += true_range
                b2_total += true_range
                b3_total += true_range
            
                # Calculate output
                output = 0.0
                if b1_total > 1e-10:
                    output += 4.0 * (a1_total / b1_total)
                if b2_total > 1e-10:
                    output += 2.0 * (a2_total / b2_total)
                if b3_total > 1e-10:
                    output += (a3_total / b3_total)
            
                # Subtract trailing values for period 1
                if trailing_idx1 >= 0:
                    temp_lt = valid_low[trailing_idx1]
                    temp_ht = valid_high[trailing_idx1]
                    temp_cy = valid_close[trailing_idx1-1] if trailing_idx1 > 0 else valid_close[0]
                    true_low = min(temp_lt, temp_cy)
                    close_minus_true_low = valid_close[trailing_idx1] - true_low
                    true_range = temp_ht - temp_lt
                    temp_double = abs(temp_cy - temp_ht)
                    if temp_double > true_range:
                        true_range = temp_double
                    temp_double = abs(temp_cy - temp_lt)
                    if temp_double > true_range:
                        true_range = temp_double
                    a1_total -= close_minus_true_low
                    b1_total -= true_range
            
                # Subtract trailing values for period 2
                if trailing_idx2 >= 0:
                    temp_lt = valid_low[trailing_idx2]
                    temp_ht = valid_high[trailing_idx2]
                    temp_cy = valid_close[trailing_idx2-1] if trailing_idx2 > 0 else valid_close[0]
                    true_low = min(temp_lt, temp_cy)
                    close_minus_true_low = valid_close[trailing_idx2] - true_low
                    true_range = temp_ht - temp_lt
                    temp_double = abs(temp_cy - temp_ht)
                    if temp_double > true_range:
                        true_range = temp_double
                    temp_double = abs(temp_cy - temp_lt)
                    if temp_double > true_range:
                        true_range = temp_double
                    a2_total -= close_minus_true_low
                    b2_total -= true_range
            
                # Subtract trailing values for period 3
                if trailing_idx3 >= 0:
                    temp_lt = valid_low[trailing_idx3]
                    temp_ht = valid_high[trailing_idx3]
                    temp_cy = valid_close[trailing_idx3-1] if trailing_idx3 > 0 else valid_close[0]
                    true_low = min(temp_lt, temp_cy)
                    close_minus_true_low = valid_close[trailing_idx3] - true_low
                    true_range = temp_ht - temp_lt
                    temp_double = abs(temp_cy - temp_ht)
                    if temp_double > true_range:
                        true_range = temp_double
                    temp_double = abs(temp_cy - temp_lt)
                    if temp_double > true_range:
                        true_range = temp_double
                    a3_total -= close_minus_true_low
                    b3_total -= true_range
            
                # Store result
                if today >= lookback_total:
                    orig_idx = valid_indices[today]
                    result[orig_idx, sec] = 100.0 * (output / 7.0)
            
                today += 1
                trailing_idx1 += 1
                trailing_idx2 += 1
                trailing_idx3 += 1
    
        return result



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
    def MACD(high, open, low, close, vol, oi, fastperiod=12, slowperiod=26, signalperiod=9):
        """
        # MACD - Moving Average Convergence/Divergence
        # MACD是一种趋势跟踪动量指标，展示了证券价格的两个移动平均线之间的关系
        """
        tdts, secs = high.shape
        
        # 初始化结果数组
        macd_line = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        macd_signal = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        macd_hist = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        
        # 如果慢周期小于快周期，交换它们
        if slowperiod < fastperiod:
            slowperiod, fastperiod = fastperiod, slowperiod
        
        # 处理使用默认值的特殊情况
        if slowperiod == 0:
            slowperiod = 26
            k_slow = 0.075  # 固定值26
        else:
            k_slow = 2.0 / (slowperiod + 1.0)
        
        if fastperiod == 0:
            fastperiod = 12
            k_fast = 0.15  # 固定值12
        else:
            k_fast = 2.0 / (fastperiod + 1.0)
            
        k_signal = 2.0 / (signalperiod + 1.0)
        
        # 计算所需的回溯周期
        lookback_signal = signalperiod - 1
        lookback_slow = slowperiod - 1
        lookback_total = lookback_signal + lookback_slow
        
        # 遍历每个证券
        for sec in range(secs):
            # 对于每个证券，一次处理所有时间点
            _close = close[:, sec]
            
            # 如果没有足够的有效数据点，则跳过这个证券
            valid_points = np.sum(~np.isnan(_close))
            if valid_points <= lookback_total:
                continue
                
            # 获取可用的收盘价数据
            valid_close = _close[~np.isnan(_close)]
            valid_length = len(valid_close)
            
            # 计算慢速EMA
            slow_ema = np.zeros(valid_length)
            slow_ema[0] = valid_close[0]
            for i in range(1, valid_length):
                slow_ema[i] = valid_close[i] * k_slow + slow_ema[i-1] * (1 - k_slow)
            
            # 计算快速EMA
            fast_ema = np.zeros(valid_length)
            fast_ema[0] = valid_close[0]
            for i in range(1, valid_length):
                fast_ema[i] = valid_close[i] * k_fast + fast_ema[i-1] * (1 - k_fast)
            
            # 计算MACD线 (快速EMA - 慢速EMA)
            macd_values = fast_ema - slow_ema
            
            # 计算信号线 (MACD的EMA)
            signal_values = np.zeros(valid_length)
            signal_values[0] = macd_values[0]
            for i in range(1, valid_length):
                signal_values[i] = macd_values[i] * k_signal + signal_values[i-1] * (1 - k_signal)
            
            # 计算柱状图 (MACD线 - 信号线)
            hist_values = macd_values - signal_values
            
            # 将结果映射回原始数据中的有效位置
            valid_indices = np.where(~np.isnan(_close))[0]
            
            # 从lookback_total开始输出结果
            output_start = lookback_total
            if output_start < valid_length:
                result_idx = 0
                for i in range(output_start, valid_length):
                    orig_idx = valid_indices[i]
                    macd_line[orig_idx, sec] = macd_values[i]
                    macd_signal[orig_idx, sec] = signal_values[i]
                    macd_hist[orig_idx, sec] = hist_values[i]
                    result_idx += 1

        return macd_line, macd_signal, macd_hist
    

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
    def AROON(high, open, low, close, vol, oi, timeperiod=14):
        """
        Aroon - Aroon Up and Down Indicators
        
        计算Aroon指标，返回Aroon Down和Aroon Up两个数组
        按照TA-Lib的接口约定，返回顺序是：(Aroon Down, Aroon Up)
        
        参数:
            high: 高价数组
            open: 开盘价数组 (未使用)
            low: 低价数组
            close: 收盘价数组 (未使用)
            vol: 成交量数组 (未使用)
            oi: 持仓量数组 (未使用)
            timeperiod: 周期长度，默认14
            
        返回:
            (Aroon Down, Aroon Up)
        """
        tdts, secs = high.shape
        result_up = np.full((tdts, secs), np.nan, dtype=np.float64)
        result_down = np.full((tdts, secs), np.nan, dtype=np.float64)
        
        factor = 100.0 / timeperiod

        for sec in range(secs):
            # 过滤出有效的数据点
            valid_indices = []
            for i in range(tdts):
                if not np.isnan(high[i, sec]) and not np.isnan(low[i, sec]):
                    valid_indices.append(i)
            
            if len(valid_indices) < timeperiod:
                continue
            
            # 将valid_indices转换为数组以便后续操作
            valid_indices = np.array(valid_indices)
            
            # 确定起始索引 - 确保不使用未来数据
            startIdx = timeperiod
            if startIdx >= len(valid_indices):
                continue
            
            # 初始化输出索引
            outIdx = 0
            
            # 开始计算AROON指标
            for i in range(startIdx, len(valid_indices)):
                today = i
                trailingIdx = today - timeperiod
                
                # 在窗口中找到最高价和最低价的位置
                highestIdx = trailingIdx
                highest = high[valid_indices[highestIdx], sec]
                
                lowestIdx = trailingIdx
                lowest = low[valid_indices[lowestIdx], sec]
                
                # 在窗口内寻找最高价和最低价
                for j in range(trailingIdx, today + 1):
                    curr_idx = valid_indices[j]
                    curr_high = high[curr_idx, sec]
                    curr_low = low[curr_idx, sec]
                    
                    if curr_high >= highest:  # 使用 >= 而不是 > 以匹配TA-Lib行为
                        highest = curr_high
                        highestIdx = j
                    
                    if curr_low <= lowest:  # 使用 <= 而不是 < 以匹配TA-Lib行为
                        lowest = curr_low
                        lowestIdx = j
                
                # 计算Aroon指标
                aroon_up = factor * (timeperiod - (today - highestIdx))
                aroon_down = factor * (timeperiod - (today - lowestIdx))
                
                # 将结果存入原始数组的对应位置
                orig_idx = valid_indices[today]
                result_up[orig_idx, sec] = aroon_up
                result_down[orig_idx, sec] = aroon_down
                
                outIdx += 1
        
        # 按照TA-Lib的接口约定，返回顺序是：(Aroon Down, Aroon Up)
        return result_down, result_up



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
    def BETA(high, open, low, close, vol, oi, timeperiod=5):
        """
        Beta指标实现，基于资产和市场之间的线性回归斜率。
        该实现基于参考文档并针对性能进行优化。
        
        在金融中，Beta衡量特定证券相对于整个市场的波动性。
        Beta = 1表示证券与市场同步变动
        Beta < 1表示证券波动性低于市场
        Beta > 1表示证券波动性高于市场
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)

        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (close[i, sec] == close[i, sec] and 
                    vol[i, sec] == vol[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod + 1:  # 需要至少timeperiod+1个点才能计算returns
                continue
            
            # 提取有效数据 - 这里close作为asset, vol作为market
            valid_asset = close[valid_mask, sec]
            valid_market = vol[valid_mask, sec]
        
            # 计算每个点的百分比变化（收益率）
            asset_returns = np.zeros(len(valid_asset))
            market_returns = np.zeros(len(valid_market))
            
            for i in range(1, len(valid_asset)):
                # 计算资产收益率
                if valid_asset[i-1] != 0:
                    asset_returns[i] = (valid_asset[i] - valid_asset[i-1]) / valid_asset[i-1]
                
                # 计算市场收益率
                if valid_market[i-1] != 0:
                    market_returns[i] = (valid_market[i] - valid_market[i-1]) / valid_market[i-1]
            
            # 计算滚动窗口的beta值
            for i in range(timeperiod, len(valid_asset)):
                # 提取时间窗口数据
                asset_window = asset_returns[i-timeperiod+1:i+1]
                market_window = market_returns[i-timeperiod+1:i+1]
                
                # 计算统计量
                s_x = 0.0
                s_y = 0.0
                s_xx = 0.0
                s_xy = 0.0
                
                for j in range(timeperiod):
                    s_x += asset_window[j]
                    s_y += market_window[j]
                    s_xx += asset_window[j] * asset_window[j]
                    s_xy += asset_window[j] * market_window[j]
                
                # 计算beta = (p * s_xy - s_x * s_y) / (p * s_xx - s_x^2)
                denominator = (timeperiod * s_xx) - (s_x * s_x)
                if abs(denominator) > 1e-10:  # 避免除零
                    beta = ((timeperiod * s_xy) - (s_x * s_y)) / denominator
                else:
                    beta = 0.0
                
                # 存储结果
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = beta

        return result



    @staticmethod
    @nb.njit
    def BOP(high, open, low, close, vol, oi):
        """
        BOP - Balance Of Power
        计算方法：(收盘价 - 开盘价) / (最高价 - 最低价)
        用途：衡量市场买卖力量的平衡
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
            if len(valid_indices) < 1:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 计算BOP值
            bop_values = np.zeros(len(valid_high))
            for i in range(len(valid_high)):
                temp_real = valid_high[i] - valid_low[i]
                if temp_real <= 1e-10:  # 避免除零，使用小阈值
                    bop_values[i] = 0.0
                else:
                    bop_values[i] = (valid_close[i] - valid_open[i]) / temp_real
        
            # 映射结果回原始数组
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
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 初始化结果数组
            cci_values = np.zeros(len(valid_high))
        
            # 计算lookback period
            lookback_total = timeperiod - 1
            start_idx = lookback_total if timeperiod > 1 else 0
        
            # 预热期处理：计算前timeperiod-1个点的典型价格
            circ_buffer = np.zeros(timeperiod)
            circ_idx = 0
        
            if timeperiod > 1:
                for i in range(start_idx):
                    typical_price = (valid_high[i] + valid_low[i] + valid_close[i]) / 3.0
                    circ_buffer[circ_idx] = typical_price
                    circ_idx = (circ_idx + 1) % timeperiod
        
            # 主计算阶段
            for i in range(start_idx, len(valid_high)):
                # 计算当前典型价格
                last_value = (valid_high[i] + valid_low[i] + valid_close[i]) / 3.0
                circ_buffer[circ_idx] = last_value
            
                # 计算平均值
                the_average = 0.0
                for j in range(timeperiod):
                    the_average += circ_buffer[j]
                the_average /= timeperiod
            
                # 计算平均偏差
                temp_real2 = 0.0
                for j in range(timeperiod):
                    temp_real2 += abs(circ_buffer[j] - the_average)
            
                # 计算CCI
                temp_real = last_value - the_average
                if temp_real != 0.0 and temp_real2 != 0.0:
                    cci_values[i] = temp_real / (0.015 * (temp_real2 / timeperiod))
                else:
                    cci_values[i] = 0.0
            
                # 更新循环缓冲区索引
                circ_idx = (circ_idx + 1) % timeperiod
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = cci_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDL2CROWS(high, open, low, close, vol, oi, body_long_period=10):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        lookback_total = 2  # As per TA-Lib, need 2 prior candles for CDL2CROWS
    
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
        
            # Initialize output for valid data
            temp_result = np.zeros(len(valid_high))
        
            # Calculate BodyLongPeriodTotal for rolling average of body long
            body_long_trailing_idx = 0
            body_long_period_total = 0.0
        
            # Initial sum for body long average before start index
            start_idx = lookback_total
            if start_idx - 2 - body_long_period >= 0:
                body_long_trailing_idx = start_idx - 2 - body_long_period
                for i in range(body_long_trailing_idx, start_idx - 2):
                    body_long_period_total += abs(valid_open[i] - valid_close[i])
        
            # Main loop starting from lookback_total
            for i in range(start_idx, len(valid_high)):
                # Check for CDL2CROWS pattern
                if (valid_close[i-2] > valid_open[i-2] and  # First candle is white (bullish)
                    abs(valid_close[i-2] - valid_open[i-2]) > (body_long_period_total / body_long_period if body_long_period > 0 else 0) and  # Long body
                    valid_close[i-1] < valid_open[i-1] and  # Second candle is black (bearish)
                    valid_open[i-1] > valid_close[i-2] and  # Gap up between first and second
                    valid_close[i] < valid_open[i] and  # Third candle is black (bearish)
                    valid_open[i] < valid_open[i-1] and valid_open[i] > valid_close[i-1] and  # Open within second candle's body
                    valid_close[i] > valid_open[i-2] and valid_close[i] < valid_close[i-2]):  # Close within first candle's body
                    temp_result[i] = -100
                else:
                    temp_result[i] = 0
                
                # Update BodyLongPeriodTotal for next iteration
                if i - 2 >= 0:
                    body_long_period_total += abs(valid_open[i-2] - valid_close[i-2])
                if body_long_trailing_idx < len(valid_high):
                    body_long_period_total -= abs(valid_open[body_long_trailing_idx] - valid_close[body_long_trailing_idx])
                    body_long_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDL3BLACKCROWS(high, open, low, close, vol, oi, shadow_period=3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (3 days for pattern + shadow_period for averages)
        lookback_total = 3 + shadow_period
    
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
        
            # Initialize shadow totals for the three candles
            shadow_totals = np.zeros(3)
            shadow_trailing_idx = 0
        
            # Pre-calculate shadow totals for the initial window
            for i in range(shadow_trailing_idx, lookback_total - 3):
                shadow_totals[2] += valid_high[i-2] - valid_low[i-2] if i >= 2 else 0
                shadow_totals[1] += valid_high[i-1] - valid_low[i-1] if i >= 1 else 0
                shadow_totals[0] += valid_high[i] - valid_low[i]
        
            # Main loop starting from lookback_total
            for i in range(lookback_total - 1, len(valid_high)):
                # Calculate candle colors (1 for bullish, -1 for bearish)
                color_3 = 1 if valid_close[i-3] > valid_open[i-3] else -1
                color_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate lower shadows
                lower_shadow_2 = valid_open[i-2] - valid_low[i-2] if color_2 == 1 else valid_close[i-2] - valid_low[i-2]
                lower_shadow_1 = valid_open[i-1] - valid_low[i-1] if color_1 == 1 else valid_close[i-1] - valid_low[i-1]
                lower_shadow_0 = valid_open[i] - valid_low[i] if color_0 == 1 else valid_close[i] - valid_low[i]
            
                # Calculate shadow averages
                shadow_avg_2 = shadow_totals[2] / shadow_period if shadow_period > 0 else 0
                shadow_avg_1 = shadow_totals[1] / shadow_period if shadow_period > 0 else 0
                shadow_avg_0 = shadow_totals[0] / shadow_period if shadow_period > 0 else 0
            
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
            
                # Update shadow totals
                for tot_idx in range(2, -1, -1):
                    curr_candle_idx = i - tot_idx
                    trail_candle_idx = shadow_trailing_idx - tot_idx
                    if curr_candle_idx >= 0:
                        shadow_totals[tot_idx] += valid_high[curr_candle_idx] - valid_low[curr_candle_idx]
                    if trail_candle_idx >= 0:
                        shadow_totals[tot_idx] -= valid_high[trail_candle_idx] - valid_low[trail_candle_idx]
            
                shadow_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDL3INSIDE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)

        # TA-Lib默认的BodyLong和BodyShort周期
        BodyLongPeriod = 5
        BodyShortPeriod = 3
        
        # 根据lookback函数计算所需的最小数据点数
        lookbackTotal = max(BodyLongPeriod, BodyShortPeriod) + 2

        for sec in range(secs):
            # 创建有效数据掩码和对应的索引
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
            
            # 获取有效数据的索引
            valid_indices = np.where(valid_mask)[0]
            
            # 检查是否有足够的数据
            if len(valid_indices) <= lookbackTotal:
                continue
                
            # 创建原始索引到连续索引的映射
            orig_to_valid_idx = {}
            for i, idx in enumerate(valid_indices):
                orig_to_valid_idx[idx] = i
                
            # 确定起始位置
            startIdx = lookbackTotal
            
            # 确保索引不会超出数组
            if startIdx >= len(valid_indices):
                continue
                
            # 按照C代码初始化累积值和滑动窗口索引
            BodyLongPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
            
            # 初始化trailing索引，对应C代码中的：
            # BodyLongTrailingIdx = startIdx - 2 - TA_CANDLEAVGPERIOD(BodyLong);
            # BodyShortTrailingIdx = startIdx - 1 - TA_CANDLEAVGPERIOD(BodyShort);
            bodyLongStartIdx = startIdx - 2 - BodyLongPeriod
            bodyShortStartIdx = startIdx - 1 - BodyShortPeriod
            
            BodyLongTrailingIdx = bodyLongStartIdx if bodyLongStartIdx >= 0 else 0
            BodyShortTrailingIdx = bodyShortStartIdx if bodyShortStartIdx >= 0 else 0

            # 计算初始的BodyLongPeriodTotal，对应C代码中的:
            # i = BodyLongTrailingIdx;
            # while(i < startIdx - 2) {
            #     BodyLongPeriodTotal += TA_CANDLERANGE(BodyLong, i);
            #     i++;
            # }
            i = BodyLongTrailingIdx
            while i < startIdx - 2:
                if i < len(valid_indices):
                    idx = valid_indices[i]
                    BodyLongPeriodTotal += abs(close[idx, sec] - open[idx, sec])
                i += 1
                
            # 计算初始的BodyShortPeriodTotal
            i = BodyShortTrailingIdx
            while i < startIdx - 1:
                if i < len(valid_indices):
                    idx = valid_indices[i]
                    BodyShortPeriodTotal += abs(close[idx, sec] - open[idx, sec])
                i += 1
                
            # 主计算循环，对应C代码中的do-while循环
            outIdx = 0
            i = startIdx
            
            while i < len(valid_indices):
                idx = valid_indices[i]
                idx_1 = valid_indices[i-1] if i-1 >= 0 else -1
                idx_2 = valid_indices[i-2] if i-2 >= 0 else -1
                
                if idx_1 == -1 or idx_2 == -1:
                    i += 1
                    continue
                    
                # 计算K线实体大小平均值
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod
                
                # 计算实体大小，对应C代码中的TA_REALBODY宏
                realbody_i_2 = abs(close[idx_2, sec] - open[idx_2, sec])
                realbody_i_1 = abs(close[idx_1, sec] - open[idx_1, sec])
                
                # 计算K线颜色，对应C代码中的TA_CANDLECOLOR宏
                color_i_2 = 1 if close[idx_2, sec] > open[idx_2, sec] else -1
                color_i = 1 if close[idx, sec] > open[idx, sec] else -1
                
                # 检查CDL3INSIDE模式，完全按C代码条件判断
                if (realbody_i_2 > BodyLongAverage and                             # 第1根: 长实体
                    realbody_i_1 <= BodyShortAverage and                           # 第2根: 短实体
                    max(close[idx_1, sec], open[idx_1, sec]) < max(close[idx_2, sec], open[idx_2, sec]) and  # 第2根被第1根完全包含
                    min(close[idx_1, sec], open[idx_1, sec]) > min(close[idx_2, sec], open[idx_2, sec]) and
                    ((color_i_2 == 1 and color_i == -1 and close[idx, sec] < open[idx_2, sec]) or  # 第3根: 与第1根相反颜色且收盘超出第1根开盘价
                    (color_i_2 == -1 and color_i == 1 and close[idx, sec] > open[idx_2, sec]))
                ):
                    result[idx, sec] = -color_i_2 * 100  # 返回值: -color_i_2 * 100
                else:
                    result[idx, sec] = 0
                    
                # 更新累计值，这部分在C代码注释中有特别说明:
                # "add the current range and subtract the first range: this is done after the pattern recognition"
                BodyLongPeriodTotal += abs(close[idx_2, sec] - open[idx_2, sec])
                
                trailing_idx = valid_indices[BodyLongTrailingIdx] if BodyLongTrailingIdx < len(valid_indices) else -1
                if trailing_idx != -1:
                    BodyLongPeriodTotal -= abs(close[trailing_idx, sec] - open[trailing_idx, sec])
                    
                BodyShortPeriodTotal += abs(close[idx_1, sec] - open[idx_1, sec])
                
                trailing_idx = valid_indices[BodyShortTrailingIdx] if BodyShortTrailingIdx < len(valid_indices) else -1
                if trailing_idx != -1:
                    BodyShortPeriodTotal -= abs(close[trailing_idx, sec] - open[trailing_idx, sec])
                    
                # 递增trailing索引
                BodyLongTrailingIdx += 1
                BodyShortTrailingIdx += 1
                
                i += 1
                outIdx += 1
        
        return result



    @staticmethod
    @nb.njit
    def CDL3LINESTRIKE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (3 prior candles needed)
        lookback_total = 3
    
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
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize NearPeriodTotal for averaging
            near_period_total_3 = 0.0
            near_period_total_2 = 0.0
            near_trailing_idx = 0
        
            # Pre-calculate initial NearPeriodTotal for the first valid output point
            start_idx = lookback_total
            if start_idx < near_period:
                near_trailing_idx = 0
            else:
                near_trailing_idx = start_idx - near_period
            
            i = near_trailing_idx
            while i < start_idx and i < len(valid_high):
                if i >= 3:
                    near_period_total_3 += valid_high[i-3] - valid_low[i-3]
                if i >= 2:
                    near_period_total_2 += valid_high[i-2] - valid_low[i-2]
                i += 1
        
            # Main calculation loop
            i = start_idx
            while i < len(valid_high):
                # Determine candle colors (1 for bullish, -1 for bearish)
                color_3 = 1 if valid_close[i-3] > valid_open[i-3] else -1
                color_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate averages for Near range
                near_avg_3 = near_period_total_3 / near_period if near_period > 0 else 0.0
                near_avg_2 = near_period_total_2 / near_period if near_period > 0 else 0.0
            
                # Check conditions for 3 Line Strike pattern
                if (color_3 == color_2 and 
                    color_2 == color_1 and 
                    color_0 == -color_1):
                
                    # Check if open prices are within the range of prior candles
                    min_3 = min(valid_open[i-3], valid_close[i-3])
                    max_3 = max(valid_open[i-3], valid_close[i-3])
                    min_2 = min(valid_open[i-2], valid_close[i-2])
                    max_2 = max(valid_open[i-2], valid_close[i-2])
                
                    open_check_2 = (valid_open[i-2] >= min_3 - near_avg_3 and 
                                   valid_open[i-2] <= max_3 + near_avg_3)
                    open_check_1 = (valid_open[i-1] >= min_2 - near_avg_2 and 
                                   valid_open[i-1] <= max_2 + near_avg_2)
                
                    if open_check_2 and open_check_1:
                        if (color_1 == 1 and 
                            valid_close[i-1] > valid_close[i-2] and 
                            valid_close[i-2] > valid_close[i-3] and 
                            valid_open[i] > valid_close[i-1] and 
                            valid_close[i] < valid_open[i-3]):
                            result[valid_indices[i], sec] = 100
                        elif (color_1 == -1 and 
                              valid_close[i-1] < valid_close[i-2] and 
                              valid_close[i-2] < valid_close[i-3] and 
                              valid_open[i] < valid_close[i-1] and 
                              valid_close[i] > valid_open[i-3]):
                            result[valid_indices[i], sec] = -100
                        else:
                            result[valid_indices[i], sec] = 0
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update NearPeriodTotal for next iteration
                if i < len(valid_high):
                    if i >= 3:
                        near_period_total_3 += (valid_high[i-3] - valid_low[i-3])
                    if i >= 2:
                        near_period_total_2 += (valid_high[i-2] - valid_low[i-2])
                    if near_trailing_idx < len(valid_high):
                        if near_trailing_idx >= 3:
                            near_period_total_3 -= (valid_high[near_trailing_idx-3] - valid_low[near_trailing_idx-3])
                        if near_trailing_idx >= 2:
                            near_period_total_2 -= (valid_high[near_trailing_idx-2] - valid_low[near_trailing_idx-2])
                    near_trailing_idx += 1
                i += 1
    
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
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for averages
            BodyLongPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal_1 = 0.0
            ShadowVeryShortPeriodTotal_0 = 0.0
            BodyShortPeriodTotal = 0.0
        
            # Calculate initial totals for averages before startIdx
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
        
            # Main loop for pattern detection
            for i in range(lookbackTotal, len(valid_high)):
                # Check for 3 Stars in the South pattern conditions
                if (valid_close[i-2] < valid_open[i-2] and  # Bearish first candle
                    valid_close[i-1] < valid_open[i-1] and  # Bearish second candle
                    valid_close[i] < valid_open[i] and      # Bearish third candle
                    abs(valid_close[i-2] - valid_open[i-2]) > (BodyLongPeriodTotal / BodyLongPeriod) and  # Long body first candle
                    (valid_close[i-2] - valid_low[i-2] if valid_close[i-2] >= valid_open[i-2] else valid_open[i-2] - valid_low[i-2]) > (ShadowLongPeriodTotal / ShadowLongPeriod) and  # Long lower shadow first candle
                    abs(valid_close[i-1] - valid_open[i-1]) < abs(valid_close[i-2] - valid_open[i-2]) and  # Smaller body second candle
                    valid_open[i-1] > valid_close[i-2] and valid_open[i-1] <= valid_high[i-2] and  # Second candle opens above first close
                    valid_low[i-1] < valid_close[i-2] and valid_low[i-1] >= valid_low[i-2] and  # Second candle low within first range
                    (valid_close[i-1] - valid_low[i-1] if valid_close[i-1] >= valid_open[i-1] else valid_open[i-1] - valid_low[i-1]) > (ShadowVeryShortPeriodTotal_1 / ShadowVeryShortPeriod) and  # Long lower shadow second candle
                    abs(valid_close[i] - valid_open[i]) < (BodyShortPeriodTotal / BodyShortPeriod) and  # Short body third candle
                    (valid_close[i] - valid_low[i] if valid_close[i] >= valid_open[i] else valid_open[i] - valid_low[i]) < (ShadowVeryShortPeriodTotal_0 / ShadowVeryShortPeriod) and  # Short lower shadow third candle
                    (valid_high[i] - valid_close[i] if valid_close[i] >= valid_open[i] else valid_high[i] - valid_open[i]) < (ShadowVeryShortPeriodTotal_0 / ShadowVeryShortPeriod) and  # Short upper shadow third candle
                    valid_low[i] > valid_low[i-1] and valid_high[i] < valid_high[i-1]):  # Third candle within second range
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update rolling totals for averages
                BodyLongPeriodTotal += abs(valid_close[i-2] - valid_open[i-2]) - abs(valid_close[BodyLongTrailingIdx-2] - valid_open[BodyLongTrailingIdx-2])
                ShadowLongPeriodTotal += (max(0.0, valid_close[i-2] - valid_low[i-2]) if valid_close[i-2] >= valid_open[i-2] else max(0.0, valid_open[i-2] - valid_low[i-2])) - \
                                         (max(0.0, valid_close[ShadowLongTrailingIdx-2] - valid_low[ShadowLongTrailingIdx-2]) if valid_close[ShadowLongTrailingIdx-2] >= valid_open[ShadowLongTrailingIdx-2] else max(0.0, valid_open[ShadowLongTrailingIdx-2] - valid_low[ShadowLongTrailingIdx-2]))
                ShadowVeryShortPeriodTotal_1 += (max(0.0, valid_close[i-1] - valid_low[i-1]) if valid_close[i-1] >= valid_open[i-1] else max(0.0, valid_open[i-1] - valid_low[i-1])) - \
                                                (max(0.0, valid_close[ShadowVeryShortTrailingIdx-1] - valid_low[ShadowVeryShortTrailingIdx-1]) if valid_close[ShadowVeryShortTrailingIdx-1] >= valid_open[ShadowVeryShortTrailingIdx-1] else max(0.0, valid_open[ShadowVeryShortTrailingIdx-1] - valid_low[ShadowVeryShortTrailingIdx-1]))
                ShadowVeryShortPeriodTotal_0 += (max(0.0, valid_close[i] - valid_low[i]) if valid_close[i] >= valid_open[i] else max(0.0, valid_open[i] - valid_low[i])) - \
                                                (max(0.0, valid_close[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]) if valid_close[ShadowVeryShortTrailingIdx] >= valid_open[ShadowVeryShortTrailingIdx] else max(0.0, valid_open[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]))
                BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i]) - abs(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx])
            
                # Increment trailing indices
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
    
        # Define lookback periods for different candle averages as per TA-Lib defaults
        ShadowVeryShortPeriod = 7
        NearPeriod = 10
        FarPeriod = 20
        BodyShortPeriod = 5
        lookbackTotal = max(ShadowVeryShortPeriod, NearPeriod, FarPeriod, BodyShortPeriod) + 2
    
        for sec in range(secs):
            # Initialize arrays for rolling totals
            ShadowVeryShortPeriodTotal = np.zeros(3)
            NearPeriodTotal = np.zeros(3)
            FarPeriodTotal = np.zeros(3)
            BodyShortPeriodTotal = 0.0
        
            # Calculate trailing indices for each period
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
            NearTrailingIdx = lookbackTotal - NearPeriod
            FarTrailingIdx = lookbackTotal - FarPeriod
            BodyShortTrailingIdx = lookbackTotal - BodyShortPeriod
        
            # Pre-calculate totals for the lookback period
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                ShadowVeryShortPeriodTotal[2] += max(high[i-2, sec] - close[i-2, sec], 0.0) if close[i-2, sec] > open[i-2, sec] else max(open[i-2, sec] - high[i-2, sec], 0.0)
                ShadowVeryShortPeriodTotal[1] += max(high[i-1, sec] - close[i-1, sec], 0.0) if close[i-1, sec] > open[i-1, sec] else max(open[i-1, sec] - high[i-1, sec], 0.0)
                ShadowVeryShortPeriodTotal[0] += max(high[i, sec] - close[i, sec], 0.0) if close[i, sec] > open[i, sec] else max(open[i, sec] - high[i, sec], 0.0)
        
            for i in range(NearTrailingIdx, lookbackTotal):
                NearPeriodTotal[2] += max(close[i-2, sec] - open[i-2, sec], 0.0) if close[i-2, sec] > open[i-2, sec] else max(open[i-2, sec] - close[i-2, sec], 0.0)
                NearPeriodTotal[1] += max(close[i-1, sec] - open[i-1, sec], 0.0) if close[i-1, sec] > open[i-1, sec] else max(open[i-1, sec] - close[i-1, sec], 0.0)
        
            for i in range(FarTrailingIdx, lookbackTotal):
                FarPeriodTotal[2] += max(close[i-2, sec] - open[i-2, sec], 0.0) if close[i-2, sec] > open[i-2, sec] else max(open[i-2, sec] - close[i-2, sec], 0.0)
                FarPeriodTotal[1] += max(close[i-1, sec] - open[i-1, sec], 0.0) if close[i-1, sec] > open[i-1, sec] else max(open[i-1, sec] - close[i-1, sec], 0.0)
        
            for i in range(BodyShortTrailingIdx, lookbackTotal):
                BodyShortPeriodTotal += abs(close[i, sec] - open[i, sec])
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, tdts):
                # Check for valid data
                if (high[i, sec] != high[i, sec] or open[i, sec] != open[i, sec] or
                    low[i, sec] != low[i, sec] or close[i, sec] != close[i, sec]):
                    continue
                
                # Calculate candle colors (1 for white/up, -1 for black/down)
                color_2 = 1 if close[i-2, sec] > open[i-2, sec] else -1
                color_1 = 1 if close[i-1, sec] > open[i-1, sec] else -1
                color_0 = 1 if close[i, sec] > open[i, sec] else -1
            
                # Calculate upper shadows
                upper_shadow_2 = high[i-2, sec] - close[i-2, sec] if color_2 == 1 else open[i-2, sec] - high[i-2, sec]
                upper_shadow_1 = high[i-1, sec] - close[i-1, sec] if color_1 == 1 else open[i-1, sec] - high[i-1, sec]
                upper_shadow_0 = high[i, sec] - close[i, sec] if color_0 == 1 else open[i, sec] - high[i, sec]
            
                # Calculate real bodies
                real_body_2 = abs(close[i-2, sec] - open[i-2, sec])
                real_body_1 = abs(close[i-1, sec] - open[i-1, sec])
                real_body_0 = abs(close[i, sec] - open[i, sec])
            
                # Calculate averages
                shadow_avg_2 = ShadowVeryShortPeriodTotal[2] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                shadow_avg_1 = ShadowVeryShortPeriodTotal[1] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                shadow_avg_0 = ShadowVeryShortPeriodTotal[0] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                near_avg_2 = NearPeriodTotal[2] / NearPeriod if NearPeriod > 0 else 0.0
                near_avg_1 = NearPeriodTotal[1] / NearPeriod if NearPeriod > 0 else 0.0
                far_avg_2 = FarPeriodTotal[2] / FarPeriod if FarPeriod > 0 else 0.0
                far_avg_1 = FarPeriodTotal[1] / FarPeriod if FarPeriod > 0 else 0.0
                body_short_avg = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check 3 White Soldiers pattern conditions
                if (color_2 == 1 and upper_shadow_2 < shadow_avg_2 and
                    color_1 == 1 and upper_shadow_1 < shadow_avg_1 and
                    color_0 == 1 and upper_shadow_0 < shadow_avg_0 and
                    close[i, sec] > close[i-1, sec] and close[i-1, sec] > close[i-2, sec] and
                    open[i-1, sec] > open[i-2, sec] and open[i-1, sec] <= close[i-2, sec] + near_avg_2 and
                    open[i, sec] > open[i-1, sec] and open[i, sec] <= close[i-1, sec] + near_avg_1 and
                    real_body_1 > real_body_2 - far_avg_2 and
                    real_body_0 > real_body_1 - far_avg_1 and
                    real_body_0 > body_short_avg):
                    result[i, sec] = 100
                else:
                    result[i, sec] = 0
            
                # Update rolling totals
                for totIdx in range(3):
                    new_shadow = max(high[i-totIdx, sec] - close[i-totIdx, sec], 0.0) if close[i-totIdx, sec] > open[i-totIdx, sec] else max(open[i-totIdx, sec] - high[i-totIdx, sec], 0.0)
                    old_shadow = max(high[ShadowVeryShortTrailingIdx-totIdx, sec] - close[ShadowVeryShortTrailingIdx-totIdx, sec], 0.0) if close[ShadowVeryShortTrailingIdx-totIdx, sec] > open[ShadowVeryShortTrailingIdx-totIdx, sec] else max(open[ShadowVeryShortTrailingIdx-totIdx, sec] - high[ShadowVeryShortTrailingIdx-totIdx, sec], 0.0)
                    ShadowVeryShortPeriodTotal[totIdx] += new_shadow - old_shadow
            
                for totIdx in range(1, 3):
                    new_near = max(close[i-totIdx, sec] - open[i-totIdx, sec], 0.0) if close[i-totIdx, sec] > open[i-totIdx, sec] else max(open[i-totIdx, sec] - close[i-totIdx, sec], 0.0)
                    old_near = max(close[NearTrailingIdx-totIdx, sec] - open[NearTrailingIdx-totIdx, sec], 0.0) if close[NearTrailingIdx-totIdx, sec] > open[NearTrailingIdx-totIdx, sec] else max(open[NearTrailingIdx-totIdx, sec] - close[NearTrailingIdx-totIdx, sec], 0.0)
                    NearPeriodTotal[totIdx] += new_near - old_near
                
                    new_far = max(close[i-totIdx, sec] - open[i-totIdx, sec], 0.0) if close[i-totIdx, sec] > open[i-totIdx, sec] else max(open[i-totIdx, sec] - close[i-totIdx, sec], 0.0)
                    old_far = max(close[FarTrailingIdx-totIdx, sec] - open[FarTrailingIdx-totIdx, sec], 0.0) if close[FarTrailingIdx-totIdx, sec] > open[FarTrailingIdx-totIdx, sec] else max(open[FarTrailingIdx-totIdx, sec] - close[FarTrailingIdx-totIdx, sec], 0.0)
                    FarPeriodTotal[totIdx] += new_far - old_far
            
                new_body = abs(close[i, sec] - open[i, sec])
                old_body = abs(close[BodyShortTrailingIdx, sec] - open[BodyShortTrailingIdx, sec])
                BodyShortPeriodTotal += new_body - old_body
            
                # Increment trailing indices
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
        body_doji_period = 10  # Default for BodyDoji in TA-Lib
        body_short_period = 10  # Default for BodyShort in TA-Lib
    
        # Lookback total is 2 days prior to current for pattern recognition
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
            if len(valid_indices) < lookback_total + 1:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for rolling averages
            body_long_total = 0.0
            body_doji_total = 0.0
            body_short_total = 0.0
        
            # Calculate initial totals for body ranges
            start_idx = lookback_total
            body_long_trailing_idx = start_idx - 2 - body_long_period
            body_doji_trailing_idx = start_idx - 1 - body_doji_period
            body_short_trailing_idx = start_idx - body_short_period
        
            i = max(0, body_long_trailing_idx)
            while i < start_idx - 2 and i < len(valid_high):
                body_long_total += abs(valid_close[i] - valid_open[i])
                i += 1
            
            i = max(0, body_doji_trailing_idx)
            while i < start_idx - 1 and i < len(valid_high):
                body_doji_total += abs(valid_close[i] - valid_open[i])
                i += 1
            
            i = max(0, body_short_trailing_idx)
            while i < start_idx and i < len(valid_high):
                body_short_total += abs(valid_close[i] - valid_open[i])
                i += 1
        
            # Main loop for pattern detection
            for i in range(start_idx, len(valid_high)):
                # Calculate real body sizes
                body_2 = abs(valid_close[i-2] - valid_open[i-2])
                body_1 = abs(valid_close[i-1] - valid_open[i-1])
                body_0 = abs(valid_close[i] - valid_open[i])
            
                # Calculate averages
                body_long_avg = body_long_total / body_long_period if body_long_period > 0 else 0.0
                body_doji_avg = body_doji_total / body_doji_period if body_doji_period > 0 else 0.0
                body_short_avg = body_short_total / body_short_period if body_short_period > 0 else 0.0
            
                # Determine candle colors (1 for bullish, -1 for bearish)
                color_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Check for gaps
                gap_up_1_2 = valid_low[i-1] > valid_high[i-2]
                gap_down_1_2 = valid_high[i-1] < valid_low[i-2]
                gap_up_0_1 = valid_low[i] > valid_high[i-1]
                gap_down_0_1 = valid_high[i] < valid_low[i-1]
            
                # Check for bullish abandoned baby
                bullish_condition = (color_2 == 1 and 
                                   color_0 == -1 and 
                                   valid_close[i] < valid_close[i-2] - body_2 * penetration and 
                                   gap_up_1_2 and 
                                   gap_down_0_1)
            
                # Check for bearish abandoned baby
                bearish_condition = (color_2 == -1 and 
                                  color_0 == 1 and 
                                  valid_close[i] > valid_close[i-2] + body_2 * penetration and 
                                  gap_down_1_2 and 
                                  gap_up_0_1)
            
                # Check if pattern conditions are met
                if (body_2 > body_long_avg and 
                    body_1 <= body_doji_avg and 
                    body_0 > body_short_avg and 
                    (bullish_condition or bearish_condition)):
                    result[valid_indices[i], sec] = color_0 * 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update rolling totals
                if i - 2 >= 0:
                    body_long_total += abs(valid_close[i-2] - valid_open[i-2])
                if body_long_trailing_idx >= 0 and body_long_trailing_idx < len(valid_high):
                    body_long_total -= abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
                body_long_trailing_idx += 1
            
                if i - 1 >= 0:
                    body_doji_total += abs(valid_close[i-1] - valid_open[i-1])
                if body_doji_trailing_idx >= 0 and body_doji_trailing_idx < len(valid_high):
                    body_doji_total -= abs(valid_close[body_doji_trailing_idx] - valid_open[body_doji_trailing_idx])
                body_doji_trailing_idx += 1
            
                body_short_total += abs(valid_close[i] - valid_open[i])
                if body_short_trailing_idx >= 0 and body_short_trailing_idx < len(valid_high):
                    body_short_total -= abs(valid_close[body_short_trailing_idx] - valid_open[body_short_trailing_idx])
                body_short_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLADVANCEBLOCK(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        ShadowShortPeriod = 5
        ShadowLongPeriod = 5
        NearPeriod = 5
        FarPeriod = 5
        BodyLongPeriod = 5
    
        # Total lookback period (maximum of all periods + 2 for pattern detection)
        lookbackTotal = max(ShadowShortPeriod, ShadowLongPeriod, NearPeriod, FarPeriod, BodyLongPeriod) + 2
    
        for sec in range(secs):
            # Initialize arrays for period totals
            ShadowShortPeriodTotal = np.zeros(3)
            ShadowLongPeriodTotal = np.zeros(2)
            NearPeriodTotal = np.zeros(3)
            FarPeriodTotal = np.zeros(3)
            BodyLongPeriodTotal = 0.0
        
            # Trailing indices for rolling window calculations
            ShadowShortTrailingIdx = lookbackTotal - ShadowShortPeriod
            ShadowLongTrailingIdx = lookbackTotal - ShadowLongPeriod
            NearTrailingIdx = lookbackTotal - NearPeriod
            FarTrailingIdx = lookbackTotal - FarPeriod
            BodyLongTrailingIdx = lookbackTotal - BodyLongPeriod
        
            # Pre-calculate period totals for the lookback period
            for i in range(ShadowShortTrailingIdx, lookbackTotal):
                ShadowShortPeriodTotal[2] += max(high[i-2, sec] - close[i-2, sec], 0.0) if open[i-2, sec] > close[i-2, sec] else max(open[i-2, sec] - close[i-2, sec], 0.0)
                ShadowShortPeriodTotal[1] += max(high[i-1, sec] - close[i-1, sec], 0.0) if open[i-1, sec] > close[i-1, sec] else max(open[i-1, sec] - close[i-1, sec], 0.0)
                ShadowShortPeriodTotal[0] += max(high[i, sec] - close[i, sec], 0.0) if open[i, sec] > close[i, sec] else max(open[i, sec] - close[i, sec], 0.0)
        
            for i in range(ShadowLongTrailingIdx, lookbackTotal):
                ShadowLongPeriodTotal[1] += max(high[i-1, sec] - close[i-1, sec], 0.0) if open[i-1, sec] > close[i-1, sec] else max(open[i-1, sec] - close[i-1, sec], 0.0)
                ShadowLongPeriodTotal[0] += max(high[i, sec] - close[i, sec], 0.0) if open[i, sec] > close[i, sec] else max(open[i, sec] - close[i, sec], 0.0)
        
            for i in range(NearTrailingIdx, lookbackTotal):
                NearPeriodTotal[2] += high[i-2, sec] - low[i-2, sec]
                NearPeriodTotal[1] += high[i-1, sec] - low[i-1, sec]
                NearPeriodTotal[0] += high[i, sec] - low[i, sec]
        
            for i in range(FarTrailingIdx, lookbackTotal):
                FarPeriodTotal[2] += high[i-2, sec] - low[i-2, sec]
                FarPeriodTotal[1] += high[i-1, sec] - low[i-1, sec]
                FarPeriodTotal[0] += high[i, sec] - low[i, sec]
        
            for i in range(BodyLongTrailingIdx, lookbackTotal):
                BodyLongPeriodTotal += abs(close[i-2, sec] - open[i-2, sec])
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, tdts):
                # Check for valid data
                if (high[i, sec] != high[i, sec] or low[i, sec] != low[i, sec] or
                    open[i, sec] != open[i, sec] or close[i, sec] != close[i, sec]):
                    result[i, sec] = 0.0
                    continue
                
                # Calculate candle color (1 for white/up, -1 for black/down)
                color_2 = 1 if close[i-2, sec] > open[i-2, sec] else -1
                color_1 = 1 if close[i-1, sec] > open[i-1, sec] else -1
                color_0 = 1 if close[i, sec] > open[i, sec] else -1
            
                # Calculate real body sizes
                realbody_2 = abs(close[i-2, sec] - open[i-2, sec])
                realbody_1 = abs(close[i-1, sec] - open[i-1, sec])
                realbody_0 = abs(close[i, sec] - open[i, sec])
            
                # Calculate upper shadows
                uppershadow_2 = high[i-2, sec] - close[i-2, sec] if open[i-2, sec] <= close[i-2, sec] else high[i-2, sec] - open[i-2, sec]
                uppershadow_1 = high[i-1, sec] - close[i-1, sec] if open[i-1, sec] <= close[i-1, sec] else high[i-1, sec] - open[i-1, sec]
                uppershadow_0 = high[i, sec] - close[i, sec] if open[i, sec] <= close[i, sec] else high[i, sec] - open[i, sec]
            
                # Calculate averages for comparison
                near_avg_2 = NearPeriodTotal[2] / NearPeriod if NearPeriod > 0 else 0.0
                near_avg_1 = NearPeriodTotal[1] / NearPeriod if NearPeriod > 0 else 0.0
                far_avg_2 = FarPeriodTotal[2] / FarPeriod if FarPeriod > 0 else 0.0
                far_avg_1 = FarPeriodTotal[1] / FarPeriod if FarPeriod > 0 else 0.0
                bodylong_avg = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                shadowshort_avg_2 = ShadowShortPeriodTotal[2] / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
                shadowshort_avg_1 = ShadowShortPeriodTotal[1] / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
                shadowshort_avg_0 = ShadowShortPeriodTotal[0] / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
                shadowlong_avg_0 = ShadowLongPeriodTotal[0] / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
            
                # Advance Block pattern conditions
                if (color_2 == 1 and color_1 == 1 and color_0 == 1 and
                    close[i, sec] > close[i-1, sec] and close[i-1, sec] > close[i-2, sec] and
                    open[i-1, sec] > open[i-2, sec] and open[i-1, sec] <= close[i-2, sec] + near_avg_2 and
                    open[i, sec] > open[i-1, sec] and open[i, sec] <= close[i-1, sec] + near_avg_1 and
                    realbody_2 > bodylong_avg and uppershadow_2 < shadowshort_avg_2 and
                    ((realbody_1 < realbody_2 - far_avg_2 and realbody_0 < realbody_1 + near_avg_1) or
                     (realbody_0 < realbody_1 - far_avg_1) or
                     (realbody_0 < realbody_1 and realbody_1 < realbody_2 and
                      (uppershadow_0 > shadowshort_avg_0 or uppershadow_1 > shadowshort_avg_1)) or
                     (realbody_0 < realbody_1 and uppershadow_0 > shadowlong_avg_0))):
                    result[i, sec] = -100
                else:
                    result[i, sec] = 0
            
                # Update period totals for next iteration
                for totIdx in range(3):
                    new_val = max(high[i-totIdx, sec] - close[i-totIdx, sec], 0.0) if open[i-totIdx, sec] > close[i-totIdx, sec] else max(open[i-totIdx, sec] - close[i-totIdx, sec], 0.0)
                    old_val = max(high[ShadowShortTrailingIdx-totIdx, sec] - close[ShadowShortTrailingIdx-totIdx, sec], 0.0) if open[ShadowShortTrailingIdx-totIdx, sec] > close[ShadowShortTrailingIdx-totIdx, sec] else max(open[ShadowShortTrailingIdx-totIdx, sec] - close[ShadowShortTrailingIdx-totIdx, sec], 0.0)
                    ShadowShortPeriodTotal[totIdx] += new_val - old_val
            
                for totIdx in range(2):
                    new_val = max(high[i-totIdx, sec] - close[i-totIdx, sec], 0.0) if open[i-totIdx, sec] > close[i-totIdx, sec] else max(open[i-totIdx, sec] - close[i-totIdx, sec], 0.0)
                    old_val = max(high[ShadowLongTrailingIdx-totIdx, sec] - close[ShadowLongTrailingIdx-totIdx, sec], 0.0) if open[ShadowLongTrailingIdx-totIdx, sec] > close[ShadowLongTrailingIdx-totIdx, sec] else max(open[ShadowLongTrailingIdx-totIdx, sec] - close[ShadowLongTrailingIdx-totIdx, sec], 0.0)
                    ShadowLongPeriodTotal[totIdx] += new_val - old_val
            
                for totIdx in range(1, 3):
                    new_val = high[i-totIdx, sec] - low[i-totIdx, sec]
                    old_val = high[FarTrailingIdx-totIdx, sec] - low[FarTrailingIdx-totIdx, sec]
                    FarPeriodTotal[totIdx] += new_val - old_val
                    new_val = high[i-totIdx, sec] - low[i-totIdx, sec]
                    old_val = high[NearTrailingIdx-totIdx, sec] - low[NearTrailingIdx-totIdx, sec]
                    NearPeriodTotal[totIdx] += new_val - old_val
            
                new_val = abs(close[i-2, sec] - open[i-2, sec])
                old_val = abs(close[BodyLongTrailingIdx-2, sec] - open[BodyLongTrailingIdx-2, sec])
                BodyLongPeriodTotal += new_val - old_val
            
                # Increment trailing indices
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
        
            # BodyLong period as per TA-Lib (typically 10 for candlestick patterns)
            body_long_period = 10
            body_long_period_total = np.zeros(len(valid_high))
        
            # Initialize BodyLongPeriodTotal for the first valid points
            for i in range(body_long_period, len(valid_high)):
                if i == body_long_period:
                    for j in range(i - body_long_period, i):
                        body_long_period_total[i] += abs(valid_close[j] - valid_open[j])
                else:
                    body_long_period_total[i] = (body_long_period_total[i-1] + 
                                                abs(valid_close[i-1] - valid_open[i-1]) - 
                                                abs(valid_close[i-1-body_long_period] - valid_open[i-1-body_long_period]))
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Calculate real body for i-4 candle
                real_body_i4 = abs(valid_close[i-4] - valid_open[i-4])
                body_long_avg = body_long_period_total[i] / body_long_period if body_long_period > 0 else 0.0
            
                # Determine candle colors (1 for bullish, -1 for bearish)
                color_i4 = 1 if valid_close[i-4] > valid_open[i-4] else -1
                color_i3 = 1 if valid_close[i-3] > valid_open[i-3] else -1
                color_i1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_i = 1 if valid_close[i] > valid_open[i] else -1
            
                # Check conditions for Breakaway pattern
                if real_body_i4 > body_long_avg:
                    if (color_i4 == color_i3 and 
                        color_i3 == color_i1 and 
                        color_i1 == -color_i):
                        if color_i4 == -1:
                            # Bearish Breakaway conditions
                            gap_down = valid_open[i-3] < valid_close[i-4]
                            high_low_check_2 = valid_high[i-2] < valid_high[i-3] and valid_low[i-2] < valid_low[i-3]
                            high_low_check_1 = valid_high[i-1] < valid_high[i-2] and valid_low[i-1] < valid_low[i-2]
                            close_check = valid_close[i] > valid_open[i-3] and valid_close[i] < valid_close[i-4]
                            if gap_down and high_low_check_2 and high_low_check_1 and close_check:
                                result[valid_indices[i], sec] = color_i * 100
                            else:
                                result[valid_indices[i], sec] = 0
                        elif color_i4 == 1:
                            # Bullish Breakaway conditions
                            gap_up = valid_open[i-3] > valid_close[i-4]
                            high_low_check_2 = valid_high[i-2] > valid_high[i-3] and valid_low[i-2] > valid_low[i-3]
                            high_low_check_1 = valid_high[i-1] > valid_high[i-2] and valid_low[i-1] > valid_low[i-2]
                            close_check = valid_close[i] < valid_open[i-3] and valid_close[i] > valid_close[i-4]
                            if gap_up and high_low_check_2 and high_low_check_1 and close_check:
                                result[valid_indices[i], sec] = color_i * 100
                            else:
                                result[valid_indices[i], sec] = 0
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
    
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
    
        # BodyLong的平均周期，通常为10
        BodyLongPeriod = 10
    
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
            if len(valid_indices) < BodyLongPeriod + 1:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 初始化输出数组
            temp_result = np.zeros(len(valid_high))
        
            # 计算lookback period
            lookback_total = BodyLongPeriod
        
            # 初始化BodyLongPeriodTotal
            BodyLongPeriodTotal = 0.0
            BodyLongTrailingIdx = 0
        
            # 预热期处理：计算初始的BodyLongPeriodTotal
            for i in range(lookback_total):
                if i < len(valid_high) - 1:
                    real_body = abs(valid_close[i + 1] - valid_open[i + 1])
                    BodyLongPeriodTotal += real_body
        
            # 主计算阶段
            out_idx = 0
            for i in range(lookback_total, len(valid_high)):
                if i >= 1:
                    # 判断Dark Cloud Cover形态
                    # 前一根K线为阳线
                    is_bullish_prev = valid_close[i - 1] > valid_open[i - 1]
                    # 前一根K线的实体长度大于平均实体长度
                    real_body_prev = abs(valid_close[i - 1] - valid_open[i - 1])
                    body_long_avg = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                    is_body_long = real_body_prev > body_long_avg
                    # 当前K线为阴线
                    is_bearish_current = valid_close[i] < valid_open[i]
                    # 当前K线开盘价高于前一根K线最高价
                    is_open_above_high = valid_open[i] > valid_high[i - 1]
                    # 当前K线收盘价高于前一根K线开盘价
                    is_close_above_open_prev = valid_close[i] > valid_open[i - 1]
                    # 当前K线收盘价低于前一根K线收盘价减去实体长度的penetration比例
                    penetration_threshold = valid_close[i - 1] - real_body_prev * penetration
                    is_close_below_threshold = valid_close[i] < penetration_threshold
                
                    if (is_bullish_prev and is_body_long and is_bearish_current and 
                        is_open_above_high and is_close_above_open_prev and is_close_below_threshold):
                        temp_result[i] = -100
                    else:
                        temp_result[i] = 0
                
                    # 更新BodyLongPeriodTotal
                    if i < len(valid_high) - 1:
                        current_real_body = abs(valid_close[i] - valid_open[i])
                        trailing_real_body = abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                        BodyLongPeriodTotal += current_real_body - trailing_real_body
                        BodyLongTrailingIdx += 1
                out_idx += 1
        
            # 映射结果回原始数组
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLENGULFING(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # Lookback period for CDLENGULFING is 1 as it needs the previous candle
            lookback_total = 1
        
            for ts in range(lookback_total, tdts):
                # Check for valid data
                if (high[ts, sec] != high[ts, sec] or 
                    open[ts, sec] != open[ts, sec] or 
                    low[ts, sec] != low[ts, sec] or 
                    close[ts, sec] != close[ts, sec] or
                    high[ts-1, sec] != high[ts-1, sec] or 
                    open[ts-1, sec] != open[ts-1, sec] or 
                    low[ts-1, sec] != low[ts-1, sec] or 
                    close[ts-1, sec] != close[ts-1, sec]):
                    continue
                
                # Determine candle color (1 for bullish, -1 for bearish)
                curr_color = 1 if close[ts, sec] > open[ts, sec] else -1
                prev_color = 1 if close[ts-1, sec] > open[ts-1, sec] else -1
            
                # Bullish Engulfing Pattern
                bullish_engulfing = (curr_color == 1 and prev_color == -1 and
                                   ((close[ts, sec] >= open[ts-1, sec] and open[ts, sec] < close[ts-1, sec]) or
                                    (close[ts, sec] > open[ts-1, sec] and open[ts, sec] <= close[ts-1, sec])))
            
                # Bearish Engulfing Pattern
                bearish_engulfing = (curr_color == -1 and prev_color == 1 and
                                   ((open[ts, sec] >= close[ts-1, sec] and close[ts, sec] < open[ts-1, sec]) or
                                    (open[ts, sec] > close[ts-1, sec] and close[ts, sec] <= open[ts-1, sec])))
            
                if bullish_engulfing or bearish_engulfing:
                    if open[ts, sec] != close[ts-1, sec] and close[ts, sec] != open[ts-1, sec]:
                        result[ts, sec] = curr_color * 100
                    else:
                        result[ts, sec] = curr_color * 80
                else:
                    result[ts, sec] = 0
                
        return result



    @staticmethod
    @nb.njit
    def CDLEVENINGDOJISTAR(high, open, low, close, vol, oi, optInPenetration=0.3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle body types as in TA-Lib
        BodyLongPeriod = 5
        BodyDojiPeriod = 3
        BodyShortPeriod = 5
        lookbackTotal = 2  # Need at least 3 candles (i-2, i-1, i) for pattern
    
        for sec in range(secs):
            # Initialize totals for rolling averages
            BodyLongPeriodTotal = 0.0
            BodyDojiPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
        
            # Initialize trailing indices for rolling window
            BodyLongTrailingIdx = lookbackTotal - 2 - BodyLongPeriod
            BodyDojiTrailingIdx = lookbackTotal - 1 - BodyDojiPeriod
            BodyShortTrailingIdx = lookbackTotal - BodyShortPeriod
        
            # Pre-calculate initial totals for averages before startIdx
            i = max(0, BodyLongTrailingIdx)
            while i < lookbackTotal - 2:
                if high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    BodyLongPeriodTotal += abs(open[i, sec] - close[i, sec])
                i += 1
            
            i = max(0, BodyDojiTrailingIdx)
            while i < lookbackTotal - 1:
                if high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    BodyDojiPeriodTotal += abs(open[i, sec] - close[i, sec])
                i += 1
            
            i = max(0, BodyShortTrailingIdx)
            while i < lookbackTotal:
                if high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    BodyShortPeriodTotal += abs(open[i, sec] - close[i, sec])
                i += 1
            
            # Main loop starting from lookbackTotal
            for i in range(lookbackTotal, tdts):
                # Check if current data point is valid
                if (high[i, sec] != high[i, sec] or low[i, sec] != low[i, sec] or 
                    open[i, sec] != open[i, sec] or close[i, sec] != close[i, sec] or
                    high[i-1, sec] != high[i-1, sec] or low[i-1, sec] != low[i-1, sec] or 
                    open[i-1, sec] != open[i-1, sec] or close[i-1, sec] != close[i-1, sec] or
                    high[i-2, sec] != high[i-2, sec] or low[i-2, sec] != low[i-2, sec] or 
                    open[i-2, sec] != open[i-2, sec] or close[i-2, sec] != close[i-2, sec]):
                    result[i, sec] = 0
                    continue
                
                # Calculate real body sizes
                realBody2 = abs(close[i-2, sec] - open[i-2, sec])
                realBody1 = abs(close[i-1, sec] - open[i-1, sec])
                realBody0 = abs(close[i, sec] - open[i, sec])
            
                # Calculate candle colors
                color2 = 1 if close[i-2, sec] > open[i-2, sec] else -1
                color0 = 1 if close[i, sec] > open[i, sec] else -1
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check for gap up between i-2 and i-1
                gapUp = min(open[i-1, sec], close[i-1, sec]) > max(open[i-2, sec], close[i-2, sec])
            
                # Check Evening Doji Star pattern conditions
                if (realBody2 > BodyLongAverage and  # First candle is long
                    color2 == 1 and  # First candle is white (bullish)
                    realBody1 <= BodyDojiAverage and  # Second candle is doji
                    gapUp and  # Gap up between first and second candle
                    realBody0 > BodyShortAverage and  # Third candle is long
                    color0 == -1 and  # Third candle is black (bearish)
                    close[i, sec] < close[i-2, sec] - realBody2 * optInPenetration):  # Penetration condition
                    result[i, sec] = -100
                else:
                    result[i, sec] = 0
                
                # Update rolling totals
                if i - 2 >= 0:
                    newBodyLong = abs(close[i-2, sec] - open[i-2, sec]) if close[i-2, sec] == close[i-2, sec] else 0.0
                    oldBodyLong = abs(close[BodyLongTrailingIdx, sec] - open[BodyLongTrailingIdx, sec]) if BodyLongTrailingIdx >= 0 and close[BodyLongTrailingIdx, sec] == close[BodyLongTrailingIdx, sec] else 0.0
                    BodyLongPeriodTotal += newBodyLong - oldBodyLong
                    BodyLongTrailingIdx += 1
                
                if i - 1 >= 0:
                    newBodyDoji = abs(close[i-1, sec] - open[i-1, sec]) if close[i-1, sec] == close[i-1, sec] else 0.0
                    oldBodyDoji = abs(close[BodyDojiTrailingIdx, sec] - open[BodyDojiTrailingIdx, sec]) if BodyDojiTrailingIdx >= 0 and close[BodyDojiTrailingIdx, sec] == close[BodyDojiTrailingIdx, sec] else 0.0
                    BodyDojiPeriodTotal += newBodyDoji - oldBodyDoji
                    BodyDojiTrailingIdx += 1
                
                newBodyShort = abs(close[i, sec] - open[i, sec]) if close[i, sec] == close[i, sec] else 0.0
                oldBodyShort = abs(close[BodyShortTrailingIdx, sec] - open[BodyShortTrailingIdx, sec]) if BodyShortTrailingIdx >= 0 and close[BodyShortTrailingIdx, sec] == close[BodyShortTrailingIdx, sec] else 0.0
                BodyShortPeriodTotal += newBodyShort - oldBodyShort
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
        
            # Initialize period totals for averaging
            BodyLongPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
            BodyShortPeriodTotal2 = 0.0
        
            # Calculate initial totals for BodyLong and BodyShort
            BodyLongTrailingIdx = lookbackTotal - 2 - BodyLongPeriod
            BodyShortTrailingIdx = lookbackTotal - 1 - BodyShortPeriod
        
            for i in range(BodyLongTrailingIdx, lookbackTotal - 2):
                if i >= 0:
                    BodyLongPeriodTotal += abs(valid_open[i] - valid_close[i])
                
            for i in range(BodyShortTrailingIdx, lookbackTotal - 1):
                if i >= 0:
                    BodyShortPeriodTotal += abs(valid_open[i] - valid_close[i])
                    if i + 1 < len(valid_open):
                        BodyShortPeriodTotal2 += abs(valid_open[i + 1] - valid_close[i + 1])
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body for current and previous candles
                realbody2 = abs(valid_open[i - 2] - valid_close[i - 2])
                realbody1 = abs(valid_open[i - 1] - valid_close[i - 1])
                realbody0 = abs(valid_open[i] - valid_close[i])
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                BodyShortAverage2 = BodyShortPeriodTotal2 / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check conditions for Evening Star pattern
                if (realbody2 > BodyLongAverage and
                    valid_close[i - 2] > valid_open[i - 2] and  # Bullish first candle
                    realbody1 <= BodyShortAverage and
                    valid_open[i - 1] > valid_close[i - 2] and  # Gap up
                    realbody0 > BodyShortAverage2 and
                    valid_close[i] < valid_open[i] and  # Bearish third candle
                    valid_close[i] < valid_close[i - 2] - realbody2 * penetration):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update trailing totals
                if i - 2 >= 0:
                    BodyLongPeriodTotal += abs(valid_open[i - 2] - valid_close[i - 2])
                    if BodyLongTrailingIdx >= 0:
                        BodyLongPeriodTotal -= abs(valid_open[BodyLongTrailingIdx] - valid_close[BodyLongTrailingIdx])
                    BodyLongTrailingIdx += 1
                
                if i - 1 >= 0:
                    BodyShortPeriodTotal += abs(valid_open[i - 1] - valid_close[i - 1])
                    if BodyShortTrailingIdx >= 0:
                        BodyShortPeriodTotal -= abs(valid_open[BodyShortTrailingIdx] - valid_close[BodyShortTrailingIdx])
                    BodyShortTrailingIdx += 1
                
                BodyShortPeriodTotal2 += abs(valid_open[i] - valid_close[i])
                if BodyShortTrailingIdx - 1 >= 0:
                    BodyShortPeriodTotal2 -= abs(valid_open[BodyShortTrailingIdx - 1] - valid_close[BodyShortTrailingIdx - 1])
    
        return result



    @staticmethod
    @nb.njit
    def CDLHANGINGMAN(high, open, low, close, vol, oi, body_short_period=10, shadow_long_period=10, shadow_very_short_period=10, near_period=10):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (maximum of the periods used)
        lookback_total = max(body_short_period, shadow_long_period, shadow_very_short_period, near_period + 1)
    
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
        
            # Initialize period totals for averages
            body_period_total = 0.0
            shadow_long_period_total = 0.0
            shadow_very_short_period_total = 0.0
            near_period_total = 0.0
        
            # Trailing indices for rolling window
            body_trailing_idx = 0
            shadow_long_trailing_idx = 0
            shadow_very_short_trailing_idx = 0
            near_trailing_idx = 0
        
            # Pre-calculate initial totals for the lookback period
            for i in range(lookback_total - body_short_period, lookback_total):
                if i < len(valid_high):
                    body_period_total += abs(valid_close[i] - valid_open[i])
            for i in range(lookback_total - shadow_long_period, lookback_total):
                if i < len(valid_high):
                    shadow_long_period_total += valid_low[i] - min(valid_close[i], valid_open[i])
            for i in range(lookback_total - shadow_very_short_period, lookback_total):
                if i < len(valid_high):
                    shadow_very_short_period_total += max(valid_close[i], valid_open[i]) - valid_high[i]
            for i in range(lookback_total - near_period - 1, lookback_total - 1):
                if i < len(valid_high):
                    near_period_total += valid_high[i] - valid_low[i]
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Calculate real body and shadows for current candle
                real_body = abs(valid_close[i] - valid_open[i])
                lower_shadow = valid_low[i] - min(valid_close[i], valid_open[i])
                upper_shadow = max(valid_close[i], valid_open[i]) - valid_high[i]
            
                # Calculate averages
                body_avg = body_period_total / body_short_period if body_short_period > 0 else 0.0
                shadow_long_avg = shadow_long_period_total / shadow_long_period if shadow_long_period > 0 else 0.0
                shadow_very_short_avg = shadow_very_short_period_total / shadow_very_short_period if shadow_very_short_period > 0 else 0.0
                near_avg = near_period_total / near_period if near_period > 0 else 0.0
            
                # Check Hanging Man conditions
                if (real_body < body_avg and
                    lower_shadow > shadow_long_avg and
                    upper_shadow < shadow_very_short_avg and
                    min(valid_close[i], valid_open[i]) >= valid_high[i-1] - near_avg):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals
                if i < len(valid_high):
                    # Add current values
                    body_period_total += abs(valid_close[i] - valid_open[i])
                    shadow_long_period_total += valid_low[i] - min(valid_close[i], valid_open[i])
                    shadow_very_short_period_total += max(valid_close[i], valid_open[i]) - valid_high[i]
                    if i - 1 < len(valid_high):
                        near_period_total += valid_high[i-1] - valid_low[i-1]
                
                    # Subtract trailing values
                    if body_trailing_idx < len(valid_high):
                        body_period_total -= abs(valid_close[body_trailing_idx] - valid_open[body_trailing_idx])
                    if shadow_long_trailing_idx < len(valid_high):
                        shadow_long_period_total -= valid_low[shadow_long_trailing_idx] - min(valid_close[shadow_long_trailing_idx], valid_open[shadow_long_trailing_idx])
                    if shadow_very_short_trailing_idx < len(valid_high):
                        shadow_very_short_period_total -= max(valid_close[shadow_very_short_trailing_idx], valid_open[shadow_very_short_trailing_idx]) - valid_high[shadow_very_short_trailing_idx]
                    if near_trailing_idx < len(valid_high):
                        near_period_total -= valid_high[near_trailing_idx] - valid_low[near_trailing_idx]
                
                    # Increment trailing indices
                    body_trailing_idx += 1
                    shadow_long_trailing_idx += 1
                    shadow_very_short_trailing_idx += 1
                    near_trailing_idx += 1
    
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
    def CDLHIKKAKE(high, open, low, close, vol, oi):
        """
        CDLHIKKAKE - Candlestick Hikkake Pattern
    
        Identifies the Hikkake pattern, a candlestick pattern used to detect potential reversals or continuations.
        The pattern consists of a specific three-bar formation followed by a confirmation.
        Returns 100 or -100 for initial pattern detection and 200 or -200 for confirmation.
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        lookback_total = 3  # As per TA-Lib lookback for CDLHIKKAKE

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
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize pattern tracking variables
            pattern_idx = 0
            pattern_result = 0
        
            # Pre-warmup phase (before start index)
            start_idx = lookback_total
            i = start_idx - 3
            while i < start_idx and i < len(valid_high):
                if i >= 2:  # Ensure enough data for comparison
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
        
            # Main computation phase
            i = start_idx
            out_idx = start_idx
            while i < len(valid_high):
                if i >= 2:  # Ensure enough data for comparison
                    if (valid_high[i-1] < valid_high[i-2] and 
                        valid_low[i-1] > valid_low[i-2] and
                        ((valid_high[i] < valid_high[i-1] and valid_low[i] < valid_low[i-1]) or
                         (valid_high[i] > valid_high[i-1] and valid_low[i] > valid_low[i-1]))):
                        pattern_result = 100 * (1 if valid_high[i] < valid_high[i-1] else -1)
                        pattern_idx = i
                        if out_idx < tdts:
                            result[valid_indices[out_idx], sec] = pattern_result
                    elif (i <= pattern_idx + 3 and
                          ((pattern_result > 0 and valid_close[i] > valid_high[pattern_idx-1]) or
                           (pattern_result < 0 and valid_close[i] < valid_low[pattern_idx-1]))):
                        if out_idx < tdts:
                            result[valid_indices[out_idx], sec] = pattern_result + 100 * (1 if pattern_result > 0 else -1)
                        pattern_idx = 0
                    else:
                        if out_idx < tdts:
                            result[valid_indices[out_idx], sec] = 0
                out_idx += 1
                i += 1
            
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
    
        # Define lookback period as per TA-Lib (2 days for pattern recognition)
        lookback_total = 2
        # Define periods for body calculations as per TA-Lib defaults
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
            if len(valid_indices) < lookback_total:
                continue
            
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            temp_result = np.zeros(len(valid_open))
        
            # Initialize trailing totals for body calculations
            body_long_total = 0.0
            body_short_total = 0.0
        
            # Calculate initial totals for body averages
            body_long_trailing_idx = 0
            body_short_trailing_idx = 0
        
            for i in range(lookback_total - 1, min(body_long_period + lookback_total - 1, len(valid_open))):
                if i >= lookback_total - 1:
                    body_long_total += abs(valid_close[i - 1] - valid_open[i - 1])
            for i in range(lookback_total - 1, min(body_short_period + lookback_total - 1, len(valid_open))):
                if i >= lookback_total - 1:
                    body_short_total += abs(valid_close[i] - valid_open[i])
        
            # Main calculation loop
            for i in range(lookback_total - 1, len(valid_open)):
                # Calculate body averages
                body_long_avg = body_long_total / body_long_period if body_long_period > 0 else 0.0
                body_short_avg = body_short_total / body_short_period if body_short_period > 0 else 0.0
            
                # Check for Homing Pigeon pattern
                if i >= 1:
                    # First candle is black (bearish)
                    first_candle_bearish = valid_close[i - 1] < valid_open[i - 1]
                    # Second candle is black (bearish)
                    second_candle_bearish = valid_close[i] < valid_open[i]
                    # First candle has long body
                    first_body_long = abs(valid_close[i - 1] - valid_open[i - 1]) > body_long_avg
                    # Second candle has short body
                    second_body_short = abs(valid_close[i] - valid_open[i]) <= body_short_avg
                    # Second candle opens lower than first candle
                    second_opens_lower = valid_open[i] < valid_open[i - 1]
                    # Second candle closes higher than first candle
                    second_closes_higher = valid_close[i] > valid_close[i - 1]
                
                    if (first_candle_bearish and second_candle_bearish and 
                        first_body_long and second_body_short and 
                        second_opens_lower and second_closes_higher):
                        temp_result[i] = 100
                    else:
                        temp_result[i] = 0
            
                # Update trailing totals
                if i >= body_long_period:
                    body_long_total += abs(valid_close[i - 1] - valid_open[i - 1])
                    body_long_total -= abs(valid_close[body_long_trailing_idx - 1] - valid_open[body_long_trailing_idx - 1]) if body_long_trailing_idx > 0 else 0.0
                    body_long_trailing_idx += 1
                if i >= body_short_period - 1:
                    body_short_total += abs(valid_close[i] - valid_open[i])
                    body_short_total -= abs(valid_close[body_short_trailing_idx] - valid_open[body_short_trailing_idx]) if body_short_trailing_idx >= 0 else 0.0
                    body_short_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total - 1:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLIDENTICAL3CROWS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # 定义TA-Lib中使用的默认周期参数
        ShadowVeryShortPeriod = 3
        EqualPeriod = 3
        lookbackTotal = 2  # 需要前两个周期的数据来计算当前周期的结果
    
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
        
            # 初始化滑动窗口总和
            ShadowVeryShortPeriodTotal = np.zeros(3)
            EqualPeriodTotal = np.zeros(3)
        
            # 计算初始的滑动窗口总和
            ShadowVeryShortTrailingIdx = max(0, lookbackTotal - ShadowVeryShortPeriod)
            EqualTrailingIdx = max(0, lookbackTotal - EqualPeriod)
        
            i = ShadowVeryShortTrailingIdx
            while i < lookbackTotal:
                if i - 2 >= 0:
                    ShadowVeryShortPeriodTotal[2] += valid_high[i-2] - valid_low[i-2]
                if i - 1 >= 0:
                    ShadowVeryShortPeriodTotal[1] += valid_high[i-1] - valid_low[i-1]
                ShadowVeryShortPeriodTotal[0] += valid_high[i] - valid_low[i]
                i += 1
            
            i = EqualTrailingIdx
            while i < lookbackTotal:
                if i - 2 >= 0:
                    EqualPeriodTotal[2] += valid_high[i-2] - valid_low[i-2]
                if i - 1 >= 0:
                    EqualPeriodTotal[1] += valid_high[i-1] - valid_low[i-1]
                i += 1
            
            # 主计算循环
            i = lookbackTotal
            ShadowVeryShortTrailingIdx = i - ShadowVeryShortPeriod
            EqualTrailingIdx = i - EqualPeriod
        
            while i < len(valid_high):
                # 计算当前K线的颜色（-1表示阴线）
                color_2 = -1 if valid_close[i-2] < valid_open[i-2] else 1
                color_1 = -1 if valid_close[i-1] < valid_open[i-1] else 1
                color_0 = -1 if valid_close[i] < valid_open[i] else 1
            
                # 计算下影线长度
                lower_shadow_2 = valid_open[i-2] - valid_low[i-2] if color_2 == -1 else valid_close[i-2] - valid_low[i-2]
                lower_shadow_1 = valid_open[i-1] - valid_low[i-1] if color_1 == -1 else valid_close[i-1] - valid_low[i-1]
                lower_shadow_0 = valid_open[i] - valid_low[i] if color_0 == -1 else valid_close[i] - valid_low[i]
            
                # 计算ShadowVeryShort的平均值
                shadow_avg_2 = ShadowVeryShortPeriodTotal[2] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0
                shadow_avg_1 = ShadowVeryShortPeriodTotal[1] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0
                shadow_avg_0 = ShadowVeryShortPeriodTotal[0] / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0
            
                # 计算Equal的平均值
                equal_avg_2 = EqualPeriodTotal[2] / EqualPeriod if EqualPeriod > 0 else 0
                equal_avg_1 = EqualPeriodTotal[1] / EqualPeriod if EqualPeriod > 0 else 0
            
                # 判断是否符合Identical Three Crows形态
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
                
                # 更新滑动窗口总和
                for totIdx in range(2, -1, -1):
                    if i - totIdx >= 0:
                        ShadowVeryShortPeriodTotal[totIdx] += (valid_high[i - totIdx] - valid_low[i - totIdx])
                    if ShadowVeryShortTrailingIdx - totIdx >= 0:
                        ShadowVeryShortPeriodTotal[totIdx] -= (valid_high[ShadowVeryShortTrailingIdx - totIdx] - valid_low[ShadowVeryShortTrailingIdx - totIdx])
                    
                for totIdx in range(2, 0, -1):
                    if i - totIdx >= 0:
                        EqualPeriodTotal[totIdx] += (valid_high[i - totIdx] - valid_low[i - totIdx])
                    if EqualTrailingIdx - totIdx >= 0:
                        EqualPeriodTotal[totIdx] -= (valid_high[EqualTrailingIdx - totIdx] - valid_low[EqualTrailingIdx - totIdx])
                    
                i += 1
                ShadowVeryShortTrailingIdx += 1
                EqualTrailingIdx += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLINNECK(high, open, low, close, vol, oi, equal_period=3, body_long_period=5):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (maximum of the two periods)
        lookback_total = max(equal_period, body_long_period)
    
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
            temp_result = np.zeros(len(valid_high))
        
            # Initialize trailing totals for Equal and BodyLong ranges
            equal_period_total = 0.0
            body_long_period_total = 0.0
        
            # Calculate initial totals for lookback period
            equal_trailing_idx = lookback_total - equal_period
            body_long_trailing_idx = lookback_total - body_long_period
        
            for i in range(equal_trailing_idx, lookback_total):
                if i >= 0:
                    equal_period_total += abs(valid_open[i] - valid_close[i])
        
            for i in range(body_long_trailing_idx, lookback_total):
                if i >= 0:
                    body_long_period_total += abs(valid_open[i] - valid_close[i])
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Check for In Neck pattern
                if i > 0:
                    # First candle is black (bearish)
                    candle_color_prev = -1 if valid_close[i-1] < valid_open[i-1] else 1
                    # Second candle is white (bullish)
                    candle_color_curr = 1 if valid_close[i] > valid_open[i] else -1
                    # Real body of first candle
                    real_body_prev = abs(valid_close[i-1] - valid_open[i-1])
                    # Calculate averages
                    equal_avg = equal_period_total / equal_period if equal_period > 0 else 0.0
                    body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
                
                    if (candle_color_prev == -1 and
                        real_body_prev > body_long_avg and
                        candle_color_curr == 1 and
                        valid_open[i] < valid_low[i-1] and
                        valid_close[i] <= valid_close[i-1] + equal_avg and
                        valid_close[i] >= valid_close[i-1]):
                        temp_result[i] = -100
                    else:
                        temp_result[i] = 0
            
                # Update trailing totals
                if i > 0:
                    equal_period_total += abs(valid_open[i-1] - valid_close[i-1])
                    body_long_period_total += abs(valid_open[i-1] - valid_close[i-1])
                
                    if equal_trailing_idx < len(valid_high):
                        equal_period_total -= abs(valid_open[equal_trailing_idx] - valid_close[equal_trailing_idx])
                    if body_long_trailing_idx < len(valid_high):
                        body_long_period_total -= abs(valid_open[body_long_trailing_idx] - valid_close[body_long_trailing_idx])
                
                    equal_trailing_idx += 1
                    body_long_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = temp_result[i]
    
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
    def CDLKICKINGBYLENGTH(high, open, low, close, vol, oi, shadow_very_short_period=7, body_long_period=10):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib logic
        lookback_total = max(shadow_very_short_period, body_long_period)
    
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
        
            # Initialize arrays for storing running totals
            shadow_very_short_total = np.zeros(2)
            body_long_total = np.zeros(2)
        
            # Initialize trailing indices for rolling window
            shadow_very_short_trailing_idx = lookback_total - shadow_very_short_period
            body_long_trailing_idx = lookback_total - body_long_period
        
            # Pre-calculate totals for the lookback period
            for i in range(shadow_very_short_trailing_idx, lookback_total):
                shadow_very_short_total[1] += max(valid_high[i-1] - valid_close[i-1], valid_open[i-1] - valid_low[i-1]) if i > 0 else 0
                shadow_very_short_total[0] += max(valid_high[i] - valid_close[i], valid_open[i] - valid_low[i])
            for i in range(body_long_trailing_idx, lookback_total):
                body_long_total[1] += abs(valid_close[i-1] - valid_open[i-1]) if i > 0 else 0
                body_long_total[0] += abs(valid_close[i] - valid_open[i])
        
            # Main calculation loop
            for i in range(lookback_total, len(valid_high)):
                # Calculate candle color for current and previous bar
                color_prev = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_curr = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate real body and shadows
                real_body_prev = abs(valid_close[i-1] - valid_open[i-1])
                real_body_curr = abs(valid_close[i] - valid_open[i])
                upper_shadow_prev = valid_high[i-1] - max(valid_close[i-1], valid_open[i-1])
                lower_shadow_prev = min(valid_close[i-1], valid_open[i-1]) - valid_low[i-1]
                upper_shadow_curr = valid_high[i] - max(valid_close[i], valid_open[i])
                lower_shadow_curr = min(valid_close[i], valid_open[i]) - valid_low[i]
            
                # Calculate averages
                body_long_avg_prev = body_long_total[1] / body_long_period if body_long_period > 0 else 0
                body_long_avg_curr = body_long_total[0] / body_long_period if body_long_period > 0 else 0
                shadow_short_avg_prev = shadow_very_short_total[1] / shadow_very_short_period if shadow_very_short_period > 0 else 0
                shadow_short_avg_curr = shadow_very_short_total[0] / shadow_very_short_period if shadow_very_short_period > 0 else 0
            
                # Check for gap conditions
                gap_up = valid_low[i] > valid_high[i-1]
                gap_down = valid_high[i] < valid_low[i-1]
            
                # Check kicking pattern conditions
                if (color_prev != color_curr and
                    real_body_prev > body_long_avg_prev and
                    upper_shadow_prev < shadow_short_avg_prev and
                    lower_shadow_prev < shadow_short_avg_prev and
                    real_body_curr > body_long_avg_curr and
                    upper_shadow_curr < shadow_short_avg_curr and
                    lower_shadow_curr < shadow_short_avg_curr and
                    ((color_prev == -1 and gap_up) or (color_prev == 1 and gap_down))):
                    # Determine which body is longer for signal direction
                    signal_idx = i if real_body_curr > real_body_prev else i-1
                    signal_color = 1 if valid_close[signal_idx] > valid_open[signal_idx] else -1
                    result[valid_indices[i], sec] = signal_color * 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals
                for tot_idx in range(1, -1, -1):
                    if tot_idx == 1 and i-1 >= 0:
                        body_long_total[tot_idx] += abs(valid_close[i-tot_idx] - valid_open[i-tot_idx])
                        body_long_total[tot_idx] -= abs(valid_close[body_long_trailing_idx-tot_idx] - valid_open[body_long_trailing_idx-tot_idx]) if body_long_trailing_idx-tot_idx >= 0 else 0
                        shadow_very_short_total[tot_idx] += max(valid_high[i-tot_idx] - valid_close[i-tot_idx], valid_open[i-tot_idx] - valid_low[i-tot_idx])
                        shadow_very_short_total[tot_idx] -= max(valid_high[shadow_very_short_trailing_idx-tot_idx] - valid_close[shadow_very_short_trailing_idx-tot_idx], valid_open[shadow_very_short_trailing_idx-tot_idx] - valid_low[shadow_very_short_trailing_idx-tot_idx]) if shadow_very_short_trailing_idx-tot_idx >= 0 else 0
                    elif tot_idx == 0:
                        body_long_total[tot_idx] += abs(valid_close[i-tot_idx] - valid_open[i-tot_idx])
                        body_long_total[tot_idx] -= abs(valid_close[body_long_trailing_idx-tot_idx] - valid_open[body_long_trailing_idx-tot_idx]) if body_long_trailing_idx-tot_idx >= 0 else 0
                        shadow_very_short_total[tot_idx] += max(valid_high[i-tot_idx] - valid_close[i-tot_idx], valid_open[i-tot_idx] - valid_low[i-tot_idx])
                        shadow_very_short_total[tot_idx] -= max(valid_high[shadow_very_short_trailing_idx-tot_idx] - valid_close[shadow_very_short_trailing_idx-tot_idx], valid_open[shadow_very_short_trailing_idx-tot_idx] - valid_low[shadow_very_short_trailing_idx-tot_idx]) if shadow_very_short_trailing_idx-tot_idx >= 0 else 0
            
                shadow_very_short_trailing_idx += 1
                body_long_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLLADDERBOTTOM(high, open, low, close, vol, oi, shadow_period=3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (4 prior candles + shadow period for averaging)
        lookback_total = 4 + shadow_period
    
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
        
            # Initialize shadow very short period total for averaging upper shadow
            shadow_very_short_period_total = 0.0
            shadow_very_short_trailing_idx = lookback_total - shadow_period
        
            # Calculate initial total for shadow average
            for i in range(shadow_very_short_trailing_idx, lookback_total):
                if i >= 0 and i < len(valid_high):
                    # Upper shadow calculation for bearish candle (as per TA-Lib ShadowVeryShort)
                    if valid_close[i] < valid_open[i]:
                        shadow_range = valid_high[i] - valid_open[i]
                    else:
                        shadow_range = valid_high[i] - valid_close[i]
                    if shadow_range == shadow_range:  # Check for NaN
                        shadow_very_short_period_total += shadow_range
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Ladder Bottom pattern conditions
                # Check for three consecutive bearish candles (days -4, -3, -2)
                color_m4 = -1 if valid_close[i-4] < valid_open[i-4] else 1
                color_m3 = -1 if valid_close[i-3] < valid_open[i-3] else 1
                color_m2 = -1 if valid_close[i-2] < valid_open[i-2] else 1
                # Check for bearish candle on day -1
                color_m1 = -1 if valid_close[i-1] < valid_open[i-1] else 1
                # Check for bullish candle on current day
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate upper shadow for day -1
                upper_shadow_m1 = valid_high[i-1] - max(valid_open[i-1], valid_close[i-1])
                # Calculate shadow average for comparison
                shadow_very_short_average = shadow_very_short_period_total / shadow_period if shadow_period > 0 else 0.0
            
                # Check all conditions for Ladder Bottom pattern
                if (color_m4 == -1 and color_m3 == -1 and color_m2 == -1 and  # Three bearish candles
                    valid_open[i-4] > valid_open[i-3] and valid_open[i-3] > valid_open[i-2] and  # Decreasing opens
                    valid_close[i-4] > valid_close[i-3] and valid_close[i-3] > valid_close[i-2] and  # Decreasing closes
                    color_m1 == -1 and  # Fourth bearish candle
                    upper_shadow_m1 > shadow_very_short_average and  # Long upper shadow on day -1
                    color_0 == 1 and  # Bullish candle on current day
                    valid_open[i] > valid_open[i-1] and  # Current open above previous open
                    valid_close[i] > valid_high[i-1]):  # Current close above previous high
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update shadow total for next iteration (sliding window)
                if i - 1 >= 0:
                    # Remove oldest shadow value
                    old_idx = i - 1 - shadow_period
                    if old_idx >= 0:
                        if valid_close[old_idx] < valid_open[old_idx]:
                            old_shadow_range = valid_high[old_idx] - valid_open[old_idx]
                        else:
                            old_shadow_range = valid_high[old_idx] - valid_close[old_idx]
                        if old_shadow_range == old_shadow_range:
                            shadow_very_short_period_total -= old_shadow_range
                
                    # Add newest shadow value
                    if valid_close[i-1] < valid_open[i-1]:
                        new_shadow_range = valid_high[i-1] - valid_open[i-1]
                    else:
                        new_shadow_range = valid_high[i-1] - valid_close[i-1]
                    if new_shadow_range == new_shadow_range:
                        shadow_very_short_period_total += new_shadow_range
    
        return result



    @staticmethod
    @nb.njit
    def CDLMATHOLD(high, open, low, close, vol, oi, penetration=0.5):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        BodyShortPeriod = 5
        BodyLongPeriod = 5
        lookbackTotal = 4  # Need 5 candles (i-4 to i) for pattern recognition
    
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
        
            # Initialize arrays for body calculations
            BodyPeriodTotal = np.zeros(5, dtype=np.float64)  # 0-3 for Short, 4 for Long
            out_values = np.zeros(len(valid_high), dtype=np.float64)
        
            # Initialize trailing indices for rolling sums
            start_idx = lookbackTotal
            BodyShortTrailingIdx = start_idx - BodyShortPeriod
            BodyLongTrailingIdx = start_idx - BodyLongPeriod
        
            # Pre-calculate initial sums for Body averages before start_idx
            for i in range(BodyShortTrailingIdx, start_idx):
                if i >= 0:
                    BodyPeriodTotal[3] += abs(valid_close[i-3] - valid_open[i-3]) if i-3 >= 0 else 0.0
                    BodyPeriodTotal[2] += abs(valid_close[i-2] - valid_open[i-2]) if i-2 >= 0 else 0.0
                    BodyPeriodTotal[1] += abs(valid_close[i-1] - valid_open[i-1]) if i-1 >= 0 else 0.0
        
            for i in range(BodyLongTrailingIdx, start_idx):
                if i >= 0:
                    BodyPeriodTotal[4] += abs(valid_close[i-4] - valid_open[i-4]) if i-4 >= 0 else 0.0
        
            # Main loop for pattern recognition
            for i in range(start_idx, len(valid_high)):
                # Calculate real body sizes
                realbody_i4 = abs(valid_close[i-4] - valid_open[i-4])
                realbody_i3 = abs(valid_close[i-3] - valid_open[i-3])
                realbody_i2 = abs(valid_close[i-2] - valid_open[i-2])
                realbody_i1 = abs(valid_close[i-1] - valid_open[i-1])
            
                # Calculate candle colors (1 for bullish, -1 for bearish)
                color_i4 = 1 if valid_close[i-4] > valid_open[i-4] else -1
                color_i3 = 1 if valid_close[i-3] > valid_open[i-3] else -1
                color_i = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate averages for comparison
                avg_body_long_i4 = BodyPeriodTotal[4] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                avg_body_short_i3 = BodyPeriodTotal[3] / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                avg_body_short_i2 = BodyPeriodTotal[2] / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                avg_body_short_i1 = BodyPeriodTotal[1] / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check for gap up between i-4 and i-3
                gap_up_i3_i4 = valid_open[i-3] > valid_close[i-4] if color_i4 == 1 else valid_open[i-3] > valid_open[i-4]
            
                # Pattern conditions as per TA-Lib logic
                if (realbody_i4 > avg_body_long_i4 and
                    realbody_i3 < avg_body_short_i3 and
                    realbody_i2 < avg_body_short_i2 and
                    realbody_i1 < avg_body_short_i1 and
                    color_i4 == 1 and
                    color_i3 == -1 and
                    color_i == 1 and
                    gap_up_i3_i4 and
                    min(valid_open[i-2], valid_close[i-2]) < valid_close[i-4] and
                    min(valid_open[i-1], valid_close[i-1]) < valid_close[i-4] and
                    min(valid_open[i-2], valid_close[i-2]) > valid_close[i-4] - realbody_i4 * penetration and
                    min(valid_open[i-1], valid_close[i-1]) > valid_close[i-4] - realbody_i4 * penetration and
                    max(valid_close[i-2], valid_open[i-2]) < valid_open[i-3] and
                    max(valid_close[i-1], valid_open[i-1]) < max(valid_close[i-2], valid_open[i-2]) and
                    valid_open[i] > valid_close[i-1] and
                    valid_close[i] > max(max(valid_high[i-3], valid_high[i-2]), valid_high[i-1])):
                    out_values[i] = 100
                else:
                    out_values[i] = 0
            
                # Update rolling sums for body averages
                if i < len(valid_high):
                    BodyPeriodTotal[4] += abs(valid_close[i-4] - valid_open[i-4]) if i-4 >= 0 else 0.0
                    if BodyLongTrailingIdx - 4 >= 0:
                        BodyPeriodTotal[4] -= abs(valid_close[BodyLongTrailingIdx-4] - valid_open[BodyLongTrailingIdx-4])
                
                    for totIdx in range(3, 0, -1):
                        BodyPeriodTotal[totIdx] += abs(valid_close[i-totIdx] - valid_open[i-totIdx]) if i-totIdx >= 0 else 0.0
                        if BodyShortTrailingIdx - totIdx >= 0:
                            BodyPeriodTotal[totIdx] -= abs(valid_close[BodyShortTrailingIdx-totIdx] - valid_open[BodyShortTrailingIdx-totIdx])
            
                BodyShortTrailingIdx += 1
                BodyLongTrailingIdx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookbackTotal:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = out_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLMORNINGDOJISTAR(high, open, low, close, vol, oi, penetration=0.3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different body types as in TA-Lib
        BodyLongPeriod = 10
        BodyDojiPeriod = 3
        BodyShortPeriod = 5
        lookbackTotal = 2  # Need at least 2 previous candles for pattern
    
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
            
            # Initialize trailing indices and totals for rolling averages
            BodyLongTrailingIdx = lookbackTotal - 2 - BodyLongPeriod
            BodyDojiTrailingIdx = lookbackTotal - 1 - BodyDojiPeriod
            BodyShortTrailingIdx = lookbackTotal - BodyShortPeriod
        
            BodyLongPeriodTotal = 0.0
            BodyDojiPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
        
            # Calculate initial totals for body ranges
            for i in range(BodyLongTrailingIdx, lookbackTotal - 2):
                if i >= 0 and valid_mask[i]:
                    BodyLongPeriodTotal += abs(close[i, sec] - open[i, sec])
            for i in range(BodyDojiTrailingIdx, lookbackTotal - 1):
                if i >= 0 and valid_mask[i]:
                    BodyDojiPeriodTotal += abs(close[i, sec] - open[i, sec])
            for i in range(BodyShortTrailingIdx, lookbackTotal):
                if i >= 0 and valid_mask[i]:
                    BodyShortPeriodTotal += abs(close[i, sec] - open[i, sec])
        
            # Main loop starting from lookbackTotal
            for i in range(lookbackTotal, tdts):
                if not valid_mask[i]:
                    continue
                
                # Calculate averages for comparison
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                BodyShortAverage = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                # Check Morning Doji Star pattern conditions
                if (i >= 2 and valid_mask[i-1] and valid_mask[i-2]):
                    # First candle: Long black body
                    realbody2 = abs(close[i-2, sec] - open[i-2, sec])
                    is_long_black = realbody2 > BodyLongAverage and close[i-2, sec] < open[i-2, sec]
                
                    # Second candle: Doji with gap down
                    realbody1 = abs(close[i-1, sec] - open[i-1, sec])
                    is_doji = realbody1 <= BodyDojiAverage
                    gap_down = max(open[i-1, sec], close[i-1, sec]) < min(open[i-2, sec], close[i-2, sec])
                
                    # Third candle: White body with penetration
                    realbody0 = abs(close[i, sec] - open[i, sec])
                    is_short_white = realbody0 > BodyShortAverage and close[i, sec] > open[i, sec]
                    penetration_check = close[i, sec] > close[i-2, sec] + realbody2 * penetration
                
                    if is_long_black and is_doji and gap_down and is_short_white and penetration_check:
                        result[i, sec] = 100
                    else:
                        result[i, sec] = 0
                    
                    # Update rolling totals
                    if i - 2 >= 0 and valid_mask[i-2]:
                        BodyLongPeriodTotal += abs(close[i-2, sec] - open[i-2, sec])
                    if BodyLongTrailingIdx >= 0 and valid_mask[BodyLongTrailingIdx]:
                        BodyLongPeriodTotal -= abs(close[BodyLongTrailingIdx, sec] - open[BodyLongTrailingIdx, sec])
                
                    if i - 1 >= 0 and valid_mask[i-1]:
                        BodyDojiPeriodTotal += abs(close[i-1, sec] - open[i-1, sec])
                    if BodyDojiTrailingIdx >= 0 and valid_mask[BodyDojiTrailingIdx]:
                        BodyDojiPeriodTotal -= abs(close[BodyDojiTrailingIdx, sec] - open[BodyDojiTrailingIdx, sec])
                
                    if valid_mask[i]:
                        BodyShortPeriodTotal += abs(close[i, sec] - open[i, sec])
                    if BodyShortTrailingIdx >= 0 and valid_mask[BodyShortTrailingIdx]:
                        BodyShortPeriodTotal -= abs(close[BodyShortTrailingIdx, sec] - open[BodyShortTrailingIdx, sec])
                
                    BodyLongTrailingIdx += 1
                    BodyDojiTrailingIdx += 1
                    BodyShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLMORNINGSTAR(high, open, low, close, vol, oi, penetration=0.3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyLong and BodyShort as per TA-Lib defaults
        body_long_period = 10  # Default period for BodyLong in TA-Lib
        body_short_period = 3  # Default period for BodyShort in TA-Lib
        lookback_total = 2 + max(body_long_period, body_short_period)
    
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
        
            # Initialize output array for valid data
            valid_result = np.zeros(len(valid_high))
        
            # Initialize trailing totals for BodyLong and BodyShort
            body_long_total = 0.0
            body_short_total = 0.0
            body_short_total2 = 0.0
        
            # Calculate initial totals for BodyLong (i-2) and BodyShort (i-1 and i)
            start_idx = lookback_total
            body_long_trailing_idx = start_idx - 2 - body_long_period
            body_short_trailing_idx = start_idx - 1 - body_short_period
        
            # Pre-calculate BodyLong totals
            for i in range(body_long_trailing_idx, start_idx - 2):
                if i >= 0:
                    body_long_total += abs(valid_open[i] - valid_close[i])
        
            # Pre-calculate BodyShort totals
            for i in range(body_short_trailing_idx, start_idx - 1):
                if i >= 0:
                    body_short_total += abs(valid_open[i] - valid_close[i])
                    if i + 1 < len(valid_high):
                        body_short_total2 += abs(valid_open[i + 1] - valid_close[i + 1])
        
            # Main loop starting from lookback_total
            for i in range(start_idx, len(valid_high)):
                # Calculate real body for i-2, i-1, i
                real_body_i2 = abs(valid_open[i - 2] - valid_close[i - 2])
                real_body_i1 = abs(valid_open[i - 1] - valid_close[i - 1])
                real_body_i = abs(valid_open[i] - valid_close[i])
            
                # Calculate averages
                body_long_avg = body_long_total / body_long_period if body_long_period > 0 else 0.0
                body_short_avg = body_short_total / body_short_period if body_short_period > 0 else 0.0
                body_short_avg2 = body_short_total2 / body_short_period if body_short_period > 0 else 0.0
            
                # Check conditions for Morning Star pattern
                if (real_body_i2 > body_long_avg and  # First candle has long body
                    valid_close[i - 2] < valid_open[i - 2] and  # First candle is bearish
                    real_body_i1 <= body_short_avg and  # Second candle has short body
                    valid_open[i - 1] < valid_close[i - 2] and  # Gap down between first and second
                    real_body_i > body_short_avg2 and  # Third candle has long body
                    valid_close[i] > valid_open[i] and  # Third candle is bullish
                    valid_close[i] > valid_close[i - 2] + real_body_i2 * penetration):  # Penetration condition
                    valid_result[i] = 100
                else:
                    valid_result[i] = 0
            
                # Update trailing totals
                if body_long_trailing_idx >= 0:
                    body_long_total += abs(valid_open[i - 2] - valid_close[i - 2])
                    body_long_total -= abs(valid_open[body_long_trailing_idx] - valid_close[body_long_trailing_idx])
                if body_short_trailing_idx >= 0:
                    body_short_total += abs(valid_open[i - 1] - valid_close[i - 1])
                    body_short_total -= abs(valid_open[body_short_trailing_idx] - valid_close[body_short_trailing_idx])
                    body_short_total2 += abs(valid_open[i] - valid_close[i])
                    if body_short_trailing_idx + 1 < len(valid_high):
                        body_short_total2 -= abs(valid_open[body_short_trailing_idx + 1] - valid_close[body_short_trailing_idx + 1])
            
                body_long_trailing_idx += 1
                body_short_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = valid_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLONNECK(high, open, low, close, vol, oi, equal_period=10, body_long_period=10):
        """
        CDLONNECK - On-Neck Pattern
        Identifies a bearish continuation pattern where a long black candle is followed by a white candle
        that opens below the previous low and closes near the previous low.
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (maximum of the two periods)
        lookback_total = max(equal_period, body_long_period)
    
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
        
            # Initialize period totals for Equal and BodyLong ranges
            equal_period_total = 0.0
            body_long_period_total = 0.0
        
            # Calculate initial totals for the lookback period
            equal_trailing_idx = 0
            body_long_trailing_idx = 0
        
            for i in range(lookback_total):
                if i < equal_period:
                    equal_range = valid_high[i] - valid_low[i] if valid_high[i] == valid_high[i] else 0.0
                    equal_period_total += equal_range
                if i < body_long_period:
                    body_long_range = abs(valid_close[i] - valid_open[i]) if valid_close[i] == valid_close[i] else 0.0
                    body_long_period_total += body_long_range
        
            # Start processing from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Check for On-Neck pattern conditions
                if i > 0:
                    # Condition 1: Previous candle is black (bearish)
                    prev_color = -1 if valid_close[i-1] < valid_open[i-1] else 1
                
                    # Condition 2: Previous candle has long body
                    prev_body = abs(valid_close[i-1] - valid_open[i-1])
                    body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
                
                    # Condition 3: Current candle is white (bullish)
                    curr_color = 1 if valid_close[i] > valid_open[i] else -1
                
                    # Condition 4: Current open is below previous low
                    open_below_low = valid_open[i] < valid_low[i-1]
                
                    # Condition 5 & 6: Current close is near previous low (within Equal range)
                    equal_avg = equal_period_total / equal_period if equal_period > 0 else 0.0
                    close_near_low_upper = valid_close[i] <= valid_low[i-1] + equal_avg
                    close_near_low_lower = valid_close[i] >= valid_low[i-1] - equal_avg
                
                    if (prev_color == -1 and 
                        prev_body > body_long_avg and 
                        curr_color == 1 and 
                        open_below_low and 
                        close_near_low_upper and 
                        close_near_low_lower):
                        result[valid_indices[i], sec] = -100
                    else:
                        result[valid_indices[i], sec] = 0
            
                # Update rolling totals for Equal and BodyLong ranges
                if i >= equal_period:
                    old_equal_range = valid_high[i - equal_period] - valid_low[i - equal_period] if valid_high[i - equal_period] == valid_high[i - equal_period] else 0.0
                    new_equal_range = valid_high[i] - valid_low[i] if valid_high[i] == valid_high[i] else 0.0
                    equal_period_total += new_equal_range - old_equal_range
            
                if i >= body_long_period:
                    old_body_long_range = abs(valid_close[i - body_long_period] - valid_open[i - body_long_period]) if valid_close[i - body_long_period] == valid_close[i - body_long_period] else 0.0
                    new_body_long_range = abs(valid_close[i] - valid_open[i]) if valid_close[i] == valid_close[i] else 0.0
                    body_long_period_total += new_body_long_range - old_body_long_range
    
        return result



    @staticmethod
    @nb.njit
    def CDLPIERCING(high, open, low, close, vol, oi, body_long_period=10):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
            if len(valid_indices) < body_long_period + 1:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 初始化输出数组
            piercing_values = np.zeros(len(valid_high))
        
            # 初始化BodyLongPeriodTotal数组，用于存储两个周期的累加值
            body_long_period_total = np.zeros(2)
            body_long_trailing_idx = 0
        
            # 计算lookback period
            lookback_total = body_long_period
        
            # 预热期处理：计算初始的BodyLongPeriodTotal
            if lookback_total < len(valid_high):
                for i in range(body_long_trailing_idx, lookback_total):
                    body_long_period_total[1] += abs(valid_open[i-1] - valid_close[i-1]) if i > 0 else 0
                    body_long_period_total[0] += abs(valid_open[i] - valid_close[i])
                body_long_trailing_idx = lookback_total - body_long_period
        
            # 主计算循环
            for i in range(lookback_total, len(valid_high)):
                # 计算Piercing形态条件
                if i > 0:
                    # 前一根K线为阴线 (收盘价 < 开盘价)
                    candle_color_prev = -1 if valid_close[i-1] < valid_open[i-1] else 1
                    # 当前K线为阳线 (收盘价 > 开盘价)
                    candle_color_curr = 1 if valid_close[i] > valid_open[i] else -1
                    # 前一根K线的实体长度
                    real_body_prev = abs(valid_close[i-1] - valid_open[i-1])
                    # 当前K线的实体长度
                    real_body_curr = abs(valid_close[i] - valid_open[i])
                    # 计算BodyLong平均值
                    body_long_avg_prev = body_long_period_total[1] / body_long_period if body_long_period > 0 else 0
                    body_long_avg_curr = body_long_period_total[0] / body_long_period if body_long_period > 0 else 0
                
                    # 判断Piercing形态
                    if (candle_color_prev == -1 and
                        real_body_prev > body_long_avg_prev and
                        candle_color_curr == 1 and
                        real_body_curr > body_long_avg_curr and
                        valid_open[i] < valid_low[i-1] and
                        valid_close[i] < valid_open[i-1] and
                        valid_close[i] > valid_close[i-1] + real_body_prev * 0.5):
                        piercing_values[i] = 100
                    else:
                        piercing_values[i] = 0
            
                # 更新BodyLongPeriodTotal
                for tot_idx in range(1, -1, -1):
                    curr_range = abs(valid_open[i - tot_idx] - valid_close[i - tot_idx]) if i - tot_idx >= 0 else 0
                    trail_range = abs(valid_open[body_long_trailing_idx - tot_idx] - valid_close[body_long_trailing_idx - tot_idx]) if body_long_trailing_idx - tot_idx >= 0 else 0
                    body_long_period_total[tot_idx] += curr_range - trail_range
            
                body_long_trailing_idx += 1
        
            # 映射结果回原始数组
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = piercing_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLRISEFALL3METHODS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as defined in TA-Lib (typically 4 for this pattern)
        lookback_total = 4
    
        # Define periods for body calculations as in TA-Lib
        body_short_period = 5  # Default short body period from TA-Lib
        body_long_period = 5   # Default long body period from TA-Lib
    
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
            valid_result = np.zeros(len(valid_high))
        
            # Initialize body period totals for long and short
            body_period_total = np.zeros(5)  # Indices 0 and 4 for long, 1-3 for short
        
            # Calculate initial body period totals
            body_short_trailing_idx = lookback_total - body_short_period
            body_long_trailing_idx = lookback_total - body_long_period
        
            # Pre-calculate initial sums for body averages (before start index)
            i = max(0, body_short_trailing_idx)
            while i < lookback_total:
                if i - 3 >= 0:
                    body_period_total[3] += abs(valid_close[i - 3] - valid_open[i - 3])
                if i - 2 >= 0:
                    body_period_total[2] += abs(valid_close[i - 2] - valid_open[i - 2])
                if i - 1 >= 0:
                    body_period_total[1] += abs(valid_close[i - 1] - valid_open[i - 1])
                i += 1
            
            i = max(0, body_long_trailing_idx)
            while i < lookback_total:
                if i - 4 >= 0:
                    body_period_total[4] += abs(valid_close[i - 4] - valid_open[i - 4])
                body_period_total[0] += abs(valid_close[i] - valid_open[i])
                i += 1
            
            # Main loop starting from lookback_total
            i = lookback_total
            body_short_trailing_idx = i - body_short_period
            body_long_trailing_idx = i - body_long_period
        
            while i < len(valid_high):
                # Calculate body averages
                body_long_avg_4 = body_period_total[4] / body_long_period if body_long_period > 0 else 0
                body_short_avg_3 = body_period_total[3] / body_short_period if body_short_period > 0 else 0
                body_short_avg_2 = body_period_total[2] / body_short_period if body_short_period > 0 else 0
                body_short_avg_1 = body_period_total[1] / body_short_period if body_short_period > 0 else 0
                body_long_avg_0 = body_period_total[0] / body_long_period if body_long_period > 0 else 0
            
                # Calculate real bodies
                real_body_4 = abs(valid_close[i - 4] - valid_open[i - 4])
                real_body_3 = abs(valid_close[i - 3] - valid_open[i - 3])
                real_body_2 = abs(valid_close[i - 2] - valid_open[i - 2])
                real_body_1 = abs(valid_close[i - 1] - valid_open[i - 1])
                real_body_0 = abs(valid_close[i] - valid_open[i])
            
                # Determine candle colors (1 for bullish, -1 for bearish)
                color_4 = 1 if valid_close[i - 4] > valid_open[i - 4] else -1
                color_3 = 1 if valid_close[i - 3] > valid_open[i - 3] else -1
                color_2 = 1 if valid_close[i - 2] > valid_open[i - 2] else -1
                color_1 = 1 if valid_close[i - 1] > valid_open[i - 1] else -1
                color_0 = 1 if valid_close[i] > valid_open[i] else -1
            
                # Check pattern conditions
                if (real_body_4 > body_long_avg_4 and
                    real_body_3 < body_short_avg_3 and
                    real_body_2 < body_short_avg_2 and
                    real_body_1 < body_short_avg_1 and
                    real_body_0 > body_long_avg_0 and
                    color_4 == -color_3 and
                    color_3 == color_2 and
                    color_2 == color_1 and
                    color_1 == -color_0 and
                    min(valid_open[i - 3], valid_close[i - 3]) < valid_high[i - 4] and
                    max(valid_open[i - 3], valid_close[i - 3]) > valid_low[i - 4] and
                    min(valid_open[i - 2], valid_close[i - 2]) < valid_high[i - 4] and
                    max(valid_open[i - 2], valid_close[i - 2]) > valid_low[i - 4] and
                    min(valid_open[i - 1], valid_close[i - 1]) < valid_high[i - 4] and
                    max(valid_open[i - 1], valid_close[i - 1]) > valid_low[i - 4] and
                    valid_close[i - 2] * color_4 < valid_close[i - 3] * color_4 and
                    valid_close[i - 1] * color_4 < valid_close[i - 2] * color_4 and
                    valid_open[i] * color_4 > valid_close[i - 1] * color_4 and
                    valid_close[i] * color_4 > valid_close[i - 4] * color_4):
                    valid_result[i] = 100 * color_4
                else:
                    valid_result[i] = 0
                
                # Update body period totals for next iteration
                if i - 4 >= 0 and body_long_trailing_idx - 4 >= 0:
                    body_period_total[4] += abs(valid_close[i - 4] - valid_open[i - 4]) - abs(valid_close[body_long_trailing_idx - 4] - valid_open[body_long_trailing_idx - 4])
                for tot_idx in range(3, 0, -1):
                    if i - tot_idx >= 0 and body_short_trailing_idx - tot_idx >= 0:
                        body_period_total[tot_idx] += abs(valid_close[i - tot_idx] - valid_open[i - tot_idx]) - abs(valid_close[body_short_trailing_idx - tot_idx] - valid_open[body_short_trailing_idx - tot_idx])
                if body_long_trailing_idx >= 0:
                    body_period_total[0] += abs(valid_close[i] - valid_open[i]) - abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
                
                i += 1
                body_short_trailing_idx += 1
                body_long_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = valid_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLSHOOTINGSTAR(high, open, low, close, vol, oi, body_short_period=10, shadow_long_period=10, shadow_very_short_period=10):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (maximum of the averaging periods)
        lookback_total = max(body_short_period, max(shadow_long_period, shadow_very_short_period))
    
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
        
            # Initialize period totals for averages
            body_period_total = 0.0
            shadow_long_period_total = 0.0
            shadow_very_short_period_total = 0.0
        
            # Trailing indices for rolling window
            body_trailing_idx = 0
            shadow_long_trailing_idx = 0
            shadow_very_short_trailing_idx = 0
        
            # Pre-calculate initial totals for the lookback period
            for i in range(lookback_total):
                # BodyShort range (real body)
                body_range = abs(valid_close[i] - valid_open[i])
                body_period_total += body_range
            
                # ShadowLong range (upper shadow)
                shadow_long_range = valid_high[i] - max(valid_open[i], valid_close[i])
                shadow_long_period_total += shadow_long_range
            
                # ShadowVeryShort range (lower shadow)
                shadow_very_short_range = min(valid_open[i], valid_close[i]) - valid_low[i]
                shadow_very_short_period_total += shadow_very_short_range
        
            # Main calculation loop starting from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
            
                # Calculate upper shadow
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
            
                # Calculate lower shadow
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Calculate averages
                body_avg = body_period_total / body_short_period if body_short_period > 0 else 0.0
                shadow_long_avg = shadow_long_period_total / shadow_long_period if shadow_long_period > 0 else 0.0
                shadow_very_short_avg = shadow_very_short_period_total / shadow_very_short_period if shadow_very_short_period > 0 else 0.0
            
                # Check for Shooting Star pattern
                if (real_body < body_avg and
                    upper_shadow > shadow_long_avg and
                    lower_shadow < shadow_very_short_avg and
                    i > 0 and
                    min(valid_open[i], valid_close[i]) > max(valid_open[i-1], valid_close[i-1])):
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals
                if body_trailing_idx < len(valid_high):
                    body_range_old = abs(valid_close[body_trailing_idx] - valid_open[body_trailing_idx])
                    body_period_total += real_body - body_range_old
                    body_trailing_idx += 1 if body_trailing_idx + body_short_period <= i else 0
                
                if shadow_long_trailing_idx < len(valid_high):
                    shadow_long_range_old = valid_high[shadow_long_trailing_idx] - max(valid_open[shadow_long_trailing_idx], valid_close[shadow_long_trailing_idx])
                    shadow_long_period_total += upper_shadow - shadow_long_range_old
                    shadow_long_trailing_idx += 1 if shadow_long_trailing_idx + shadow_long_period <= i else 0
                
                if shadow_very_short_trailing_idx < len(valid_high):
                    shadow_very_short_range_old = min(valid_open[shadow_very_short_trailing_idx], valid_close[shadow_very_short_trailing_idx]) - valid_low[shadow_very_short_trailing_idx]
                    shadow_very_short_period_total += lower_shadow - shadow_very_short_range_old
                    shadow_very_short_trailing_idx += 1 if shadow_very_short_trailing_idx + shadow_very_short_period <= i else 0
    
        return result



    @staticmethod
    @nb.njit
    def CDLSPINNINGTOP(high, open, low, close, vol, oi, body_period=10):
        """
        CDLSPINNINGTOP - Candlestick Spinning Top Pattern
        Identifies Spinning Top pattern where the body is small compared to the average body
        and both upper and lower shadows are larger than the body.
        """
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
            if len(valid_indices) < body_period:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            valid_result = np.zeros(len(valid_high))
        
            # Calculate lookback total (start index for output)
            lookback_total = body_period
        
            # Initialize body period total for trailing average
            body_period_total = 0.0
            body_trailing_idx = 0
        
            # Pre-calculate initial body period total
            for i in range(lookback_total):
                if i < len(valid_high):
                    body_range = abs(valid_close[i] - valid_open[i])
                    body_period_total += body_range
        
            # Main calculation loop
            out_idx = 0
            for i in range(lookback_total, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
            
                # Calculate average body over period
                body_average = body_period_total / body_period
            
                # Calculate upper and lower shadows
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Check Spinning Top conditions:
                # 1. Real body is smaller than average body
                # 2. Upper shadow is larger than real body
                # 3. Lower shadow is larger than real body
                if (real_body < body_average and 
                    upper_shadow > real_body and 
                    lower_shadow > real_body):
                    # Output 100 for white candle (bullish), -100 for black candle (bearish)
                    candle_color = 1 if valid_close[i] > valid_open[i] else -1
                    valid_result[i] = candle_color * 100
                else:
                    valid_result[i] = 0
                
                # Update body period total for next iteration
                if body_trailing_idx < len(valid_high):
                    body_period_total += abs(valid_close[i] - valid_open[i])
                    body_period_total -= abs(valid_close[body_trailing_idx] - valid_open[body_trailing_idx])
                    body_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = valid_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLSTALLEDPATTERN(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as in TA-Lib
        BodyLongPeriod = 10
        BodyShortPeriod = 10
        ShadowVeryShortPeriod = 7
        NearPeriod = 7
        lookbackTotal = max(BodyLongPeriod, max(BodyShortPeriod, max(ShadowVeryShortPeriod, NearPeriod))) + 2
    
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
        
            # Initialize period totals for averages
            BodyLongPeriodTotal = np.zeros(3)
            NearPeriodTotal = np.zeros(3)
            BodyShortPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Initialize trailing indices
            BodyLongTrailingIdx = lookbackTotal - BodyLongPeriod
            BodyShortTrailingIdx = lookbackTotal - BodyShortPeriod
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
            NearTrailingIdx = lookbackTotal - NearPeriod
        
            # Pre-calculate initial totals for averages
            for i in range(BodyLongTrailingIdx, lookbackTotal):
                BodyLongPeriodTotal[2] += max(valid_close[i-2] - valid_open[i-2], 0.0) if valid_close[i-2] > valid_open[i-2] else max(valid_open[i-2] - valid_close[i-2], 0.0)
                BodyLongPeriodTotal[1] += max(valid_close[i-1] - valid_open[i-1], 0.0) if valid_close[i-1] > valid_open[i-1] else max(valid_open[i-1] - valid_close[i-1], 0.0)
        
            for i in range(BodyShortTrailingIdx, lookbackTotal):
                BodyShortPeriodTotal += max(valid_close[i] - valid_open[i], 0.0) if valid_close[i] > valid_open[i] else max(valid_open[i] - valid_close[i], 0.0)
        
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                ShadowVeryShortPeriodTotal += valid_high[i-1] - valid_close[i-1] if valid_close[i-1] > valid_open[i-1] else valid_high[i-1] - valid_open[i-1]
        
            for i in range(NearTrailingIdx, lookbackTotal):
                NearPeriodTotal[2] += valid_close[i-2] - valid_open[i-2] if valid_close[i-2] > valid_open[i-2] else valid_open[i-2] - valid_close[i-2]
                NearPeriodTotal[1] += valid_close[i-1] - valid_open[i-1] if valid_close[i-1] > valid_open[i-1] else valid_open[i-1] - valid_close[i-1]
        
            # Main calculation loop
            for i in range(lookbackTotal, len(valid_high)):
                # Check for Stalled Pattern conditions
                if (valid_close[i-2] > valid_open[i-2] and  # First candle is white
                    valid_close[i-1] > valid_open[i-1] and  # Second candle is white
                    valid_close[i] > valid_open[i] and      # Third candle is white
                    valid_close[i] > valid_close[i-1] and valid_close[i-1] > valid_close[i-2] and  # Upward trend
                    (valid_close[i-2] - valid_open[i-2] if valid_close[i-2] > valid_open[i-2] else valid_open[i-2] - valid_close[i-2]) > BodyLongPeriodTotal[2] / BodyLongPeriod and  # Long body for first
                    (valid_close[i-1] - valid_open[i-1] if valid_close[i-1] > valid_open[i-1] else valid_open[i-1] - valid_close[i-1]) > BodyLongPeriodTotal[1] / BodyLongPeriod and  # Long body for second
                    (valid_high[i-1] - valid_close[i-1] if valid_close[i-1] > valid_open[i-1] else valid_high[i-1] - valid_open[i-1]) < ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod and  # Short upper shadow for second
                    valid_open[i-1] > valid_open[i-2] and
                    valid_open[i-1] <= valid_close[i-2] + (NearPeriodTotal[2] / NearPeriod) and  # Second opens near first's close
                    (valid_close[i] - valid_open[i] if valid_close[i] > valid_open[i] else valid_open[i] - valid_close[i]) < BodyShortPeriodTotal / BodyShortPeriod and  # Short body for third
                    valid_open[i] >= valid_close[i-1] - (valid_close[i] - valid_open[i] if valid_close[i] > valid_open[i] else valid_open[i] - valid_close[i]) - (NearPeriodTotal[1] / NearPeriod)):  # Third opens near second's close
                    result[valid_indices[i], sec] = -100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update period totals
                for totIdx in range(2, 0, -1):
                    BodyLongPeriodTotal[totIdx] += (max(valid_close[i-totIdx] - valid_open[i-totIdx], 0.0) if valid_close[i-totIdx] > valid_open[i-totIdx] else max(valid_open[i-totIdx] - valid_close[i-totIdx], 0.0)) - \
                                                   (max(valid_close[BodyLongTrailingIdx-totIdx] - valid_open[BodyLongTrailingIdx-totIdx], 0.0) if valid_close[BodyLongTrailingIdx-totIdx] > valid_open[BodyLongTrailingIdx-totIdx] else max(valid_open[BodyLongTrailingIdx-totIdx] - valid_close[BodyLongTrailingIdx-totIdx], 0.0))
                    NearPeriodTotal[totIdx] += (valid_close[i-totIdx] - valid_open[i-totIdx] if valid_close[i-totIdx] > valid_open[i-totIdx] else valid_open[i-totIdx] - valid_close[i-totIdx]) - \
                                               (valid_close[NearTrailingIdx-totIdx] - valid_open[NearTrailingIdx-totIdx] if valid_close[NearTrailingIdx-totIdx] > valid_open[NearTrailingIdx-totIdx] else valid_open[NearTrailingIdx-totIdx] - valid_close[NearTrailingIdx-totIdx])
            
                BodyShortPeriodTotal += (max(valid_close[i] - valid_open[i], 0.0) if valid_close[i] > valid_open[i] else max(valid_open[i] - valid_close[i], 0.0)) - \
                                        (max(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx], 0.0) if valid_close[BodyShortTrailingIdx] > valid_open[BodyShortTrailingIdx] else max(valid_open[BodyShortTrailingIdx] - valid_close[BodyShortTrailingIdx], 0.0))
                ShadowVeryShortPeriodTotal += (valid_high[i-1] - valid_close[i-1] if valid_close[i-1] > valid_open[i-1] else valid_high[i-1] - valid_open[i-1]) - \
                                              (valid_high[ShadowVeryShortTrailingIdx-1] - valid_close[ShadowVeryShortTrailingIdx-1] if valid_close[ShadowVeryShortTrailingIdx-1] > valid_open[ShadowVeryShortTrailingIdx-1] else valid_high[ShadowVeryShortTrailingIdx-1] - valid_open[ShadowVeryShortTrailingIdx-1])
            
                BodyLongTrailingIdx += 1
                BodyShortTrailingIdx += 1
                ShadowVeryShortTrailingIdx += 1
                NearTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLSTICKSANDWICH(high, open, low, close, vol, oi, equal_period=3):
        """
        CDLSTICKSANDWICH - Candlestick Stick Sandwich Pattern
    
        Identifies a specific candlestick pattern where a bullish candle is sandwiched
        between two bearish candles, with specific price relationships.
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (needs 2 previous candles)
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
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            valid_result = np.zeros(len(valid_high))
        
            # Calculate initial EqualPeriodTotal for the lookback period
            equal_trailing_idx = 0
            equal_period_total = 0.0
            start_idx = lookback_total
        
            # Pre-calculate initial total for Equal range
            for i in range(equal_trailing_idx, start_idx):
                if i >= 0 and i - 2 >= 0:
                    equal_range = valid_close[i-2] - valid_open[i-2] if valid_close[i-2] >= valid_open[i-2] else valid_open[i-2] - valid_close[i-2]
                    equal_period_total += equal_range
        
            # Main calculation loop
            for i in range(start_idx, len(valid_high)):
                # Check candle colors: bearish-bullish-bearish pattern
                color_2 = -1 if valid_close[i-2] < valid_open[i-2] else 1
                color_1 = -1 if valid_close[i-1] < valid_open[i-1] else 1
                color_0 = -1 if valid_close[i] < valid_open[i] else 1
            
                # Calculate Equal average for comparison
                equal_avg = equal_period_total / equal_period if equal_period > 0 else 0.0
            
                # Check pattern conditions
                if (color_2 == -1 and 
                    color_1 == 1 and 
                    color_0 == -1 and 
                    valid_low[i-1] > valid_close[i-2] and 
                    valid_close[i] <= valid_close[i-2] + equal_avg and 
                    valid_close[i] >= valid_close[i-2] - equal_avg):
                    valid_result[i] = 100
                else:
                    valid_result[i] = 0
                
                # Update EqualPeriodTotal for next iteration
                if i - 2 >= 0:
                    old_range = valid_close[equal_trailing_idx-2] - valid_open[equal_trailing_idx-2] if valid_close[equal_trailing_idx-2] >= valid_open[equal_trailing_idx-2] else valid_open[equal_trailing_idx-2] - valid_close[equal_trailing_idx-2]
                    new_range = valid_close[i-2] - valid_open[i-2] if valid_close[i-2] >= valid_open[i-2] else valid_open[i-2] - valid_close[i-2]
                    equal_period_total += new_range - old_range
                equal_trailing_idx += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = valid_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLTASUKIGAP(high, open, low, close, vol, oi, near_period=3):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
            if len(valid_indices) < near_period + 2:  # 需要至少near_period + 2个数据点
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 初始化输出数组
            temp_result = np.zeros(len(valid_high))
        
            # 计算lookback period
            lookback_total = near_period + 2
        
            # 如果数据不足lookback_total，跳过
            if len(valid_high) < lookback_total:
                continue
            
            # 初始化NearPeriodTotal
            near_period_total = 0.0
            near_trailing_idx = 0
        
            # 初始计算NearPeriodTotal
            for i in range(near_trailing_idx, near_period):
                near_period_total += valid_high[i] - valid_low[i]
        
            # 主计算循环
            for i in range(near_period, len(valid_high)):
                # 检查是否满足Tasuki Gap条件
                # 条件1：向上跳空
                condition1 = (
                    valid_open[i-1] > valid_close[i-2] and  # 跳空
                    (valid_close[i-1] - valid_open[i-1]) > 0 and  # 前一根阳线
                    (valid_close[i] - valid_open[i]) < 0 and  # 当前阴线
                    valid_open[i] < valid_close[i-1] and valid_open[i] > valid_open[i-1] and  # 开盘价在实体内
                    valid_close[i] < valid_open[i-1] and  # 收盘价低于前一根开盘价
                    valid_close[i] > max(valid_close[i-2], valid_open[i-2]) and  # 收盘价高于前前一根最高价
                    abs((valid_close[i-1] - valid_open[i-1]) - abs(valid_close[i] - valid_open[i])) < (near_period_total / near_period)  # 实体大小接近
                )
            
                # 条件2：向下跳空
                condition2 = (
                    valid_open[i-1] < valid_close[i-2] and  # 跳空
                    (valid_close[i-1] - valid_open[i-1]) < 0 and  # 前一根阴线
                    (valid_close[i] - valid_open[i]) > 0 and  # 当前阳线
                    valid_open[i] < valid_open[i-1] and valid_open[i] > valid_close[i-1] and  # 开盘价在实体内
                    valid_close[i] > valid_open[i-1] and  # 收盘价高于前一根开盘价
                    valid_close[i] < min(valid_close[i-2], valid_open[i-2]) and  # 收盘价低于前前一根最低价
                    abs(abs(valid_close[i-1] - valid_open[i-1]) - (valid_close[i] - valid_open[i])) < (near_period_total / near_period)  # 实体大小接近
                )
            
                if condition1:
                    temp_result[i] = 100  # 向上跳空形态
                elif condition2:
                    temp_result[i] = -100  # 向下跳空形态
                else:
                    temp_result[i] = 0
                
                # 更新NearPeriodTotal
                if i < len(valid_high):
                    near_period_total += (valid_high[i] - valid_low[i]) - (valid_high[near_trailing_idx] - valid_low[near_trailing_idx])
                    near_trailing_idx += 1
        
            # 映射结果回原始数组
            start_idx = lookback_total - 1
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = temp_result[i]
    
        return result



    @staticmethod
    @nb.njit
    def CDLTHRUSTING(high, open, low, close, vol, oi, equal_period=3, body_long_period=5):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (maximum of the two periods)
        lookback_total = max(equal_period, body_long_period)
    
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
        
            # Initialize totals for Equal and BodyLong periods
            equal_period_total = 0.0
            body_long_period_total = 0.0
        
            # Calculate initial totals for the lookback period
            equal_trailing_idx = 0
            body_long_trailing_idx = 0
        
            for i in range(lookback_total):
                if i < equal_period:
                    equal_range = valid_close[i] - valid_open[i] if valid_close[i] >= valid_open[i] else valid_open[i] - valid_close[i]
                    equal_period_total += equal_range
                if i < body_long_period:
                    body_long_range = valid_close[i] - valid_open[i] if valid_close[i] >= valid_open[i] else valid_open[i] - valid_close[i]
                    body_long_period_total += body_long_range
        
            # Main calculation loop
            for i in range(lookback_total, len(valid_high)):
                # Check for Thrusting pattern conditions
                if i > 0:
                    # Condition 1: Previous day is bearish (close < open)
                    prev_color = -1 if valid_close[i-1] < valid_open[i-1] else 1
                    # Condition 2: Previous day body is long
                    prev_body = abs(valid_close[i-1] - valid_open[i-1])
                    body_long_avg = body_long_period_total / body_long_period if body_long_period > 0 else 0.0
                    # Condition 3: Current day is bullish (close > open)
                    curr_color = 1 if valid_close[i] > valid_open[i] else -1
                    # Condition 4: Current open below previous low
                    # Condition 5: Current close above previous close + equal average
                    equal_avg = equal_period_total / equal_period if equal_period > 0 else 0.0
                    # Condition 6: Current close <= previous close + 0.5 * previous body
                
                    if (prev_color == -1 and
                        prev_body > body_long_avg and
                        curr_color == 1 and
                        valid_open[i] < valid_low[i-1] and
                        valid_close[i] > valid_close[i-1] + equal_avg and
                        valid_close[i] <= valid_close[i-1] + prev_body * 0.5):
                        result[valid_indices[i], sec] = -100
                    else:
                        result[valid_indices[i], sec] = 0
            
                # Update totals for next iteration
                if i >= equal_period:
                    old_equal_range = valid_close[i - equal_period] - valid_open[i - equal_period] if valid_close[i - equal_period] >= valid_open[i - equal_period] else valid_open[i - equal_period] - valid_close[i - equal_period]
                    new_equal_range = valid_close[i - 1] - valid_open[i - 1] if valid_close[i - 1] >= valid_open[i - 1] else valid_open[i - 1] - valid_close[i - 1]
                    equal_period_total += new_equal_range - old_equal_range
            
                if i >= body_long_period:
                    old_body_long_range = valid_close[i - body_long_period] - valid_open[i - body_long_period] if valid_close[i - body_long_period] >= valid_open[i - body_long_period] else valid_open[i - body_long_period] - valid_close[i - body_long_period]
                    new_body_long_range = valid_close[i - 1] - valid_open[i - 1] if valid_close[i - 1] >= valid_open[i - 1] else valid_open[i - 1] - valid_close[i - 1]
                    body_long_period_total += new_body_long_range - old_body_long_range
    
        return result



    @staticmethod
    @nb.njit
    def CDLUNIQUE3RIVER(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # 对应TA-Lib中的BodyLong和BodyShort的平均周期，常用默认值
        BodyLongPeriod = 5
        BodyShortPeriod = 3
        lookbackTotal = 2  # 需要前两根K线数据
    
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
        
            # 初始化BodyLong和BodyShort的累加值
            BodyLongPeriodTotal = 0.0
            BodyShortPeriodTotal = 0.0
        
            # 计算初始的BodyLongPeriodTotal (前BodyLongPeriod个周期)
            BodyLongTrailingIdx = 0
            for i in range(BodyLongTrailingIdx, min(BodyLongPeriod, len(valid_high))):
                if i <= len(valid_high) - 3:  # 确保有足够的数据
                    BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # 计算初始的BodyShortPeriodTotal (前BodyShortPeriod个周期)
            BodyShortTrailingIdx = 0
            for i in range(BodyShortTrailingIdx, min(BodyShortPeriod, len(valid_high))):
                if i <= len(valid_high) - 1:
                    BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # 主计算循环
            for i in range(lookbackTotal, len(valid_high)):
                # 计算Unique 3 River形态的条件
                # 条件1: 前两根K线为阴线，实体较长
                realbody_2 = valid_close[i-2] - valid_open[i-2]
                realbody_1 = valid_close[i-1] - valid_open[i-1]
                realbody_0 = valid_close[i] - valid_open[i]
                body_long_avg = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                body_short_avg = BodyShortPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
            
                if (realbody_2 < 0 and abs(realbody_2) > body_long_avg and  # 第一根阴线，实体长
                    realbody_1 < 0 and  # 第二根阴线
                    valid_close[i-1] > valid_close[i-2] and  # 第二根收盘价高于第一根
                    valid_open[i-1] <= valid_open[i-2] and  # 第二根开盘价低于或等于第一根
                    valid_low[i-1] < valid_low[i-2] and  # 第二根低点低于第一根
                    realbody_0 > 0 and abs(realbody_0) < body_short_avg and  # 第三根阳线，实体短
                    valid_open[i] > valid_low[i-1]):  # 第三根开盘价高于第二根低点
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # 更新BodyLongPeriodTotal
                if i - 2 >= 0 and BodyLongTrailingIdx < len(valid_high):
                    BodyLongPeriodTotal += abs(valid_close[i-2] - valid_open[i-2])
                    if BodyLongTrailingIdx >= 0:
                        BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                    BodyLongTrailingIdx += 1
            
                # 更新BodyShortPeriodTotal
                if i >= 0 and BodyShortTrailingIdx < len(valid_high):
                    BodyShortPeriodTotal += abs(valid_close[i] - valid_open[i])
                    if BodyShortTrailingIdx >= 0:
                        BodyShortPeriodTotal -= abs(valid_close[BodyShortTrailingIdx] - valid_open[BodyShortTrailingIdx])
                    BodyShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLUPSIDEGAP2CROWS(high, open, low, close, vol, oi, body_long_period=10, body_short_period=10):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (2 days for pattern + max of body periods for averages)
        lookback_total = 2 + max(body_long_period, body_short_period)
    
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
        
            # Initialize totals for body averages
            body_long_total = 0.0
            body_short_total = 0.0
        
            # Calculate initial totals for body averages
            body_long_trailing_idx = 0
            body_short_trailing_idx = 0
        
            start_idx = lookback_total
            if start_idx > len(valid_high):
                continue
            
            # Initialize trailing indices for rolling window
            body_long_trailing_idx = start_idx - 2 - body_long_period
            body_short_trailing_idx = start_idx - 1 - body_short_period
        
            # Calculate initial sums for body averages
            i = body_long_trailing_idx if body_long_trailing_idx >= 0 else 0
            while i < start_idx - 2 and i < len(valid_high):
                if i >= 0:
                    body_long_total += abs(valid_close[i] - valid_open[i])
                i += 1
            
            i = body_short_trailing_idx if body_short_trailing_idx >= 0 else 0
            while i < start_idx - 1 and i < len(valid_high):
                if i >= 0:
                    body_short_total += abs(valid_close[i] - valid_open[i])
                i += 1
            
            # Main loop for pattern detection
            i = start_idx
            while i < len(valid_high):
                if i - 2 >= 0:
                    # Calculate body averages
                    body_long_avg = body_long_total / body_long_period if body_long_period > 0 else 0.0
                    body_short_avg = body_short_total / body_short_period if body_short_period > 0 else 0.0
                
                    # Check pattern conditions
                    # First candle: White (bullish)
                    first_candle_white = valid_close[i-2] > valid_open[i-2]
                    # First candle: Long body
                    first_body_long = abs(valid_close[i-2] - valid_open[i-2]) > body_long_avg
                    # Second candle: Black (bearish)
                    second_candle_black = valid_close[i-1] < valid_open[i-1]
                    # Second candle: Short body
                    second_body_short = abs(valid_close[i-1] - valid_open[i-1]) <= body_short_avg
                    # Gap up between first and second candle
                    gap_up = valid_open[i-1] > valid_close[i-2]
                    # Third candle: Black (bearish)
                    third_candle_black = valid_close[i] < valid_open[i]
                    # Third candle opens above second candle's open
                    third_open_above = valid_open[i] > valid_open[i-1]
                    # Third candle closes below second candle's close
                    third_close_below = valid_close[i] < valid_close[i-1]
                    # Third candle closes above first candle's close
                    third_close_above_first = valid_close[i] > valid_close[i-2]
                
                    if (first_candle_white and first_body_long and 
                        second_candle_black and second_body_short and 
                        gap_up and third_candle_black and 
                        third_open_above and third_close_below and 
                        third_close_above_first):
                        result[valid_indices[i], sec] = -100
                    else:
                        result[valid_indices[i], sec] = 0
                    
                    # Update rolling sums for body averages
                    if i - 2 >= 0 and body_long_trailing_idx >= 0 and body_long_trailing_idx < len(valid_high):
                        body_long_total += abs(valid_close[i-2] - valid_open[i-2])
                        body_long_total -= abs(valid_close[body_long_trailing_idx] - valid_open[body_long_trailing_idx])
                    if i - 1 >= 0 and body_short_trailing_idx >= 0 and body_short_trailing_idx < len(valid_high):
                        body_short_total += abs(valid_close[i-1] - valid_open[i-1])
                        body_short_total -= abs(valid_close[body_short_trailing_idx] - valid_open[body_short_trailing_idx])
                    
                    body_long_trailing_idx += 1
                    body_short_trailing_idx += 1
                
                i += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLXSIDEGAP3METHODS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (needs 2 previous candles)
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
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Start processing from lookback_total
            for i in range(lookback_total, len(valid_high)):
                # Determine candle colors (1 for bullish, -1 for bearish)
                color_i_2 = 1 if valid_close[i-2] > valid_open[i-2] else -1
                color_i_1 = 1 if valid_close[i-1] > valid_open[i-1] else -1
                color_i = 1 if valid_close[i] > valid_open[i] else -1
            
                # Check conditions as per TA-Lib logic
                if (color_i_2 == color_i_1 and 
                    color_i_1 == -color_i and
                    valid_open[i] < max(valid_close[i-1], valid_open[i-1]) and
                    valid_open[i] > min(valid_close[i-1], valid_open[i-1]) and
                    valid_close[i] < max(valid_close[i-2], valid_open[i-2]) and
                    valid_close[i] > min(valid_close[i-2], valid_open[i-2])):
                
                    # Check for gap conditions
                    if color_i_2 == 1:
                        # Bullish case: check for gap up between i-2 and i-1
                        gap_up = max(valid_close[i-2], valid_open[i-2]) < min(valid_close[i-1], valid_open[i-1])
                        if gap_up:
                            result[valid_indices[i], sec] = color_i_2 * 100
                        else:
                            result[valid_indices[i], sec] = 0
                    else:
                        # Bearish case: check for gap down between i-2 and i-1
                        gap_down = min(valid_close[i-2], valid_open[i-2]) > max(valid_close[i-1], valid_open[i-1])
                        if gap_down:
                            result[valid_indices[i], sec] = color_i_2 * 100
                        else:
                            result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
    
        return result



    @staticmethod
    @nb.njit
    def CMO(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
        
            # 初始化变量
            lookback_total = timeperiod - 1 if timeperiod > 1 else 0
            start_idx = lookback_total
        
            # 特殊情况：timeperiod为1时直接返回收盘价
            if timeperiod == 1:
                for i in range(len(valid_indices)):
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = valid_close[i]
                continue
            
            # 初始化计算
            today = 0
            prev_value = valid_close[today]
            prev_gain = 0.0
            prev_loss = 0.0
        
            # 第一个循环：计算初始的gain和loss
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
        
            # 初始平均值
            prev_loss /= timeperiod
            prev_gain /= timeperiod
        
            # 处理到start_idx之前的数据（预热期）
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
        
            # 主计算循环
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
            
                temp_value3 = prev_gain + prev_loss
                if temp_value3 > 1e-10:
                    cmo_value = 100.0 * ((prev_gain - prev_loss) / temp_value3)
                else:
                    cmo_value = 0.0
                
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = cmo_value
    
        return result



    @staticmethod
    @nb.njit
    def CORREL(high, open, low, close, vol, oi, timeperiod=30):
        """
        皮尔逊相关系数 (Pearson's Correlation Coefficient)
        
        与TA-Lib的CORREL函数完全一致的实现。对应test_indicator中，CORREL函数使用high和low作为输入。
        """
        tdts, secs = high.shape
        result = np.full((tdts, secs), np.nan, dtype=np.float64)

        for sec in range(secs):
            # 对应test_indicator函数里面CORREL的输入是high和low
            # 注意：根据test_indicator函数的代码，实际上是这样调用TA-Lib的:
            # mask = ~np.isnan(high_1d) & ~np.isnan(low_1d)
            # input_args = (high_1d[mask], low_1d[mask])
            # talib_result = talib_func(*input_args, **talib_params)
            
            # 首先创建一个掩码来过滤掉NaN值
            mask = ~np.isnan(high[:, sec]) & ~np.isnan(low[:, sec])
            valid_indices = np.where(mask)[0]
            
            # 如果没有足够的有效数据点，则跳过
            if len(valid_indices) < timeperiod:
                continue
                
            # 提取有效数据
            valid_high = high[mask, sec]
            valid_low = low[mask, sec]
            
            # TA-Lib的CORREL函数计算的是两个数组间的滚动相关系数
            # 有效数据的长度
            num_valid = len(valid_high)
            
            # 计算起始位置
            lookbackTotal = timeperiod - 1
            
            # 根据C源码，我们需要从第timeperiod个数据点开始计算
            # 这对应于索引timeperiod-1
            startIdx = lookbackTotal
            
            # 如果有效数据不够，则跳过
            if startIdx >= num_valid:
                continue
                
            # 初始化累加器变量
            sumXY = 0.0
            sumX = 0.0
            sumY = 0.0
            sumX2 = 0.0
            sumY2 = 0.0
            
            # 填充初始窗口
            for i in range(timeperiod):
                x = valid_high[i]
                y = valid_low[i]
                sumX += x
                sumX2 += x * x
                sumY += y
                sumY2 += y * y
                sumXY += x * y
            
            # 计算第一个结果
            tempReal = (sumX2 - ((sumX * sumX) / timeperiod)) * (sumY2 - ((sumY * sumY) / timeperiod))
            if tempReal > 0.0:  # 直接使用>0检查，避免除以零
                corr = (sumXY - ((sumX * sumY) / timeperiod)) / np.sqrt(tempReal)
            else:
                corr = 0.0
                
            # 保存结果到对应的有效索引位置
            result_idx = valid_indices[startIdx]
            result[result_idx, sec] = corr
            
            # 准备滑动窗口计算
            trailingIdx = 0
            today = startIdx + 1
            
            # 滑动窗口计算剩余的相关系数
            while today < num_valid:
                # 移除尾部值
                trailingX = valid_high[trailingIdx]
                trailingY = valid_low[trailingIdx]
                trailingIdx += 1
                
                sumX -= trailingX
                sumX2 -= trailingX * trailingX
                sumY -= trailingY
                sumY2 -= trailingY * trailingY
                sumXY -= trailingX * trailingY
                
                # 添加新值
                x = valid_high[today]
                y = valid_low[today]
                sumX += x
                sumX2 += x * x
                sumY += y
                sumY2 += y * y
                sumXY += x * y
                
                # 计算新的相关系数
                tempReal = (sumX2 - ((sumX * sumX) / timeperiod)) * (sumY2 - ((sumY * sumY) / timeperiod))
                if tempReal > 0.0:
                    corr = (sumXY - ((sumX * sumY) / timeperiod)) / np.sqrt(tempReal)
                else:
                    corr = 0.0
                    
                # 保存结果到对应的有效索引位置
                result_idx = valid_indices[today]
                result[result_idx, sec] = corr
                
                today += 1

        return result



    @staticmethod
    @nb.njit
    def DX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        unstable_period = 25  # TA-Lib default unstable period for DX
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            lookback_total = timeperiod + unstable_period if timeperiod > 1 else 2
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize variables
            prev_minus_dm = 0.0
            prev_plus_dm = 0.0
            prev_tr = 0.0
            dx_values = np.zeros(len(valid_high))
        
            # Initialize first point
            prev_high = valid_high[0]
            prev_low = valid_low[0]
            prev_close = valid_close[0]
        
            # First loop: Initialize cumulative values for MinusDM, PlusDM, and TR
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
        
            # Second loop: Handle unstable period
            for i in range(timeperiod, timeperiod + unstable_period + 1):
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
        
            # Calculate first DX value
            start_idx = timeperiod + unstable_period
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
    def HT_DCPHASE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)

        # TA-Lib constants
        a = 0.0962
        b = 0.5769
        temp_real = np.arctan(1.0)
        rad2deg = 45.0 / temp_real
        const_deg2rad_by360 = temp_real * 8.0
        lookback_total = 63  # As per TA-Lib HT_DCPHASE lookback
        smooth_price_size = 50  # Size from TA-Lib C code

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:  # Not NaN
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
            output = np.array([np.float64(np.nan)] * len(valid_close))
        
            # Initialize variables for price smoother (weighted moving average)
            trailing_wma_idx = 0
            today = trailing_wma_idx
            period_wma_sub = 0.0
            period_wma_sum = 0.0
            trailing_wma_value = 0.0
        
            # Initial WMA setup for first 3 points
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
        
            # Process next 34 points for WMA as per TA-Lib
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
        
            # Initialize Hilbert Transform variables
            hilbert_idx = 0
            
            # Hilbert variables for each component
            detrender_odd = np.zeros(3)
            detrender_even = np.zeros(3)
            detrender = 0.0
            prev_detrender_odd = 0.0
            prev_detrender_even = 0.0
            prev_detrender_input_odd = 0.0
            prev_detrender_input_even = 0.0
            
            q1_odd = np.zeros(3)
            q1_even = np.zeros(3)
            q1 = 0.0
            prev_q1_odd = 0.0
            prev_q1_even = 0.0
            prev_q1_input_odd = 0.0
            prev_q1_input_even = 0.0
            
            ji_odd = np.zeros(3)
            ji_even = np.zeros(3)
            ji = 0.0
            prev_ji_odd = 0.0
            prev_ji_even = 0.0
            prev_ji_input_odd = 0.0
            prev_ji_input_even = 0.0
            
            jq_odd = np.zeros(3)
            jq_even = np.zeros(3)
            jq = 0.0
            prev_jq_odd = 0.0
            prev_jq_even = 0.0
            prev_jq_input_odd = 0.0
            prev_jq_input_even = 0.0
            
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
            
            # Initialize smoothPrice circular buffer
            smooth_price = np.zeros(smooth_price_size)
            smooth_price_idx = 0
            dc_phase = 0.0
        
            # Main loop for calculating the dominant cycle phase
            while today < len(valid_close):
                adjusted_prev_period = (0.075 * period) + 0.54
                today_value = valid_close[today]
            
                # Update WMA
                period_wma_sub += today_value
                period_wma_sub -= trailing_wma_value
                period_wma_sum += today_value * 4.0
                if trailing_wma_idx < len(valid_close):
                    trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
            
                # Store smoothed value in circular buffer
                smooth_price[smooth_price_idx] = smoothed_value
            
                # Hilbert Transform calculations based on whether index is even/odd
                if (today % 2) == 0:
                    # Even index processing - Using DO_HILBERT_EVEN macro logic
                    
                    # DO_HILBERT_EVEN for detrender
                    hilbert_temp_real = a * smoothed_value
                    detrender = -detrender_even[hilbert_idx]
                    detrender_even[hilbert_idx] = hilbert_temp_real
                    detrender += hilbert_temp_real
                    detrender -= prev_detrender_even
                    prev_detrender_even = b * prev_detrender_input_even
                    detrender += prev_detrender_even
                    prev_detrender_input_even = smoothed_value
                    detrender *= adjusted_prev_period
                    
                    # DO_HILBERT_EVEN for Q1
                    hilbert_temp_real = a * detrender
                    q1 = -q1_even[hilbert_idx]
                    q1_even[hilbert_idx] = hilbert_temp_real
                    q1 += hilbert_temp_real
                    q1 -= prev_q1_even
                    prev_q1_even = b * prev_q1_input_even
                    q1 += prev_q1_even
                    prev_q1_input_even = detrender
                    q1 *= adjusted_prev_period
                    
                    # DO_HILBERT_EVEN for jI
                    hilbert_temp_real = a * i1_for_even_prev3
                    ji = -ji_even[hilbert_idx]
                    ji_even[hilbert_idx] = hilbert_temp_real
                    ji += hilbert_temp_real
                    ji -= prev_ji_even
                    prev_ji_even = b * prev_ji_input_even
                    ji += prev_ji_even
                    prev_ji_input_even = i1_for_even_prev3
                    ji *= adjusted_prev_period
                    
                    # DO_HILBERT_EVEN for jQ
                    hilbert_temp_real = a * q1
                    jq = -jq_even[hilbert_idx]
                    jq_even[hilbert_idx] = hilbert_temp_real
                    jq += hilbert_temp_real
                    jq -= prev_jq_even
                    prev_jq_even = b * prev_jq_input_even
                    jq += prev_jq_even
                    prev_jq_input_even = q1
                    jq *= adjusted_prev_period
                    
                    hilbert_idx = (hilbert_idx + 1) % 3
                    
                    q2 = (0.2 * (q1 + ji)) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_even_prev3 - jq)) + (0.8 * prev_i2)
                    
                    # Save for odd processing
                    i1_for_odd_prev3 = i1_for_odd_prev2
                    i1_for_odd_prev2 = detrender
                    
                else:
                    # Odd index processing - Using DO_HILBERT_ODD macro logic
                    
                    # DO_HILBERT_ODD for detrender
                    hilbert_temp_real = a * smoothed_value
                    detrender = -detrender_odd[hilbert_idx]
                    detrender_odd[hilbert_idx] = hilbert_temp_real
                    detrender += hilbert_temp_real
                    detrender -= prev_detrender_odd
                    prev_detrender_odd = b * prev_detrender_input_odd
                    detrender += prev_detrender_odd
                    prev_detrender_input_odd = smoothed_value
                    detrender *= adjusted_prev_period
                    
                    # DO_HILBERT_ODD for Q1
                    hilbert_temp_real = a * detrender
                    q1 = -q1_odd[hilbert_idx]
                    q1_odd[hilbert_idx] = hilbert_temp_real
                    q1 += hilbert_temp_real
                    q1 -= prev_q1_odd
                    prev_q1_odd = b * prev_q1_input_odd
                    q1 += prev_q1_odd
                    prev_q1_input_odd = detrender
                    q1 *= adjusted_prev_period
                    
                    # DO_HILBERT_ODD for jI
                    hilbert_temp_real = a * i1_for_odd_prev3
                    ji = -ji_odd[hilbert_idx]
                    ji_odd[hilbert_idx] = hilbert_temp_real
                    ji += hilbert_temp_real
                    ji -= prev_ji_odd
                    prev_ji_odd = b * prev_ji_input_odd
                    ji += prev_ji_odd
                    prev_ji_input_odd = i1_for_odd_prev3
                    ji *= adjusted_prev_period
                    
                    # DO_HILBERT_ODD for jQ
                    hilbert_temp_real = a * q1
                    jq = -jq_odd[hilbert_idx]
                    jq_odd[hilbert_idx] = hilbert_temp_real
                    jq += hilbert_temp_real
                    jq -= prev_jq_odd
                    prev_jq_odd = b * prev_jq_input_odd
                    jq += prev_jq_odd
                    prev_jq_input_odd = q1
                    jq *= adjusted_prev_period
                    
                    q2 = (0.2 * (q1 + ji)) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_odd_prev3 - jq)) + (0.8 * prev_i2)
                    
                    # Save for even processing
                    i1_for_even_prev3 = i1_for_even_prev2
                    i1_for_even_prev2 = detrender
                
                # Adjust the period for next price bar
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
            
                # Calculate Dominant Cycle Phase
                dc_period = smooth_period + 0.5
                dc_period_int = int(dc_period)
                real_part = 0.0
                imag_part = 0.0
                
                # Calculate using smoothPrice circular buffer
                idx = smooth_price_idx
                for i in range(dc_period_int):
                    temp_real = (i * const_deg2rad_by360) / dc_period_int
                    temp_real2 = smooth_price[idx]
                    real_part += np.sin(temp_real) * temp_real2
                    imag_part += np.cos(temp_real) * temp_real2
                    
                    # Move idx backward in circular buffer
                    if idx == 0:
                        idx = smooth_price_size - 1
                    else:
                        idx -= 1
            
                # Calculate DCPhase
                temp_real = np.abs(imag_part)
                if temp_real > 0.0:
                    dc_phase = np.arctan(real_part / imag_part) * rad2deg
                elif temp_real <= 0.01:
                    if real_part < 0.0:
                        dc_phase -= 90.0
                    elif real_part > 0.0:
                        dc_phase += 90.0
                        
                dc_phase += 90.0
                
                # Compensate for one bar lag of the weighted moving average
                dc_phase += 360.0 / smooth_period
                if imag_part < 0.0:
                    dc_phase += 180.0
                if dc_phase > 315.0:
                    dc_phase -= 360.0
            
                # Store output if beyond lookback period
                if today >= lookback_total:
                    output[today] = dc_phase
            
                # Update circular buffer index
                smooth_price_idx = (smooth_price_idx + 1) % smooth_price_size
                today += 1
        
            # Map results back to original array
            output_idx = 0
            for i in range(len(valid_indices)):
                if valid_indices[i] >= lookback_total:
                    result[valid_indices[i], sec] = output[i]

        return result



    @staticmethod
    @nb.njit
    def HT_TRENDLINE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        lookback_total = 63  # As per C source code

        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True

            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue

            # Extract valid data
            valid_close = close[valid_mask, sec]
            output = np.array([np.float64(np.nan)] * len(valid_close))

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

            # WMA for first 34 periods
            i = 34
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
            smooth_price = np.zeros(7)  # Size as per typical implementation
            smooth_price_idx = 0
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
            i_trend1 = 0.0
            i_trend2 = 0.0
            i_trend3 = 0.0
            rad2deg = 45.0 / np.arctan(1.0)

            while today < len(valid_close):
                adjusted_prev_period = (0.075 * period) + 0.54
                today_value = valid_close[today]
                period_wma_sub += today_value
                period_wma_sub -= trailing_wma_value
                period_wma_sum += today_value * 4.0
                trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub

                smooth_price[smooth_price_idx] = smoothed_value

                if (today % 2) == 0:
                    # Even index processing
                    detrender_even[hilbert_idx] = (0.091 * smooth_price[(smooth_price_idx - 6) % 7]) + (0.369 * smooth_price[(smooth_price_idx - 4) % 7]) - (0.73 * smooth_price[(smooth_price_idx - 2) % 7]) + (0.27 * smooth_price[smooth_price_idx])
                    q1_even[hilbert_idx] = (0.27 * detrender_even[hilbert_idx]) + (0.73 * detrender_even[(hilbert_idx - 1) % 3]) - (0.369 * detrender_even[(hilbert_idx - 2) % 3]) - (0.091 * detrender_even[(hilbert_idx + 1) % 3])
                    ji_even[hilbert_idx] = (0.27 * i1_for_even_prev3) + (0.73 * i1_for_even_prev2) - (0.369 * detrender_even[(hilbert_idx - 2) % 3]) - (0.091 * detrender_even[(hilbert_idx + 1) % 3])
                    jq_even[hilbert_idx] = (0.091 * q1_even[(hilbert_idx + 1) % 3]) + (0.369 * q1_even[(hilbert_idx - 2) % 3]) - (0.73 * q1_even[(hilbert_idx - 1) % 3]) + (0.27 * q1_even[hilbert_idx])
                    if hilbert_idx == 2:
                        hilbert_idx = 0
                    else:
                        hilbert_idx += 1
                    q2 = (0.2 * (q1_even[(hilbert_idx - 1) % 3] + ji_even[(hilbert_idx - 1) % 3])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_even_prev3 - jq_even[(hilbert_idx - 1) % 3])) + (0.8 * prev_i2)
                    i1_for_odd_prev3 = i1_for_odd_prev2
                    i1_for_odd_prev2 = detrender_even[(hilbert_idx - 1) % 3]
                else:
                    # Odd index processing
                    detrender_odd[hilbert_idx] = (0.091 * smooth_price[(smooth_price_idx - 6) % 7]) + (0.369 * smooth_price[(smooth_price_idx - 4) % 7]) - (0.73 * smooth_price[(smooth_price_idx - 2) % 7]) + (0.27 * smooth_price[smooth_price_idx])
                    q1_odd[hilbert_idx] = (0.27 * detrender_odd[hilbert_idx]) + (0.73 * detrender_odd[(hilbert_idx - 1) % 3]) - (0.369 * detrender_odd[(hilbert_idx - 2) % 3]) - (0.091 * detrender_odd[(hilbert_idx + 1) % 3])
                    ji_odd[hilbert_idx] = (0.27 * i1_for_odd_prev3) + (0.73 * i1_for_odd_prev2) - (0.369 * detrender_odd[(hilbert_idx - 2) % 3]) - (0.091 * detrender_odd[(hilbert_idx + 1) % 3])
                    jq_odd[hilbert_idx] = (0.091 * q1_odd[(hilbert_idx + 1) % 3]) + (0.369 * q1_odd[(hilbert_idx - 2) % 3]) - (0.73 * q1_odd[(hilbert_idx - 1) % 3]) + (0.27 * q1_odd[hilbert_idx])
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
                    output[today] = temp_real2

                smooth_price_idx = (smooth_price_idx + 1) % 7
                today += 1

            # Map results back to original array
            for i in range(len(valid_indices)):
                if valid_indices[i] >= lookback_total and i < len(output):
                    result[valid_indices[i], sec] = output[i]

        return result



    @staticmethod
    @nb.njit
    def LINEARREG(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib
        lookback_total = timeperiod - 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Pre-calculate constants for linear regression
            sum_x = timeperiod * (timeperiod - 1) * 0.5
            sum_x_sqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            divisor = sum_x * sum_x - timeperiod * sum_x_sqr
        
            # Start calculation from the point where we have enough data
            start_idx = lookback_total
            for i in range(start_idx, len(valid_close)):
                sum_xy = 0.0
                sum_y = 0.0
            
                # Calculate sums for linear regression
                for j in range(timeperiod):
                    temp_value = valid_close[i - j]
                    sum_y += temp_value
                    sum_xy += j * temp_value
            
                # Calculate slope (m) and intercept (b)
                m = (timeperiod * sum_xy - sum_x * sum_y) / divisor
                b = (sum_y - m * sum_x) / timeperiod
            
                # Calculate the regression value at the last point
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
        
            # 初始化输出数组
            angle_values = np.zeros(len(valid_close))
        
            # 预计算常数
            SumX = timeperiod * (timeperiod - 1) * 0.5
            SumXSqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            Divisor = SumX * SumX - timeperiod * SumXSqr
        
            # 主计算循环
            for today in range(timeperiod - 1, len(valid_close)):
                SumXY = 0.0
                SumY = 0.0
                for i in range(timeperiod):
                    tempValue = valid_close[today - i]
                    SumY += tempValue
                    SumXY += i * tempValue
            
                # 计算斜率 m
                if Divisor != 0:
                    m = (timeperiod * SumXY - SumX * SumY) / Divisor
                    # 计算角度（弧度转角度）
                    angle_values[today] = np.arctan(m) * (180.0 / np.pi)
                else:
                    angle_values[today] = 0.0
        
            # 映射结果回原始数组
            for i in range(timeperiod - 1, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = angle_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def LINEARREG_INTERCEPT(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
        
            # 计算线性回归截距
            SumX = timeperiod * (timeperiod - 1) * 0.5
            SumXSqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            Divisor = SumX * SumX - timeperiod * SumXSqr
        
            # 开始计算线性回归截距
            start_idx = timeperiod - 1
            for i in range(start_idx, len(valid_close)):
                SumXY = 0.0
                SumY = 0.0
                for j in range(timeperiod):
                    tempValue = valid_close[i - j]
                    SumY += tempValue
                    SumXY += j * tempValue
            
                # 计算斜率 m
                m = (timeperiod * SumXY - SumX * SumY) / Divisor
                # 计算截距
                intercept = (SumY - m * SumX) / timeperiod
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = intercept
    
        return result



    @staticmethod
    @nb.njit
    def LINEARREG_SLOPE(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib
        lookback_total = timeperiod - 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Pre-calculate constants as per C source
            sum_x = timeperiod * (timeperiod - 1) * 0.5
            sum_x_sqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            divisor = sum_x * sum_x - timeperiod * sum_x_sqr
        
            # Calculate slope for each valid position
            slope_values = np.zeros(len(valid_close))
            start_idx = lookback_total
        
            for today in range(start_idx, len(valid_close)):
                sum_xy = 0.0
                sum_y = 0.0
                for i in range(timeperiod):
                    temp_value = valid_close[today - i]
                    sum_y += temp_value
                    sum_xy += i * temp_value
            
                if divisor != 0:
                    slope_values[today] = (timeperiod * sum_xy - sum_x * sum_y) / divisor
                else:
                    slope_values[today] = 0.0
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = slope_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MACDEXT(high, open, low, close, vol, oi, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
        tdts, secs = close.shape
        result_macd = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_signal = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_hist = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Swap fast and slow periods if necessary
        if slowperiod < fastperiod:
            temp_period = slowperiod
            slowperiod = fastperiod
            fastperiod = temp_period
            temp_matype = slowmatype
            slowmatype = fastmatype
            fastmatype = temp_matype
    
        # Calculate lookback periods for MA functions (simplified as max periods)
        lookback_fast = fastperiod - 1
        lookback_slow = slowperiod - 1
        lookback_largest = max(lookback_fast, lookback_slow)
        lookback_signal = signalperiod - 1
        lookback_total = lookback_signal + lookback_largest
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Allocate temporary buffers for fast and slow MA
            temp_size = len(valid_close)
            fast_ma_buffer = np.zeros(temp_size)
            slow_ma_buffer = np.zeros(temp_size)
        
            # Compute Fast MA
            if fastmatype == 0:  # SMA
                for i in range(fastperiod - 1, temp_size):
                    if i >= fastperiod - 1:
                        sum_val = 0.0
                        for j in range(i - fastperiod + 1, i + 1):
                            sum_val += valid_close[j]
                        fast_ma_buffer[i] = sum_val / fastperiod
            else:  # EMA as default fallback
                alpha = 2.0 / (fastperiod + 1)
                for i in range(temp_size):
                    if i == 0:
                        fast_ma_buffer[i] = valid_close[i]
                    else:
                        fast_ma_buffer[i] = alpha * valid_close[i] + (1 - alpha) * fast_ma_buffer[i - 1]
        
            # Compute Slow MA
            if slowmatype == 0:  # SMA
                for i in range(slowperiod - 1, temp_size):
                    if i >= slowperiod - 1:
                        sum_val = 0.0
                        for j in range(i - slowperiod + 1, i + 1):
                            sum_val += valid_close[j]
                        slow_ma_buffer[i] = sum_val / slowperiod
            else:  # EMA as default fallback
                alpha = 2.0 / (slowperiod + 1)
                for i in range(temp_size):
                    if i == 0:
                        slow_ma_buffer[i] = valid_close[i]
                    else:
                        slow_ma_buffer[i] = alpha * valid_close[i] + (1 - alpha) * slow_ma_buffer[i - 1]
        
            # Compute MACD Line (Fast MA - Slow MA)
            macd_buffer = np.zeros(temp_size)
            for i in range(temp_size):
                macd_buffer[i] = fast_ma_buffer[i] - slow_ma_buffer[i]
        
            # Compute Signal Line
            signal_buffer = np.zeros(temp_size)
            if signalmatype == 0:  # SMA
                for i in range(signalperiod - 1, temp_size):
                    if i >= signalperiod - 1:
                        sum_val = 0.0
                        for j in range(i - signalperiod + 1, i + 1):
                            sum_val += macd_buffer[j]
                        signal_buffer[i] = sum_val / signalperiod
            else:  # EMA as default fallback
                alpha = 2.0 / (signalperiod + 1)
                for i in range(temp_size):
                    if i == 0:
                        signal_buffer[i] = macd_buffer[i]
                    else:
                        signal_buffer[i] = alpha * macd_buffer[i] + (1 - alpha) * signal_buffer[i - 1]
        
            # Compute Histogram
            hist_buffer = np.zeros(temp_size)
            for i in range(temp_size):
                hist_buffer[i] = macd_buffer[i] - signal_buffer[i]
        
            # Map results back to original array
            start_idx = lookback_total
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result_macd[orig_idx, sec] = macd_buffer[i]
                if i >= lookback_total:
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
            # Create mask for valid data
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_close = close[valid_mask, sec]
            valid_indices = np.where(valid_mask)[0]
        
            # Check if there is enough data
            if len(valid_close) < 34 + signalperiod - 1:  # Lookback period for MACD FIX
                continue
        
            # Initialize arrays for EMA calculations
            ema12 = np.zeros(len(valid_close))
            ema26 = np.zeros(len(valid_close))
            macd_line = np.zeros(len(valid_close))
            signal_line = np.zeros(len(valid_close))
            hist_line = np.zeros(len(valid_close))
        
            # EMA12 and EMA26 coefficients (fixed for MACDFIX)
            k12 = 2.0 / (12.0 + 1.0)
            k26 = 2.0 / (26.0 + 1.0)
        
            # Calculate EMA12 and EMA26
            for i in range(len(valid_close)):
                if i == 0:
                    ema12[i] = valid_close[i]
                    ema26[i] = valid_close[i]
                else:
                    ema12[i] = valid_close[i] * k12 + ema12[i-1] * (1.0 - k12)
                    ema26[i] = valid_close[i] * k26 + ema26[i-1] * (1.0 - k26)
        
            # Calculate MACD Line (difference between EMA12 and EMA26)
            for i in range(len(valid_close)):
                macd_line[i] = ema12[i] - ema26[i]
        
            # Calculate Signal Line (EMA of MACD Line)
            k_signal = 2.0 / (signalperiod + 1.0)
            for i in range(len(valid_close)):
                if i == 0:
                    signal_line[i] = macd_line[i]
                else:
                    signal_line[i] = macd_line[i] * k_signal + signal_line[i-1] * (1.0 - k_signal)
        
            # Calculate Histogram (difference between MACD Line and Signal Line)
            for i in range(len(valid_close)):
                hist_line[i] = macd_line[i] - signal_line[i]
        
            # Map results back to original array
            start_idx = 33  # TA-Lib MACD output starts after lookback period
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result_macd[orig_idx, sec] = macd_line[i]
                result_signal[orig_idx, sec] = signal_line[i]
                result_hist[orig_idx, sec] = hist_line[i]
    
        return result_macd, result_signal, result_hist



    @staticmethod
    @nb.njit
    def MAXINDEX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if high[i, sec] == high[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < timeperiod:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
        
            # 初始化输出数组
            maxindex_values = np.zeros(len(valid_high))
        
            # 计算lookback期
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
                    while i + 1 <= today:
                        i += 1
                        tmp_val = valid_high[i]
                        if tmp_val > highest:
                            highest_idx = i
                            highest = tmp_val
                elif tmp >= highest:
                    highest_idx = today
                    highest = tmp
                
                maxindex_values[out_idx] = highest_idx
                out_idx += 1
                trailing_idx += 1
                today += 1
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
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
            # Create a mask for valid data points
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            # Get indices of valid data
            valid_indices = np.where(valid_mask)[0]
        
            # If no valid data, skip to next security
            if len(valid_indices) == 0:
                continue
        
            # Extract valid high and low data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Calculate median price as (high + low) / 2
            medprice_values = np.zeros(len(valid_high))
            for i in range(len(valid_high)):
                medprice_values[i] = (valid_high[i] + valid_low[i]) / 2.0
        
            # Map results back to original array
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
        lookback_total = timeperiod + unstable_period
    
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
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
            valid_vol = vol[valid_mask, sec]
        
            # Initialize output array for this security
            mfi_values = np.zeros(len(valid_high))
        
            # Initialize circular buffer simulation for positive and negative money flow
            pos_mf_buffer = np.zeros(timeperiod)
            neg_mf_buffer = np.zeros(timeperiod)
            buffer_idx = 0
        
            # Initialize sums
            pos_sum_mf = 0.0
            neg_sum_mf = 0.0
        
            # Start from the first valid point
            today = 0
            prev_value = (valid_high[today] + valid_low[today] + valid_close[today]) / 3.0
            today += 1
        
            # First loop: Initialize the buffer with first timeperiod values
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
        
            # Check if we can output the first value after lookback
            start_idx = lookback_total
            if today > start_idx:
                temp_value1 = pos_sum_mf + neg_sum_mf
                if temp_value1 < 1.0:
                    mfi_values[start_idx] = 0.0
                else:
                    mfi_values[start_idx] = 100.0 * (pos_sum_mf / temp_value1)
        
            # Second loop: Process data until start_idx if not reached
            while today < start_idx and today < len(valid_high):
                # Remove oldest values from sums
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
        
            # Main loop: Process remaining data
            while today < len(valid_high):
                # Remove oldest values from sums
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
                
                temp_value1 = pos_sum_mf + neg_sum_mf
                if temp_value1 < 1.0:
                    mfi_values[today - 1] = 0.0
                else:
                    mfi_values[today - 1] = 100.0 * (pos_sum_mf / temp_value1)
                
                buffer_idx = (buffer_idx + 1) % timeperiod
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = mfi_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MIDPOINT(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per C source code
        nb_initial_element_needed = timeperiod - 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= nb_initial_element_needed:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Initialize output array for valid data
            midpoint_values = np.zeros(len(valid_high))
        
            # Start index for output as per C source code
            start_idx = nb_initial_element_needed
        
            # Compute midpoint for each valid data point starting from start_idx
            for today in range(start_idx, len(valid_high)):
                trailing_idx = today - nb_initial_element_needed
                lowest = valid_low[trailing_idx]
                highest = valid_high[trailing_idx]
            
                # Find highest and lowest in the window
                for i in range(trailing_idx + 1, today + 1):
                    tmp_high = valid_high[i]
                    tmp_low = valid_low[i]
                    if tmp_low < lowest:
                        lowest = tmp_low
                    if tmp_high > highest:
                        highest = tmp_high
            
                # Compute midpoint
                midpoint_values[today] = (highest + lowest) / 2.0
        
            # Map results back to original array
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = midpoint_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MIDPRICE(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per C source code
        lookback = timeperiod - 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # Initialize output array for valid data
            midprice_values = np.zeros(len(valid_high))
        
            # Start index for output as per C source code
            start_idx = lookback
        
            # Compute midprice for each valid point after lookback
            for today in range(start_idx, len(valid_high)):
                trailing_idx = today - lookback
                lowest = valid_low[trailing_idx]
                highest = valid_high[trailing_idx]
            
                # Find min and max over the timeperiod window
                for i in range(trailing_idx + 1, today + 1):
                    tmp_low = valid_low[i]
                    if tmp_low < lowest:
                        lowest = tmp_low
                    tmp_high = valid_high[i]
                    if tmp_high > highest:
                        highest = tmp_high
            
                # Calculate midprice as per C source code
                midprice_values[today] = (highest + lowest) / 2.0
        
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
        
            # 初始化输出数组
            minindex_values = np.zeros(len(valid_close))
        
            # 计算lookback期
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed if nb_initial_element_needed < len(valid_close) else len(valid_close) - 1
        
            if start_idx >= len(valid_close):
                continue
            
            out_idx = 0
            today = start_idx
            trailing_idx = start_idx - nb_initial_element_needed
            lowest_idx = -1
            lowest = 0.0
        
            while today < len(valid_close):
                tmp = valid_close[today]
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_close[lowest_idx]
                    i = lowest_idx
                    while i <= today:
                        tmp_val = valid_close[i]
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
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = minindex_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MINMAX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result_max = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_min = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        nb_initial_element_needed = timeperiod - 1
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= nb_initial_element_needed:
                continue
            
            valid_close = close[valid_mask, sec]
            out_max = np.zeros(len(valid_close))
            out_min = np.zeros(len(valid_close))
            out_idx = 0
            today = nb_initial_element_needed
            trailing_idx = 0
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
                    while i < today + 1:
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
                    while i < today + 1:
                        tmp_low = valid_close[i]
                        if tmp_low < lowest:
                            lowest_idx = i
                            lowest = tmp_low
                        i += 1
                elif tmp_low <= lowest:
                    lowest_idx = today
                    lowest = tmp_low
                
                out_max[out_idx] = highest
                out_min[out_idx] = lowest
                out_idx += 1
                trailing_idx += 1
                today += 1
        
            # 映射结果回原始数组
            for i in range(nb_initial_element_needed, len(valid_indices)):
                orig_idx = valid_indices[i]
                result_max[orig_idx, sec] = out_max[i - nb_initial_element_needed]
                result_min[orig_idx, sec] = out_min[i - nb_initial_element_needed]
    
        return result_max, result_min



    @staticmethod
    @nb.njit
    def MINMAXINDEX(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result_max = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_min = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
        
            # 初始化输出数组
            out_max_idx = np.zeros(len(valid_close))
            out_min_idx = np.zeros(len(valid_close))
        
            # 计算lookback期
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed if nb_initial_element_needed < len(valid_close) else len(valid_close) - 1
        
            if start_idx >= len(valid_close):
                continue
            
            out_idx = 0
            today = start_idx
            trailing_idx = today - nb_initial_element_needed
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
                    while i + 1 <= today:
                        i += 1
                        tmp_high = valid_close[i]
                        if tmp_high > highest:
                            highest_idx = i
                            highest = tmp_high
                elif tmp_high >= highest:
                    highest_idx = today
                    highest = tmp_high
                
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_close[lowest_idx]
                    i = lowest_idx
                    while i + 1 <= today:
                        i += 1
                        tmp_low = valid_close[i]
                        if tmp_low < lowest:
                            lowest_idx = i
                            lowest = tmp_low
                elif tmp_low <= lowest:
                    lowest_idx = today
                    lowest = tmp_low
                
                out_max_idx[out_idx] = highest_idx
                out_min_idx[out_idx] = lowest_idx
                out_idx += 1
                trailing_idx += 1
                today += 1
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
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
            lookback_total = timeperiod + unstable_period if timeperiod > 1 else 1
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for this security
            minus_di_values = np.zeros(len(valid_high))
        
            if timeperiod <= 1:
                # Special case for timeperiod = 1
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
                # Normal case for timeperiod > 1
                prev_minus_dm = 0.0
                prev_tr = 0.0
                prev_high = valid_high[0]
                prev_low = valid_low[0]
                prev_close = valid_close[0]
            
                # First loop: Initialize MinusDM and TR sums
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
                
                    tr = max(valid_high[i] - valid_low[i], 
                            max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                    prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                    prev_close = valid_close[i]
            
                # Set first output value after lookback period
                start_idx = lookback_total
                if start_idx - 1 < len(valid_high):
                    if prev_tr > 1e-10:
                        minus_di_values[start_idx - 1] = 100.0 * (prev_minus_dm / prev_tr)
                    else:
                        minus_di_values[start_idx - 1] = 0.0
            
                # Main loop: Calculate remaining Minus DI values
                for i in range(start_idx, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    prev_minus_dm -= prev_minus_dm / timeperiod
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
            start_idx = lookback_total if timeperiod > 1 else 1
            for i in range(start_idx - 1, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = minus_di_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MINUS_DM(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        unstable_period = 25  # TA-Lib默认不稳定期 for MinusDM
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod + unstable_period - 1:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # 计算lookbackTotal
            if timeperiod > 1:
                lookback_total = timeperiod + unstable_period - 1
            else:
                lookback_total = 1
            
            # 初始化输出数组
            minus_dm_values = np.zeros(len(valid_high))
        
            # 特殊情况：timeperiod <= 1
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
                # 映射结果回原始数组
                for i in range(lookback_total, len(valid_indices)):
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = minus_dm_values[i]
                continue
        
            # 正常情况：timeperiod > 1
            # 初始化阶段
            prev_minus_dm = 0.0
            prev_high = valid_high[0]
            prev_low = valid_low[0]
        
            # 第一个循环：初始化MinusDM的累计值
            for i in range(1, timeperiod):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm += diff_m
        
            # 第二个循环：处理不稳定期
            for i in range(timeperiod, timeperiod + unstable_period):
                if i >= len(valid_high):
                    break
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm = prev_minus_dm - (prev_minus_dm / timeperiod) + diff_m
                else:
                    prev_minus_dm = prev_minus_dm - (prev_minus_dm / timeperiod)
        
            # 记录第一个输出值
            if timeperiod + unstable_period - 1 < len(valid_high):
                minus_dm_values[timeperiod + unstable_period - 1] = prev_minus_dm
        
            # 主循环：计算剩余的MinusDM值
            for i in range(timeperiod + unstable_period, len(valid_high)):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                if diff_m > 0 and diff_p < diff_m:
                    prev_minus_dm = prev_minus_dm - (prev_minus_dm / timeperiod) + diff_m
                else:
                    prev_minus_dm = prev_minus_dm - (prev_minus_dm / timeperiod)
                minus_dm_values[i] = prev_minus_dm
        
            # 映射结果回原始数组
            for i in range(lookback_total, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = minus_dm_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def MOM(high, open, low, close, vol, oi, timeperiod=10):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
        
            # 计算MOM值
            mom_values = np.zeros(len(valid_close))
            for i in range(timeperiod, len(valid_close)):
                mom_values[i] = valid_close[i] - valid_close[i - timeperiod]
        
            # 映射结果回原始数组，起始索引为timeperiod
            for i in range(timeperiod, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = mom_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def NATR(high, open, low, close, vol, oi, timeperiod=14):
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
            if len(valid_indices) < timeperiod:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 计算TR (True Range)
            tr_values = np.zeros(len(valid_high))
            tr_values[0] = valid_high[0] - valid_low[0]
            for i in range(1, len(valid_high)):
                tr_1 = valid_high[i] - valid_low[i]
                tr_2 = abs(valid_close[i-1] - valid_high[i])
                tr_3 = abs(valid_close[i-1] - valid_low[i])
                tr_values[i] = max(tr_1, tr_2, tr_3)
        
            # 处理timeperiod=1的特殊情况，直接返回TR
            if timeperiod <= 1:
                for i in range(len(valid_indices)):
                    orig_idx = valid_indices[i]
                    if close[orig_idx, sec] > 1e-10:
                        result[orig_idx, sec] = (tr_values[i] / close[orig_idx, sec]) * 100.0
                    else:
                        result[orig_idx, sec] = 0.0
                continue
        
            # 计算ATR初始值
            atr_values = np.zeros(len(valid_high))
            first_atr = 0.0
            for i in range(timeperiod):
                first_atr += tr_values[i]
            first_atr /= timeperiod
            atr_values[timeperiod-1] = first_atr
        
            # 使用Wilder平滑计算后续ATR
            for i in range(timeperiod, len(valid_high)):
                atr_values[i] = (atr_values[i-1] * (timeperiod - 1) + tr_values[i]) / timeperiod
        
            # 处理不稳定期 (TA-Lib默认不稳定期为timeperiod)
            unstable_period = timeperiod
            start_idx = timeperiod - 1 + unstable_period
        
            # 计算NATR = (ATR / Close) * 100
            for i in range(start_idx, len(valid_high)):
                orig_idx = valid_indices[i]
                if valid_close[i] > 1e-10:
                    result[orig_idx, sec] = (atr_values[i] / valid_close[i]) * 100.0
                else:
                    result[orig_idx, sec] = 0.0
    
        return result



    @staticmethod
    @nb.njit
    def OBV(high, open, low, close, vol, oi):
        """
        OBV - On Balance Volume
        OBV是一个累积成交量指标，根据价格变动方向累加或减去成交量。
        计算方法：如果当日收盘价高于前一日，则累加当日成交量；如果低于前一日，则减去当日成交量。
        用途：用于衡量资金流入和流出，预测价格趋势。
        """
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (close[i, sec] == close[i, sec] and 
                    vol[i, sec] == vol[i, sec]):
                    valid_mask[i] = True
        
            # 获取有效数据的索引
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) < 1:  # 需要至少一个数据点
                continue
        
            # 提取有效数据
            valid_close = close[valid_mask, sec]
            valid_vol = vol[valid_mask, sec]
        
            # 初始化OBV值
            obv_values = np.zeros(len(valid_close))
            if len(valid_close) > 0:
                obv_values[0] = valid_vol[0]
                prev_close = valid_close[0]
            
                # 主计算循环，严格遵循C源码逻辑
                for i in range(1, len(valid_close)):
                    current_close = valid_close[i]
                    if current_close > prev_close:
                        obv_values[i] = obv_values[i-1] + valid_vol[i]
                    elif current_close < prev_close:
                        obv_values[i] = obv_values[i-1] - valid_vol[i]
                    else:
                        obv_values[i] = obv_values[i-1]
                    prev_close = current_close
        
            # 将结果映射回原始数组
            # TA-Lib从第一个有效数据点开始输出OBV
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
        
            # Initialize output array for this security
            plus_di_values = np.zeros(len(valid_high))
        
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
                
                    if diff_p > 0 and diff_p > diff_m:
                        # True Range calculation
                        tr = max(valid_high[i] - valid_low[i], 
                                max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                        if tr > 1e-10:
                            plus_di_values[i] = diff_p / tr
                        else:
                            plus_di_values[i] = 0.0
                    else:
                        plus_di_values[i] = 0.0
                    prev_close = valid_close[i]
            else:
                # Normal case with timeperiod > 1
                prev_plus_dm = 0.0
                prev_tr = 0.0
                prev_high = valid_high[0]
                prev_low = valid_low[0]
                prev_close = valid_close[0]
            
                # First loop: Initialize PlusDM and TR sums
                for i in range(1, timeperiod):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    if diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm += diff_p
                
                    # True Range calculation
                    tr = max(valid_high[i] - valid_low[i], 
                            max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                    prev_tr += tr
                    prev_close = valid_close[i]
            
                # Second loop: Handle unstable period
                for i in range(timeperiod, timeperiod + unstable_period):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    if diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod) + diff_p
                    else:
                        prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod)
                
                    # True Range calculation
                    tr = max(valid_high[i] - valid_low[i], 
                            max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                    prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                    prev_close = valid_close[i]
            
                # Set first output value
                start_idx = timeperiod + unstable_period - 1
                if prev_tr > 1e-10:
                    plus_di_values[start_idx] = 100.0 * (prev_plus_dm / prev_tr)
                else:
                    plus_di_values[start_idx] = 0.0
            
                # Main loop: Calculate remaining values
                for i in range(start_idx + 1, len(valid_high)):
                    temp_real = valid_high[i]
                    diff_p = temp_real - prev_high
                    prev_high = temp_real
                
                    temp_real = valid_low[i]
                    diff_m = prev_low - temp_real
                    prev_low = temp_real
                
                    if diff_p > 0 and diff_p > diff_m:
                        prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod) + diff_p
                    else:
                        prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod)
                
                    # True Range calculation
                    tr = max(valid_high[i] - valid_low[i], 
                            max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                    prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                    prev_close = valid_close[i]
                
                    if prev_tr > 1e-10:
                        plus_di_values[i] = 100.0 * (prev_plus_dm / prev_tr)
                    else:
                        plus_di_values[i] = 0.0
        
            # Map results back to original array
            lookback_total = timeperiod + unstable_period - 1 if timeperiod > 1 else 1
            for i in range(lookback_total, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = plus_di_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def PLUS_DM(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        unstable_period = 25  # TA-Lib默认不稳定期 for PLUS_DM
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec]):
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod + unstable_period - 1:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # 计算lookbackTotal
            if timeperiod > 1:
                lookback_total = timeperiod + unstable_period - 1
            else:
                lookback_total = 1
            
            # 初始化输出数组
            plus_dm_values = np.zeros(len(valid_high))
        
            # 特殊情况：timeperiod <= 1
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
                # 映射结果回原始数组
                for i in range(len(valid_indices)):
                    if i >= lookback_total:
                        orig_idx = valid_indices[i]
                        result[orig_idx, sec] = plus_dm_values[i]
                continue
        
            # 正常情况：timeperiod > 1
            # 初始化变量
            prev_plus_dm = 0.0
            prev_high = valid_high[0]
            prev_low = valid_low[0]
        
            # 第一阶段：初始化PlusDM的累加值
            for i in range(1, timeperiod):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                if diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm += diff_p
        
            # 第二阶段：处理不稳定期
            for i in range(timeperiod, timeperiod + unstable_period):
                if i >= len(valid_high):
                    break
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                if diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod) + diff_p
                else:
                    prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod)
        
            # 记录第一个有效输出值
            if timeperiod + unstable_period - 1 < len(valid_high):
                plus_dm_values[timeperiod + unstable_period - 1] = prev_plus_dm
        
            # 第三阶段：主计算循环
            for i in range(timeperiod + unstable_period, len(valid_high)):
                temp_real = valid_high[i]
                diff_p = temp_real - prev_high
                prev_high = temp_real
                temp_real = valid_low[i]
                diff_m = prev_low - temp_real
                prev_low = temp_real
                if diff_p > 0 and diff_p > diff_m:
                    prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod) + diff_p
                else:
                    prev_plus_dm = prev_plus_dm - (prev_plus_dm / timeperiod)
                plus_dm_values[i] = prev_plus_dm
        
            # 映射结果回原始数组
            for i in range(len(valid_indices)):
                if i >= lookback_total:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = plus_dm_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def PPO(high, open, low, close, vol, oi, fastperiod=12, slowperiod=26, matype=0):
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
        
            # 计算快速和慢速移动平均
            fast_ma = np.zeros(len(valid_close))
            slow_ma = np.zeros(len(valid_close))
        
            if matype == 0:  # SMA
                for i in range(fastperiod - 1, len(valid_close)):
                    if i >= fastperiod - 1:
                        fast_ma[i] = np.mean(valid_close[i - fastperiod + 1:i + 1])
                for i in range(slowperiod - 1, len(valid_close)):
                    if i >= slowperiod - 1:
                        slow_ma[i] = np.mean(valid_close[i - slowperiod + 1:i + 1])
            else:  # EMA as default fallback (can be extended for other MA types)
                alpha_fast = 2.0 / (fastperiod + 1)
                alpha_slow = 2.0 / (slowperiod + 1)
                for i in range(len(valid_close)):
                    if i == 0:
                        fast_ma[i] = valid_close[i]
                        slow_ma[i] = valid_close[i]
                    else:
                        fast_ma[i] = alpha_fast * valid_close[i] + (1 - alpha_fast) * fast_ma[i - 1]
                        slow_ma[i] = alpha_slow * valid_close[i] + (1 - alpha_slow) * slow_ma[i - 1]
        
            # 计算PPO值
            ppo_values = np.zeros(len(valid_close))
            start_idx = max(fastperiod, slowperiod) - 1
            for i in range(start_idx, len(valid_close)):
                if slow_ma[i] > 1e-10:  # 避免除零
                    ppo_values[i] = ((fast_ma[i] - slow_ma[i]) / slow_ma[i]) * 100.0
                else:
                    ppo_values[i] = 0.0
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = ppo_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def ROC(high, open, low, close, vol, oi, timeperiod=10):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= timeperiod:
                continue
            
            # 提取有效数据
            valid_close = close[valid_mask, sec]
        
            # 计算ROC值
            roc_values = np.zeros(len(valid_close))
            start_idx = timeperiod
        
            for i in range(start_idx, len(valid_close)):
                trailing_idx = i - timeperiod
                temp_real = valid_close[trailing_idx]
                if temp_real > 1e-10:  # 避免除零
                    roc_values[i] = ((valid_close[i] / temp_real) - 1.0) * 100.0
                else:
                    roc_values[i] = 0.0
        
            # 映射结果回原始数组
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
        
            # 计算ROCP
            rocp_values = np.zeros(len(valid_close))
            start_idx = timeperiod
        
            for i in range(start_idx, len(valid_close)):
                trailing_idx = i - timeperiod
                temp_real = valid_close[trailing_idx]
                if temp_real > 1e-10:  # 避免除零
                    rocp_values[i] = (valid_close[i] - temp_real) / temp_real
                else:
                    rocp_values[i] = 0.0
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = rocp_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def ROCR(high, open, low, close, vol, oi, timeperiod=10):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
        
            # 计算ROCR
            rocr_values = np.zeros(len(valid_close))
            start_idx = timeperiod
        
            for i in range(start_idx, len(valid_close)):
                trailing_idx = i - timeperiod
                temp_real = valid_close[trailing_idx]
                if temp_real != 0.0:
                    rocr_values[i] = valid_close[i] / temp_real
                else:
                    rocr_values[i] = 0.0
        
            # 映射结果回原始数组
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
        
            # 计算ROCR100
            rocr100_values = np.zeros(len(valid_close))
            start_idx = timeperiod
        
            for i in range(start_idx, len(valid_close)):
                trailing_idx = i - timeperiod
                temp_real = valid_close[trailing_idx]
                if temp_real > 1e-10:  # 避免除零
                    rocr100_values[i] = (valid_close[i] / temp_real) * 100.0
                else:
                    rocr100_values[i] = 0.0
        
            # 映射结果回原始数组
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
    def SAR(high, open, low, close, vol, oi, acceleration=0.02, maximum=0.2):
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
            if len(valid_indices) < 2:  # 需要至少2个数据点
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
        
            # 初始化变量
            start_idx = 1  # TA-Lib从第二个点开始计算
            if start_idx >= len(valid_high):
                continue
            
            # 调整加速因子
            af = acceleration
            if af > maximum:
                af = acceleration = maximum
            
            # 初始化SAR计算
            today_idx = start_idx
            new_high = valid_high[today_idx - 1]
            new_low = valid_low[today_idx - 1]
        
            # 确定初始趋势方向
            ep_temp = 0.0
            if valid_low[today_idx] < valid_high[today_idx - 1]:
                is_long = 0
                ep = valid_low[today_idx]
                sar = new_high
            else:
                is_long = 1
                ep = valid_high[today_idx]
                sar = new_low
            
            new_low = valid_low[today_idx]
            new_high = valid_high[today_idx]
            sar_values = np.zeros(len(valid_high))
        
            # 主计算循环
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
                        if out_idx < len(valid_high):
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
                        if out_idx < len(valid_high):
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
                        if out_idx < len(valid_high):
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
                        if out_idx < len(valid_high):
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
        
            # 映射结果回原始数组
            for i in range(out_idx):
                if i + start_idx - 1 < len(valid_indices):
                    orig_idx = valid_indices[i + start_idx - 1]
                    result[orig_idx, sec] = sar_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def SAREXT(high, open, low, close, vol, oi, start_value=0.0, offset_on_reverse=0.0, 
               acceleration_init_long=0.02, acceleration_long=0.02, acceleration_max_long=0.2,
               acceleration_init_short=0.02, acceleration_short=0.02, acceleration_max_short=0.2):
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
            af_long = acceleration_init_long
            af_short = acceleration_init_short
        
            # Cap acceleration factors
            if af_long > acceleration_max_long:
                af_long = acceleration_max_long
            if acceleration_long > acceleration_max_long:
                acceleration_long = acceleration_max_long
            if af_short > acceleration_max_short:
                af_short = acceleration_max_short
            if acceleration_short > acceleration_max_short:
                acceleration_short = acceleration_max_short
            
            # Determine initial position (long or short)
            is_long = 0
            if start_value == 0.0:
                if valid_high[1] - valid_low[1] > 0:
                    is_long = 0
                else:
                    is_long = 1
            elif start_value > 0:
                is_long = 1
            else:
                is_long = 0
            
            # Initialize SAR and EP (Extreme Point)
            today_idx = 1
            new_high = valid_high[0]
            new_low = valid_low[0]
        
            if start_value == 0.0:
                if is_long == 1:
                    ep = valid_high[today_idx]
                    sar = new_low
                else:
                    ep = valid_low[today_idx]
                    sar = new_high
            elif start_value > 0:
                ep = valid_high[today_idx]
                sar = start_value
            else:
                ep = valid_low[today_idx]
                sar = abs(start_value)
            
            # Update new high and low for current position
            new_low = valid_low[today_idx]
            new_high = valid_high[today_idx]
        
            # Initialize output array for valid data
            sar_values = np.zeros(len(valid_high))
        
            # Start from index 1 as per TA-Lib logic
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
                        if offset_on_reverse != 0.0:
                            sar += sar * offset_on_reverse
                        sar_values[out_idx] = -sar
                        out_idx += 1
                        af_short = acceleration_init_short
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
                            af_long += acceleration_long
                            if af_long > acceleration_max_long:
                                af_long = acceleration_max_long
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
                        if offset_on_reverse != 0.0:
                            sar -= sar * offset_on_reverse
                        sar_values[out_idx] = sar
                        out_idx += 1
                        af_long = acceleration_init_long
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
                            af_short += acceleration_short
                            if af_short > acceleration_max_short:
                                af_short = acceleration_max_short
                        sar = sar + af_short * (ep - sar)
                        if sar < prev_high:
                            sar = prev_high
                        if sar < new_high:
                            sar = new_high
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i > 0:  # Start output from second point as per TA-Lib
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = sar_values[i-1]
    
        return result



    @staticmethod
    @nb.njit
    def STDDEV(high, open, low, close, vol, oi, timeperiod=5, nbdev=1.0):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
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
        
            # 计算移动平均值 (SMA)
            mov_avg = np.zeros(len(valid_close))
            for i in range(timeperiod - 1, len(valid_close)):
                sum_val = 0.0
                for j in range(i - timeperiod + 1, i + 1):
                    sum_val += valid_close[j]
                mov_avg[i] = sum_val / timeperiod
        
            # 计算标准差
            stddev_values = np.zeros(len(valid_close))
            for i in range(timeperiod - 1, len(valid_close)):
                period_total2 = 0.0
                for j in range(i - timeperiod + 1, i + 1):
                    temp_real = valid_close[j]
                    period_total2 += temp_real * temp_real
            
                mean_value2 = period_total2 / timeperiod
                temp_real = mov_avg[i]
                temp_real *= temp_real
                mean_value2 -= temp_real
            
                if mean_value2 > 1e-10:
                    stddev_values[i] = np.sqrt(mean_value2)
                else:
                    stddev_values[i] = 0.0
                
            # 应用nbdev因子
            if nbdev != 1.0:
                for i in range(timeperiod - 1, len(valid_close)):
                    if stddev_values[i] > 1e-10:
                        stddev_values[i] *= nbdev
        
            # 映射结果回原始数组
            for i in range(timeperiod - 1, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = stddev_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def STOCH(high, open, low, close, vol, oi, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
        tdts, secs = high.shape
        result_slowk = np.full((tdts, secs), np.nan)
        result_slowd = np.full((tdts, secs), np.nan)

        # 参数验证与默认值处理
        if fastk_period <= 0:
            fastk_period = 5
        if slowk_period <= 0:
            slowk_period = 3
        if slowd_period <= 0:
            slowd_period = 3

        for sec in range(secs):
            # 计算有效数据点
            valid_indices = []
            for i in range(tdts):
                if not (np.isnan(high[i, sec]) or np.isnan(low[i, sec]) or np.isnan(close[i, sec])):
                    valid_indices.append(i)
                    
            valid_indices = np.array(valid_indices)
            if len(valid_indices) == 0:
                continue
                
            # 提取有效数据
            v_high = np.zeros(len(valid_indices))
            v_low = np.zeros(len(valid_indices))
            v_close = np.zeros(len(valid_indices))
            
            for i, idx in enumerate(valid_indices):
                v_high[i] = high[idx, sec]
                v_low[i] = low[idx, sec]
                v_close[i] = close[idx, sec]
                
            # 计算FASTK所需的lookback
            lookback_k = fastk_period - 1
            lookback_kslow = slowk_period - 1 if slowk_matype == 0 else slowk_period - 1
            lookback_dslow = slowd_period - 1 if slowd_matype == 0 else slowd_period - 1
            lookback_total = lookback_k + lookback_kslow + lookback_dslow
            
            if len(valid_indices) <= lookback_total:
                continue
                
            # 计算FastK
            temp_buffer = np.zeros(len(valid_indices) - lookback_k)
            
            for i in range(lookback_k, len(valid_indices)):
                # 在fastk_period范围内查找最高价和最低价
                highest = v_high[i-lookback_k]
                lowest = v_low[i-lookback_k]
                
                for j in range(i-lookback_k+1, i+1):
                    if v_high[j] > highest:
                        highest = v_high[j]
                    if v_low[j] < lowest:
                        lowest = v_low[j]
                
                # 计算 FastK = (Close - Lowest Low)/(Highest High - Lowest Low) * 100
                if highest != lowest:
                    fast_k = (v_close[i] - lowest) / (highest - lowest) * 100.0
                else:
                    fast_k = 0.0
                    
                temp_buffer[i-lookback_k] = fast_k
                
            # 计算SlowK (MA of FastK)
            slowk_buffer = np.zeros_like(temp_buffer)
            if slowk_matype == 0:  # SMA
                for i in range(len(temp_buffer) - slowk_period + 1):
                    slowk_buffer[i+slowk_period-1] = np.mean(temp_buffer[i:i+slowk_period])
                    
            # 计算SlowD (MA of SlowK)
            slowd_buffer = np.zeros_like(slowk_buffer)
            if slowd_matype == 0:  # SMA
                for i in range(slowk_period-1, len(slowk_buffer) - slowd_period + 1):
                    slowd_buffer[i+slowd_period-1] = np.mean(slowk_buffer[i:i+slowd_period])
                
            # 将结果映射回原始数组
            start_idx = lookback_total
            for i in range(len(valid_indices) - start_idx):
                orig_idx = valid_indices[i + start_idx]
                k_idx = i + lookback_k
                if k_idx < len(slowk_buffer):
                    result_slowk[orig_idx, sec] = slowk_buffer[k_idx]
                if k_idx < len(slowd_buffer):
                    result_slowd[orig_idx, sec] = slowd_buffer[k_idx]
                    
        return result_slowk, result_slowd



    @staticmethod
    @nb.njit
    def STOCHF(high, open, low, close, vol, oi, fastk_period=5, fastd_period=3, fastd_matype=0):
        """
        STOCHF - Stochastic Fast
        
        计算快速随机指标，根据TA-Lib C实现重写
        
        参数:
            high: 最高价格
            open: 开盘价格
            low: 最低价格
            close: 收盘价格
            vol: 成交量
            oi: 持仓量
            fastk_period: K线计算周期，默认为5
            fastd_period: D线计算周期，默认为3
            fastd_matype: D线移动平均类型，默认为0（简单移动平均）
        
        返回:
            (fastk, fastd): 快速随机K线和D线
        """
        tdts, secs = high.shape
        result_fastk = np.full((tdts, secs), np.nan)
        result_fastd = np.full((tdts, secs), np.nan)
        
        # 计算回溯期
        lookback_k = fastk_period - 1
        
        # 根据talib实现
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=nb.boolean)
            for i in range(tdts):
                if (not np.isnan(high[i, sec]) and 
                    not np.isnan(low[i, sec]) and 
                    not np.isnan(close[i, sec])):
                    valid_mask[i] = True
            
            valid_indices = np.where(valid_mask)[0]
            
            # 如果没有足够的数据，就继续下一个证券
            if len(valid_indices) <= lookback_k:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
            
            # 临时存储FastK值的缓冲区
            tempBuffer = np.zeros(len(valid_indices) - lookback_k)
            
            # FastK计算
            outIdx = 0
            
            # 按照TA-Lib进行计算
            for today in range(lookback_k, len(valid_indices)):
                # 找当前周期内的最低价
                lowestIdx = -1
                highestIdx = -1
                
                # TA-Lib重复查找所有窗口内的最高/最低价格
                lowestIdx = today - fastk_period + 1
                lowest = valid_low[lowestIdx]
                for i in range(lowestIdx + 1, today + 1):
                    tmp = valid_low[i]
                    if tmp < lowest:
                        lowest = tmp
                
                # 找当前周期内的最高价
                highestIdx = today - fastk_period + 1
                highest = valid_high[highestIdx]
                for i in range(highestIdx + 1, today + 1):
                    tmp = valid_high[i]
                    if tmp > highest:
                        highest = tmp
                
                # 计算K值，乘以100注意完全按照TA-Lib的公式
                # TA-Lib中是 (close-lowest)/(highest-lowest)/100.0，这里我们也除以100
                diff = highest - lowest
                if diff != 0.0:
                    tempBuffer[outIdx] = (valid_close[today] - lowest) / (diff / 100.0)
                else:
                    tempBuffer[outIdx] = 0.0
                    
                outIdx += 1
            
            # 计算FastD
            # 准备数组
            fastd_values = np.zeros(len(tempBuffer))
            
            # 根据指定的MA类型计算FastD
            if fastd_matype == 0:  # SMA
                # 简单移动平均
                for i in range(len(tempBuffer)):
                    if i >= fastd_period - 1:
                        sum_val = 0.0
                        for j in range(i - fastd_period + 1, i + 1):
                            sum_val += tempBuffer[j]
                        fastd_values[i] = sum_val / fastd_period
                    else:
                        fastd_values[i] = np.nan
            else:
                # 简单实现EMA (对于其他MA类型的近似)
                alpha = 2.0 / (fastd_period + 1)
                
                # 初始化EMA
                if len(tempBuffer) > 0:
                    fastd_values[0] = tempBuffer[0]
                    
                    # 计算后续EMA
                    for i in range(1, len(tempBuffer)):
                        fastd_values[i] = alpha * tempBuffer[i] + (1 - alpha) * fastd_values[i-1]
            
            # 将结果映射回原始数组
            for i in range(len(tempBuffer)):
                orig_idx = valid_indices[i + lookback_k]
                result_fastk[orig_idx, sec] = tempBuffer[i]
                
                if not np.isnan(fastd_values[i]):
                    result_fastd[orig_idx, sec] = fastd_values[i]
        
        return result_fastk, result_fastd



    @staticmethod
    @nb.njit
    def SUM(high, open, low, close, vol, oi, timeperiod=30):
        tdts, secs = close.shape
        result = np.full((tdts, secs), np.nan, dtype=np.float64)
        
        # 参数验证
        if timeperiod < 2 or timeperiod > 100000:
            return result
        
        lookbackTotal = timeperiod - 1
        
        for sec in range(secs):
            # 找出所有非NaN数据
            valid_mask = ~np.isnan(close[:, sec])
            valid_indices = np.where(valid_mask)[0]
            
            if len(valid_indices) <= lookbackTotal:
                continue  # 数据不足
            
            # 将连续的有效数据提取出来处理，而不是在原始数组上跳过NaN
            valid_close = close[valid_mask, sec]
            
            # 初始化计算
            periodTotal = 0.0
            trailingIdx = 0
            
            # C代码中的初始窗口累加
            if timeperiod > 1:
                for i in range(lookbackTotal):
                    periodTotal += valid_close[i]
            
            # 这是C代码的关键循环
            for i in range(lookbackTotal, len(valid_close)):
                # 添加当前值到滑动窗口
                periodTotal += valid_close[i]
                
                # 保存当前总和
                tempReal = periodTotal
                
                # 减去窗口最旧的值
                periodTotal -= valid_close[trailingIdx]
                trailingIdx += 1
                
                # 将结果映射回原始索引
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = tempReal
        
        return result



    @staticmethod
    @nb.njit
    def TRANGE(high, open, low, close, vol, oi):
        """
        TRANGE - True Range
        True Range is the greatest of the following:
        - High of the current day minus low of the current day
        - Absolute value of high of the current day minus close of the previous day
        - Absolute value of low of the current day minus close of the previous day
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
            # TA-Lib starts output from index 1
            for i in range(1, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = tr_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def TRIX(high, open, low, close, vol, oi, timeperiod=30):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # 计算lookback period，与C源码保持一致
        ema_lookback = timeperiod - 1
        roc_lookback = 1
        total_lookback = (ema_lookback * 3) + roc_lookback
    
        for sec in range(secs):
            # 创建有效数据掩码
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= total_lookback:
                continue
            
            # 提取有效数据
            valid_close = close[valid_mask, sec]
        
            # 计算第一层EMA
            k = 2.0 / (timeperiod + 1)
            ema1 = np.zeros(len(valid_close))
            ema1[0] = valid_close[0]
            for i in range(1, len(valid_close)):
                ema1[i] = ema1[i-1] + k * (valid_close[i] - ema1[i-1])
        
            # 计算第二层EMA
            ema2 = np.zeros(len(valid_close))
            ema2[ema_lookback] = ema1[ema_lookback]
            for i in range(ema_lookback + 1, len(valid_close)):
                ema2[i] = ema2[i-1] + k * (ema1[i] - ema2[i-1])
        
            # 计算第三层EMA (TEMA)
            ema3 = np.zeros(len(valid_close))
            ema3[ema_lookback * 2] = ema2[ema_lookback * 2]
            for i in range(ema_lookback * 2 + 1, len(valid_close)):
                ema3[i] = ema3[i-1] + k * (ema2[i] - ema3[i-1])
        
            # 计算ROC (Rate of Change)
            trix_values = np.zeros(len(valid_close))
            for i in range(total_lookback, len(valid_close)):
                if ema3[i-1] > 1e-10:  # 避免除零
                    trix_values[i] = 100.0 * (ema3[i] - ema3[i-1]) / ema3[i-1]
                else:
                    trix_values[i] = 0.0
        
            # 映射结果回原始数组
            for i in range(total_lookback, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = trix_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def TSF(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib
        lookback_total = timeperiod - 1
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
            valid_close = close[valid_mask, sec]
        
            # Pre-calculate constants for linear regression
            sum_x = timeperiod * (timeperiod - 1) * 0.5
            sum_x_sqr = timeperiod * (timeperiod - 1) * (2 * timeperiod - 1) / 6
            divisor = sum_x * sum_x - timeperiod * sum_x_sqr
        
            # Calculate TSF values
            tsf_values = np.zeros(len(valid_close))
            for today in range(lookback_total, len(valid_close)):
                sum_xy = 0.0
                sum_y = 0.0
                for i in range(timeperiod):
                    temp_value = valid_close[today - i]
                    sum_y += temp_value
                    sum_xy += i * temp_value
            
                # Calculate slope (m) and intercept (b) for linear regression
                m = (timeperiod * sum_xy - sum_x * sum_y) / divisor
                b = (sum_y - m * sum_x) / timeperiod
            
                # Forecast value at the end of the period
                tsf_values[today] = b + m * timeperiod
        
            # Map results back to original array
            for i in range(lookback_total, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = tsf_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def TYPPRICE(high, open, low, close, vol, oi):
        """
        TYPPRICE - Typical Price
        Typical Price is the average of high, low, and close prices for a given period.
        """
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
        
            # Get valid indices
            valid_indices = np.where(valid_mask)[0]
        
            # If no valid data, skip to next security
            if len(valid_indices) == 0:
                continue
        
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Calculate Typical Price for valid data points
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
        
            # 初始化变量
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed if nb_initial_element_needed < len(valid_close) else len(valid_close) - 1
        
            if start_idx >= len(valid_close):
                continue
            
            # 初始化累加器
            period_total1 = 0.0
            period_total2 = 0.0
            trailing_idx = start_idx - nb_initial_element_needed
        
            # 预热期处理：计算初始的累加值
            i = trailing_idx
            if timeperiod > 1:
                while i < start_idx:
                    temp_real = valid_close[i]
                    period_total1 += temp_real
                    temp_real *= temp_real
                    period_total2 += temp_real
                    i += 1
        
            # 主计算阶段
            out_idx = start_idx
            while out_idx < len(valid_close):
                temp_real = valid_close[out_idx]
                period_total1 += temp_real
                temp_real *= temp_real
                period_total2 += temp_real
            
                mean_value1 = period_total1 / timeperiod
                mean_value2 = period_total2 / timeperiod
            
                temp_real = valid_close[trailing_idx]
                period_total1 -= temp_real
                temp_real *= temp_real
                period_total2 -= temp_real
            
                # 计算方差：E(X^2) - (E(X))^2
                if out_idx >= nb_initial_element_needed:
                    result[valid_indices[out_idx], sec] = mean_value2 - mean_value1 * mean_value1
                
                trailing_idx += 1
                out_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def WCLPRICE(high, open, low, close, vol, oi):
        """
        WCLPRICE - Weighted Close Price
        Weighted Close Price is calculated as (High + Low + 2*Close)/4
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
            if len(valid_indices) == 0:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Calculate Weighted Close Price
            wcl_values = np.zeros(len(valid_high))
            for i in range(len(valid_high)):
                wcl_values[i] = (valid_high[i] + valid_low[i] + (valid_close[i] * 2.0)) / 4.0
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = wcl_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def WILLR(high, open, low, close, vol, oi, timeperiod=14):
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
            if len(valid_indices) < timeperiod:
                continue
            
            # 提取有效数据
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # 初始化输出数组
            willr_values = np.zeros(len(valid_high))
        
            # 计算起始索引
            nb_initial_element_needed = timeperiod - 1
            start_idx = nb_initial_element_needed if nb_initial_element_needed < len(valid_high) else len(valid_high) - 1
        
            if start_idx >= len(valid_high):
                continue
            
            # 初始化变量
            out_idx = 0
            today = start_idx
            trailing_idx = start_idx - nb_initial_element_needed
            lowest_idx = -1
            highest_idx = -1
            diff = 0.0
            highest = 0.0
            lowest = 0.0
        
            # 主循环，计算WILLR
            while today < len(valid_high):
                # 处理最低价
                tmp = valid_low[today]
                if lowest_idx < trailing_idx:
                    lowest_idx = trailing_idx
                    lowest = valid_low[lowest_idx]
                    i = lowest_idx
                    while i + 1 <= today:
                        i += 1
                        tmp = valid_low[i]
                        if tmp < lowest:
                            lowest_idx = i
                            lowest = tmp
                    diff = (highest - lowest) / (-100.0)
                elif tmp <= lowest:
                    lowest_idx = today
                    lowest = tmp
                    diff = (highest - lowest) / (-100.0)
                
                # 处理最高价
                tmp = valid_high[today]
                if highest_idx < trailing_idx:
                    highest_idx = trailing_idx
                    highest = valid_high[highest_idx]
                    i = highest_idx
                    while i + 1 <= today:
                        i += 1
                        tmp = valid_high[i]
                        if tmp > highest:
                            highest_idx = i
                            highest = tmp
                    diff = (highest - lowest) / (-100.0)
                elif tmp >= highest:
                    highest_idx = today
                    highest = tmp
                    diff = (highest - lowest) / (-100.0)
                
                # 计算WILLR值
                if diff != 0.0:
                    willr_values[today] = (highest - valid_close[today]) / diff
                else:
                    willr_values[today] = 0.0
                
                trailing_idx += 1
                today += 1
        
            # 映射结果回原始数组
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = willr_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def STOCHRSI(high, open, low, close, vol, oi, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
        tdts, secs = close.shape
        result_fastk = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_fastd = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Calculate lookback periods as per TA-Lib logic
        lookback_stochf = fastk_period + fastd_period - 1
        lookback_total = timeperiod + lookback_stochf - 1
    
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
        
            # Step 1: Calculate RSI
            rsi_values = np.zeros(len(valid_close))
            up_avg = 0.0
            down_avg = 0.0
        
            # Initialize first period for RSI
            for i in range(1, timeperiod + 1):
                if i >= len(valid_close):
                    break
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
                delta = abs(valid_close[i] - valid_close[i-1])
                if delta > 0:
                    up_val = delta if valid_close[i] > valid_close[i-1] else 0.0
                    down_val = 0.0 if valid_close[i] > valid_close[i-1] else delta
                else:
                    up_val = 0.0
                    down_val = 0.0
            
                up_avg = ((up_avg * (timeperiod - 1)) + up_val) / timeperiod
                down_avg = ((down_avg * (timeperiod - 1)) + down_val) / timeperiod
            
                if down_avg > 1e-10:
                    rs = up_avg / down_avg
                    rsi_values[i] = 100.0 - (100.0 / (1.0 + rs))
                else:
                    rsi_values[i] = 100.0 if up_avg > 0 else 0.0
        
            # Step 2: Calculate Stochastic FastK and FastD on RSI values
            stochf_start_idx = timeperiod - 1
            if stochf_start_idx + lookback_stochf >= len(valid_close):
                continue
            
            fastk_values = np.zeros(len(valid_close))
            fastd_values = np.zeros(len(valid_close))
        
            for i in range(stochf_start_idx + fastk_period - 1, len(valid_close)):
                # Calculate FastK
                period_high = rsi_values[i - fastk_period + 1:i + 1]
                period_low = rsi_values[i - fastk_period + 1:i + 1]
                high_val = np.nanmax(period_high)
                low_val = np.nanmin(period_low)
            
                if high_val - low_val > 1e-10:
                    fastk_values[i] = 100.0 * (rsi_values[i] - low_val) / (high_val - low_val)
                else:
                    fastk_values[i] = 0.0
        
            # Calculate FastD based on matype (0 = SMA as default)
            if fastd_matype == 0:  # Simple Moving Average
                for i in range(stochf_start_idx + fastk_period + fastd_period - 2, len(valid_close)):
                    period_fastk = fastk_values[i - fastd_period + 1:i + 1]
                    valid_fastk = period_fastk[~np.isnan(period_fastk)]
                    if len(valid_fastk) > 0:
                        fastd_values[i] = np.mean(valid_fastk)
                    else:
                        fastd_values[i] = np.nan
        
            # Map results back to original array
            start_idx = lookback_total
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result_fastk[orig_idx, sec] = fastk_values[i]
                result_fastd[orig_idx, sec] = fastd_values[i]
    
        return result_fastk, result_fastd



    @staticmethod
    @nb.njit
    def HT_SINE(high, open, low, close, vol, oi, unstable_period=63):
        """
        Hilbert Transform - SineWave
        Implemented based on Ehlers' approach from "Rocket Science for Traders"
        """
        tdts, secs = close.shape
        result_sine = np.full((tdts, secs), np.nan, dtype=np.float64)
        result_lead_sine = np.full((tdts, secs), np.nan, dtype=np.float64)

        # Constants for the calculation
        LOOKBACK_TOTAL = 64
        LOOKBACK_HT = 7
        LOOKBACK_HT_SKIP = 25  # Skip before applying HT

        # Constants for angle calculations
        rad2deg = 180.0 / np.arctan(1.0) / 4.0
        deg2rad = 1.0 / rad2deg
        deg2radby360 = 360.0 / rad2deg

        for sec in range(secs):
            # 根据参考代码的处理方式选择价格数据
            # 如果有high和low，使用(high+low)/2作为价格数据
            # 否则使用close作为价格数据
            if np.isnan(high[:, sec]).any() or np.isnan(low[:, sec]).any():
                price_data = close[:, sec].copy()
            else:
                price_data = (high[:, sec] + low[:, sec]) / 2.0
            
            # Skip if not enough valid data
            valid_mask = ~np.isnan(price_data)
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= LOOKBACK_TOTAL + unstable_period:
                continue
            
            # Extract valid price data
            valid_price = price_data[valid_mask]
            
            # Pre-allocate arrays for results
            price_len = len(valid_price)
            smooth_price = np.zeros(price_len)
            sine_buffer = np.zeros(price_len)
            leadsine_buffer = np.zeros(price_len)
            
            # Initial smoothing of price - 初始平滑价格
            # 只处理大于LOOKBACK_TOTAL+LOOKBACK_HT_SKIP的点
            for i in range(3, price_len):
                smooth_price[i] = (4.0*valid_price[i] + 
                                3.0*valid_price[i-1] + 
                                2.0*valid_price[i-2] + 
                                valid_price[i-3]) / 10.0
            
            # Circular buffers for Hilbert Transform calculations
            detrender = np.zeros(LOOKBACK_HT)
            i1_buffer = np.zeros(LOOKBACK_HT)
            q1_buffer = np.zeros(LOOKBACK_HT)
            
            # Initialize variables
            i2, q2 = 0.0, 0.0
            re, im = 0.0, 0.0
            period, smoothperiod = 0.0, 0.0
            idx = 0  # Index for circular buffers
            
            # Start processing after the minimum required lookback
            start_idx = LOOKBACK_TOTAL
            
            # 初始化阶段
            # 与参考代码保持一致，跳过前面的处理点
            
            for i in range(start_idx, price_len):
                # Adjust period for HT calculations
                adjperiod = 0.075 * period + 0.54
                
                # Calculate Hilbert Transform detrender
                ht_detrender = 0.0962 * smooth_price[i] + \
                            0.5769 * smooth_price[i-2] - \
                            0.5769 * smooth_price[i-4] - \
                            0.0962 * smooth_price[i-6]
                            
                detrender[idx] = ht_detrender * adjperiod
                
                # Calculate inphase and quadrature components
                i10 = detrender[(idx - 3) % LOOKBACK_HT]  # 3 periods ago
                
                # Hilbert Transform of detrender for quadrature
                q10 = 0.0962 * detrender[idx] + \
                    0.5769 * detrender[(idx - 2) % LOOKBACK_HT] - \
                    0.5769 * detrender[(idx - 4) % LOOKBACK_HT] - \
                    0.0962 * detrender[(idx - 6) % LOOKBACK_HT]
                q10 *= adjperiod
                
                i1_buffer[idx] = i10
                q1_buffer[idx] = q10
                
                # Hilbert Transform of I1 and Q1
                ji = 0.0962 * i1_buffer[idx] + \
                    0.5769 * i1_buffer[(idx - 2) % LOOKBACK_HT] - \
                    0.5769 * i1_buffer[(idx - 4) % LOOKBACK_HT] - \
                    0.0962 * i1_buffer[(idx - 6) % LOOKBACK_HT]
                ji *= adjperiod
                
                jq = 0.0962 * q1_buffer[idx] + \
                    0.5769 * q1_buffer[(idx - 2) % LOOKBACK_HT] - \
                    0.5769 * q1_buffer[(idx - 4) % LOOKBACK_HT] - \
                    0.0962 * q1_buffer[(idx - 6) % LOOKBACK_HT]
                jq *= adjperiod
                
                # Store previous values for smoothing
                i21, q21 = i2, q2
                
                # Calculate new I2 and Q2 values
                i2 = i10 - jq
                q2 = q10 + ji
                
                # Smooth I2 and Q2
                i2 = 0.2 * i2 + 0.8 * i21
                q2 = 0.2 * q2 + 0.8 * q21
                
                # Calculate Re and Im components
                re0 = i2 * i21 + q2 * q21
                im0 = i2 * q21 - q2 * i21
                
                # Smooth Re and Im
                re = 0.2 * re0 + 0.8 * re
                im = 0.2 * im0 + 0.8 * im
                
                # Calculate and adjust dominant cycle period
                period1 = period
                if re != 0.0 and im != 0.0:
                    period = 360.0 / (rad2deg * np.arctan(im / re))
                    
                # 精确匹配原始代码的逻辑处理顺序
                if period1 > 0:
                    period = min(period, period1 * 1.5)
                    period = max(period, period1 * 0.67)
                
                period = max(period, 6.0)
                period = min(period, 50.0)
                period = 0.2 * period + 0.8 * period1
                
                smoothperiod = 0.33 * period + 0.67 * smoothperiod
                
                # Calculate dominant cycle phase
                dcperiod = int(smoothperiod + 0.5)
                
                realpart, imagpart = 0.0, 0.0
                # 使用参考代码的范围处理方式
                for dci in range(min(dcperiod, i+1)):
                    x = dci * deg2radby360 / dcperiod
                    y = smooth_price[i - dci]  # backward from last
                    realpart += np.sin(x) * y
                    imagpart += np.cos(x) * y
                
                # Calculate phase - 精确匹配参考代码相位计算
                dcphase = 0.0
                abs_imagpart = abs(imagpart)
                if abs_imagpart > 0.0:
                    dcphase = np.arctan(realpart / imagpart) * rad2deg
                elif abs_imagpart <= 0.01:
                    if realpart < 0.0:
                        dcphase -= 90.0
                    elif realpart > 0.0:
                        dcphase += 90.0
                
                dcphase += 90.0
                dcphase += 360.0 / smoothperiod
                
                if imagpart < 0.0:
                    dcphase += 180.0
                    
                if dcphase > 315.0:
                    dcphase -= 360.0
                
                # Store results in buffer
                sine_buffer[i] = np.sin(dcphase * deg2rad)
                leadsine_buffer[i] = np.sin((dcphase + 45.0) * deg2rad)
                
                # Move to next position in circular buffers
                idx = (idx + 1) % LOOKBACK_HT
            
            # Map results back to original indices
            # 按照参考代码的实现，处理不稳定期
            for i in range(start_idx + unstable_period, price_len):
                orig_idx = valid_indices[i]
                result_sine[orig_idx, sec] = sine_buffer[i]
                result_lead_sine[orig_idx, sec] = leadsine_buffer[i]
        
        return result_sine, result_lead_sine






    '''
    Unmatched Indicators
    '''

    @staticmethod
    @nb.njit
    def CDLBELTHOLD(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyLong and ShadowVeryShort as per TA-Lib defaults
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
                # BodyLong range is typically close-open for the real body
                BodyLongRange = abs(valid_close[i] - valid_open[i])
                BodyLongPeriodTotal += BodyLongRange
            
                # ShadowVeryShort range for shadows
                if valid_close[i] > valid_open[i]:
                    ShadowRange = valid_high[i] - valid_close[i]
                else:
                    ShadowRange = valid_open[i] - valid_low[i]
                ShadowVeryShortPeriodTotal += ShadowRange
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
            
                # Calculate candle color: 1 for bullish, -1 for bearish
                candle_color = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate current shadow based on candle color
                if candle_color == 1:
                    lower_shadow = valid_open[i] - valid_low[i]
                    upper_shadow = valid_high[i] - valid_close[i]
                else:
                    lower_shadow = valid_close[i] - valid_low[i]
                    upper_shadow = valid_high[i] - valid_open[i]
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Belt Hold pattern logic
                if real_body > BodyLongAverage:
                    if candle_color == 1 and lower_shadow < ShadowVeryShortAverage:
                        result[valid_indices[i], sec] = 100 * candle_color
                    elif candle_color == -1 and upper_shadow < ShadowVeryShortAverage:
                        result[valid_indices[i], sec] = 100 * candle_color
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update trailing totals
                # Remove oldest value and add newest value for BodyLong
                oldest_body_range = abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                newest_body_range = abs(valid_close[i] - valid_open[i])
                BodyLongPeriodTotal += newest_body_range - oldest_body_range
                BodyLongTrailingIdx += 1
            
                # Remove oldest value and add newest value for ShadowVeryShort
                if valid_close[ShadowVeryShortTrailingIdx] > valid_open[ShadowVeryShortTrailingIdx]:
                    oldest_shadow_range = valid_high[ShadowVeryShortTrailingIdx] - valid_close[ShadowVeryShortTrailingIdx]
                else:
                    oldest_shadow_range = valid_open[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]
                
                if valid_close[i] > valid_open[i]:
                    newest_shadow_range = valid_high[i] - valid_close[i]
                else:
                    newest_shadow_range = valid_open[i] - valid_low[i]
                
                ShadowVeryShortPeriodTotal += newest_shadow_range - oldest_shadow_range
                ShadowVeryShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLCLOSINGMARUBOZU(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for periods as per TA-Lib defaults
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
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing totals
            BodyLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for BodyLong and ShadowVeryShort
            BodyLongTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
        
            for i in range(BodyLongPeriod):
                if i < len(valid_high):
                    BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            for i in range(ShadowVeryShortPeriod):
                if i < len(valid_high):
                    if valid_close[i] > valid_open[i]:
                        ShadowVeryShortPeriodTotal += valid_high[i] - valid_close[i]
                    else:
                        ShadowVeryShortPeriodTotal += valid_open[i] - valid_low[i]
        
            # Start processing from lookback period
            lookbackTotal = max(BodyLongPeriod, ShadowVeryShortPeriod)
            outIdx = lookbackTotal
        
            while outIdx < len(valid_high):
                # Calculate real body
                real_body = abs(valid_close[outIdx] - valid_open[outIdx])
            
                # Calculate candle color (1 for bullish, -1 for bearish)
                candle_color = 1 if valid_close[outIdx] > valid_open[outIdx] else -1
            
                # Calculate upper and lower shadows
                upper_shadow = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx])
                lower_shadow = min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Check for Closing Marubozu pattern
                if real_body > BodyLongAverage:
                    if candle_color == 1 and upper_shadow < ShadowVeryShortAverage:
                        result[valid_indices[outIdx], sec] = 100
                    elif candle_color == -1 and lower_shadow < ShadowVeryShortAverage:
                        result[valid_indices[outIdx], sec] = -100
                    else:
                        result[valid_indices[outIdx], sec] = 0
                else:
                    result[valid_indices[outIdx], sec] = 0
            
                # Update trailing totals
                if outIdx + 1 < len(valid_high):
                    # Remove oldest value and add newest for BodyLong
                    if BodyLongTrailingIdx < len(valid_high):
                        BodyLongPeriodTotal += abs(valid_close[outIdx] - valid_open[outIdx])
                        if BodyLongTrailingIdx + BodyLongPeriod < len(valid_high):
                            BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                        BodyLongTrailingIdx += 1
                
                    # Remove oldest value and add newest for ShadowVeryShort
                    if ShadowVeryShortTrailingIdx < len(valid_high):
                        if candle_color == 1:
                            ShadowVeryShortPeriodTotal += valid_high[outIdx] - valid_close[outIdx]
                        else:
                            ShadowVeryShortPeriodTotal += valid_open[outIdx] - valid_low[outIdx]
                        if ShadowVeryShortTrailingIdx + ShadowVeryShortPeriod < len(valid_high):
                            old_candle_color = 1 if valid_close[ShadowVeryShortTrailingIdx] > valid_open[ShadowVeryShortTrailingIdx] else -1
                            if old_candle_color == 1:
                                ShadowVeryShortPeriodTotal -= valid_high[ShadowVeryShortTrailingIdx] - valid_close[ShadowVeryShortTrailingIdx]
                            else:
                                ShadowVeryShortPeriodTotal -= valid_open[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]
                        ShadowVeryShortTrailingIdx += 1
            
                outIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLCOUNTERATTACK(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults (typically 3 for candlestick patterns)
        EqualPeriod = 3
        BodyLongPeriod = 3
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
            if len(valid_indices) < lookbackTotal + 1:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for Equal and BodyLong
            EqualPeriodTotal = 0.0
            BodyLongPeriodTotal = np.zeros(2, dtype=np.float64)
            EqualTrailingIdx = lookbackTotal - EqualPeriod
            BodyLongTrailingIdx = lookbackTotal - BodyLongPeriod
        
            # Calculate initial totals for Equal range
            i = EqualTrailingIdx
            while i < lookbackTotal:
                if i >= 0 and i < len(valid_high):
                    EqualPeriodTotal += max(valid_high[i] - valid_low[i], 0.0)
                i += 1
            
            # Calculate initial totals for BodyLong range
            i = BodyLongTrailingIdx
            while i < lookbackTotal:
                if i >= 0 and i < len(valid_high):
                    BodyLongPeriodTotal[1] += abs(valid_close[i-1] - valid_open[i-1]) if i > 0 else 0.0
                    BodyLongPeriodTotal[0] += abs(valid_close[i] - valid_open[i])
                i += 1
            
            # Main calculation loop starting from lookbackTotal
            i = lookbackTotal
            while i < len(valid_high):
                # Calculate averages
                EqualAverage = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0.0
                BodyLongAverage1 = BodyLongPeriodTotal[1] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyLongAverage0 = BodyLongPeriodTotal[0] / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
            
                # Determine candle colors (1 for bullish, -1 for bearish)
                color_current = 1.0 if valid_close[i] > valid_open[i] else -1.0
                color_prev = 1.0 if valid_close[i-1] > valid_open[i-1] else -1.0
            
                # Calculate real body sizes
                realbody_prev = abs(valid_close[i-1] - valid_open[i-1])
                realbody_current = abs(valid_close[i] - valid_open[i])
            
                # Check counterattack conditions
                if (color_prev == -color_current and
                    realbody_prev > BodyLongAverage1 and
                    realbody_current > BodyLongAverage0 and
                    valid_close[i] <= valid_close[i-1] + EqualAverage and
                    valid_close[i] >= valid_close[i-1] - EqualAverage):
                    result[valid_indices[i], sec] = color_current * 100.0
                else:
                    result[valid_indices[i], sec] = 0.0
                
                # Update period totals by adding new value and subtracting trailing value
                if i < len(valid_high):
                    EqualPeriodTotal += max(valid_high[i] - valid_low[i], 0.0)
                    if EqualTrailingIdx >= 0 and EqualTrailingIdx < len(valid_high):
                        EqualPeriodTotal -= max(valid_high[EqualTrailingIdx] - valid_low[EqualTrailingIdx], 0.0)
                    
                    for totIdx in range(1, -1, -1):
                        current_body = abs(valid_close[i-totIdx] - valid_open[i-totIdx])
                        trailing_body = abs(valid_close[BodyLongTrailingIdx-totIdx] - valid_open[BodyLongTrailingIdx-totIdx]) if BodyLongTrailingIdx-totIdx >= 0 else 0.0
                        BodyLongPeriodTotal[totIdx] += current_body
                        BodyLongPeriodTotal[totIdx] -= trailing_body
                    
                i += 1
                EqualTrailingIdx += 1
                BodyLongTrailingIdx += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLDOJISTAR(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for averaging body sizes as per TA-Lib defaults
        BodyLongPeriod = 10
        BodyDojiPeriod = 3
    
        # Lookback period as per TA-Lib (maximum of the two periods + 1 for the previous day check)
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
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for averaging
            BodyLongPeriodTotal = 0.0
            BodyDojiPeriodTotal = 0.0
        
            # Calculate initial totals for BodyLong
            BodyLongTrailingIdx = 0
            for i in range(BodyLongTrailingIdx, min(BodyLongPeriod, len(valid_high) - 1)):
                BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # Calculate initial totals for BodyDoji
            BodyDojiTrailingIdx = 0
            for i in range(BodyDojiTrailingIdx, min(BodyDojiPeriod, len(valid_high))):
                BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            # Start processing from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body for previous day (i-1) and current day (i)
                realbody_prev = abs(valid_close[i-1] - valid_open[i-1])
                realbody_curr = abs(valid_close[i] - valid_open[i])
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
            
                # Determine candle color for previous day
                candle_color_prev = 1 if valid_close[i-1] > valid_open[i-1] else -1
            
                # Check for gap up or gap down
                gap_up = (candle_color_prev == 1 and 
                          min(valid_open[i], valid_close[i]) > max(valid_open[i-1], valid_close[i-1]))
                gap_down = (candle_color_prev == -1 and 
                            max(valid_open[i], valid_close[i]) < min(valid_open[i-1], valid_close[i-1]))
            
                # Check Doji Star conditions
                if (realbody_prev > BodyLongAverage and 
                    realbody_curr <= BodyDojiAverage and 
                    (gap_up or gap_down)):
                    result[valid_indices[i], sec] = -candle_color_prev * 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update totals for next iteration
                if i - 1 >= BodyLongTrailingIdx + BodyLongPeriod:
                    BodyLongPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
                    BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                    BodyLongTrailingIdx += 1
                
                BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                if i >= BodyDojiTrailingIdx + BodyDojiPeriod:
                    BodyDojiPeriodTotal -= abs(valid_close[BodyDojiTrailingIdx] - valid_open[BodyDojiTrailingIdx])
                    BodyDojiTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLDRAGONFLYDOJI(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for BodyDoji and ShadowVeryShort as per TA-Lib defaults
        BodyDojiPeriod = 10
        ShadowVeryShortPeriod = 10
        lookbackTotal = max(BodyDojiPeriod, ShadowVeryShortPeriod)
    
        for sec in range(secs):
            # Initialize period totals for averaging
            BodyDojiPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Data validation mask
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
        
            # Initialize trailing indices for rolling averages
            BodyDojiTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
        
            # Calculate initial totals for the lookback period
            for i in range(lookbackTotal):
                # BodyDoji range is typically the real body (abs(open - close))
                BodyDojiRange = abs(valid_open[i] - valid_close[i])
                # ShadowVeryShort range is typically the high-low range for shadow calculations
                ShadowVeryShortRange = valid_high[i] - valid_low[i]
            
                if i < BodyDojiPeriod:
                    BodyDojiPeriodTotal += BodyDojiRange
                if i < ShadowVeryShortPeriod:
                    ShadowVeryShortPeriodTotal += ShadowVeryShortRange
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body and shadows
                real_body = abs(valid_open[i] - valid_close[i])
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Calculate averages for comparison
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Dragonfly Doji conditions:
                # 1. Real body is very small compared to average body
                # 2. Upper shadow is very short compared to average shadow
                # 3. Lower shadow is long compared to average shadow
                if (real_body <= BodyDojiAverage and
                    upper_shadow < ShadowVeryShortAverage and
                    lower_shadow > ShadowVeryShortAverage):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals for next iteration
                if i - BodyDojiTrailingIdx >= BodyDojiPeriod:
                    oldBodyDojiRange = abs(valid_open[BodyDojiTrailingIdx] - valid_close[BodyDojiTrailingIdx])
                    newBodyDojiRange = abs(valid_open[i] - valid_close[i])
                    BodyDojiPeriodTotal += newBodyDojiRange - oldBodyDojiRange
                    BodyDojiTrailingIdx += 1
                
                if i - ShadowVeryShortTrailingIdx >= ShadowVeryShortPeriod:
                    oldShadowRange = valid_high[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx]
                    newShadowRange = valid_high[i] - valid_low[i]
                    ShadowVeryShortPeriodTotal += newShadowRange - oldShadowRange
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
            if len(valid_indices) <= lookback_total:
                continue
            
            # Extract valid data
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
            for i in range(start_idx, len(valid_high)):
                # Check for gap conditions (up or down for both candles compared to two days ago)
                gap_up_1 = valid_open[i-1] > valid_close[i-2] if i >= 2 else False
                gap_up_2 = valid_open[i] > valid_close[i-2] if i >= 2 else False
                gap_down_1 = valid_open[i-1] < valid_close[i-2] if i >= 2 else False
                gap_down_2 = valid_open[i] < valid_close[i-2] if i >= 2 else False
            
                # Check if both candles are white (bullish)
                is_white_1 = valid_close[i-1] > valid_open[i-1] if i >= 1 else False
                is_white_2 = valid_close[i] > valid_open[i]
            
                # Calculate real body sizes
                real_body_1 = abs(valid_close[i-1] - valid_open[i-1]) if i >= 1 else 0.0
                real_body_2 = abs(valid_close[i] - valid_open[i])
            
                # Calculate averages for Near and Equal
                near_avg = near_period_total / near_period if near_period > 0 else 0.0
                equal_avg = equal_period_total / equal_period if equal_period > 0 else 0.0
            
                # Check conditions for Side-by-Side White Lines pattern
                if ((gap_up_1 and gap_up_2) or (gap_down_1 and gap_down_2)) and \
                   is_white_1 and is_white_2 and \
                   real_body_2 >= real_body_1 - near_avg and \
                   real_body_2 <= real_body_1 + near_avg and \
                   valid_open[i] >= valid_open[i-1] - equal_avg and \
                   valid_open[i] <= valid_open[i-1] + equal_avg:
                    result[valid_indices[i], sec] = 100 if gap_up_1 else -100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update totals for next iteration
                if i - 1 >= 0:
                    near_period_total += (valid_high[i-1] - valid_low[i-1])
                    equal_period_total += (valid_high[i-1] - valid_low[i-1])
                if near_trailing_idx < len(valid_high):
                    near_period_total -= (valid_high[near_trailing_idx] - valid_low[near_trailing_idx])
                    near_trailing_idx += 1
                if equal_trailing_idx < len(valid_high):
                    equal_period_total -= (valid_high[equal_trailing_idx] - valid_low[equal_trailing_idx])
                    equal_trailing_idx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLGRAVESTONEDOJI(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for BodyDoji and ShadowVeryShort as per TA-Lib defaults (typically 10)
        BodyDojiPeriod = 10
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
            if len(valid_indices) < max(BodyDojiPeriod, ShadowVeryShortPeriod):
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for BodyDoji and ShadowVeryShort
            BodyDojiPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyDojiTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
        
            for i in range(BodyDojiPeriod):
                if i < len(valid_high):
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
        
            for i in range(ShadowVeryShortPeriod):
                if i < len(valid_high):
                    ShadowVeryShortPeriodTotal += valid_high[i] - valid_low[i]
        
            # Start processing from the lookback period
            start_idx = max(BodyDojiPeriod, ShadowVeryShortPeriod)
            for i in range(start_idx, len(valid_high)):
                # Calculate real body and shadows
                real_body = abs(valid_close[i] - valid_open[i])
                lower_shadow = valid_open[i] - valid_low[i] if valid_open[i] > valid_close[i] else valid_close[i] - valid_low[i]
                upper_shadow = valid_high[i] - valid_open[i] if valid_open[i] > valid_close[i] else valid_high[i] - valid_close[i]
            
                # Calculate averages
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Check for Gravestone Doji pattern
                if (real_body <= BodyDojiAverage and
                    lower_shadow < ShadowVeryShortAverage and
                    upper_shadow > ShadowVeryShortAverage):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update period totals by subtracting the trailing value and adding the current
                if BodyDojiTrailingIdx < len(valid_high):
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i]) - abs(valid_close[BodyDojiTrailingIdx] - valid_open[BodyDojiTrailingIdx])
                    BodyDojiTrailingIdx += 1
            
                if ShadowVeryShortTrailingIdx < len(valid_high):
                    ShadowVeryShortPeriodTotal += (valid_high[i] - valid_low[i]) - (valid_high[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx])
                    ShadowVeryShortTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLHAMMER(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle components as per TA-Lib defaults
        BodyShortPeriod = 5
        ShadowLongPeriod = 5
        ShadowVeryShortPeriod = 5
        NearPeriod = 5
    
        # Total lookback period as per TA-Lib (maximum of individual lookbacks + 1 for Near)
        lookbackTotal = max(BodyShortPeriod, ShadowLongPeriod, ShadowVeryShortPeriod, NearPeriod + 1)
    
        for sec in range(secs):
            # Initialize period totals for averaging
            BodyPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
            NearPeriodTotal = 0.0
        
            # Trailing indices for rolling window calculations
            BodyTrailingIdx = lookbackTotal - BodyShortPeriod
            ShadowLongTrailingIdx = lookbackTotal - ShadowLongPeriod
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
            NearTrailingIdx = lookbackTotal - 1 - NearPeriod
        
            # Initialize period totals for the lookback window
            i = BodyTrailingIdx
            while i < lookbackTotal:
                if i < tdts and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    BodyPeriodTotal += abs(close[i, sec] - open[i, sec])
                i += 1
            
            i = ShadowLongTrailingIdx
            while i < lookbackTotal:
                if i < tdts and low[i, sec] == low[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    ShadowLongPeriodTotal += min(open[i, sec], close[i, sec]) - low[i, sec]
                i += 1
            
            i = ShadowVeryShortTrailingIdx
            while i < lookbackTotal:
                if i < tdts and high[i, sec] == high[i, sec] and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    ShadowVeryShortPeriodTotal += high[i, sec] - max(open[i, sec], close[i, sec])
                i += 1
            
            i = NearTrailingIdx
            while i < lookbackTotal - 1:
                if i < tdts and high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec]:
                    NearPeriodTotal += high[i, sec] - low[i, sec]
                i += 1
            
            # Main calculation loop starting from lookbackTotal
            i = lookbackTotal
            while i < tdts:
                # Check for valid data
                if (i - 1 >= 0 and high[i, sec] == high[i, sec] and low[i, sec] == low[i, sec] and 
                    open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec] and 
                    low[i - 1, sec] == low[i - 1, sec]):
                
                    # Calculate real body and shadows for current candle
                    real_body = abs(close[i, sec] - open[i, sec])
                    lower_shadow = min(open[i, sec], close[i, sec]) - low[i, sec]
                    upper_shadow = high[i, sec] - max(open[i, sec], close[i, sec])
                
                    # Calculate averages for comparison
                    body_avg = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                    shadow_long_avg = ShadowLongPeriodTotal / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
                    shadow_short_avg = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                    near_avg = NearPeriodTotal / NearPeriod if NearPeriod > 0 else 0.0
                
                    # Hammer pattern conditions
                    if (real_body < body_avg and 
                        lower_shadow > shadow_long_avg and 
                        upper_shadow < shadow_short_avg and 
                        min(close[i, sec], open[i, sec]) <= low[i - 1, sec] + near_avg):
                        result[i, sec] = 100
                    else:
                        result[i, sec] = 0
                    
                    # Update rolling totals for next iteration
                    if BodyTrailingIdx < tdts:
                        old_body = abs(close[BodyTrailingIdx, sec] - open[BodyTrailingIdx, sec]) if (BodyTrailingIdx < tdts and open[BodyTrailingIdx, sec] == open[BodyTrailingIdx, sec] and close[BodyTrailingIdx, sec] == close[BodyTrailingIdx, sec]) else 0.0
                        BodyPeriodTotal += real_body - old_body
                    
                    if ShadowLongTrailingIdx < tdts:
                        old_shadow_long = min(open[ShadowLongTrailingIdx, sec], close[ShadowLongTrailingIdx, sec]) - low[ShadowLongTrailingIdx, sec] if (ShadowLongTrailingIdx < tdts and low[ShadowLongTrailingIdx, sec] == low[ShadowLongTrailingIdx, sec] and open[ShadowLongTrailingIdx, sec] == open[ShadowLongTrailingIdx, sec] and close[ShadowLongTrailingIdx, sec] == close[ShadowLongTrailingIdx, sec]) else 0.0
                        ShadowLongPeriodTotal += lower_shadow - old_shadow_long
                    
                    if ShadowVeryShortTrailingIdx < tdts:
                        old_shadow_short = high[ShadowVeryShortTrailingIdx, sec] - max(open[ShadowVeryShortTrailingIdx, sec], close[ShadowVeryShortTrailingIdx, sec]) if (ShadowVeryShortTrailingIdx < tdts and high[ShadowVeryShortTrailingIdx, sec] == high[ShadowVeryShortTrailingIdx, sec] and open[ShadowVeryShortTrailingIdx, sec] == open[ShadowVeryShortTrailingIdx, sec] and close[ShadowVeryShortTrailingIdx, sec] == close[ShadowVeryShortTrailingIdx, sec]) else 0.0
                        ShadowVeryShortPeriodTotal += upper_shadow - old_shadow_short
                    
                    if NearTrailingIdx < tdts:
                        old_near = high[NearTrailingIdx, sec] - low[NearTrailingIdx, sec] if (NearTrailingIdx < tdts and high[NearTrailingIdx, sec] == high[NearTrailingIdx, sec] and low[NearTrailingIdx, sec] == low[NearTrailingIdx, sec]) else 0.0
                        near_range = high[i - 1, sec] - low[i - 1, sec] if (i - 1 < tdts and high[i - 1, sec] == high[i - 1, sec] and low[i - 1, sec] == low[i - 1, sec]) else 0.0
                        NearPeriodTotal += near_range - old_near
                    
                    # Increment trailing indices
                    BodyTrailingIdx += 1
                    ShadowLongTrailingIdx += 1
                    ShadowVeryShortTrailingIdx += 1
                    NearTrailingIdx += 1
                
                i += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLHARAMICROSS(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for BodyLong and BodyDoji as per TA-Lib defaults
        BodyLongPeriod = 10
        BodyDojiPeriod = 3
    
        # Lookback total as per TA-Lib (maximum of the periods involved)
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
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize totals for rolling averages
            BodyLongPeriodTotal = 0.0
            BodyDojiPeriodTotal = 0.0
        
            # Calculate initial totals for BodyLong and BodyDoji ranges
            BodyLongTrailingIdx = 0
            BodyDojiTrailingIdx = lookbackTotal - BodyDojiPeriod
        
            for i in range(BodyLongTrailingIdx, lookbackTotal - 1):
                BodyLongPeriodTotal += abs(valid_high[i] - valid_low[i])
        
            for i in range(BodyDojiTrailingIdx, lookbackTotal):
                BodyDojiPeriodTotal += abs(valid_high[i] - valid_low[i])
        
            # Start processing from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body for current and previous candle
                realbody_prev = abs(valid_close[i-1] - valid_open[i-1])
                realbody_curr = abs(valid_close[i] - valid_open[i])
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
            
                # Determine max and min for current and previous candle
                max_prev = max(valid_close[i-1], valid_open[i-1])
                min_prev = min(valid_close[i-1], valid_open[i-1])
                max_curr = max(valid_close[i], valid_open[i])
                min_curr = min(valid_close[i], valid_open[i])
            
                # Determine candle color for previous candle
                candle_color_prev = 1 if valid_close[i-1] > valid_open[i-1] else -1
            
                # Check for Harami Cross pattern
                if realbody_prev > BodyLongAverage and realbody_curr <= BodyDojiAverage:
                    if max_curr < max_prev and min_curr > min_prev:
                        result[valid_indices[i], sec] = -candle_color_prev * 100
                    elif max_curr <= max_prev and min_curr >= min_prev:
                        result[valid_indices[i], sec] = -candle_color_prev * 80
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals for next iteration
                if i - 1 >= BodyLongTrailingIdx + BodyLongPeriod:
                    BodyLongPeriodTotal += abs(valid_high[i-1] - valid_low[i-1]) - abs(valid_high[BodyLongTrailingIdx] - valid_low[BodyLongTrailingIdx])
                    BodyLongTrailingIdx += 1
                else:
                    BodyLongPeriodTotal += abs(valid_high[i-1] - valid_low[i-1])
            
                if i >= BodyDojiTrailingIdx + BodyDojiPeriod:
                    BodyDojiPeriodTotal += abs(valid_high[i] - valid_low[i]) - abs(valid_high[BodyDojiTrailingIdx] - valid_low[BodyDojiTrailingIdx])
                    BodyDojiTrailingIdx += 1
                else:
                    BodyDojiPeriodTotal += abs(valid_high[i] - valid_low[i])
    
        return result



    @staticmethod
    @nb.njit
    def CDLHIGHWAVE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods as per TA-Lib defaults
        BodyShortPeriod = 10
        ShadowVeryLongPeriod = 10
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
        
            # Initialize period totals for body and shadow
            BodyPeriodTotal = 0.0
            ShadowPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyTrailingIdx = 0
            ShadowTrailingIdx = 0
        
            for i in range(lookbackTotal):
                # Body range for BodyShort
                body_range = abs(valid_close[i] - valid_open[i])
                BodyPeriodTotal += body_range
            
                # Shadow range for ShadowVeryLong (using high-low as range)
                shadow_range = valid_high[i] - valid_low[i]
                ShadowPeriodTotal += shadow_range
        
            # Start processing from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body
                real_body = abs(valid_close[i] - valid_open[i])
            
                # Calculate upper and lower shadows
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Calculate averages
                BodyAverage = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                ShadowAverage = ShadowPeriodTotal / ShadowVeryLongPeriod if ShadowVeryLongPeriod > 0 else 0.0
            
                # Check High Wave conditions
                if (real_body < BodyAverage and
                    upper_shadow > ShadowAverage and
                    lower_shadow > ShadowAverage):
                    candle_color = 1 if valid_close[i] > valid_open[i] else -1
                    result[valid_indices[i], sec] = candle_color * 100
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update trailing totals
                if i - BodyShortPeriod >= 0:
                    old_body_range = abs(valid_close[BodyTrailingIdx] - valid_open[BodyTrailingIdx])
                    new_body_range = abs(valid_close[i] - valid_open[i])
                    BodyPeriodTotal += new_body_range - old_body_range
                    BodyTrailingIdx += 1
                
                if i - ShadowVeryLongPeriod >= 0:
                    old_shadow_range = valid_high[ShadowTrailingIdx] - valid_low[ShadowTrailingIdx]
                    new_shadow_range = valid_high[i] - valid_low[i]
                    ShadowPeriodTotal += new_shadow_range - old_shadow_range
                    ShadowTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLINVERTEDHAMMER(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define lookback periods for different candle parts as per TA-Lib defaults
        BodyShortPeriod = 10
        ShadowLongPeriod = 3
        ShadowVeryShortPeriod = 3
        lookbackTotal = max(BodyShortPeriod, ShadowLongPeriod, ShadowVeryShortPeriod)
    
        for sec in range(secs):
            # Initialize period totals for averaging
            BodyPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyTrailingIdx = lookbackTotal - BodyShortPeriod
            ShadowLongTrailingIdx = lookbackTotal - ShadowLongPeriod
            ShadowVeryShortTrailingIdx = lookbackTotal - ShadowVeryShortPeriod
        
            for i in range(BodyTrailingIdx, lookbackTotal):
                if i < tdts and open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                    BodyPeriodTotal += abs(close[i, sec] - open[i, sec])
        
            for i in range(ShadowLongTrailingIdx, lookbackTotal):
                if i < tdts and high[i, sec] == high[i, sec] and close[i, sec] == close[i, sec] and open[i, sec] == open[i, sec]:
                    real_body_high = max(open[i, sec], close[i, sec])
                    ShadowLongPeriodTotal += high[i, sec] - real_body_high
        
            for i in range(ShadowVeryShortTrailingIdx, lookbackTotal):
                if i < tdts and low[i, sec] == low[i, sec] and close[i, sec] == close[i, sec] and open[i, sec] == open[i, sec]:
                    real_body_low = min(open[i, sec], close[i, sec])
                    ShadowVeryShortPeriodTotal += real_body_low - low[i, sec]
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, tdts):
                if (high[i, sec] != high[i, sec] or low[i, sec] != low[i, sec] or 
                    open[i, sec] != open[i, sec] or close[i, sec] != close[i, sec] or
                    i - 1 < 0 or close[i-1, sec] != close[i-1, sec]):
                    result[i, sec] = 0
                    continue
                
                # Calculate real body and shadows for current candle
                real_body = abs(close[i, sec] - open[i, sec])
                real_body_high = max(open[i, sec], close[i, sec])
                real_body_low = min(open[i, sec], close[i, sec])
                upper_shadow = high[i, sec] - real_body_high
                lower_shadow = real_body_low - low[i, sec]
            
                # Calculate averages
                BodyAverage = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                ShadowLongAverage = ShadowLongPeriodTotal / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Check for gap down
                gap_down = close[i-1, sec] > open[i, sec]
            
                # Check Inverted Hammer conditions
                if (real_body < BodyAverage and 
                    upper_shadow > ShadowLongAverage and 
                    lower_shadow < ShadowVeryShortAverage and 
                    gap_down):
                    result[i, sec] = 100
                else:
                    result[i, sec] = 0
            
                # Update period totals for next iteration
                if i + 1 < tdts:
                    # Add current values
                    if open[i, sec] == open[i, sec] and close[i, sec] == close[i, sec]:
                        BodyPeriodTotal += abs(close[i, sec] - open[i, sec])
                    if high[i, sec] == high[i, sec] and close[i, sec] == close[i, sec] and open[i, sec] == open[i, sec]:
                        ShadowLongPeriodTotal += high[i, sec] - real_body_high
                    if low[i, sec] == low[i, sec] and close[i, sec] == close[i, sec] and open[i, sec] == open[i, sec]:
                        ShadowVeryShortPeriodTotal += real_body_low - low[i, sec]
                
                    # Subtract trailing values
                    trailing_body_idx = i - BodyShortPeriod + 1
                    trailing_shadow_long_idx = i - ShadowLongPeriod + 1
                    trailing_shadow_short_idx = i - ShadowVeryShortPeriod + 1
                
                    if trailing_body_idx >= 0 and open[trailing_body_idx, sec] == open[trailing_body_idx, sec] and close[trailing_body_idx, sec] == close[trailing_body_idx, sec]:
                        BodyPeriodTotal -= abs(close[trailing_body_idx, sec] - open[trailing_body_idx, sec])
                    if trailing_shadow_long_idx >= 0 and high[trailing_shadow_long_idx, sec] == high[trailing_shadow_long_idx, sec] and close[trailing_shadow_long_idx, sec] == close[trailing_shadow_long_idx, sec] and open[trailing_shadow_long_idx, sec] == open[trailing_shadow_long_idx, sec]:
                        trailing_real_body_high = max(open[trailing_shadow_long_idx, sec], close[trailing_shadow_long_idx, sec])
                        ShadowLongPeriodTotal -= high[trailing_shadow_long_idx, sec] - trailing_real_body_high
                    if trailing_shadow_short_idx >= 0 and low[trailing_shadow_short_idx, sec] == low[trailing_shadow_short_idx, sec] and close[trailing_shadow_short_idx, sec] == close[trailing_shadow_short_idx, sec] and open[trailing_shadow_short_idx, sec] == open[trailing_shadow_short_idx, sec]:
                        trailing_real_body_low = min(open[trailing_shadow_short_idx, sec], close[trailing_shadow_short_idx, sec])
                        ShadowVeryShortPeriodTotal -= trailing_real_body_low - low[trailing_shadow_short_idx, sec]
    
        return result



    @staticmethod
    @nb.njit
    def CDLLONGLEGGEDDOJI(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for BodyDoji and ShadowLong as per TA-Lib defaults
        BodyDojiPeriod = 5
        ShadowLongPeriod = 5
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
            if len(valid_indices) < lookbackTotal:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for BodyDoji and ShadowLong
            BodyDojiPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyDojiTrailingIdx = 0
            ShadowLongTrailingIdx = 0
        
            for i in range(lookbackTotal):
                if i < BodyDojiPeriod:
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                if i < ShadowLongPeriod:
                    ShadowLongPeriodTotal += valid_high[i] - valid_low[i]
        
            outIdx = lookbackTotal
            while outIdx < len(valid_high):
                # Calculate real body and shadows
                realBody = abs(valid_close[outIdx] - valid_open[outIdx])
                upperShadow = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx])
                lowerShadow = min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
            
                # Calculate averages
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                ShadowLongAverage = ShadowLongPeriodTotal / ShadowLongPeriod if ShadowLongPeriod > 0 else 0.0
            
                # Check for Long Legged Doji conditions
                if (realBody <= BodyDojiAverage and
                    (lowerShadow > ShadowLongAverage or upperShadow > ShadowLongAverage)):
                    result[valid_indices[outIdx], sec] = 100
                else:
                    result[valid_indices[outIdx], sec] = 0
            
                # Update totals for next iteration
                if outIdx - BodyDojiTrailingIdx >= BodyDojiPeriod:
                    BodyDojiPeriodTotal += abs(valid_close[outIdx] - valid_open[outIdx])
                    BodyDojiPeriodTotal -= abs(valid_close[BodyDojiTrailingIdx] - valid_open[BodyDojiTrailingIdx])
                    BodyDojiTrailingIdx += 1
            
                if outIdx - ShadowLongTrailingIdx >= ShadowLongPeriod:
                    ShadowLongPeriodTotal += valid_high[outIdx] - valid_low[outIdx]
                    ShadowLongPeriodTotal -= valid_high[ShadowLongTrailingIdx] - valid_low[ShadowLongTrailingIdx]
                    ShadowLongTrailingIdx += 1
            
                outIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLLONGLINE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for periods as in TA-Lib
        BodyLongPeriod = 5
        ShadowShortPeriod = 5
    
        # Lookback total as per TA-Lib (maximum of the periods used)
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
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize period totals for body and shadow
            BodyPeriodTotal = 0.0
            ShadowPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyTrailingIdx = 0
            ShadowTrailingIdx = 0
        
            for i in range(lookbackTotal):
                # Body range for BodyLong (typically close - open)
                body_range = abs(valid_close[i] - valid_open[i])
                BodyPeriodTotal += body_range
            
                # Shadow range for ShadowShort (typically high - low for total candle height)
                shadow_range = valid_high[i] - valid_low[i]
                ShadowPeriodTotal += shadow_range
        
            # Start processing from lookbackTotal onwards
            outIdx = lookbackTotal
            while outIdx < len(valid_high):
                # Calculate real body and shadows for current candle
                real_body = abs(valid_close[outIdx] - valid_open[outIdx])
                upper_shadow = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx])
                lower_shadow = min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
            
                # Calculate averages
                BodyAverage = BodyPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                ShadowAverage = ShadowPeriodTotal / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
            
                # Check conditions for long line pattern
                if (real_body > BodyAverage and
                    upper_shadow < ShadowAverage and
                    lower_shadow < ShadowAverage):
                    # Determine candle color (1 for bullish, -1 for bearish) and multiply by 100
                    candle_color = 1 if valid_close[outIdx] > valid_open[outIdx] else -1
                    result[valid_indices[outIdx], sec] = candle_color * 100
                else:
                    result[valid_indices[outIdx], sec] = 0
                
                # Update trailing totals by subtracting oldest value and adding newest
                if outIdx >= BodyLongPeriod:
                    old_body_range = abs(valid_close[BodyTrailingIdx] - valid_open[BodyTrailingIdx])
                    new_body_range = abs(valid_close[outIdx] - valid_open[outIdx])
                    BodyPeriodTotal += new_body_range - old_body_range
                    BodyTrailingIdx += 1
                
                if outIdx >= ShadowShortPeriod:
                    old_shadow_range = valid_high[ShadowTrailingIdx] - valid_low[ShadowTrailingIdx]
                    new_shadow_range = valid_high[outIdx] - valid_low[outIdx]
                    ShadowPeriodTotal += new_shadow_range - old_shadow_range
                    ShadowTrailingIdx += 1
                
                outIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLMARUBOZU(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for BodyLong and ShadowVeryShort as per TA-Lib defaults
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
        
            # Initialize lookback total as the maximum of the periods
            lookback_total = max(BodyLongPeriod, ShadowVeryShortPeriod)
            start_idx = lookback_total if lookback_total < len(valid_high) else len(valid_high) - 1
        
            if start_idx > len(valid_high) - 1:
                continue
            
            # Initialize totals for BodyLong and ShadowVeryShort
            BodyLongPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
        
            # Calculate initial totals for BodyLong
            BodyLongTrailingIdx = start_idx - BodyLongPeriod
            for i in range(BodyLongTrailingIdx, start_idx):
                if i >= 0:
                    real_body = abs(valid_close[i] - valid_open[i])
                    BodyLongPeriodTotal += real_body
        
            # Calculate initial totals for ShadowVeryShort
            ShadowVeryShortTrailingIdx = start_idx - ShadowVeryShortPeriod
            for i in range(ShadowVeryShortTrailingIdx, start_idx):
                if i >= 0:
                    upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                    lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
                    ShadowVeryShortPeriodTotal += upper_shadow + lower_shadow
        
            # Main calculation loop
            for i in range(start_idx, len(valid_high)):
                # Calculate real body and shadows for current candle
                real_body = abs(valid_close[i] - valid_open[i])
                upper_shadow = valid_high[i] - max(valid_open[i], valid_close[i])
                lower_shadow = min(valid_open[i], valid_close[i]) - valid_low[i]
            
                # Calculate averages
                BodyLongAverage = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Marubozu condition: long body and very short shadows
                if (real_body > BodyLongAverage and 
                    upper_shadow < ShadowVeryShortAverage and 
                    lower_shadow < ShadowVeryShortAverage):
                    candle_color = 1 if valid_close[i] > valid_open[i] else -1
                    result[valid_indices[i], sec] = candle_color * 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update totals for next iteration
                if i + 1 < len(valid_high):
                    # Add current values
                    BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
                    ShadowVeryShortPeriodTotal += (valid_high[i] - max(valid_open[i], valid_close[i])) + (min(valid_open[i], valid_close[i]) - valid_low[i])
                
                    # Subtract trailing values if within bounds
                    if BodyLongTrailingIdx >= 0:
                        BodyLongPeriodTotal -= abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                    if ShadowVeryShortTrailingIdx >= 0:
                        ShadowVeryShortPeriodTotal -= (valid_high[ShadowVeryShortTrailingIdx] - max(valid_open[ShadowVeryShortTrailingIdx], valid_close[ShadowVeryShortTrailingIdx])) + (min(valid_open[ShadowVeryShortTrailingIdx], valid_close[ShadowVeryShortTrailingIdx]) - valid_low[ShadowVeryShortTrailingIdx])
                
                    BodyLongTrailingIdx += 1
                    ShadowVeryShortTrailingIdx += 1
    
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
        
            # Initial sum of candle ranges for EqualPeriod before startIdx
            start_idx = lookback_total
            for i in range(EqualTrailingIdx, start_idx):
                if i < len(valid_high):
                    EqualPeriodTotal += valid_high[i] - valid_low[i]
        
            out_idx = start_idx
            i = start_idx
        
            while i < len(valid_high):
                # Check for Matching Low pattern
                if i >= 1:
                    # Candle color check: both candles should be black (bearish)
                    color1 = -1 if valid_close[i-1] < valid_open[i-1] else 1
                    color2 = -1 if valid_close[i] < valid_open[i] else 1
                
                    # Calculate Equal average for the range
                    EqualAverage = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0.0
                
                    # Matching Low conditions
                    if (color1 == -1 and color2 == -1 and
                        valid_close[i] <= valid_close[i-1] + EqualAverage and
                        valid_close[i] >= valid_close[i-1] - EqualAverage):
                        result[valid_indices[i], sec] = 100
                    else:
                        result[valid_indices[i], sec] = 0
                else:
                    result[valid_indices[i], sec] = 0
                
                # Update EqualPeriodTotal for next iteration
                if i < len(valid_high):
                    EqualPeriodTotal += (valid_high[i] - valid_low[i])
                if EqualTrailingIdx < len(valid_high):
                    EqualPeriodTotal -= (valid_high[EqualTrailingIdx] - valid_low[EqualTrailingIdx])
            
                i += 1
                EqualTrailingIdx += 1
            
        return result



    @staticmethod
    @nb.njit
    def CDLRICKSHAWMAN(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for averaging as per TA-Lib defaults
        BodyDojiPeriod = 3
        ShadowLongPeriod = 3
        NearPeriod = 3
    
        # Lookback total as per TA-Lib (maximum of the periods)
        lookbackTotal = max(BodyDojiPeriod, max(ShadowLongPeriod, NearPeriod))
    
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
        
            # Initialize totals for averaging
            BodyDojiPeriodTotal = 0.0
            ShadowLongPeriodTotal = 0.0
            NearPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            BodyDojiTrailingIdx = 0
            ShadowLongTrailingIdx = 0
            NearTrailingIdx = 0
        
            for i in range(lookbackTotal):
                # BodyDoji range (real body size)
                BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                # ShadowLong range (high - low for long shadow comparison)
                ShadowLongPeriodTotal += valid_high[i] - valid_low[i]
                # Near range (high - low for near comparison)
                NearPeriodTotal += valid_high[i] - valid_low[i]
        
            outIdx = 0
            i = lookbackTotal
            BodyDojiTrailingIdx = 0
            ShadowLongTrailingIdx = 0
            NearTrailingIdx = 0
        
            while i < len(valid_high):
                # Calculate averages
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod
                ShadowLongAverage = ShadowLongPeriodTotal / ShadowLongPeriod
                NearAverage = NearPeriodTotal / NearPeriod
            
                # Calculate real body
                realBody = abs(valid_close[i] - valid_open[i])
                # Calculate lower shadow
                lowerShadow = valid_open[i] if valid_close[i] > valid_open[i] else valid_close[i]
                lowerShadow = lowerShadow - valid_low[i]
                # Calculate upper shadow
                upperShadow = valid_high[i] - (valid_open[i] if valid_close[i] > valid_open[i] else valid_close[i])
                # Calculate high-low range
                highLowRange = valid_high[i] - valid_low[i]
            
                # Conditions for Rickshaw Man pattern
                if (realBody <= BodyDojiAverage and
                    lowerShadow > ShadowLongAverage and
                    upperShadow > ShadowLongAverage and
                    min(valid_open[i], valid_close[i]) <= valid_low[i] + highLowRange / 2 + NearAverage and
                    max(valid_open[i], valid_close[i]) >= valid_low[i] + highLowRange / 2 - NearAverage):
                    if i < len(valid_indices):
                        orig_idx = valid_indices[i]
                        result[orig_idx, sec] = 100
                else:
                    if i < len(valid_indices):
                        orig_idx = valid_indices[i]
                        result[orig_idx, sec] = 0
            
                # Update totals for next iteration
                if i + 1 < len(valid_high):
                    # Add new values
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                    ShadowLongPeriodTotal += valid_high[i] - valid_low[i]
                    NearPeriodTotal += valid_high[i] - valid_low[i]
                
                    # Subtract trailing values
                    BodyDojiPeriodTotal -= abs(valid_close[BodyDojiTrailingIdx] - valid_open[BodyDojiTrailingIdx])
                    ShadowLongPeriodTotal -= valid_high[ShadowLongTrailingIdx] - valid_low[ShadowLongTrailingIdx]
                    NearPeriodTotal -= valid_high[NearTrailingIdx] - valid_low[NearTrailingIdx]
                
                    BodyDojiTrailingIdx += 1
                    ShadowLongTrailingIdx += 1
                    NearTrailingIdx += 1
            
                i += 1
                outIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLSEPARATINGLINES(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for averaging as per TA-Lib defaults
        ShadowVeryShortPeriod = 10
        BodyLongPeriod = 10
        EqualPeriod = 10
    
        # Lookback period as per TA-Lib (needs at least 1 prior candle)
        lookbackTotal = 1
    
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
            if len(valid_indices) <= lookbackTotal:
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize trailing indices for rolling averages
            start_idx = lookbackTotal
            ShadowVeryShortTrailingIdx = start_idx - ShadowVeryShortPeriod
            BodyLongTrailingIdx = start_idx - BodyLongPeriod
            EqualTrailingIdx = start_idx - EqualPeriod
        
            # Initialize totals for rolling averages
            ShadowVeryShortPeriodTotal = 0.0
            BodyLongPeriodTotal = 0.0
            EqualPeriodTotal = 0.0
        
            # Calculate initial totals for ShadowVeryShort
            i = ShadowVeryShortTrailingIdx if ShadowVeryShortTrailingIdx >= 0 else 0
            while i < start_idx and i < len(valid_high):
                if valid_high[i] == valid_high[i] and valid_low[i] == valid_low[i]:
                    if valid_close[i] > valid_open[i]:
                        ShadowVeryShortPeriodTotal += valid_high[i] - valid_close[i]
                    else:
                        ShadowVeryShortPeriodTotal += valid_open[i] - valid_low[i]
                i += 1
        
            # Calculate initial totals for BodyLong
            i = BodyLongTrailingIdx if BodyLongTrailingIdx >= 0 else 0
            while i < start_idx and i < len(valid_high):
                if valid_close[i] == valid_close[i] and valid_open[i] == valid_open[i]:
                    BodyLongPeriodTotal += abs(valid_close[i] - valid_open[i])
                i += 1
        
            # Calculate initial totals for Equal
            i = EqualTrailingIdx if EqualTrailingIdx >= 0 else 0
            while i < start_idx and i < len(valid_high):
                if i - 1 >= 0 and valid_open[i-1] == valid_open[i-1]:
                    EqualPeriodTotal += abs(valid_close[i-1] - valid_open[i-1])
                i += 1
        
            # Main calculation loop
            for i in range(start_idx, len(valid_high)):
                # Calculate candle color for current and previous candle
                color_prev = 1 if i - 1 >= 0 and valid_close[i-1] > valid_open[i-1] else -1
                color_curr = 1 if valid_close[i] > valid_open[i] else -1
            
                # Calculate real body for current candle
                real_body_curr = abs(valid_close[i] - valid_open[i])
            
                # Calculate shadows for current candle
                upper_shadow_curr = valid_high[i] - valid_close[i] if color_curr == 1 else valid_high[i] - valid_open[i]
                lower_shadow_curr = valid_open[i] - valid_low[i] if color_curr == 1 else valid_close[i] - valid_low[i]
            
                # Calculate averages
                equal_avg = EqualPeriodTotal / EqualPeriod if EqualPeriod > 0 else 0.0
                body_long_avg = BodyLongPeriodTotal / BodyLongPeriod if BodyLongPeriod > 0 else 0.0
                shadow_short_avg = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
            
                # Check Separating Lines conditions
                if (color_prev == -color_curr and
                    valid_open[i] <= valid_open[i-1] + equal_avg and
                    valid_open[i] >= valid_open[i-1] - equal_avg and
                    real_body_curr > body_long_avg and
                    ((color_curr == 1 and lower_shadow_curr < shadow_short_avg) or
                     (color_curr == -1 and upper_shadow_curr < shadow_short_avg))):
                    result[valid_indices[i], sec] = color_curr * 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals for next iteration
                # ShadowVeryShort update
                if i < len(valid_high):
                    shadow_curr = upper_shadow_curr if color_curr == -1 else lower_shadow_curr
                    if ShadowVeryShortTrailingIdx >= 0 and ShadowVeryShortTrailingIdx < len(valid_high):
                        shadow_trail = (valid_high[ShadowVeryShortTrailingIdx] - valid_close[ShadowVeryShortTrailingIdx]) if valid_close[ShadowVeryShortTrailingIdx] > valid_open[ShadowVeryShortTrailingIdx] else (valid_open[ShadowVeryShortTrailingIdx] - valid_low[ShadowVeryShortTrailingIdx])
                        ShadowVeryShortPeriodTotal += shadow_curr - shadow_trail
                    else:
                        ShadowVeryShortPeriodTotal += shadow_curr
                    ShadowVeryShortTrailingIdx += 1
            
                # BodyLong update
                if i < len(valid_high):
                    body_curr = real_body_curr
                    if BodyLongTrailingIdx >= 0 and BodyLongTrailingIdx < len(valid_high):
                        body_trail = abs(valid_close[BodyLongTrailingIdx] - valid_open[BodyLongTrailingIdx])
                        BodyLongPeriodTotal += body_curr - body_trail
                    else:
                        BodyLongPeriodTotal += body_curr
                    BodyLongTrailingIdx += 1
            
                # Equal update
                if i < len(valid_high):
                    equal_curr = abs(valid_close[i-1] - valid_open[i-1]) if i-1 >= 0 else 0.0
                    if EqualTrailingIdx - 1 >= 0 and EqualTrailingIdx - 1 < len(valid_high):
                        equal_trail = abs(valid_close[EqualTrailingIdx-1] - valid_open[EqualTrailingIdx-1])
                        EqualPeriodTotal += equal_curr - equal_trail
                    else:
                        EqualPeriodTotal += equal_curr
                    EqualTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLSHORTLINE(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define constants for lookback periods as per TA-Lib defaults
        BodyShortPeriod = 5
        ShadowShortPeriod = 5
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
        
            # Calculate initial totals for the lookback period
            BodyTrailingIdx = 0
            ShadowTrailingIdx = 0
            for i in range(BodyTrailingIdx, lookbackTotal):
                if i < BodyShortPeriod:
                    BodyPeriodTotal += abs(valid_close[i] - valid_open[i])
                if i < ShadowShortPeriod:
                    ShadowPeriodTotal += max(valid_high[i] - valid_open[i], valid_close[i] - valid_low[i]) if valid_close[i] >= valid_open[i] else max(valid_high[i] - valid_close[i], valid_open[i] - valid_low[i])
        
            # Main calculation loop starting from lookbackTotal
            outIdx = lookbackTotal
            while outIdx < len(valid_high):
                # Calculate real body and shadows for current candle
                real_body = abs(valid_close[outIdx] - valid_open[outIdx])
                upper_shadow = valid_high[outIdx] - max(valid_open[outIdx], valid_close[outIdx])
                lower_shadow = min(valid_open[outIdx], valid_close[outIdx]) - valid_low[outIdx]
            
                # Calculate averages
                BodyAverage = BodyPeriodTotal / BodyShortPeriod if BodyShortPeriod > 0 else 0.0
                ShadowAverage = ShadowPeriodTotal / ShadowShortPeriod if ShadowShortPeriod > 0 else 0.0
            
                # Check if current candle meets Short Line criteria
                if (real_body < BodyAverage and 
                    upper_shadow < ShadowAverage and 
                    lower_shadow < ShadowAverage):
                    candle_color = 1 if valid_close[outIdx] > valid_open[outIdx] else -1
                    result[valid_indices[outIdx], sec] = candle_color * 100
                else:
                    result[valid_indices[outIdx], sec] = 0
                
                # Update period totals by removing oldest value and adding newest
                if outIdx >= BodyShortPeriod:
                    BodyPeriodTotal += abs(valid_close[outIdx] - valid_open[outIdx]) - abs(valid_close[BodyTrailingIdx] - valid_open[BodyTrailingIdx])
                    BodyTrailingIdx += 1
                else:
                    BodyPeriodTotal += abs(valid_close[outIdx] - valid_open[outIdx])
                
                if outIdx >= ShadowShortPeriod:
                    old_shadow = max(valid_high[ShadowTrailingIdx] - valid_open[ShadowTrailingIdx], valid_close[ShadowTrailingIdx] - valid_low[ShadowTrailingIdx]) if valid_close[ShadowTrailingIdx] >= valid_open[ShadowTrailingIdx] else max(valid_high[ShadowTrailingIdx] - valid_close[ShadowTrailingIdx], valid_open[ShadowTrailingIdx] - valid_low[ShadowTrailingIdx])
                    new_shadow = max(valid_high[outIdx] - valid_open[outIdx], valid_close[outIdx] - valid_low[outIdx]) if valid_close[outIdx] >= valid_open[outIdx] else max(valid_high[outIdx] - valid_close[outIdx], valid_open[outIdx] - valid_low[outIdx])
                    ShadowPeriodTotal += new_shadow - old_shadow
                    ShadowTrailingIdx += 1
                else:
                    new_shadow = max(valid_high[outIdx] - valid_open[outIdx], valid_close[outIdx] - valid_low[outIdx]) if valid_close[outIdx] >= valid_open[outIdx] else max(valid_high[outIdx] - valid_close[outIdx], valid_open[outIdx] - valid_low[outIdx])
                    ShadowPeriodTotal += new_shadow
                
                outIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLTAKURI(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Define periods for different candlestick characteristics as per TA-Lib defaults
        BodyDojiPeriod = 3
        ShadowVeryShortPeriod = 3
        ShadowVeryLongPeriod = 3
    
        # Lookback total as per TA-Lib (maximum of the periods)
        lookbackTotal = max(BodyDojiPeriod, max(ShadowVeryShortPeriod, ShadowVeryLongPeriod))
    
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
        
            # Initialize totals for rolling averages
            BodyDojiPeriodTotal = 0.0
            ShadowVeryShortPeriodTotal = 0.0
            ShadowVeryLongPeriodTotal = 0.0
        
            # Calculate initial totals for the lookback period
            for i in range(lookbackTotal):
                if i < BodyDojiPeriod:
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                if i < ShadowVeryShortPeriod:
                    ShadowVeryShortPeriodTotal += valid_high[i] - valid_open[i] if valid_close[i] > valid_open[i] else valid_high[i] - valid_close[i]
                if i < ShadowVeryLongPeriod:
                    ShadowVeryLongPeriodTotal += valid_open[i] - valid_low[i] if valid_close[i] > valid_open[i] else valid_close[i] - valid_low[i]
        
            # Initialize trailing indices for rolling window
            BodyDojiTrailingIdx = 0
            ShadowVeryShortTrailingIdx = 0
            ShadowVeryLongTrailingIdx = 0
        
            # Main calculation loop starting from lookbackTotal
            for i in range(lookbackTotal, len(valid_high)):
                # Calculate real body and shadows for current candle
                real_body = abs(valid_close[i] - valid_open[i])
                upper_shadow = valid_high[i] - (valid_close[i] if valid_close[i] > valid_open[i] else valid_open[i])
                lower_shadow = (valid_open[i] if valid_close[i] > valid_open[i] else valid_close[i]) - valid_low[i]
            
                # Calculate averages
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod if BodyDojiPeriod > 0 else 0.0
                ShadowVeryShortAverage = ShadowVeryShortPeriodTotal / ShadowVeryShortPeriod if ShadowVeryShortPeriod > 0 else 0.0
                ShadowVeryLongAverage = ShadowVeryLongPeriodTotal / ShadowVeryLongPeriod if ShadowVeryLongPeriod > 0 else 0.0
            
                # Check Takuri pattern conditions
                if (real_body <= BodyDojiAverage and 
                    upper_shadow < ShadowVeryShortAverage and 
                    lower_shadow > ShadowVeryLongAverage):
                    result[valid_indices[i], sec] = 100
                else:
                    result[valid_indices[i], sec] = 0
            
                # Update rolling totals by adding new value and subtracting trailing value
                if i + 1 < len(valid_high):
                    # Add new values
                    BodyDojiPeriodTotal += abs(valid_close[i] - valid_open[i])
                    ShadowVeryShortPeriodTotal += valid_high[i] - (valid_close[i] if valid_close[i] > valid_open[i] else valid_open[i])
                    ShadowVeryLongPeriodTotal += (valid_open[i] if valid_close[i] > valid_open[i] else valid_close[i]) - valid_low[i]
                
                    # Subtract trailing values
                    if BodyDojiTrailingIdx < len(valid_high):
                        BodyDojiPeriodTotal -= abs(valid_close[BodyDojiTrailingIdx] - valid_open[BodyDojiTrailingIdx])
                    if ShadowVeryShortTrailingIdx < len(valid_high):
                        ShadowVeryShortPeriodTotal -= valid_high[ShadowVeryShortTrailingIdx] - (valid_close[ShadowVeryShortTrailingIdx] if valid_close[ShadowVeryShortTrailingIdx] > valid_open[ShadowVeryShortTrailingIdx] else valid_open[ShadowVeryShortTrailingIdx])
                    if ShadowVeryLongTrailingIdx < len(valid_high):
                        ShadowVeryLongPeriodTotal -= (valid_open[ShadowVeryLongTrailingIdx] if valid_close[ShadowVeryLongTrailingIdx] > valid_open[ShadowVeryLongTrailingIdx] else valid_close[ShadowVeryLongTrailingIdx]) - valid_low[ShadowVeryLongTrailingIdx]
                
                    # Increment trailing indices
                    BodyDojiTrailingIdx += 1
                    ShadowVeryShortTrailingIdx += 1
                    ShadowVeryLongTrailingIdx += 1
    
        return result



    @staticmethod
    @nb.njit
    def CDLTRISTAR(high, open, low, close, vol, oi):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        # Lookback period as per TA-Lib (2 days prior for pattern recognition + average period)
        lookback_total = 2 + 3  # 2 for pattern, 3 for BodyDoji average period
    
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
            if len(valid_indices) < lookback_total:
                continue
            
            valid_high = high[valid_mask, sec]
            valid_open = open[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Initialize output array for valid data
            out_values = np.zeros(len(valid_high))
        
            # BodyDoji average period as per TA-Lib
            body_doji_period = 3
            body_period_total = 0.0
            body_trailing_idx = 0
        
            # Initialize BodyPeriodTotal for the first valid calculation point
            start_idx = lookback_total
            for i in range(start_idx - 2 - body_doji_period, start_idx - 2):
                if i >= 0:
                    body_range = valid_high[i] - valid_low[i]
                    body_period_total += body_range
        
            i = start_idx
            while i < len(valid_high):
                # Calculate real body for current and previous two candles
                real_body_2 = abs(valid_close[i-2] - valid_open[i-2])
                real_body_1 = abs(valid_close[i-1] - valid_open[i-1])
                real_body_0 = abs(valid_close[i] - valid_open[i])
            
                # Calculate average body range for comparison
                body_avg = body_period_total / body_doji_period if body_doji_period > 0 else 0.0
            
                # Check if all three candles are doji-like (small body)
                if (real_body_2 <= body_avg and 
                    real_body_1 <= body_avg and 
                    real_body_0 <= body_avg):
                    out_values[i] = 0.0
                
                    # Check for bearish pattern (gap up between first and second candle)
                    if (min(valid_open[i-1], valid_close[i-1]) > max(valid_open[i-2], valid_close[i-2]) and
                        max(valid_open[i], valid_close[i]) < max(valid_open[i-1], valid_close[i-1])):
                        out_values[i] = -100.0
                
                    # Check for bullish pattern (gap down between first and second candle)
                    if (max(valid_open[i-1], valid_close[i-1]) < min(valid_open[i-2], valid_close[i-2]) and
                        min(valid_open[i], valid_close[i]) > min(valid_open[i-1], valid_close[i-1])):
                        out_values[i] = 100.0
                else:
                    out_values[i] = 0.0
            
                # Update BodyPeriodTotal for next iteration
                if i < len(valid_high):
                    body_range_current = valid_high[i-2] - valid_low[i-2]
                    body_range_trailing = valid_high[body_trailing_idx] - valid_low[body_trailing_idx]
                    body_period_total += body_range_current - body_range_trailing
                    body_trailing_idx += 1
            
                i += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if i >= start_idx:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = out_values[i]
    
        return result



    @staticmethod
    @nb.njit
    def HT_DCPERIOD(high, open, low, close, vol, oi):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
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
            startIdx = lookbackTotal
            trailingWMAIdx = startIdx - lookbackTotal
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
            smoothedValue = 0.0
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
            prevI2 = 0.0
            prevQ2 = 0.0
            Re = 0.0
            Im = 0.0
            I1ForOddPrev3 = 0.0
            I1ForEvenPrev3 = 0.0
            I1ForOddPrev2 = 0.0
            I1ForEvenPrev2 = 0.0
            smoothPeriod = 0.0
            outIdx = 0

            while today < len(valid_close):
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
                    detrender[hilbertIdx] = (0.0962 * smoothedValue + 0.5769 * detrender[(hilbertIdx - 2) % 3] - 0.5769 * detrender[hilbertIdx] - 0.0962 * detrender[(hilbertIdx + 1) % 3]) * adjustedPrevPeriod
                    Q1[hilbertIdx] = (0.0962 * detrender[hilbertIdx] + 0.5769 * Q1[(hilbertIdx - 2) % 3] - 0.5769 * Q1[hilbertIdx] - 0.0962 * Q1[(hilbertIdx + 1) % 3]) * adjustedPrevPeriod
                    jI[hilbertIdx] = (0.0962 * I1ForEvenPrev3 + 0.5769 * jI[(hilbertIdx - 2) % 3] - 0.5769 * jI[hilbertIdx] - 0.0962 * jI[(hilbertIdx + 1) % 3]) * adjustedPrevPeriod
                    jQ[hilbertIdx] = (0.0962 * Q1[hilbertIdx] + 0.5769 * jQ[(hilbertIdx - 2) % 3] - 0.5769 * jQ[hilbertIdx] - 0.0962 * jQ[(hilbertIdx + 1) % 3]) * adjustedPrevPeriod
                    if hilbertIdx == 2:
                        hilbertIdx = 0
                    else:
                        hilbertIdx += 1
                    Q2 = (0.2 * (Q1[(hilbertIdx - 1) % 3] + jI[(hilbertIdx - 1) % 3])) + (0.8 * prevQ2)
                    I2 = (0.2 * (I1ForEvenPrev3 - jQ[(hilbertIdx - 1) % 3])) + (0.8 * prevI2)
                    I1ForOddPrev3 = I1ForOddPrev2
                    I1ForOddPrev2 = detrender[(hilbertIdx - 1) % 3]
                else:
                    detrender[hilbertIdx] = (0.091 * smoothedValue + 0.822 * detrender[(hilbertIdx - 2) % 3] - 0.411 * detrender[hilbertIdx] - 0.091 * detrender[(hilbertIdx + 1) % 3]) * adjustedPrevPeriod
                    Q1[hilbertIdx] = (0.091 * detrender[hilbertIdx] + 0.822 * Q1[(hilbertIdx - 2) % 3] - 0.411 * Q1[hilbertIdx] - 0.091 * Q1[(hilbertIdx + 1) % 3]) * adjustedPrevPeriod
                    jI[hilbertIdx] = (0.091 * I1ForOddPrev3 + 0.822 * jI[(hilbertIdx - 2) % 3] - 0.411 * jI[hilbertIdx] - 0.091 * jI[(hilbertIdx + 1) % 3]) * adjustedPrevPeriod
                    jQ[hilbertIdx] = (0.091 * Q1[hilbertIdx] + 0.822 * jQ[(hilbertIdx - 2) % 3] - 0.411 * jQ[hilbertIdx] - 0.091 * jQ[(hilbertIdx + 1) % 3]) * adjustedPrevPeriod
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
                smoothPeriod = (0.33 * period) + (0.67 * smoothPeriod)

                if today >= startIdx:
                    if outIdx < len(valid_indices):
                        orig_idx = valid_indices[today]
                        result[orig_idx, sec] = smoothPeriod
                        outIdx += 1
                today += 1

        return result



    @staticmethod
    @nb.njit
    def HT_PHASOR(high, open, low, close, vol, oi):
        tdts, secs = close.shape
        result_inphase = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        result_quadrature = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
        lookback_total = 32
        rad2deg = 180.0 / (4.0 * np.arctan(1.0))
    
        for sec in range(secs):
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            valid_close = close[valid_mask, sec]
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
        
            i = 9
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
        
            while today < len(valid_close):
                adjusted_prev_period = (0.075 * period) + 0.54
                today_value = valid_close[today]
                period_wma_sub += today_value
                period_wma_sub -= trailing_wma_value
                period_wma_sum += today_value * 4.0
                if trailing_wma_idx < len(valid_close):
                    trailing_wma_value = valid_close[trailing_wma_idx]
                    trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
            
                if (today % 2) == 0:
                    detrender_even[hilbert_idx] = smoothed_value
                    detrender = (0.0962 * detrender_even[hilbert_idx]) + (0.5769 * detrender_even[(hilbert_idx - 2) % 3]) - (0.5769 * detrender_even[(hilbert_idx - 1) % 3]) - (0.0962 * detrender_even[(hilbert_idx + 1) % 3])
                    q1_even[hilbert_idx] = detrender
                    q1 = (0.0962 * q1_even[hilbert_idx]) + (0.5769 * q1_even[(hilbert_idx - 2) % 3]) - (0.5769 * q1_even[(hilbert_idx - 1) % 3]) - (0.0962 * q1_even[(hilbert_idx + 1) % 3])
                    ji_even[hilbert_idx] = i1_for_even_prev3
                    ji = (0.0962 * ji_even[hilbert_idx]) + (0.5769 * ji_even[(hilbert_idx - 2) % 3]) - (0.5769 * ji_even[(hilbert_idx - 1) % 3]) - (0.0962 * ji_even[(hilbert_idx + 1) % 3])
                    jq_even[hilbert_idx] = q1
                    jq = (0.0962 * jq_even[hilbert_idx]) + (0.5769 * jq_even[(hilbert_idx - 2) % 3]) - (0.5769 * jq_even[(hilbert_idx - 1) % 3]) - (0.0962 * jq_even[(hilbert_idx + 1) % 3])
                    if today >= lookback_total:
                        out_idx = valid_indices[today]
                        result_quadrature[out_idx, sec] = q1
                        result_inphase[out_idx, sec] = i1_for_even_prev3
                    q2 = (0.2 * (q1 + ji)) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_even_prev3 - jq)) + (0.8 * prev_i2)
                    i1_for_odd_prev3 = i1_for_odd_prev2
                    i1_for_odd_prev2 = detrender
                else:
                    detrender_odd[hilbert_idx] = smoothed_value
                    detrender = (0.0962 * detrender_odd[hilbert_idx]) + (0.5769 * detrender_odd[(hilbert_idx - 2) % 3]) - (0.5769 * detrender_odd[(hilbert_idx - 1) % 3]) - (0.0962 * detrender_odd[(hilbert_idx + 1) % 3])
                    q1_odd[hilbert_idx] = detrender
                    q1 = (0.0962 * q1_odd[hilbert_idx]) + (0.5769 * q1_odd[(hilbert_idx - 2) % 3]) - (0.5769 * q1_odd[(hilbert_idx - 1) % 3]) - (0.0962 * q1_odd[(hilbert_idx + 1) % 3])
                    ji_odd[hilbert_idx] = i1_for_odd_prev3
                    ji = (0.0962 * ji_odd[hilbert_idx]) + (0.5769 * ji_odd[(hilbert_idx - 2) % 3]) - (0.5769 * ji_odd[(hilbert_idx - 1) % 3]) - (0.0962 * ji_odd[(hilbert_idx + 1) % 3])
                    jq_odd[hilbert_idx] = q1
                    jq = (0.0962 * jq_odd[hilbert_idx]) + (0.5769 * jq_odd[(hilbert_idx - 2) % 3]) - (0.5769 * jq_odd[(hilbert_idx - 1) % 3]) - (0.0962 * jq_odd[(hilbert_idx + 1) % 3])
                    if today >= lookback_total:
                        out_idx = valid_indices[today]
                        result_quadrature[out_idx, sec] = q1
                        result_inphase[out_idx, sec] = i1_for_odd_prev3
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
            
                if hilbert_idx == 2:
                    hilbert_idx = 0
                else:
                    hilbert_idx += 1
                
                today += 1
    
        return result_inphase, result_quadrature



    @staticmethod
    @nb.njit
    def HT_TRENDMODE(high, open, low, close, vol, oi):
        tdts, secs = close.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        lookback_total = 63  # As per C code, lookback total is 63 + unstable period, but we handle it directly as 63 for start index
    
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if close[i, sec] == close[i, sec]:
                    valid_mask[i] = True
        
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= lookback_total:
                continue
            
            valid_close = close[valid_mask, sec]
            output = np.zeros(len(valid_close))
        
            # Initialize variables as per C code
            i_trend1 = 0.0
            i_trend2 = 0.0
            i_trend3 = 0.0
            days_in_trend = 0
            prev_dc_phase = 0.0
            dc_phase = 0.0
            prev_sine = 0.0
            sine = 0.0
            prev_lead_sine = 0.0
            lead_sine = 0.0
        
            # Constants from C code
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
        
            # Initial WMA loop for 34 periods as per C code
            i = 34
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
        
            # Hilbert transform variables
            hilbert_idx = 0
            detrender = np.zeros(3)
            q1 = np.zeros(3)
            ji = np.zeros(3)
            jq = np.zeros(3)
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
            smooth_price_size = 64  # Assuming a reasonable size for circular buffer
            smooth_price = np.zeros(smooth_price_size)
            smooth_price_idx = 0
        
            while today < len(valid_close):
                adjusted_prev_period = (0.075 * period) + 0.54
                today_value = valid_close[today]
                # WMA calculation
                period_wma_sub += today_value
                period_wma_sub -= trailing_wma_value
                period_wma_sum += today_value * 4.0
                trailing_wma_value = valid_close[trailing_wma_idx]
                trailing_wma_idx += 1
                smoothed_value = period_wma_sum * 0.1
                period_wma_sum -= period_wma_sub
            
                smooth_price[smooth_price_idx] = smoothed_value
            
                if (today % 2) == 0:
                    # Even Hilbert transform
                    detrender[hilbert_idx] = (0.0962 * smoothed_value + 0.5769 * detrender[(hilbert_idx - 2) % 3] - 0.5769 * detrender[hilbert_idx] - 0.0962 * detrender[(hilbert_idx - 1) % 3]) * adjusted_prev_period
                    q1[hilbert_idx] = (0.0962 * detrender[hilbert_idx] + 0.5769 * q1[(hilbert_idx - 2) % 3] - 0.5769 * q1[hilbert_idx] - 0.0962 * q1[(hilbert_idx - 1) % 3]) * adjusted_prev_period
                    ji[hilbert_idx] = (0.0962 * i1_for_even_prev3 + 0.5769 * ji[(hilbert_idx - 2) % 3] - 0.5769 * ji[hilbert_idx] - 0.0962 * ji[(hilbert_idx - 1) % 3]) * adjusted_prev_period
                    jq[hilbert_idx] = (0.0962 * q1[hilbert_idx] + 0.5769 * jq[(hilbert_idx - 2) % 3] - 0.5769 * jq[hilbert_idx] - 0.0962 * jq[(hilbert_idx - 1) % 3]) * adjusted_prev_period
                    if hilbert_idx + 1 == 3:
                        hilbert_idx = 0
                    else:
                        hilbert_idx += 1
                    q2 = (0.2 * (q1[(hilbert_idx - 1) % 3] + ji[(hilbert_idx - 1) % 3])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_even_prev3 - jq[(hilbert_idx - 1) % 3])) + (0.8 * prev_i2)
                    i1_for_odd_prev3 = i1_for_odd_prev2
                    i1_for_odd_prev2 = detrender[(hilbert_idx - 1) % 3]
                else:
                    # Odd Hilbert transform
                    detrender[hilbert_idx] = (0.0962 * smoothed_value + 0.5769 * detrender[(hilbert_idx - 2) % 3] - 0.5769 * detrender[hilbert_idx] - 0.0962 * detrender[(hilbert_idx - 1) % 3]) * adjusted_prev_period
                    q1[hilbert_idx] = (0.0962 * detrender[hilbert_idx] + 0.5769 * q1[(hilbert_idx - 2) % 3] - 0.5769 * q1[hilbert_idx] - 0.0962 * q1[(hilbert_idx - 1) % 3]) * adjusted_prev_period
                    ji[hilbert_idx] = (0.0962 * i1_for_odd_prev3 + 0.5769 * ji[(hilbert_idx - 2) % 3] - 0.5769 * ji[hilbert_idx] - 0.0962 * ji[(hilbert_idx - 1) % 3]) * adjusted_prev_period
                    jq[hilbert_idx] = (0.0962 * q1[hilbert_idx] + 0.5769 * jq[(hilbert_idx - 2) % 3] - 0.5769 * jq[hilbert_idx] - 0.0962 * jq[(hilbert_idx - 1) % 3]) * adjusted_prev_period
                    q2 = (0.2 * (q1[hilbert_idx] + ji[hilbert_idx])) + (0.8 * prev_q2)
                    i2 = (0.2 * (i1_for_odd_prev3 - jq[hilbert_idx])) + (0.8 * prev_i2)
                    i1_for_even_prev3 = i1_for_even_prev2
                    i1_for_even_prev2 = detrender[hilbert_idx]
            
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
                    if idx >= len(smooth_price):
                        break
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
            
                prev_sine = sine
                prev_lead_sine = lead_sine
                sine = np.sin(dc_phase * deg2rad)
                lead_sine = np.sin((dc_phase + 45) * deg2rad)
            
                dc_period = smooth_period + 0.5
                dc_period_int = int(dc_period)
                idx = today
                temp_real = 0.0
                for i in range(dc_period_int):
                    if idx >= 0 and idx < len(valid_close):
                        temp_real += valid_close[idx]
                        idx -= 1
                if dc_period_int > 0:
                    temp_real = temp_real / float(dc_period_int)
            
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
                if smooth_period != 0.0 and ((temp_real > (0.67 * 360.0 / smooth_period)) and (temp_real < (1.5 * 360.0 / smooth_period))):
                    trend = 0
            
                temp_real = smooth_price[smooth_price_idx]
                if trendline != 0.0 and np.abs((temp_real - trendline) / trendline) >= 0.015:
                    trend = 1
            
                if today >= lookback_total:
                    output[today] = trend
            
                # Circular buffer next for smooth_price
                smooth_price_idx = (smooth_price_idx + 1) % smooth_price_size
                today += 1
        
            # Map results back to original array
            for i in range(len(valid_indices)):
                if valid_indices[i] >= lookback_total and i < len(output):
                    result[valid_indices[i], sec] = output[i]
    
        return result



    @staticmethod
    @nb.njit
    def ULTOSC(high, open, low, close, vol, oi, timeperiod1=7, timeperiod2=14, timeperiod3=28):
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
            if len(valid_indices) < max(timeperiod1, timeperiod2, timeperiod3):
                continue
            
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
        
            # Sort periods to ensure correct order (longest to shortest)
            periods = np.array([timeperiod1, timeperiod2, timeperiod3])
            sorted_periods = np.sort(periods)[::-1]  # Descending order
            opt_timeperiod1 = sorted_periods[0]
            opt_timeperiod2 = sorted_periods[1]
            opt_timeperiod3 = sorted_periods[2]
        
            # Calculate lookback period
            lookback_total = opt_timeperiod1 - 1
        
            # Check if we have enough data
            if len(valid_high) <= lookback_total:
                continue
            
            # Initialize totals for each period
            a1_total = 0.0
            a2_total = 0.0
            a3_total = 0.0
            b1_total = 0.0
            b2_total = 0.0
            b3_total = 0.0
        
            # Prime the totals for each period
            for i in range(lookback_total - opt_timeperiod1 + 1, lookback_total):
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
            
            for i in range(lookback_total - opt_timeperiod2 + 1, lookback_total):
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
            
            for i in range(lookback_total - opt_timeperiod3 + 1, lookback_total):
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
            trailing_idx1 = today - opt_timeperiod1 + 1
            trailing_idx2 = today - opt_timeperiod2 + 1
            trailing_idx3 = today - opt_timeperiod3 + 1
        
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



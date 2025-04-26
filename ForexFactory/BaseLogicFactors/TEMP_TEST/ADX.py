import numba as nb
import numpy as np
from operators import *
from baselogicfactors import getavailabledata
import matplotlib.pyplot as plt
import talib
import time


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

def test_ADX():
    """
    # 测试ADX指标的实现与TA-Lib的对比
    # 生成随机数据，计算指标，比较结果
    """
    # 设置随机种子确保可复现
    np.random.seed(42)
    
    # 生成样本数据
    num_samples = 2000
    num_securities = 1  # 只测试一个证券
    
    # 生成基础价格数据
    base_price = 100 + np.cumsum(np.random.normal(0, 1, (num_samples, num_securities)), axis=0)
    
    # 生成符合要求的OHLCV+OI数据
    high = base_price + np.random.uniform(0, 2, (num_samples, num_securities))
    low = base_price - np.random.uniform(0, 2, (num_samples, num_securities))
    open_price = low + np.random.uniform(0, 1, (num_samples, num_securities)) * (high - low)
    close = open_price + np.random.uniform(-1, 1, (num_samples, num_securities))
    vol = np.random.uniform(1000, 5000, (num_samples, num_securities))
    oi = np.random.uniform(5000, 10000, (num_samples, num_securities))
    
    # 插入一些NaN值
    nan_indices = np.random.choice(num_samples, size=int(num_samples * 0.05), replace=False)
    for idx in nan_indices:
        if np.random.random() < 0.5:
            high[idx, 0] = np.nan
        if np.random.random() < 0.5:
            low[idx, 0] = np.nan
        if np.random.random() < 0.5:
            close[idx, 0] = np.nan
        if np.random.random() < 0.5:
            open_price[idx, 0] = np.nan
        if np.random.random() < 0.5:
            vol[idx, 0] = np.nan
        if np.random.random() < 0.5:
            oi[idx, 0] = np.nan
    
    # 确保数据有效：high >= low
    for i in range(num_samples):
        for j in range(num_securities):
            if (high[i,j] == high[i,j] and low[i,j] == low[i,j] and 
                high[i,j] < low[i,j]):
                high[i,j], low[i,j] = low[i,j], high[i,j]
    
    print(f"生成了{num_samples}个样本点，包含{len(nan_indices)}个带有NaN值的位置")
    
    # 设置ADX周期
    timeperiod = 14
    
    # 计时并计算自定义ADX指标
    start_time = time.time()
    our_adx = ADX(high, open_price, low, close, vol, oi, timeperiod=timeperiod)
    our_time = time.time() - start_time
    print(f"自定义ADX计算用时: {our_time:.4f}秒")
    
    # 使用TA-Lib计算ADX指标
    start_time = time.time()
    
    # TA-Lib需要一维数组作为输入，且不接受NaN值
    high_1d = high[:, 0]
    low_1d = low[:, 0]
    close_1d = close[:, 0]
    
    # 使用掩码处理NaN值
    mask = ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d)
    
    if np.sum(mask) > 0:
        talib_high = high_1d[mask]
        talib_low = low_1d[mask]
        talib_close = close_1d[mask]
        
        # 计算TA-Lib的ADX
        talib_adx_result = talib.ADX(talib_high, talib_low, talib_close, timeperiod=timeperiod)
        
        # 重建结果数组，填充NaN
        talib_adx = np.full(num_samples, np.nan)
        talib_adx[np.where(mask)[0][-len(talib_adx_result):]] = talib_adx_result
    else:
        talib_adx = np.full(num_samples, np.nan)
    
    talib_time = time.time() - start_time
    print(f"TA-Lib ADX计算用时: {talib_time:.4f}秒")
    
    # 准备比较结果
    our_adx_flat = our_adx[:, 0]  # 提取第一个证券的结果
    
    # 计算相关性和均方误差
    mask = ~np.isnan(our_adx_flat) & ~np.isnan(talib_adx)
    if np.sum(mask) > 0:
        correlation = np.corrcoef(our_adx_flat[mask], talib_adx[mask])[0, 1]
        mse = np.mean((our_adx_flat[mask] - talib_adx[mask])**2)
        mae = np.mean(np.abs(our_adx_flat[mask] - talib_adx[mask]))
        
        print(f"相关系数: {correlation:.6f}")
        print(f"均方误差: {mse:.6f}")
        print(f"平均绝对误差: {mae:.6f}")
        print(f"我们的实现有效数据点: {np.sum(~np.isnan(our_adx_flat))}")
        print(f"TA-Lib有效数据点: {np.sum(~np.isnan(talib_adx))}")
        print(f"共同有效数据点: {np.sum(mask)}")
    else:
        print("没有足够的非NaN值进行比较")
    
    # 绘制结果比较图
    plt.figure(figsize=(12, 10))
    
    # 创建ADX值比较图
    ax1 = plt.subplot(3, 1, 1)
    valid_indices = np.where(mask)[0]
    if len(valid_indices) > 0:
        min_idx = np.min(valid_indices)
        max_idx = np.max(valid_indices)
        plot_range = range(min_idx, max_idx + 1)
        ax1.plot(plot_range, our_adx_flat[plot_range], 'b-', label='自定义ADX')
        ax1.plot(plot_range, talib_adx[plot_range], 'r--', label='TA-Lib ADX')
        ax1.set_title('ADX指标比较')
        ax1.set_ylabel('ADX值')
        ax1.legend()
        ax1.grid(True)
    
    # 创建差值图
    ax2 = plt.subplot(3, 1, 2)
    if len(valid_indices) > 0:
        difference = our_adx_flat - talib_adx
        ax2.plot(plot_range, difference[plot_range], 'g-', label='差值 (自定义 - TA-Lib)')
        ax2.axhline(y=0, color='r', linestyle='-', alpha=0.3)
        ax2.set_title('ADX差值')
        ax2.set_ylabel('差值')
        ax2.legend()
        ax2.grid(True)
    
    # 创建价格和ADX图
    ax3 = plt.subplot(3, 1, 3)
    if len(valid_indices) > 0:
        ax3.plot(plot_range, close[plot_range, 0], 'k-', label='收盘价', alpha=0.7)
        ax3_twin = ax3.twinx()
        ax3_twin.plot(plot_range, our_adx_flat[plot_range], 'b-', label='自定义ADX', alpha=0.8)
        ax3.set_title('价格与ADX关系')
        ax3.set_xlabel('时间')
        ax3.set_ylabel('价格', color='k')
        ax3_twin.set_ylabel('ADX值', color='b')
        
        # 合并两个y轴的图例
        lines1, labels1 = ax3.get_legend_handles_labels()
        lines2, labels2 = ax3_twin.get_legend_handles_labels()
        ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        ax3.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_ADX()
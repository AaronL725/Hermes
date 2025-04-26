import numba as nb
import numpy as np
from operators import *
from baselogicfactors import getavailabledata
import matplotlib.pyplot as plt
import talib
import time


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


def test_ADOSC():
    """
    # 测试ADOSC指标的实现与TA-Lib的对比
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
    
    # 设置ADOSC参数
    fast_period = 3
    slow_period = 10
    
    # 计时并计算自定义ADOSC指标
    start_time = time.time()
    our_adosc = ADOSC(high, open_price, low, close, vol, oi, fast_period=fast_period, slow_period=slow_period)
    our_time = time.time() - start_time
    print(f"自定义ADOSC计算用时: {our_time:.4f}秒")
    
    # 使用TA-Lib计算ADOSC指标
    start_time = time.time()
    
    # TA-Lib需要一维数组作为输入，且不接受NaN值
    high_1d = high[:, 0]
    low_1d = low[:, 0]
    close_1d = close[:, 0]
    vol_1d = vol[:, 0]
    
    # 使用掩码处理NaN值
    mask = ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d) & ~np.isnan(vol_1d)
    
    if np.sum(mask) > 0:
        talib_high = high_1d[mask]
        talib_low = low_1d[mask]
        talib_close = close_1d[mask]
        talib_vol = vol_1d[mask]
        
        # 计算TA-Lib的ADOSC
        talib_adosc_result = talib.ADOSC(talib_high, talib_low, talib_close, talib_vol, 
                                         fastperiod=fast_period, slowperiod=slow_period)
        
        # 重建结果数组，填充NaN
        talib_adosc = np.full(num_samples, np.nan)
        talib_adosc[np.where(mask)[0][-len(talib_adosc_result):]] = talib_adosc_result
    else:
        talib_adosc = np.full(num_samples, np.nan)
    
    talib_time = time.time() - start_time
    print(f"TA-Lib ADOSC计算用时: {talib_time:.4f}秒")
    
    # 准备比较结果
    our_adosc_flat = our_adosc[:, 0]  # 提取第一个证券的结果
    
    # 计算相关性和均方误差
    mask = ~np.isnan(our_adosc_flat) & ~np.isnan(talib_adosc)
    if np.sum(mask) > 0:
        correlation = np.corrcoef(our_adosc_flat[mask], talib_adosc[mask])[0, 1]
        mse = np.mean((our_adosc_flat[mask] - talib_adosc[mask])**2)
        mae = np.mean(np.abs(our_adosc_flat[mask] - talib_adosc[mask]))
        
        print(f"相关系数: {correlation:.6f}")
        print(f"均方误差: {mse:.6f}")
        print(f"平均绝对误差: {mae:.6f}")
        print(f"我们的实现有效数据点: {np.sum(~np.isnan(our_adosc_flat))}")
        print(f"TA-Lib有效数据点: {np.sum(~np.isnan(talib_adosc))}")
        print(f"共同有效数据点: {np.sum(mask)}")
    else:
        print("没有足够的非NaN值进行比较")
    
    # 绘制结果比较图
    plt.figure(figsize=(12, 10))
    
    # 创建ADOSC值比较图
    ax1 = plt.subplot(3, 1, 1)
    valid_indices = np.where(mask)[0]
    if len(valid_indices) > 0:
        min_idx = np.min(valid_indices)
        max_idx = np.max(valid_indices)
        plot_range = range(min_idx, max_idx + 1)
        ax1.plot(plot_range, our_adosc_flat[plot_range], 'b-', label='自定义ADOSC')
        ax1.plot(plot_range, talib_adosc[plot_range], 'r--', label='TA-Lib ADOSC')
        ax1.set_title('ADOSC指标比较')
        ax1.set_ylabel('ADOSC值')
        ax1.legend()
        ax1.grid(True)
    
    # 创建差值图
    ax2 = plt.subplot(3, 1, 2)
    if len(valid_indices) > 0:
        difference = our_adosc_flat - talib_adosc
        ax2.plot(plot_range, difference[plot_range], 'g-', label='差值 (自定义 - TA-Lib)')
        ax2.axhline(y=0, color='r', linestyle='-', alpha=0.3)
        ax2.set_title('ADOSC差值')
        ax2.set_ylabel('差值')
        ax2.legend()
        ax2.grid(True)
    
    # 创建价格和ADOSC图
    ax3 = plt.subplot(3, 1, 3)
    if len(valid_indices) > 0:
        ax3.plot(plot_range, close[plot_range, 0], 'k-', label='收盘价', alpha=0.7)
        ax3_twin = ax3.twinx()
        ax3_twin.plot(plot_range, our_adosc_flat[plot_range], 'b-', label='自定义ADOSC', alpha=0.8)
        ax3.set_title('价格与ADOSC关系')
        ax3.set_xlabel('时间')
        ax3.set_ylabel('价格', color='k')
        ax3_twin.set_ylabel('ADOSC值', color='b')
        
        # 合并两个y轴的图例
        lines1, labels1 = ax3.get_legend_handles_labels()
        lines2, labels2 = ax3_twin.get_legend_handles_labels()
        ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        ax3.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_ADOSC()
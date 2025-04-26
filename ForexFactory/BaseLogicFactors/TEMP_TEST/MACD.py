import numba as nb
import numpy as np
from operators import *
from baselogicfactors import getavailabledata
import matplotlib.pyplot as plt
import talib
import time


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

def test_MACD():
    """
    # 测试MACD指标的实现与TA-Lib的对比
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
    close = low + np.random.uniform(0, 1, (num_samples, num_securities)) * (high - low)
    open_price = low + np.random.uniform(0, 1, (num_samples, num_securities)) * (high - low)
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
    
    # 确保数据有效
    for i in range(num_samples):
        for j in range(num_securities):
            if (high[i,j] == high[i,j] and low[i,j] == low[i,j] and 
                high[i,j] < low[i,j]):
                high[i,j], low[i,j] = low[i,j], high[i,j]
    
    print(f"生成了{num_samples}个样本点，包含{len(nan_indices)}个带有NaN值的位置")
    
    # 设置MACD参数
    fastperiod = 12
    slowperiod = 26
    signalperiod = 9
    
    # 计时并计算自定义MACD指标
    start_time = time.time()
    our_macd, our_macd_signal, our_macd_hist = MACD(high, open_price, low, close, vol, oi, 
                                                   fastperiod, slowperiod, signalperiod)
    our_time = time.time() - start_time
    print(f"自定义MACD计算用时: {our_time:.4f}秒")
    
    # 使用TA-Lib计算MACD指标
    start_time = time.time()
    
    # TA-Lib需要一维数组作为输入，且不接受NaN值
    close_1d = close[:, 0]
    
    # 使用掩码处理NaN值
    mask = ~np.isnan(close_1d)
    
    # 初始化TA-Lib结果数组
    talib_macd = np.full(num_samples, np.nan)
    talib_macd_signal = np.full(num_samples, np.nan)
    talib_macd_hist = np.full(num_samples, np.nan)
    
    if np.sum(mask) > 0:
        talib_close = close_1d[mask]
        
        # 计算TA-Lib的MACD
        talib_macd_result, talib_signal_result, talib_hist_result = talib.MACD(
            talib_close, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
        
        # 重建结果数组，填充NaN
        valid_indices = np.where(mask)[0]
        for i in range(len(talib_macd_result)):
            if i < len(valid_indices):
                idx = valid_indices[i]
                if idx < len(talib_macd) and i < len(talib_macd_result):
                    if not np.isnan(talib_macd_result[i]):
                        talib_macd[idx] = talib_macd_result[i]
                    if not np.isnan(talib_signal_result[i]):
                        talib_macd_signal[idx] = talib_signal_result[i]
                    if not np.isnan(talib_hist_result[i]):
                        talib_macd_hist[idx] = talib_hist_result[i]
    
    talib_time = time.time() - start_time
    print(f"TA-Lib MACD计算用时: {talib_time:.4f}秒")
    
    # 准备比较结果
    our_macd_flat = our_macd[:, 0]  # 提取第一个证券的结果
    our_signal_flat = our_macd_signal[:, 0]
    our_hist_flat = our_macd_hist[:, 0]
    
    # 计算MACD线的非NaN值的相对误差
    mask_macd = ~np.isnan(our_macd_flat) & ~np.isnan(talib_macd)
    if np.sum(mask_macd) > 0:
        # 相对误差计算
        relative_error_macd = np.abs((our_macd_flat[mask_macd] - talib_macd[mask_macd]) / 
                                     (np.abs(talib_macd[mask_macd]) + 1e-10))
        avg_rel_error_macd = np.mean(relative_error_macd)
        max_rel_error_macd = np.max(relative_error_macd)
        
        print(f"MACD线平均相对误差: {avg_rel_error_macd:.8f}")
        print(f"MACD线最大相对误差: {max_rel_error_macd:.8f}")
    else:
        print("MACD线没有足够的非NaN值进行比较")
    
    # 计算信号线的非NaN值的相对误差
    mask_signal = ~np.isnan(our_signal_flat) & ~np.isnan(talib_macd_signal)
    if np.sum(mask_signal) > 0:
        relative_error_signal = np.abs((our_signal_flat[mask_signal] - talib_macd_signal[mask_signal]) / 
                                       (np.abs(talib_macd_signal[mask_signal]) + 1e-10))
        avg_rel_error_signal = np.mean(relative_error_signal)
        max_rel_error_signal = np.max(relative_error_signal)
        
        print(f"信号线平均相对误差: {avg_rel_error_signal:.8f}")
        print(f"信号线最大相对误差: {max_rel_error_signal:.8f}")
    else:
        print("信号线没有足够的非NaN值进行比较")
    
    # 计算直方图的非NaN值的相对误差
    mask_hist = ~np.isnan(our_hist_flat) & ~np.isnan(talib_macd_hist)
    if np.sum(mask_hist) > 0:
        relative_error_hist = np.abs((our_hist_flat[mask_hist] - talib_macd_hist[mask_hist]) / 
                                     (np.abs(talib_macd_hist[mask_hist]) + 1e-10))
        avg_rel_error_hist = np.mean(relative_error_hist)
        max_rel_error_hist = np.max(relative_error_hist)
        
        print(f"直方图平均相对误差: {avg_rel_error_hist:.8f}")
        print(f"直方图最大相对误差: {max_rel_error_hist:.8f}")
    else:
        print("直方图没有足够的非NaN值进行比较")
    
    # 绘制结果比较图 - MACD线
    plt.figure(figsize=(12, 6))
    plt.subplot(3, 1, 1)
    plt.plot(our_macd_flat, label='自定义MACD实现', alpha=0.7)
    plt.plot(talib_macd, label='TA-Lib MACD', alpha=0.7, linestyle='--')
    plt.title('MACD线比较')
    plt.ylabel('MACD值')
    plt.legend()
    plt.grid(True)
    
    # 绘制信号线
    plt.subplot(3, 1, 2)
    plt.plot(our_signal_flat, label='自定义信号线实现', alpha=0.7)
    plt.plot(talib_macd_signal, label='TA-Lib信号线', alpha=0.7, linestyle='--')
    plt.title('信号线比较')
    plt.ylabel('信号值')
    plt.legend()
    plt.grid(True)
    
    # 绘制直方图
    plt.subplot(3, 1, 3)
    plt.plot(our_hist_flat, label='自定义直方图实现', alpha=0.7)
    plt.plot(talib_macd_hist, label='TA-Lib直方图', alpha=0.7, linestyle='--')
    plt.title('直方图比较')
    plt.xlabel('时间')
    plt.ylabel('直方图值')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_MACD()

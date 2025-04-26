import numba as nb
import numpy as np
from operators import *
from baselogicfactors import getavailabledata
import matplotlib.pyplot as plt
import talib
import time
import matplotlib
# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']  # 优先使用的中文字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题


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

def test_ATR():
    """
    # 测试ATR指标的实现与TA-Lib的对比
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
    
    # 设置ATR周期
    timeperiod = 14
    
    # 计时并计算自定义ATR指标
    start_time = time.time()
    our_atr = ATR(high, open_price, low, close, vol, oi, timeperiod=timeperiod)
    our_time = time.time() - start_time
    print(f"自定义ATR计算用时: {our_time:.4f}秒")
    
    # 使用TA-Lib计算ATR指标
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
        
        # 计算TA-Lib的ATR
        talib_atr_result = talib.ATR(talib_high, talib_low, talib_close, timeperiod=timeperiod)
        
        # 重建结果数组，填充NaN
        talib_atr = np.full(num_samples, np.nan)
        talib_atr[np.where(mask)[0][-len(talib_atr_result):]] = talib_atr_result
    else:
        talib_atr = np.full(num_samples, np.nan)
    
    talib_time = time.time() - start_time
    print(f"TA-Lib ATR计算用时: {talib_time:.4f}秒")
    
    # 准备比较结果
    our_atr_flat = our_atr[:, 0]  # 提取第一个证券的结果
    
    # 计算相关性和均方误差
    mask = ~np.isnan(our_atr_flat) & ~np.isnan(talib_atr)
    if np.sum(mask) > 0:
        correlation = np.corrcoef(our_atr_flat[mask], talib_atr[mask])[0, 1]
        mse = np.mean((our_atr_flat[mask] - talib_atr[mask])**2)
        mae = np.mean(np.abs(our_atr_flat[mask] - talib_atr[mask]))
        
        print(f"相关系数: {correlation:.6f}")
        print(f"均方误差: {mse:.6f}")
        print(f"平均绝对误差: {mae:.6f}")
        print(f"我们的实现有效数据点: {np.sum(~np.isnan(our_atr_flat))}")
        print(f"TA-Lib有效数据点: {np.sum(~np.isnan(talib_atr))}")
        print(f"共同有效数据点: {np.sum(mask)}")
    else:
        print("没有足够的非NaN值进行比较")
    
    # 绘制结果比较图
    plt.figure(figsize=(12, 10))
    
    # 创建ATR值比较图
    ax1 = plt.subplot(3, 1, 1)
    valid_indices = np.where(mask)[0]
    if len(valid_indices) > 0:
        min_idx = np.min(valid_indices)
        max_idx = np.max(valid_indices)
        plot_range = range(min_idx, max_idx + 1)
        ax1.plot(plot_range, our_atr_flat[plot_range], 'b-', label='自定义ATR')
        ax1.plot(plot_range, talib_atr[plot_range], 'r--', label='TA-Lib ATR')
        ax1.set_title('ATR指标比较')
        ax1.set_ylabel('ATR值')
        ax1.legend()
        ax1.grid(True)
    
    # 创建差值图
    ax2 = plt.subplot(3, 1, 2)
    if len(valid_indices) > 0:
        difference = our_atr_flat - talib_atr
        ax2.plot(plot_range, difference[plot_range], 'g-', label='差值 (自定义 - TA-Lib)')
        ax2.axhline(y=0, color='r', linestyle='-', alpha=0.3)
        ax2.set_title('ATR差值')
        ax2.set_ylabel('差值')
        ax2.legend()
        ax2.grid(True)
    
    # 创建价格和ATR图
    ax3 = plt.subplot(3, 1, 3)
    if len(valid_indices) > 0:
        ax3.plot(plot_range, close[plot_range, 0], 'k-', label='收盘价', alpha=0.7)
        ax3_twin = ax3.twinx()
        ax3_twin.plot(plot_range, our_atr_flat[plot_range], 'b-', label='自定义ATR', alpha=0.8)
        ax3.set_title('价格与ATR关系')
        ax3.set_xlabel('时间')
        ax3.set_ylabel('价格', color='k')
        ax3_twin.set_ylabel('ATR值', color='b')
        
        # 合并两个y轴的图例
        lines1, labels1 = ax3.get_legend_handles_labels()
        lines2, labels2 = ax3_twin.get_legend_handles_labels()
        ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        ax3.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_ATR()

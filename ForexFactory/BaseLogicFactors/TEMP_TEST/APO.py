import numba as nb
import numpy as np
from operators import *
from baselogicfactors import getavailabledata
import matplotlib.pyplot as plt
import talib
import time


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


def test_APO():
    """
    # 测试APO指标的实现与TA-Lib的对比
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
            close[idx, 0] = np.nan
    
    print(f"生成了{num_samples}个样本点，包含{len(nan_indices)}个带有NaN值的位置")
    
    # 设置APO参数
    fastperiod = 12
    slowperiod = 26
    matype = 0
    
    # 计时并计算自定义APO指标
    start_time = time.time()
    our_apo = APO(high, open_price, low, close, vol, oi, fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
    our_time = time.time() - start_time
    print(f"自定义APO计算用时: {our_time:.4f}秒")
    
    # 使用TA-Lib计算APO指标
    start_time = time.time()
    
    # TA-Lib需要一维数组作为输入，且不接受NaN值
    close_1d = close[:, 0]
    
    # 使用掩码处理NaN值
    mask = ~np.isnan(close_1d)
    
    if np.sum(mask) > 0:
        talib_close = close_1d[mask]
        
        # 确保有足够的数据计算APO
        if len(talib_close) >= max(fastperiod, slowperiod):
            # 计算TA-Lib的APO
            talib_apo_result = talib.APO(talib_close, fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
            
            # 重建结果数组，填充NaN
            talib_apo = np.full(num_samples, np.nan)
            talib_apo[np.where(mask)[0][-len(talib_apo_result):]] = talib_apo_result
        else:
            print("警告: TA-Lib没有足够的有效数据计算APO")
            talib_apo = np.full(num_samples, np.nan)
    else:
        talib_apo = np.full(num_samples, np.nan)
    
    talib_time = time.time() - start_time
    print(f"TA-Lib APO计算用时: {talib_time:.4f}秒")
    
    # 准备比较结果
    our_apo_flat = our_apo[:, 0]  # 提取第一个证券的结果
    
    # 计算相关性和均方误差
    mask = ~np.isnan(our_apo_flat) & ~np.isnan(talib_apo)
    if np.sum(mask) > 0:
        correlation = np.corrcoef(our_apo_flat[mask], talib_apo[mask])[0, 1]
        mse = np.mean((our_apo_flat[mask] - talib_apo[mask])**2)
        mae = np.mean(np.abs(our_apo_flat[mask] - talib_apo[mask]))
        
        print(f"相关系数: {correlation:.6f}")
        print(f"均方误差: {mse:.6f}")
        print(f"平均绝对误差: {mae:.6f}")
        print(f"我们的实现有效数据点: {np.sum(~np.isnan(our_apo_flat))}")
        print(f"TA-Lib有效数据点: {np.sum(~np.isnan(talib_apo))}")
        print(f"共同有效数据点: {np.sum(mask)}")
    else:
        print("没有足够的非NaN值进行比较")
    
    # 绘制结果比较图
    plt.figure(figsize=(12, 10))
    
    # 创建APO值比较图
    ax1 = plt.subplot(3, 1, 1)
    valid_indices = np.where(mask)[0]
    if len(valid_indices) > 0:
        min_idx = np.min(valid_indices)
        max_idx = np.max(valid_indices)
        plot_range = range(min_idx, max_idx + 1)
        ax1.plot(plot_range, our_apo_flat[plot_range], 'b-', label='自定义APO')
        ax1.plot(plot_range, talib_apo[plot_range], 'r--', label='TA-Lib APO')
        ax1.set_title('APO指标比较')
        ax1.set_ylabel('APO值')
        ax1.legend()
        ax1.grid(True)
    
    # 创建差值图
    ax2 = plt.subplot(3, 1, 2)
    if len(valid_indices) > 0:
        difference = our_apo_flat - talib_apo
        ax2.plot(plot_range, difference[plot_range], 'g-', label='差值 (自定义 - TA-Lib)')
        ax2.axhline(y=0, color='r', linestyle='-', alpha=0.3)
        ax2.set_title('APO差值')
        ax2.set_ylabel('差值')
        ax2.legend()
        ax2.grid(True)
    
    # 创建价格和APO图
    ax3 = plt.subplot(3, 1, 3)
    if len(valid_indices) > 0:
        ax3.plot(plot_range, close[plot_range, 0], 'k-', label='收盘价', alpha=0.7)
        ax3_twin = ax3.twinx()
        ax3_twin.plot(plot_range, our_apo_flat[plot_range], 'b-', label='自定义APO', alpha=0.8)
        ax3.set_title('价格与APO关系')
        ax3.set_xlabel('时间')
        ax3.set_ylabel('价格', color='k')
        ax3_twin.set_ylabel('APO值', color='b')
        
        # 合并两个y轴的图例
        lines1, labels1 = ax3.get_legend_handles_labels()
        lines2, labels2 = ax3_twin.get_legend_handles_labels()
        ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        ax3.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_APO()



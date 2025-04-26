import numba as nb
import numpy as np
from operators import *
from baselogicfactors import getavailabledata
import matplotlib.pyplot as plt
import talib
import time


@nb.njit
def CDLDOJI(high, open, low, close, vol, oi):
    # 获取数据维度
    tdts, secs = high.shape
    
    # 初始化结果数组
    result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    
    # BodyDoji的平均周期，通常为3
    BodyDojiPeriod = 3
    
    for sec in range(secs):
        for ts in range(tdts):
            # 数据验证
            if ts <= BodyDojiPeriod or close[ts, sec] != close[ts, sec]:
                continue
                
            # 数据准备
            _high = high[:ts + 1, sec]
            _open = open[:ts + 1, sec]
            _low = low[:ts + 1, sec]
            _close = close[:ts + 1, sec]
            _vol = vol[:ts + 1, sec]
            _oi = oi[:ts + 1, sec]
            
            # 使用getavailabledata函数获取可用数据
            myopen = getavailabledata(_open, ts + 1)
            myhigh = getavailabledata(_high, ts + 1)
            myclose = getavailabledata(_close, ts + 1)
            mylow = getavailabledata(_low, ts + 1)
            myvol = getavailabledata(_vol, ts + 1)
            myoi = getavailabledata(_oi, ts + 1)
            
            # 计算实体大小
            realbody = np.abs(myclose - myopen)
            
            # 计算蜡烛图范围（这里假设BodyDoji类型对应高低点之差的一定比例）
            candleRange = myhigh - mylow
            
            # 初始化BodyDojiPeriodTotal
            BodyDojiPeriodTotal = 0
            
            # 计算前BodyDojiPeriod个周期的candleRange总和
            for i in range(ts - BodyDojiPeriod, ts):
                # 确保数据有效
                if i >= 0 and candleRange[i] == candleRange[i]:
                    BodyDojiPeriodTotal += candleRange[i]
            
            # 计算平均值
            if BodyDojiPeriod > 0:
                BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod
            else:
                BodyDojiAverage = 0
                
            # Doji判断：实体大小小于等于平均范围的一定比例
            # 设定一个较小的系数，例如0.1，表示实体大小不超过平均范围的10%
            DojiBodyCoef = 0.1
            
            # 判断当前k线是否是Doji
            if realbody[ts] <= BodyDojiAverage * DojiBodyCoef:
                result[ts, sec] = 100
            else:
                result[ts, sec] = 0
                
    return result

def test_CDLDOJI():
    """
    # 测试CDLDOJI指标的实现与TA-Lib的对比
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
    
    # 为了生成更多的Doji模式，让部分数据的开盘价和收盘价非常接近
    open_price = low + np.random.uniform(0, 1, (num_samples, num_securities)) * (high - low)
    close = np.copy(open_price)
    
    # 在30%的样本中引入小的差异，模拟Doji模式
    doji_indices = np.random.choice(num_samples, size=int(num_samples * 0.3), replace=False)
    for idx in doji_indices:
        # 很小的价差，模拟Doji
        close[idx, 0] = open_price[idx, 0] + np.random.uniform(-0.1, 0.1, 1)[0]
    
    # 在其他样本中引入更大的差异，模拟非Doji模式
    non_doji_indices = np.setdiff1d(np.arange(num_samples), doji_indices)
    for idx in non_doji_indices:
        # 较大的价差，模拟非Doji
        close[idx, 0] = open_price[idx, 0] + np.random.uniform(-1.5, 1.5, 1)[0]
    
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
    
    # 计时并计算自定义CDLDOJI指标
    start_time = time.time()
    our_doji = CDLDOJI(high, open_price, low, close, vol, oi)
    our_time = time.time() - start_time
    print(f"自定义CDLDOJI计算用时: {our_time:.4f}秒")
    
    # 使用TA-Lib计算CDLDOJI指标
    start_time = time.time()
    
    # TA-Lib需要一维数组作为输入，且不接受NaN值
    high_1d = high[:, 0]
    low_1d = low[:, 0]
    close_1d = close[:, 0]
    open_1d = open_price[:, 0]
    
    # 使用掩码处理NaN值
    mask = ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d) & ~np.isnan(open_1d)
    
    if np.sum(mask) > 0:
        talib_high = high_1d[mask]
        talib_low = low_1d[mask]
        talib_close = close_1d[mask]
        talib_open = open_1d[mask]
        
        # 计算TA-Lib的CDLDOJI
        talib_doji_result = talib.CDLDOJI(talib_open, talib_high, talib_low, talib_close)
        
        # 重建结果数组，填充NaN
        talib_doji = np.full(num_samples, np.nan)
        talib_doji[np.where(mask)[0]] = talib_doji_result
    else:
        talib_doji = np.full(num_samples, np.nan)
    
    talib_time = time.time() - start_time
    print(f"TA-Lib CDLDOJI计算用时: {talib_time:.4f}秒")
    
    # 准备比较结果
    our_doji_flat = our_doji[:, 0]  # 提取第一个证券的结果
    
    # 计算一致性（因为是离散值，我们计算模式识别的一致率）
    mask = ~np.isnan(our_doji_flat) & ~np.isnan(talib_doji)
    if np.sum(mask) > 0:
        # 一致性计算
        agreement = np.sum((our_doji_flat[mask] > 0) == (talib_doji[mask] > 0)) / np.sum(mask)
        both_positive = np.sum((our_doji_flat[mask] > 0) & (talib_doji[mask] > 0)) / np.sum(our_doji_flat[mask] > 0) if np.sum(our_doji_flat[mask] > 0) > 0 else 0
        both_negative = np.sum((our_doji_flat[mask] == 0) & (talib_doji[mask] == 0)) / np.sum(our_doji_flat[mask] == 0) if np.sum(our_doji_flat[mask] == 0) > 0 else 0
        
        print(f"总体一致率: {agreement:.4f}")
        print(f"识别为Doji的一致率: {both_positive:.4f}")
        print(f"识别为非Doji的一致率: {both_negative:.4f}")
        print(f"我们的实现识别出的Doji数量: {np.sum(our_doji_flat[mask] > 0)}")
        print(f"TA-Lib识别出的Doji数量: {np.sum(talib_doji[mask] > 0)}")
    else:
        print("没有足够的非NaN值进行比较")
    
    # 绘制结果比较图
    plt.figure(figsize=(12, 6))
    
    # 创建一个展示两种实现都识别的Doji的子图
    ax1 = plt.subplot(2, 1, 1)
    ax1.scatter(np.where(our_doji_flat > 0)[0], np.ones(np.sum(our_doji_flat > 0)), 
               c='blue', marker='o', alpha=0.5, label='自定义CDLDOJI')
    ax1.scatter(np.where(talib_doji > 0)[0], np.ones(np.sum(talib_doji > 0)) * 0.8, 
               c='red', marker='x', alpha=0.5, label='TA-Lib CDLDOJI')
    ax1.set_title('Doji识别结果比较')
    ax1.set_ylabel('Doji识别')
    ax1.legend()
    ax1.grid(True)
    
    # 创建子图展示原始价格数据，以及识别出的Doji位置
    ax2 = plt.subplot(2, 1, 2)
    ax2.plot(close[:, 0], label='收盘价', alpha=0.7, color='black')
    
    # 标记两种实现都识别出的Doji
    both_doji = (our_doji_flat > 0) & (talib_doji > 0)
    only_ours = (our_doji_flat > 0) & (~(talib_doji > 0))
    only_talib = (~(our_doji_flat > 0)) & (talib_doji > 0)
    
    ax2.scatter(np.where(both_doji)[0], close[both_doji, 0], 
               c='green', marker='o', alpha=0.8, label='两者都识别的Doji')
    ax2.scatter(np.where(only_ours)[0], close[only_ours, 0], 
               c='blue', marker='^', alpha=0.8, label='仅自定义实现识别的Doji')
    ax2.scatter(np.where(only_talib)[0], close[only_talib, 0], 
               c='red', marker='x', alpha=0.8, label='仅TA-Lib识别的Doji')
    
    ax2.set_title('价格数据与Doji识别')
    ax2.set_xlabel('时间')
    ax2.set_ylabel('价格')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_CDLDOJI()




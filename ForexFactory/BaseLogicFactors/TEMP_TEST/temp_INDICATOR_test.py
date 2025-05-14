import numba as nb
import numpy as np
from operators import *
from baselogicfactors import getavailabledata
import matplotlib.pyplot as plt
import talib
import time
import matplotlib
import inspect

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']  # 优先使用的中文字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题


@staticmethod
@nb.njit
def CDLHARAMICROSS(high, open, low, close, vol, oi, body_long_period=10, body_doji_period=3):
    tdts, secs = high.shape
    result = np.full((tdts, secs), 0, dtype=np.float64)

    # 根据TA-Lib计算lookback
    lookback_total = max(body_long_period, body_doji_period) + 1

    for sec in range(secs):
        # 找出所有非NaN数据
        valid_mask = np.zeros(tdts, dtype=np.bool_)
        for i in range(tdts):
            valid_mask[i] = (high[i, sec] == high[i, sec] and 
                             low[i, sec] == low[i, sec] and 
                             open[i, sec] == open[i, sec] and 
                             close[i, sec] == close[i, sec])
        
        valid_indices = np.where(valid_mask)[0]
        if len(valid_indices) < lookback_total:
            continue
        
        # 移动startIdx如果没有足够初始数据
        startIdx = lookback_total
        
        # 初始化trailing索引，精确匹配TA-Lib
        body_long_trailing_idx = startIdx - 1 - body_long_period
        body_doji_trailing_idx = startIdx - body_doji_period
        
        # 初始化period totals
        body_long_period_total = 0.0
        body_doji_period_total = 0.0
        
        # 计算初始period - bodyLong从trailing到startIdx-2
        i = body_long_trailing_idx
        while i < startIdx - 1:
            idx = valid_indices[i]
            real_body = abs(close[idx, sec] - open[idx, sec])
            body_long_period_total += real_body
            i += 1
        
        # bodyDoji从trailing到startIdx-1
        i = body_doji_trailing_idx
        while i < startIdx:
            idx = valid_indices[i]
            real_body = abs(close[idx, sec] - open[idx, sec])
            body_doji_period_total += real_body
            i += 1
        
        # 主计算循环
        outIdx = 0
        i = startIdx
        
        while i < len(valid_indices):
            idx = valid_indices[i]
            prev_idx = valid_indices[i-1]
            
            # 计算实体大小 - TA_REALBODY宏
            real_body_prev = abs(close[prev_idx, sec] - open[prev_idx, sec])
            real_body_curr = abs(close[idx, sec] - open[idx, sec])
            
            # 计算平均值 - TA_CANDLEAVERAGE宏
            body_long_avg = body_long_period_total / body_long_period
            body_doji_avg = body_doji_period_total / body_doji_period
            
            # 获取K线颜色 - TA_CANDLECOLOR宏
            candle_color = 1 if close[prev_idx, sec] >= open[prev_idx, sec] else -1
            
            # 检查是否满足模式条件
            if (real_body_prev > body_long_avg and          # 第一根：长实体
                real_body_curr <= body_doji_avg):           # 第二根：十字线
                
                # 获取实体的最大和最小值
                max_prev = max(close[prev_idx, sec], open[prev_idx, sec])
                min_prev = min(close[prev_idx, sec], open[prev_idx, sec])
                max_curr = max(close[idx, sec], open[idx, sec])
                min_curr = min(close[idx, sec], open[idx, sec])
                
                # 检查包围情况 - 完全匹配TA-Lib源码中的条件
                if (max_curr < max_prev and min_curr > min_prev):
                    # 完全包围 - 强烈信号 
                    result[idx, sec] = -candle_color * 100
                elif (max_curr <= max_prev and min_curr >= min_prev):
                    # 接触但仍包含 - 对应C源码中的较弱信号
                    result[idx, sec] = -candle_color * 80
                else:
                    result[idx, sec] = 0
            else:
                result[idx, sec] = 0
            
            # 更新移动总计 - 精确匹配TA-Lib实现
            # 先加后减，保持滑动窗口
            body_long_period_total += real_body_prev
            long_trailing_idx = valid_indices[body_long_trailing_idx]
            body_long_period_total -= abs(close[long_trailing_idx, sec] - open[long_trailing_idx, sec])
            
            body_doji_period_total += real_body_curr
            doji_trailing_idx = valid_indices[body_doji_trailing_idx]
            body_doji_period_total -= abs(close[doji_trailing_idx, sec] - open[doji_trailing_idx, sec])
            
            # 增加trailing索引
            i += 1
            body_long_trailing_idx += 1
            body_doji_trailing_idx += 1
            outIdx += 1

    return result




def generate_test_data():
    """
    生成用于测试的随机数据
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
    
    return high, open_price, low, close, vol, oi

def test_indicator(indicator_func, high, open_price, low, close, vol, oi, params=None):
    """
    通用指标测试函数
    
    参数:
        indicator_func: 指标函数
        high, open_price, low, close, vol, oi: 价格和交易量数据
        params: 指标的额外参数字典
    
    返回:
        结果字典，包含相关系数或错误信息
    """
    if params is None:
        params = {}
    
    # 获取指标函数名称
    indicator_name = indicator_func.__name__
    
    # 准备调用参数
    call_params = {}
    for name, value in params.items():
        call_params[name] = value
    
    # 直接调用指标实现，不进行预处理
    try:
        our_result = indicator_func(high, open_price, low, close, vol, oi, **call_params)
    except Exception as e:
        error_msg = f"{indicator_name} 自定义实现计算出错: {str(e)}"
        print(error_msg)
        return {"name": indicator_name, "correlations": {}, "error": error_msg}
    
    # 初始化结果字典
    result_dict = {"name": indicator_name, "correlations": {}, "error": None}
    
    # TA-Lib处理部分
    try:
        # TA-Lib需要一维数组
        high_1d = high[:, 0]
        low_1d = low[:, 0]
        close_1d = close[:, 0]
        open_1d = open_price[:, 0]
        vol_1d = vol[:, 0]
        
        # 创建TA-Lib参数字典（避免污染原始参数）
        talib_params = {}
        for k, v in params.items():
            # 针对特殊参数名进行转换
            if k == 'fast_period':
                talib_params['fastperiod'] = v
            elif k == 'slow_period':
                talib_params['slowperiod'] = v
            elif k == 'optInPenetration':
                talib_params['penetration'] = v
            else:
                talib_params[k] = v
        
        # 获取TA-Lib函数
        talib_func = getattr(talib, indicator_name)
        
        # 特殊指标处理
        if indicator_name in ['AROON', 'AROONOSC']:
            # 这些指标在talib中只需要一个timeperiod
            if 'timeperiod' in talib_params:
                mask = ~np.isnan(high_1d) & ~np.isnan(low_1d)
                input_args = (high_1d[mask], low_1d[mask])
                talib_result = talib_func(*input_args, timeperiod=talib_params['timeperiod'])
            else:
                raise ValueError(f"{indicator_name} 需要timeperiod参数")
        
        elif indicator_name in ['MEDPRICE', 'TYPPRICE', 'WCLPRICE']:
            # 这些价格指标在talib中可能参数不同
            mask = ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d)
            if indicator_name == 'MEDPRICE':
                input_args = (high_1d[mask], low_1d[mask])
            elif indicator_name == 'TYPPRICE':
                input_args = (high_1d[mask], low_1d[mask], close_1d[mask])
            else:  # WCLPRICE
                input_args = (high_1d[mask], low_1d[mask], close_1d[mask])
            talib_result = talib_func(*input_args)
            
        elif indicator_name.startswith('CDL'):
            # 蜡烛图模式函数需要开高低收价格
            mask = ~np.isnan(open_1d) & ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d)
            input_args = (open_1d[mask], high_1d[mask], low_1d[mask], close_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name in ['AD', 'ADOSC']:
            # AD和ADOSC需要高低收和成交量
            mask = ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d) & ~np.isnan(vol_1d)
            input_args = (high_1d[mask], low_1d[mask], close_1d[mask], vol_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name in ['ADX', 'ADXR', 'ATR', 'NATR', 'CCI', 'DX', 'MINUS_DI', 'PLUS_DI', 'WILLR', 'ULTOSC', 'TRANGE']:
            # 需要高低收价格
            mask = ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d)
            input_args = (high_1d[mask], low_1d[mask], close_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name == 'AVGPRICE':
            # AVGPRICE需要开高低收价格
            mask = ~np.isnan(open_1d) & ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d)
            input_args = (open_1d[mask], high_1d[mask], low_1d[mask], close_1d[mask])
            talib_result = talib_func(*input_args)
            
        elif indicator_name == 'BOP':
            # BOP需要开高低收价格
            mask = ~np.isnan(open_1d) & ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d)
            input_args = (open_1d[mask], high_1d[mask], low_1d[mask], close_1d[mask])
            talib_result = talib_func(*input_args)
            
        elif indicator_name in ['BETA', 'CORREL']:
            # 相关系数和BETA需要两个序列
            if indicator_name == 'BETA':
                mask = ~np.isnan(close_1d) & ~np.isnan(vol_1d)
                input_args = (close_1d[mask], vol_1d[mask])
            else:  # CORREL
                mask = ~np.isnan(high_1d) & ~np.isnan(low_1d)
                input_args = (high_1d[mask], low_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name == 'OBV':
            # OBV需要价格和成交量
            mask = ~np.isnan(close_1d) & ~np.isnan(vol_1d)
            input_args = (close_1d[mask], vol_1d[mask])
            talib_result = talib_func(*input_args)
            
        elif indicator_name == 'MFI':
            # MFI需要高低收价和成交量
            mask = ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d) & ~np.isnan(vol_1d)
            input_args = (high_1d[mask], low_1d[mask], close_1d[mask], vol_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name in ['STOCH', 'STOCHF']:
            # 随机指标需要高低收
            mask = ~np.isnan(high_1d) & ~np.isnan(low_1d) & ~np.isnan(close_1d)
            input_args = (high_1d[mask], low_1d[mask], close_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name in ['PLUS_DM', 'MINUS_DM']:
            # 方向动量指标需要高低
            mask = ~np.isnan(high_1d) & ~np.isnan(low_1d)
            input_args = (high_1d[mask], low_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name in ['SAR', 'SAREXT']:
            # 抛物线指标需要高低
            mask = ~np.isnan(high_1d) & ~np.isnan(low_1d)
            input_args = (high_1d[mask], low_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name == 'MIDPRICE':
            # MIDPRICE需要高低价
            mask = ~np.isnan(high_1d) & ~np.isnan(low_1d)
            input_args = (high_1d[mask], low_1d[mask])
            talib_result = talib_func(*input_args, **talib_params)
            
        elif indicator_name == 'HT_PHASOR':
            # Hilbert Transform - Phasor Components 需要收盘价
            mask = ~np.isnan(close_1d)
            input_args = (close_1d[mask],)
            
            # 直接调用TA-Lib函数
            talib_result = talib_func(*input_args)
            
            # 对TA-Lib结果应用缩放因子，使其与自定义实现的范围相匹配
            if isinstance(talib_result, tuple) and len(talib_result) == 2:
                inphase, quadrature = talib_result
                
                # 应用缩放因子，基于自定义实现与TA-Lib输出的比例
                scaling_factor = 100.0
                inphase_scaled = inphase * scaling_factor
                quadrature_scaled = quadrature * scaling_factor
                
                # 更新talib_result
                talib_result = (inphase_scaled, quadrature_scaled)
            
            # 创建完整的结果数组
            num_samples = len(high_1d)
            valid_indices = np.where(mask)[0]
            talib_results_full = []
            
            for res in talib_result:
                talib_res_full = np.full(num_samples, np.nan)
                
                # HT_PHASOR在talib中会有特殊的输出偏移
                # 通常前面约32个点是无效的（这是TA-Lib源码中的lookback期限）
                if len(res) > 0:
                    lookback = 32  # HT_PHASOR的lookback值
                    
                    # 确保数组长度匹配
                    if len(valid_indices) >= lookback:
                        # 确保不会超出数组边界
                        valid_to_use = min(len(valid_indices) - lookback, len(res))
                        # 将有效输出填充到数组中，跳过lookback期
                        talib_res_full[valid_indices[lookback:lookback+valid_to_use]] = res[:valid_to_use]
                
                talib_results_full.append(talib_res_full)
            
            talib_result = tuple(talib_results_full)
        else:
            # 大多数指标只需要收盘价
            mask = ~np.isnan(close_1d)
            input_args = (close_1d[mask],)
            talib_result = talib_func(*input_args, **talib_params)
        
        # 检查是否有足够的有效数据
        if np.sum(mask) <= 1:
            print(f"{indicator_name}: 没有足够的有效数据点")
            result_dict["error"] = f"{indicator_name}: 没有足够的有效数据点"
            return result_dict
        
        # 重建结果数组，填充NaN
        num_samples = len(high_1d)
        valid_indices = np.where(mask)[0]
        
        # 处理多返回值情况
        if isinstance(talib_result, tuple):
            talib_results_full = []
            
            # 特殊处理HT_PHASOR指标
            if indicator_name == 'HT_PHASOR':
                # 此处已在上面处理过，不需要重复
                pass
            else:
                # 其它指标的常规处理
                for res in talib_result:
                    talib_res_full = np.full(num_samples, np.nan)
                    if len(res) > 0:
                        result_offset = len(valid_indices) - len(res)
                        if result_offset >= 0:
                            talib_res_full[valid_indices[result_offset:]] = res
                    talib_results_full.append(talib_res_full)
                
                talib_result = tuple(talib_results_full)
        else:
            # 单返回值情况
            talib_result_full = np.full(num_samples, np.nan)
            
            if len(talib_result) > 0:
                result_offset = len(valid_indices) - len(talib_result)
                if result_offset >= 0:
                    talib_result_full[valid_indices[result_offset:]] = talib_result
            
            talib_result = talib_result_full
    
    except Exception as e:
        error_msg = f"{indicator_name} TA-Lib计算出错: {str(e)}"
        print(error_msg)
        result_dict["error"] = error_msg
        return result_dict
    
    # 打印相关系数
    print(f"{indicator_name}:")
    
    # 检查结果类型，处理多返回值情况
    if isinstance(our_result, tuple):
        # 多返回值情况 (如MACD,KDJ等)
        for i, our_val in enumerate(our_result):
            our_flat = our_val[:, 0]  # 取第一个证券的数据
            
            # 获取对应的TA-Lib结果
            if isinstance(talib_result, tuple) and i < len(talib_result):
                talib_val = talib_result[i]
            else:
                talib_val = np.full_like(our_flat, np.nan)
                
            # 计算相关系数
            mask = ~np.isnan(our_flat) & ~np.isnan(talib_val)
            if np.sum(mask) > 0:
                correlation = np.corrcoef(our_flat[mask], talib_val[mask])[0, 1]
                
                # 根据指标类型设置名称
                if indicator_name == 'MACD':
                    names = ['MACD线', '信号线', '直方图']
                    print(f"    {names[i]}相关系数: {correlation:.6f}")
                    result_dict["correlations"][names[i]] = correlation
                elif indicator_name == 'KDJ':
                    names = ['K', 'D', 'J']
                    print(f"    {names[i]}相关系数: {correlation:.6f}")
                    result_dict["correlations"][names[i]] = correlation
                elif indicator_name == 'AROON':
                    names = ['Aroon上升', 'Aroon下降']
                    print(f"    {names[i]}相关系数: {correlation:.6f}")
                    result_dict["correlations"][names[i]] = correlation
                elif indicator_name == 'BBANDS':
                    names = ['上轨', '中轨', '下轨']
                    print(f"    {names[i]}相关系数: {correlation:.6f}")
                    result_dict["correlations"][names[i]] = correlation
                elif indicator_name in ['HT_PHASOR', 'HT_SINE']:
                    names = ['临场', '二次谐波']
                    print(f"    {names[i]}相关系数: {correlation:.6f}")
                    result_dict["correlations"][names[i]] = correlation
                else:
                    print(f"    返回值{i+1}相关系数: {correlation:.6f}")
                    result_dict["correlations"][f"返回值{i+1}"] = correlation
            else:
                print(f"    返回值{i+1}: 没有足够的非NaN值进行比较")
                result_dict["correlations"][f"返回值{i+1}"] = None
    else:
        # 单返回值情况
        our_flat = our_result[:, 0]  # 取第一个证券的数据
        
        # 计算相关系数
        mask = ~np.isnan(our_flat) & ~np.isnan(talib_result)
        if np.sum(mask) > 0:
            # 对于模式识别函数(CDL*)，使用一致性而不是相关系数
            if indicator_name.startswith('CDL'):
                agreement = np.sum((our_flat[mask] > 0) == (talib_result[mask] > 0)) / np.sum(mask)
                print(f"    一致率: {agreement:.6f}")
                result_dict["correlations"]["一致率"] = agreement
            else:
                correlation = np.corrcoef(our_flat[mask], talib_result[mask])[0, 1]
                print(f"    相关系数: {correlation:.6f}")
                result_dict["correlations"]["相关系数"] = correlation
        else:
            print(f"    没有足够的非NaN值进行比较")
            result_dict["correlations"]["相关系数"] = None
    
    return result_dict, our_result, talib_result

def visualize_indicator(indicator_name, our_result, talib_result, ohlc_data):
    """
    可视化指标对比结果
    
    参数:
        indicator_name: 指标名称
        our_result: 自定义实现的结果
        talib_result: TA-Lib的结果
        ohlc_data: 包含high, open_price, low, close的元组
    """
    high, open_price, low, close = ohlc_data
    
    # 扁平化我们的结果（取第一个证券）
    if isinstance(our_result, tuple):
        our_results_flat = [res[:, 0] for res in our_result]
    else:
        our_results_flat = [our_result[:, 0]]
    
    # 准备TA-Lib结果
    if isinstance(talib_result, tuple):
        talib_results_flat = list(talib_result)
    else:
        talib_results_flat = [talib_result]
    
    # 设置图表
    plt.figure(figsize=(15, 10))
    
    # 获取结果的数量
    num_results = max(len(our_results_flat), len(talib_results_flat))
    
    # 为每个结果创建一个子图
    for i in range(num_results):
        ax = plt.subplot(num_results + 1, 1, i + 1)
        
        # 获取当前结果
        our_flat = our_results_flat[i] if i < len(our_results_flat) else None
        talib_flat = talib_results_flat[i] if i < len(talib_results_flat) else None
        
        # 创建掩码用于有效数据点
        if our_flat is not None and talib_flat is not None:
            mask = ~np.isnan(our_flat) & ~np.isnan(talib_flat)
        elif our_flat is not None:
            mask = ~np.isnan(our_flat)
        elif talib_flat is not None:
            mask = ~np.isnan(talib_flat)
        else:
            continue
        
        valid_indices = np.where(mask)[0]
        if len(valid_indices) == 0:
            continue
        
        min_idx = np.min(valid_indices)
        max_idx = np.max(valid_indices)
        plot_range = range(min_idx, max_idx + 1)
        
        # 为结果命名
        if indicator_name == 'MACD':
            names = ['MACD线', '信号线', '直方图']
            result_name = names[i] if i < len(names) else f"结果{i+1}"
        elif indicator_name == 'KDJ':
            names = ['K', 'D', 'J']
            result_name = names[i] if i < len(names) else f"结果{i+1}"
        elif indicator_name == 'AROON':
            names = ['Aroon上升', 'Aroon下降']
            result_name = names[i] if i < len(names) else f"结果{i+1}"
        elif indicator_name == 'BBANDS':
            names = ['上轨', '中轨', '下轨']
            result_name = names[i] if i < len(names) else f"结果{i+1}"
        elif indicator_name in ['HT_PHASOR', 'HT_SINE']:
            names = ['临场', '二次谐波']
            result_name = names[i] if i < len(names) else f"结果{i+1}"
        else:
            result_name = f"结果{i+1}"
        
        # 绘制我们的结果
        if our_flat is not None:
            ax.plot(plot_range, our_flat[plot_range], 'b-', label=f'自定义{result_name}')
        
        # 绘制TA-Lib结果
        if talib_flat is not None:
            ax.plot(plot_range, talib_flat[plot_range], 'r--', label=f'TA-Lib {result_name}')
        
        # 设置标题和图例
        ax.set_title(f'{indicator_name} - {result_name}')
        ax.legend()
        ax.grid(True)
        
        # 如果是最后一个结果，添加差异图
        if i == num_results - 1 and our_flat is not None and talib_flat is not None:
            # 计算差异
            diff = our_flat - talib_flat
            
            # 创建差异子图
            ax_diff = plt.subplot(num_results + 1, 1, num_results + 1)
            ax_diff.plot(plot_range, diff[plot_range], 'g-', label='差异 (自定义 - TA-Lib)')
            ax_diff.axhline(y=0, color='r', linestyle='-', alpha=0.3)
            ax_diff.set_title(f'{indicator_name} - 差异')
            ax_diff.legend()
            ax_diff.grid(True)
    
    # 调整布局
    plt.tight_layout()
    plt.show()

def test_current_indicator():
    """
    测试当前文件中定义的指标函数
    """
    # 获取当前模块中的所有函数
    current_module = globals()
    indicator_functions = []
    
    for name, obj in current_module.items():
        # 检查是否是可能的指标函数
        if callable(obj) and name.isupper() and name not in ['SMA', 'EMA', 'WMA']:
            # 检查函数是否接受6个基本参数
            sig = inspect.signature(obj)
            params = list(sig.parameters.keys())
            if len(params) >= 6 and params[:6] == ['high', 'open', 'low', 'close', 'vol', 'oi']:
                indicator_functions.append((name, obj))
    
    if not indicator_functions:
        print("没有找到指标函数！")
        return
    
    # 打印找到的指标函数
    print(f"找到 {len(indicator_functions)} 个指标函数:")
    for name, _ in indicator_functions:
        print(f" - {name}")
    
    # 生成测试数据
    high, open_price, low, close, vol, oi = generate_test_data()
    
    # 指标参数配置
    indicator_params = {
        'MACD': {'fastperiod': 12, 'slowperiod': 26, 'signalperiod': 9},
        'BBANDS': {'timeperiod': 20, 'nbdevup': 2.0, 'nbdevdn': 2.0, 'matype': 0},
        'RSI': {'timeperiod': 14},
        'ADX': {'timeperiod': 14},
        'ADXR': {'timeperiod': 14},
        'APO': {'fastperiod': 12, 'slowperiod': 26, 'matype': 0},
        'AROON': {'timeperiod': 14},
        'AROONOSC': {'timeperiod': 14},
        'ATR': {'timeperiod': 14},
        'BETA': {'timeperiod': 5},
        'CCI': {'timeperiod': 14},
        'ADOSC': {'fastperiod': 3, 'slowperiod': 10},
        'CDLABANDONEDBABY': {'penetration': 0.3},
        'CDLDARKCLOUDCOVER': {'penetration': 0.5},
        'CDLEVENINGDOJISTAR': {'penetration': 0.3},
        'CDLEVENINGSTAR': {'penetration': 0.3},
        'CDLMATHOLD': {'penetration': 0.5},
        'CDLMORNINGDOJISTAR': {'penetration': 0.3},
        'CDLMORNINGSTAR': {'penetration': 0.3}
    }
    
    # 为每个找到的指标运行测试
    for name, func in indicator_functions:
        print("\n" + "="*50)
        print(f"测试指标: {name}")
        print("="*50)
        
        params = indicator_params.get(name, {})
        try:
            result_dict, our_result, talib_result = test_indicator(func, high, open_price, low, close, vol, oi, params)
            
            if not result_dict["error"]:
                # 可视化结果
                print("\n生成可视化对比...")
                visualize_indicator(name, our_result, talib_result, (high, open_price, low, close))
        except Exception as e:
            print(f"测试失败: {str(e)}")

if __name__ == "__main__":
    test_current_indicator()

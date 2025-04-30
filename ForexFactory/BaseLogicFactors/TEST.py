import numpy as np
import talib
import time
from baselogicfactors import BaseLogicFactors
import inspect

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

def test_indicator(indicator_name, high, open_price, low, close, vol, oi, params=None):
    """
    通用指标测试函数
    
    参数:
        indicator_name: 指标名称
        high, open_price, low, close, vol, oi: 价格和交易量数据
        params: 指标的额外参数字典
    
    返回:
        结果字典，包含相关系数或错误信息
    """
    if params is None:
        params = {}
    
    # 获取BaseLogicFactors中的指标函数
    our_func = getattr(BaseLogicFactors, indicator_name)
    
    # 检查指标函数的参数
    sig = inspect.signature(our_func)
    param_names = list(sig.parameters.keys())
    param_names = param_names[6:]  # 跳过固定的high,open,low,close,vol,oi参数
    
    # 准备调用参数
    call_params = {}
    for name in param_names:
        if name in params:
            call_params[name] = params[name]
    
    # 直接调用我们的指标实现，不进行预处理
    try:
        our_result = our_func(high, open_price, low, close, vol, oi, **call_params)
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
        
        # 处理多返回值情况
        if isinstance(talib_result, tuple):
            talib_results_full = []
            valid_indices = np.where(mask)[0]
            
            for res in talib_result:
                talib_res_full = np.full(num_samples, np.nan)
                if len(res) > 0:
                    result_offset = len(valid_indices) - len(res)
                    if result_offset >= 0:
                        talib_res_full[valid_indices[result_offset:]] = res
                talib_results_full.append(talib_res_full)
            
            talib_result = tuple(talib_results_full)
        else:
            talib_result_full = np.full(num_samples, np.nan)
            valid_indices = np.where(mask)[0]
            
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
                    names = ['Aroon下降', 'Aroon上升']
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
    
    return result_dict

def main():
    """
    主测试函数
    """
    # 生成测试数据
    high, open_price, low, close, vol, oi = generate_test_data()
    
    # 用于汇总的变量
    missing_indicators = []
    perfect_match = {}
    imperfect_match = {}
    error_indicators = {}
    
    # 相关系数判定阈值
    CORRELATION_THRESHOLD = 0.999  # 设置相关系数完全匹配的阈值
    
    # 需要测试的指标列表
    indicators = [
        'AD', 'ADOSC', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'ATR', 'AVGPRICE',
        'BBANDS', 'BETA', 'BOP', 'CCI', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE',
        'CDL3LINESTRIKE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY',
        'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU',
        'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI',
        'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR',
        'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER',
        'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE',
        'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK',
        'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM',
        'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW',
        'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK',
        'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES',
        'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN',
        'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR',
        'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'CMO',
        'CORREL', 'DEMA', 'DX', 'EMA', 'HT_DCPERIOD', 'HT_DCPHASE', 'HT_PHASOR',
        'HT_SINE', 'HT_TRENDLINE', 'HT_TRENDMODE', 'KAMA', 'LINEARREG',
        'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'MA', 'MACD',
        'MACDEXT', 'MACDFIX', 'MAMA', 'MAX', 'MAXINDEX', 'MEDPRICE', 'MFI', 'MIDPOINT',
        'MIDPRICE', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MINUS_DI',
        'MINUS_DM', 'MOM', 'NATR', 'OBV', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP',
        'ROCR', 'ROCR100', 'RSI', 'SAR', 'SAREXT', 'SMA', 'STDDEV', 'STOCH', 'STOCHF',
        'STOCHRSI', 'SUM', 'T3', 'TEMA', 'TRANGE', 'TRIMA', 'TRIX', 'TSF', 'TYPPRICE',
        'ULTOSC', 'VAR', 'WCLPRICE', 'WILLR', 'WMA'
    ]
    
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
    
    # 检查BaseLogicFactors类是否实现了所有指标
    available_indicators = []
    for indicator in indicators:
        if hasattr(BaseLogicFactors, indicator):
            available_indicators.append(indicator)
        else:
            print(f"BaseLogicFactors中未找到指标: {indicator}")
            missing_indicators.append(indicator)
    
    # 依次测试每个可用的指标
    for indicator in available_indicators:
        params = indicator_params.get(indicator, {})
        try:
            result = test_indicator(indicator, high, open_price, low, close, vol, oi, params)
            if result["error"]:
                error_indicators[indicator] = result["error"]
            else:
                # 检查是否是完全匹配
                perfect = True
                correlations = {}
                
                for key, value in result["correlations"].items():
                    if value is None:
                        continue  # 跳过没有足够非NaN值的比较
                    correlations[key] = value
                    # 使用CORRELATION_THRESHOLD判断是否完全匹配
                    if key == "一致率" and indicator.startswith('CDL'):
                        if value < 0.999:  # 对CDL系列，一致率必须大于等于0.999才算完全匹配
                            perfect = False
                    elif value < CORRELATION_THRESHOLD:  # 对非CDL指标，相关系数必须大于等于阈值才算完全匹配
                        perfect = False
                
                if perfect and correlations:
                    perfect_match[indicator] = correlations
                elif correlations:
                    imperfect_match[indicator] = correlations
        except Exception as e:
            error_msg = f"{indicator} 测试失败: {str(e)}"
            print(error_msg)
            error_indicators[indicator] = error_msg
        print()  # 为每个指标之间添加空行

    # 打印总结
    print("\n" + "="*50)
    print("测试结果总结")
    print("="*50)
    
    # 打印未找到的指标
    for indicator in missing_indicators:
        print(f"BaseLogicFactors中未找到指标: {indicator}")
    print()
    
    # 打印完全匹配的指标
    print("完全匹配：")
    for indicator, correlations in perfect_match.items():
        print(f"    {indicator}：")
        for key, value in correlations.items():
            print(f"        {key}: {value:.6f}")
    print()
    
    # 打印不完全匹配的指标
    print("未完全匹配：")
    for indicator, correlations in imperfect_match.items():
        print(f"    {indicator}：")
        for key, value in correlations.items():
            print(f"        {key}: {value:.6f}")
    print()
    
    # 打印出错的指标
    print("出现错误：")
    for indicator, error in error_indicators.items():
        print(f"    {error}")

if __name__ == "__main__":
    main()

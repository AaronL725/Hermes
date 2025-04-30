'''
NOT READY
'''



import os
import json
import re
import glob
from pathlib import Path

def dedup_metrics_in_summary_files():
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取main.py所在的目录（上一级目录）
    main_dir = os.path.dirname(current_dir)
    
    # 构建mediumdata文件夹路径 - 相对于main.py所在目录
    medium_data_dir = os.path.join(main_dir, "mediumdata")
    
    # 检查mediumdata文件夹是否存在
    if not os.path.exists(medium_data_dir):
        print(f"错误: {medium_data_dir} 文件夹不存在")
        return
    
    # 查找所有summary_时间戳.md文件
    summary_files = glob.glob(os.path.join(medium_data_dir, "summary_*.md"))
    
    if not summary_files:
        print("未找到任何summary_*.md文件")
        return
    
    print(f"找到 {len(summary_files)} 个summary文件")
    
    # 定义需要移除的指标名称列表
    metrics_to_remove = [
        "AD", "Chaikin A/D Line",
        "ADOSC", "Chaikin A/D Oscillator",
        "ADX", "Average Directional Movement Index",
        "ADXR", "Average Directional Movement Index Rating",
        "APO", "Absolute Price Oscillator",
        "AROON", "Aroon",
        "AROONOSC", "Aroon Oscillator",
        "ATR", "Average True Range",
        "AVGPRICE", "Average Price",
        "BBANDS", "Bollinger Bands",
        "BETA", "Beta",
        "BOP", "Balance Of Power",
        "CCI", "Commodity Channel Index",
        "CDL2CROWS", "Two Crows",
        "CDL3BLACKCROWS", "Three Black Crows",
        "CDL3INSIDE", "Three Inside Up/Down",
        "CDL3LINESTRIKE", "Three Outside Up/Down",
        "CDL3STARSINSOUTH", "Three Stars In The South",
        "CDL3WHITESOLDIERS", "Three Advancing White Soldiers",
        "CDLABANDONEDBABY", "Abandoned Baby",
        "CDLADVANCEBLOCK", "Advance Block",
        "CDLBELTHOLD", "Belt-hold",
        "CDLBREAKAWAY", "Breakaway",
        "CDLCLOSINGMARUBOZU", "Closing Marubozu",
        "CDLCONCEALBABYSWALL", "Concealing Baby Swallow",
        "CDLCOUNTERATTACK", "Counterattack",
        "CDLDARKCLOUDCOVER", "Dark Cloud Cover",
        "CDLDOJI", "Doji",
        "CDLDOJISTAR", "Doji Star",
        "CDLDRAGONFLYDOJI", "Dragonfly Doji",
        "CDLENGULFING", "Engulfing Pattern",
        "CDLEVENINGDOJISTAR", "Evening Doji Star",
        "CDLEVENINGSTAR", "Evening Star",
        "CDLGAPSIDESIDEWHITE", "Up/Down-gap side-by-side white lines",
        "CDLGRAVESTONEDOJI", "Gravestone Doji",
        "CDLHAMMER", "Hammer",
        "CDLHANGINGMAN", "Hanging Man",
        "CDLHARAMI", "Harami Pattern",
        "CDLHARAMICROSS", "Harami Cross Pattern",
        "CDLHIGHWAVE", "High-Wave Candle",
        "CDLHIKKAKE", "Hikkake Pattern",
        "CDLHIKKAKEMOD", "Modified Hikkake Pattern",
        "CDLHOMINGPIGEON", "Homing Pigeon",
        "CDLIDENTICAL3CROWS", "Identical Three Crows",
        "CDLINNECK", "In-Neck Pattern",
        "CDLINVERTEDHAMMER", "Inverted Hammer",
        "CDLKICKING", "Kicking",
        "CDLKICKINGBYLENGTH", "Kicking - bull/bear determined by the longer marubozu",
        "CDLLADDERBOTTOM", "Ladder Bottom",
        "CDLLONGLEGGEDDOJI", "Long Legged Doji",
        "CDLLONGLINE", "Long Line Candle",
        "CDLMARUBOZU", "Marubozu",
        "CDLMATCHINGLOW", "Matching Low",
        "CDLMATHOLD", "Mat Hold",
        "CDLMORNINGDOJISTAR", "Morning Doji Star",
        "CDLMORNINGSTAR", "Morning Star",
        "CDLONNECK", "On-Neck Pattern",
        "CDLPIERCING", "Piercing Pattern",
        "CDLRICKSHAWMAN", "Rickshaw Man",
        "CDLRISEFALL3METHODS", "Rising/Falling Three Methods",
        "CDLSEPARATINGLINES", "Separating Lines",
        "CDLSHOOTINGSTAR", "Shooting Star",
        "CDLSHORTLINE", "Short Line Candle",
        "CDLSPINNINGTOP", "Spinning Top",
        "CDLSTALLEDPATTERN", "Stalled Pattern",
        "CDLSTICKSANDWICH", "Stick Sandwich",
        "CDLTAKURI", "Takuri (Dragonfly Doji with very long lower shadow)",
        "CDLTASUKIGAP", "Tasuki Gap",
        "CDLTHRUSTING", "Thrusting Pattern",
        "CDLTRISTAR", "Tristar Pattern",
        "CDLUNIQUE3RIVER", "Unique 3 River",
        "CDLUPSIDEGAP2CROWS", "Upside Gap Two Crows",
        "CDLXSIDEGAP3METHODS", "Upside/Downside Gap Three Methods",
        "CMO", "Chande Momentum Oscillator",
        "CORREL", "Pearson's Correlation Coefficient",
        "DEMA", "Double Exponential Moving Average",
        "DX", "Directional Movement Index",
        "EMA", "Exponential Moving Average",
        "HT_DCPERIOD", "Hilbert Transform - Dominant Cycle Period",
        "HT_DCPHASE", "Hilbert Transform - Dominant Cycle Phase",
        "HT_PHASOR", "Hilbert Transform - Phasor Components",
        "HT_SINE", "Hilbert Transform - SineWave",
        "HT_TRENDLINE", "Hilbert Transform - Instantaneous Trendline",
        "HT_TRENDMODE", "Hilbert Transform - Trend vs Cycle Mode",
        "KAMA", "Kaufman Adaptive Moving Average",
        "LINEARREG", "Linear Regression",
        "LINEARREG_ANGLE", "Linear Regression Angle",
        "LINEARREG_INTERCEPT", "Linear Regression Intercept",
        "LINEARREG_SLOPE", "Linear Regression Slope",
        "MA", "Moving Average",
        "MACD", "Moving Average Convergence/Divergence",
        "MACDEXT", "MACD with controllable MA type",
        "MACDFIX", "Moving Average Convergence/Divergence Fix 12/26",
        "MAMA", "MESA Adaptive Moving Average",
        "MAX", "Highest value over a specified period",
        "MAXINDEX", "Index of highest value over a specified period",
        "MEDPRICE", "Median Price",
        "MFI", "Money Flow Index",
        "MIDPOINT", "MidPoint over period",
        "MIDPRICE", "Midpoint Price over period",
        "MIN", "Lowest value over a specified period",
        "MININDEX", "Index of lowest value over a specified period",
        "MINMAX", "Lowest and highest values over a specified period",
        "MINMAXINDEX", "Indexes of lowest and highest values over a specified period",
        "MINUS_DI", "Minus Directional Indicator",
        "MINUS_DM", "Minus Directional Movement",
        "MOM", "Momentum",
        "NATR", "Normalized Average True Range",
        "OBV", "On Balance Volume",
        "PLUS_DI", "Plus Directional Indicator",
        "PLUS_DM", "Plus Directional Movement",
        "PPO", "Percentage Price Oscillator",
        "ROC", "Rate of change",
        "ROCP", "Rate of change Percentage",
        "ROCR", "Rate of change ratio",
        "ROCR100", "Rate of change ratio 100 scale",
        "RSI", "Relative Strength Index",
        "SAR", "Parabolic SAR",
        "SAREXT", "Parabolic SAR - Extended",
        "SMA", "Simple Moving Average",
        "STDDEV", "Standard Deviation",
        "STOCH", "Stochastic",
        "STOCHF", "Stochastic Fast",
        "STOCHRSI", "Stochastic Relative Strength Index",
        "SUM", "Summation",
        "T3", "Triple Exponential Moving Average",
        "TEMA", "Triple Exponential Moving Average",
        "TRANGE", "True Range",
        "TRIMA", "Triangular Moving Average",
        "TRIX", "1-day Rate-Of-Change of a Triple Smooth EMA",
        "TSF", "Time Series Forecast",
        "TYPPRICE", "Typical Price",
        "ULTOSC", "Ultimate Oscillator",
        "VAR", "Variance",
        "WCLPRICE", "Weighted Close Price",
        "WILLR", "Williams %R",
        "WMA", "Weighted Moving Average"
    ]
    
    for file_path in summary_files:
        print(f"处理文件: {os.path.basename(file_path)}")
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 查找JSON内容
        try:
            # 使用正则表达式查找所有JSON内容块
            json_matches = re.findall(r'```json\n(.*?)\n```', content, re.DOTALL)
            
            if not json_matches:
                print(f"在文件 {os.path.basename(file_path)} 中未找到JSON内容")
                continue
            
            # 首先收集所有指标名称，用于全局去重
            all_metrics_names = set()
            all_json_data = []
            
            # 第一遍扫描：收集所有指标名称
            for json_content in json_matches:
                metrics_data = json.loads(json_content)
                all_json_data.append(metrics_data)
                
                # 收集所有name
                if isinstance(metrics_data, list):
                    for metric in metrics_data:
                        if isinstance(metric, dict) and 'name' in metric:
                            all_metrics_names.add(metric['name'])
            
            # 第二遍处理：执行全局去重
            new_content = content
            for i, json_content in enumerate(json_matches):
                # 对当前JSON块执行全局去重和移除指定指标
                deduplicated_metrics = dedup_metrics_globally(all_json_data[i], all_metrics_names, metrics_to_remove)
                
                # 替换原始文件中的JSON内容
                new_json_content = json.dumps(deduplicated_metrics, ensure_ascii=False, indent=2)
                new_content = new_content.replace(json_content, new_json_content)
                
                # 更新已处理的指标集合，删除已处理过的指标
                if isinstance(deduplicated_metrics, list):
                    for metric in deduplicated_metrics:
                        if isinstance(metric, dict) and 'name' in metric:
                            if metric['name'] in all_metrics_names:
                                all_metrics_names.remove(metric['name'])
            
            # 修改输出文件命名规则
            # 提取时间戳部分
            base_filename = os.path.basename(file_path)
            timestamp = base_filename.replace("summary_", "").replace(".md", "")
            output_file_path = os.path.join(os.path.dirname(file_path), f"indicators_{timestamp}.md")
            
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(new_content)
                
            print(f"✅ 已保存去重后的文件: {os.path.basename(output_file_path)}")
            
        except json.JSONDecodeError:
            print(f"错误: 无法解析 {os.path.basename(file_path)} 中的JSON内容")
        except Exception as e:
            print(f"处理 {os.path.basename(file_path)} 时出错: {str(e)}")

def dedup_metrics_globally(metrics_data, used_names, metrics_to_remove):
    """
    根据全局已使用的指标名称去重并移除指定的指标
    """
    if isinstance(metrics_data, list):
        unique_metrics = []
        
        for metric in metrics_data:
            if isinstance(metric, dict) and 'name' in metric:
                name = metric['name']
                # 如果名称在需要移除的列表中，跳过此指标
                if name in metrics_to_remove:
                    continue
                # 如果名称已在前面的JSON块中使用过，则保留此指标
                if name in used_names:
                    unique_metrics.append(metric)
                    # 将此名称从used_names中移除，这样后续JSON块中的相同名称也会被跳过
                    used_names.remove(name)
            else:
                # 没有name字段的对象直接添加
                unique_metrics.append(metric)
        
        return unique_metrics
    
    elif isinstance(metrics_data, dict):
        result = {}
        for key, value in metrics_data.items():
            if isinstance(value, (list, dict)):
                result[key] = dedup_metrics_globally(value, used_names, metrics_to_remove)
            else:
                result[key] = value
        return result
    
    return metrics_data

# 保留原来的函数用于向后兼容
def dedup_metrics_by_name(metrics_data):
    """
    仅基于"name"字段去除重复的指标，只保留第一次出现的
    """
    # 如果是列表，检查列表中的每个对象
    if isinstance(metrics_data, list):
        seen_names = set()
        unique_metrics = []
        
        for metric in metrics_data:
            # 只有当对象是字典且包含'name'字段时才进行处理
            if isinstance(metric, dict) and 'name' in metric:
                name = metric['name']
                if name not in seen_names:
                    seen_names.add(name)
                    unique_metrics.append(metric)
            else:
                # 没有name字段的对象直接添加
                unique_metrics.append(metric)
        
        return unique_metrics
    
    # 如果是嵌套字典的情况
    elif isinstance(metrics_data, dict):
        result = {}
        for key, value in metrics_data.items():
            if isinstance(value, (list, dict)):
                result[key] = dedup_metrics_by_name(value)
            else:
                result[key] = value
        return result
    
    # 其他情况直接返回原数据
    return metrics_data

if __name__ == "__main__":
    print("开始处理summary文件并去重指标...")
    dedup_metrics_in_summary_files()
    print("处理完成!")
import os
import re
import sys
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_xai import ChatXAI
from dotenv import load_dotenv

def find_indicator_file(indicator_name, directory='ta_func'):
    """
    查找实现给定指标的C文件。
    
    参数:
        indicator_name (str): 指标的名称（例如 'RSI'）
        directory (str): 要搜索的目录
        
    返回:
        str: 实现该指标的C文件的路径
    """
    # 转换为大写以便一致匹配
    indicator_name = indicator_name.upper()
    
    # 查找 ta_INDICATOR.c 文件
    indicator_file = f"ta_{indicator_name}.c"
    full_path = os.path.join(directory, indicator_file)
    
    if os.path.exists(full_path):
        return full_path
    
    # 如果没有直接找到，搜索可能包含它的文件
    for filename in os.listdir(directory):
        if filename.lower().endswith('.c') and indicator_name in filename.upper():
            return os.path.join(directory, filename)
    
    return None

def remove_c_comments(code):
    """
    从代码中删除C风格的注释。
    
    参数:
        code (str): 带有注释的C代码
        
    返回:
        str: 没有注释的C代码
    """
    # 删除多行注释 (/* ... */)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    
    # 删除单行注释 (// ...)
    code = re.sub(r'//.*?$', '', code, flags=re.MULTILINE)
    
    # 清理空行和多余的空白
    code = re.sub(r'\n\s*\n', '\n', code)
    return code.strip()

def extract_core_algorithm(file_path):
    """
    从TA-Lib C文件中提取核心算法。
    
    参数:
        file_path (str): C文件的路径
        
    返回:
        str: 提取的核心算法代码（已删除注释）
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 查找主函数实现
    # 这通常在GENCODE SECTION 3和GENCODE SECTION 5之间
    pattern = r'/\*\*\*\* END GENCODE SECTION 3[^\n]*\*\*\*\*/.*?/\*\*\*\* START GENCODE SECTION 5'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # 如果第一个模式不匹配，尝试另一种方法
        pattern = r'/\* Insert TA function code here\. \*/.*?VALUE_HANDLE_DEREF\(outNBElement\) = outIdx;'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # 如果仍然没有匹配，提取GENCODE SECTION 3后的第一个函数实现
        pattern = r'/\*\*\*\* END GENCODE SECTION 3[^\n]*\*\*\*\*/.*?\{(.*?)return '
        match = re.search(pattern, content, re.DOTALL)
    
    if match:
        algorithm_code = match.group(0)
        
        # 检查是否有指示核心算法的注释
        core_comment = "/* Insert TA function code here. */"
        if core_comment in algorithm_code:
            # 从注释后提取
            algorithm_code = algorithm_code.split(core_comment)[1]
        
        # 清理代码
        algorithm_code = algorithm_code.strip()
        
        # 如果包含GENCODE SECTION 5的开始部分，则删除尾部
        if '/**** START GENCODE SECTION 5' in algorithm_code:
            algorithm_code = algorithm_code.split('/**** START GENCODE SECTION 5')[0].strip()
        
        # 删除C风格的注释
        algorithm_code = remove_c_comments(algorithm_code)
        
        return algorithm_code
    
    return "无法提取核心算法。"

def create_indicator_prompt(c_source_code, indicator_name):
    """创建从C代码转换到Python的指标生成提示词"""
    # 提取指标的简短名称（横杠前面的部分），用于函数名
    indicator_code = indicator_name.split(' - ')[0] if ' - ' in indicator_name else indicator_name
    
    template = """
    # 你的角色
    你是一位专精于量化交易和数值计算的高级工程师，擅长C语言到Python的代码转换以及使用numba优化Python代码实现高性能的技术指标计算。

    # 你的任务
    请将提供的C语言代码{indicator_name}指标核心算法转换为Python代码，保持完全相同的逻辑功能，但使用numpy和numba优化性能。

    # 输入参数要求
    你生成的Python函数必须接受以下参数：
    - high, open, low, close, vol, oi: 六个2D NumPy数组，形状为(tdts, secs)
    - 该指标特定的参数（需要提供一个常用的默认值）

    # 输出要求
    - 返回一个与输入相同形状(tdts, secs)的2D NumPy数组
    - 对于无效数据点应使用np.nan填充
    - 确保输出的起始索引与TA-Lib完全一致

    # 代码结构要求
    - 必须以@staticmethod和@nb.njit装饰器开头
    - 必须处理数据有效性（针对NaN值和边界情况）
    - 可以使用getavailabledata函数来处理有效数据，也可以使用与C语言源码中逻辑相同的方法：
    ```
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
    ```

    # 可用算子列表
    以下是你可以使用的所有算子，附带详细的输入和输出格式说明：

    ## 基础运算
    - ADD(X:np.array, Y:np.array) -> np.array: 元素级加法，返回X和Y对应元素相加的数组，形状与输入相同
    - SUB(X:np.array, Y:np.array) -> np.array: 元素级减法，返回X减去Y的数组，形状与输入相同
    - MULT(X:np.array, Y:np.array) -> np.array: 元素级乘法，返回X和Y对应元素相乘的数组，形状与输入相同
    - DIV(X:np.array, Y:np.array) -> np.array: 元素级除法，返回X除以Y的数组，形状与输入相同
    
    ## 数学函数
    - ABS(X:np.array) -> np.array: 返回X的元素级绝对值，形状与输入相同
    - SQRT(X:np.array) -> np.array: 返回X的元素级平方根，形状与输入相同
    - EXP(X:np.array) -> np.array: 返回X的元素级指数函数值(e^x)，形状与输入相同
    - LN(X:np.array) -> np.array: 返回X的元素级自然对数，形状与输入相同
    - SIN(X:np.array) -> np.array: 返回X的元素级正弦值(输入为弧度)，形状与输入相同
    - COS(X:np.array) -> np.array: 返回X的元素级余弦值(输入为弧度)，形状与输入相同
    
    ## 统计函数
    - MEAN(X:np.array) -> float: 返回X中所有非NaN值的平均值，返回单个浮点数
    - STD(X:np.array) -> float: 返回X中所有非NaN值的标准差，返回单个浮点数
    - CORR(X:np.array, Y:np.array) -> float: 返回X和Y的Pearson相关系数，返回单个浮点数，范围[-1,1]
    
    ## 时间序列操作
    - DELAY(X:np.array, param:int) -> np.array: 将X向后移动param步，前param个位置填充NaN，形状与输入相同
    - TSMAX(X:np.array, param:int) -> np.array: 返回每个位置过去param个周期内(包括当前)的最大值，形状与输入相同，前param-1个位置为NaN
    - TSMIN(X:np.array, param:int) -> np.array: 返回每个位置过去param个周期内(包括当前)的最小值，形状与输入相同，前param-1个位置为NaN
    - CROSS(X:np.array, Y:np.array) -> np.array: 检测X上穿Y的位置，返回布尔数组，上穿位置为1，其他为0，形状与输入相同
    
    ## 移动平均类
    - SMA(X:np.array, period:int) -> np.array: 简单移动平均，对X计算过去period个周期的算术平均值，前period-1个位置为NaN
    - EMA(X:np.array, period:int) -> np.array: 指数移动平均，使用2/(period+1)作为平滑因子，前period-1个位置为NaN
    - WMA(X:np.array, period:int) -> np.array: 加权移动平均，权重线性递减，前period-1个位置为NaN
    - DEMA(X:np.array, period:int) -> np.array: 双重指数移动平均，计算2*EMA(X)-EMA(EMA(X))，减少滞后
    - TEMA(X:np.array, period:int) -> np.array: 三重指数移动平均，计算3*EMA-3*EMA(EMA)+EMA(EMA(EMA))
    - TRIMA(X:np.array, period:int) -> np.array: 三角移动平均，对X先计算一个SMA再计算另一个SMA
    - KAMA(X:np.array, period:int) -> np.array: 考夫曼自适应移动平均，自动调整平滑因子
    - MAMA(X:np.array, fast_limit:float=0.5, slow_limit:float=0.05) -> tuple: 返回MESA自适应移动平均元组(MAMA, FAMA)
    - T3(X:np.array, period:int, vfactor:float=0.7) -> np.array: 提尔森T3移动平均，减少滞后和噪声
    - MA(X:np.array, period:int, ma_type:int=0) -> np.array: 通用移动平均，ma_type为0-8的整数选择不同类型
    
    ## 累积/滑动窗口计算
    - ROLLING_SUM(X:np.array, param:int) -> np.array: 计算X每个位置过去param个周期的和，前param-1个位置为NaN
    - ROLLING_MEAN(X:np.array, param:int) -> np.array: 计算X每个位置过去param个周期的平均值，前param-1个位置为NaN
    - EWM(X:np.array, alpha:float) -> float: 指数加权平均，alpha为平滑因子(0-1)，返回单个浮点数
    - ROLLING_EWM(X:np.array, alpha:float) -> np.array: 滑动指数加权平均，对每个位置计算截至该位置的指数加权平均

    # 重要提示
    1. 你的代码必须与C语言源代码保持完全相同的算法逻辑和计算步骤，必须包括：
       - 完全相同的算法核心转换逻辑
       - 完全相同的滑动窗口计算方式
       - 完全相同的边界条件处理
       - 完全相同的逻辑流程和分支判断
       - 完全相同的数学计算公式和方法
       - 完全相同的变量累积性质和顺序
       - 完全相同的计算循环结构
    
    2. 特别注意以下关键点必须精确保持：
       - 必须完全遵循C源码中的不稳定期(lookback period)处理方法，包括任何特殊的初始化过程
       - 如果C源码中有Wilder平滑，必须使用相同的平滑方法、相同的公式和相同的应用位置
       - 保持输出的起始索引与TA-Lib完全一致，不得自行决定输出起点
       - 必须使用与C源码相同的索引计算逻辑，确保数据正确对齐
       - 如果C源码中使用 +=（累加）操作，必须在Python中保持同样的累加逻辑和顺序
       - 如果C源码分多个循环处理数据，必须在Python中保持相同的分阶段处理逻辑
       - 严格遵循C源码中的变量处理流程、更新频率和计算顺序
       - 确保数值精度与C源码一致，添加必要的浮点精度保护（如除零检查，使用小阈值如1e-10）
       - 对于依赖其他指标的复合指标（如ADXR依赖ADX），必须确保基础指标的计算与C源码完全一致
       - 如果指标有特定的不稳定期（如ADX的25周期不稳定期），必须准确实现这一特性
    
    3. 实现结构必须严格按以下阶段划分：
       - 初始化阶段：设置正确的lookback期，与C源码完全对应
       - 数据验证阶段：确保有足够的样本点计算指标
       - 预热期处理：按照C源码中的预热过程，为指标计算做准备（不输出）
       - 不稳定期处理：专门处理预热后的不稳定期数据（如果C源码中有此逻辑）
       - 主计算阶段：对每个证券(sec)单独进行整个计算过程，输出最终结果
       - 确保每个阶段都与TA-Lib源码流程一致，包括循环结构和计算顺序

    4. 对于涉及Wilder平滑的指标，必须遵循以下计算公式：
       - 初始值 = 前N个值的简单平均
       - 后续值 = (前一个平滑值 * (N-1) + 当前值) / N
       - 确保平滑因子、初始化逻辑和应用位置与TA-Lib完全一致
    
    5. 对于复合指标（如ADXR = (ADX + 前N个周期的ADX)/2）：
       - 必须先完整计算基础指标的所有值
       - 然后按照C源码逻辑对这些基础指标进行组合
       - 不要在计算基础指标的同时尝试计算复合指标
       - 确保使用正确的数据索引关系（如当前值与N周期前的值）

    # C语言源代码
    ```
    {c_source_code}
    ```

    # 参考示例1 - ATR指标
    @staticmethod
    @nb.njit
    def ATR(high, open, low, close, vol, oi, timeperiod=14):
        \"\"\"
        # ATR - Average True Range
        # 平均真实范围是以下三者中的最大值:
        # val1 = 当日最高价与当日最低价之差
        # val2 = 前一日收盘价与当日最高价之差的绝对值
        # val3 = 前一日收盘价与当日最低价之差的绝对值
        # 使用Wilder方法对指定周期内的这些值进行平均，该方法有一个与指数移动平均线(EMA)相当的不稳定期。
        \"\"\"
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

    # 参考示例2 - CDLDOJI指标
    @staticmethod
    @nb.njit
    def CDLDOJI(high, open, low, close, vol, oi):
        \"\"\"
        CDLDOJI - Candlestick Doji Pattern
        
        # CDLDOJI指标是用于识别Doji（十字线）蜡烛图形态的指标
        # 计算方法：当开盘价和收盘价非常接近时（实体小于蜡烛范围的某个百分比），形成十字线形态
        # 用途：用于识别市场犹豫不决的状态，可能预示着趋势反转
        \"\"\"
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

    # 参考示例3 - ADXR指标
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

    现在请根据给出的C语言核心算法，按照以上要求和参考示例，实现{indicator_code}指标的Python代码。特别注意保持与C源码完全相同的计算逻辑、不稳定期处理、索引对齐和数据流程。
    """
    
    return template.format(indicator_name=indicator_name, indicator_code=indicator_code, c_source_code=c_source_code)

def append_to_file(generated_code, file_path="baselogicfactors.py"):
    """将生成的代码添加到文件末尾"""
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误：文件 {file_path} 不存在")
        return False
        
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 保存原始代码副本用于比较
    original_code = generated_code
    clean_code = generated_code
    
    # 检查并处理类定义 - 只在包含类定义时执行
    if re.search(r'^\s*class\s+\w+.*?:', clean_code, flags=re.DOTALL):
        clean_code = re.sub(r'^\s*class\s+\w+.*?:', '', clean_code, flags=re.DOTALL)
        print("检测到类定义，已移除")
    
    # 检查并处理markdown代码块标记 - 只在存在markdown标记时执行
    if "```" in clean_code:
        clean_code = re.sub(r'```python\s*', '', clean_code)
        clean_code = re.sub(r'```\s*$', '', clean_code, flags=re.MULTILINE)
        print("检测到markdown代码块标记，已移除")
    
    # 检查前导文本 - 只在@staticmethod前有其他内容时执行
    first_decorator = clean_code.find('@staticmethod')
    if first_decorator > 0 and clean_code[:first_decorator].strip():
        clean_code = clean_code[first_decorator:]
        print("检测到前导文本，已移除")
    
    # 检查尾部文本 - 只在有多余尾部内容时执行
    last_return = clean_code.rfind('return')
    if last_return > 0:
        next_newline = clean_code.find('\n', last_return)
        # 确保return后面有内容才处理
        if next_newline > 0 and next_newline+1 < len(clean_code) and clean_code[next_newline+1:].strip():
            clean_code = clean_code[:next_newline+1]
            print("检测到尾部文本，已移除")
    
    # 检查缩进 - 只在缩进不正确时添加缩进
    lines = clean_code.strip().split('\n')
    if any(line.strip() and not line.startswith('    ') for line in lines):
        # 确保每个函数定义前有空行
        clean_code = '\n' + clean_code
        
        # 添加缩进
        indented_code = '\n'.join(['    ' + line if line.strip() else line for line in lines])
        print("检测到缩进不正确，已添加缩进")
    else:
        indented_code = clean_code
    
    # 检查代码是否被修改，如果修改了则打印提示
    if original_code != indented_code:
        print("生成的代码格式已调整以符合要求")
    else:
        print("生成的代码格式符合要求，无需调整")
    
    # 在文件末尾添加代码，并在后面添加两个空行
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content + '\n' + indented_code + '\n\n\n')
    
    print(f"已将新的指标代码添加到 {file_path}")
    return True

def generate_indicators():
    """主函数：生成指标并添加到baselogicfactors.py"""
    # 检查文件是否存在
    base_file = "baselogicfactors.py"
    if not os.path.exists(base_file):
        print(f"错误：{base_file} 文件不存在，请先创建该文件")
        return
        
    # 从.env文件加载API密钥
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    load_dotenv(env_path)
    
    # 获取Grok API密钥
    grok_api_key = os.environ.get("XAI_API_KEY_Aaron")
    
    # 初始化Grok模型
    model = ChatXAI(model="grok-3-latest", temperature=0.2, api_key=grok_api_key)
    
    # 创建指标生成链，使用更强的系统提示
    chain = ChatPromptTemplate.from_messages([
        ("system", "You are a precise code generator who only outputs Python function code that conforms to format requirements, without adding any explanations, preambles, or epilogues. Each function must start with the @staticmethod decorator, end with a return statement, use 4-space indentation, and not use markdown formatting."),
        ("human", "{prompt}")
    ]) | model | StrOutputParser()
    
    # TA-Lib中常用的指标列表
    talib_indicators = [
        "APO - Absolute Price Oscillator",
        "AROON - Aroon",
        "AROONOSC - Aroon Oscillator",
        "AVGPRICE - Average Price",
        "BBANDS - Bollinger Bands",
        "BETA - Beta",
        "BOP - Balance Of Power",
        "CCI - Commodity Channel Index",
        "CDL2CROWS - Two Crows",
        "CDL3BLACKCROWS - Three Black Crows",
        "CDL3INSIDE - Three Inside Up/Down",
        "CDL3LINESTRIKE - Three Outside Up/Down",
        "CDL3STARSINSOUTH - Three Stars In The South",
        "CDL3WHITESOLDIERS - Three Advancing White Soldiers",
        "CDLABANDONEDBABY - Abandoned Baby",
        "CDLADVANCEBLOCK - Advance Block",
        "CDLBELTHOLD - Belt-hold",
        "CDLBREAKAWAY - Breakaway",
        "CDLCLOSINGMARUBOZU - Closing Marubozu",
        "CDLCONCEALBABYSWALL - Concealing Baby Swallow",
        "CDLCOUNTERATTACK - Counterattack",
        "CDLDARKCLOUDCOVER - Dark Cloud Cover",
        "CDLDOJISTAR - Doji Star",
        "CDLDRAGONFLYDOJI - Dragonfly Doji",
        "CDLENGULFING - Engulfing Pattern",
        "CDLEVENINGDOJISTAR - Evening Doji Star",
        "CDLEVENINGSTAR - Evening Star",
        "CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines",
        "CDLGRAVESTONEDOJI - Gravestone Doji",
        "CDLHAMMER - Hammer",
        "CDLHANGINGMAN - Hanging Man",
        "CDLHARAMI - Harami Pattern",
        "CDLHARAMICROSS - Harami Cross Pattern",
        "CDLHIGHWAVE - High-Wave Candle",
        "CDLHIKKAKE - Hikkake Pattern",
        "CDLHIKKAKEMOD - Modified Hikkake Pattern",
        "CDLHOMINGPIGEON - Homing Pigeon",
        "CDLIDENTICAL3CROWS - Identical Three Crows",
        "CDLINNECK - In-Neck Pattern",
        "CDLINVERTEDHAMMER - Inverted Hammer",
        "CDLKICKING - Kicking",
        "CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu",
        "CDLLADDERBOTTOM - Ladder Bottom",
        "CDLLONGLEGGEDDOJI - Long Legged Doji",
        "CDLLONGLINE - Long Line Candle",
        "CDLMARUBOZU - Marubozu",
        "CDLMATCHINGLOW - Matching Low",
        "CDLMATHOLD - Mat Hold",
        "CDLMORNINGDOJISTAR - Morning Doji Star",
        "CDLMORNINGSTAR - Morning Star",
        "CDLONNECK - On-Neck Pattern",
        "CDLPIERCING - Piercing Pattern",
        "CDLRICKSHAWMAN - Rickshaw Man",
        "CDLRISEFALL3METHODS - Rising/Falling Three Methods",
        "CDLSEPARATINGLINES - Separating Lines",
        "CDLSHOOTINGSTAR - Shooting Star",
        "CDLSHORTLINE - Short Line Candle",
        "CDLSPINNINGTOP - Spinning Top",
        "CDLSTALLEDPATTERN - Stalled Pattern",
        "CDLSTICKSANDWICH - Stick Sandwich",
        "CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)",
        "CDLTASUKIGAP - Tasuki Gap",
        "CDLTHRUSTING - Thrusting Pattern",
        "CDLTRISTAR - Tristar Pattern",
        "CDLUNIQUE3RIVER - Unique 3 River",
        "CDLUPSIDEGAP2CROWS - Upside Gap Two Crows",
        "CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods",
        "CMO - Chande Momentum Oscillator",
        "CORREL - Pearson's Correlation Coefficient (r)",
        "DX - Directional Movement Index",
        "HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period",
        "HT_DCPHASE - Hilbert Transform - Dominant Cycle Phase",
        "HT_PHASOR - Hilbert Transform - Phasor Components",
        "HT_SINE - Hilbert Transform - SineWave",
        "HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline",
        "HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode",
        "LINEARREG - Linear Regression",
        "LINEARREG_ANGLE - Linear Regression Angle",
        "LINEARREG_INTERCEPT - Linear Regression Intercept",
        "LINEARREG_SLOPE - Linear Regression Slope",
        "MACDEXT - MACD with controllable MA type",
        "MACDFIX - Moving Average Convergence/Divergence Fix 12/26",
        "MAXINDEX - Index of highest value over a specified period",
        "MEDPRICE - Median Price",
        "MFI - Money Flow Index",
        "MIDPOINT - MidPoint over period",
        "MIDPRICE - Midpoint Price over period",
        "MININDEX - Index of lowest value over a specified period",
        "MINMAX - Lowest and highest values over a specified period",
        "MINMAXINDEX - Indexes of lowest and highest values over a specified period",
        "MINUS_DI - Minus Directional Indicator",
        "MINUS_DM - Minus Directional Movement",
        "MOM - Momentum",
        "NATR - Normalized Average True Range",
        "OBV - On Balance Volume",
        "PLUS_DI - Plus Directional Indicator",
        "PLUS_DM - Plus Directional Movement",
        "PPO - Percentage Price Oscillator",
        "ROC - Rate of change : ((price/prevPrice)-1)*100",
        "ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice",
        "ROCR - Rate of change ratio: (price/prevPrice)",
        "ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100",
        "RSI - Relative Strength Index",
        "SAR - Parabolic SAR",
        "SAREXT - Parabolic SAR - Extended",
        "STDDEV - Standard Deviation",
        "STOCH - Stochastic",
        "STOCHF - Stochastic Fast",
        "STOCHRSI - Stochastic Relative Strength Index",
        "SUM - Summation",
        "TRANGE - True Range",
        "TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA",
        "TSF - Time Series Forecast",
        "TYPPRICE - Typical Price",
        "ULTOSC - Ultimate Oscillator",
        "VAR - Variance",
        "WCLPRICE - Weighted Close Price",
        "WILLR - Williams' %R"
    ]
    
    # 检查已有的指标 - 改进的检测逻辑
    try:
        with open("baselogicfactors.py", 'r', encoding='utf-8') as f:
            existing_code = f.read()
    except FileNotFoundError:
        print(f"错误：baselogicfactors.py 文件不存在，请先创建该文件")
        return
    
    # 使用正则表达式查找所有已实现的指标函数
    implemented_indicators = set()
    # 寻找形如 "def INDICATOR_NAME(" 的模式
    pattern = re.compile(r'@nb\.njit\s+def\s+([A-Z0-9_]+)\s*\(', re.MULTILINE)
    # 也查找形如 "@staticmethod\n    @nb.njit\n    def INDICATOR_NAME(" 的模式
    alternative_pattern = re.compile(r'@staticmethod\s+@nb\.njit\s+def\s+([A-Z0-9_]+)\s*\(', re.MULTILINE | re.DOTALL)
    
    # 合并两种模式的匹配结果
    for match in pattern.finditer(existing_code):
        implemented_indicators.add(match.group(1))
    for match in alternative_pattern.finditer(existing_code):
        implemented_indicators.add(match.group(1))
    
    print(f"已检测到 {len(implemented_indicators)} 个已实现的指标")
    print("已实现的指标列表:")
    for indicator in implemented_indicators:
        print(f"- {indicator}")
    
    # 过滤掉已经实现的指标
    indicators_to_generate = []
    for indicator in talib_indicators:
        indicator_name = indicator.split(' - ')[0]
        if indicator_name not in implemented_indicators:
            indicators_to_generate.append(indicator)
    
    print(f"准备生成以下指标: {indicators_to_generate}")
    
    # 如果没有需要生成的指标，直接返回
    if not indicators_to_generate:
        print("所有指标已实现，无需生成。")
        return
    
    # 一个一个处理指标
    total = len(indicators_to_generate)
    for index, indicator_full in enumerate(indicators_to_generate):
        # 提取指标名称
        indicator_name = indicator_full.split(' - ')[0]
        
        print(f"[{index+1}/{total}] 正在处理指标 '{indicator_name}'...")
        
        # 从ta_func目录中查找并提取对应的C代码
        c_file_path = find_indicator_file(indicator_name)
        
        if not c_file_path:
            print(f"找不到指标'{indicator_name}'的C文件，跳过")
            continue
            
        # 提取核心算法
        c_source_code = extract_core_algorithm(c_file_path)
        
        if c_source_code == "无法提取核心算法。":
            print(f"无法提取指标'{indicator_name}'的核心算法，跳过")
            continue
            
        print(f"已从{c_file_path}提取'{indicator_name}'的核心算法")
        
        # 创建提示词
        prompt = create_indicator_prompt(c_source_code, indicator_name)
        
        # 生成Python代码
        generated_code = chain.invoke({"prompt": prompt})
        
        # 添加到文件
        success = append_to_file(generated_code)
        
        if not success:
            print("添加代码到文件失败，停止处理")
            return
            
        print(f"已完成指标'{indicator_name}'的转换")
    
    print("所有指标生成完成！")

if __name__ == "__main__":
    generate_indicators()

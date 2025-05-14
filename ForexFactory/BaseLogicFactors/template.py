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
    # Your Role
    You are a senior engineer specializing in quantitative trading and numerical computation, skilled in converting C code to Python and optimizing Python code with numba to achieve high-performance technical indicator calculations.

    # Your Task
    Please convert the provided C code core algorithm for the {indicator_name} indicator to Python code, maintaining exactly the same logical functionality while using numpy and numba for performance optimization. You must rigorously analyze and understand every line of code and every minute detail in the C source code, ensuring that the converted Python code is completely identical to the original C code in terms of functionality and behavior.

    # Input Parameter Requirements
    Your generated Python function must accept the following parameters:
    - high, open, low, close, vol, oi: six 2D NumPy arrays with shape (tdts, secs)
    - Specific parameters for this indicator (which should be provided with a commonly used default value)

    # Output Requirements
    - Return a 2D NumPy array with the same shape as the input (tdts, secs)
    - Fill invalid data points with np.nan
    - Ensure the starting index of the output exactly matches TA-Lib

    # Code Structure Requirements
    - Must begin with @staticmethod and @nb.njit decorators
    - Must handle data validity (for NaN values and edge cases)
    - Can use the getavailabledata function to handle valid data, or use a method with logic identical to that in the C source code:
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

    # Available Operators List
    Here are all the operators you can use, with detailed input and output format descriptions:

    ## Basic Operations
    - ADD(X:np.array, Y:np.array) -> np.array: Element-wise addition, returns an array of the sum of corresponding elements of X and Y, with the same shape as the input
    - SUB(X:np.array, Y:np.array) -> np.array: Element-wise subtraction, returns an array of X minus Y, with the same shape as the input
    - MULT(X:np.array, Y:np.array) -> np.array: Element-wise multiplication, returns an array of the product of corresponding elements of X and Y, with the same shape as the input
    - DIV(X:np.array, Y:np.array) -> np.array: Element-wise division, returns an array of X divided by Y, with the same shape as the input
    
    ## Mathematical Functions
    - ABS(X:np.array) -> np.array: Returns the element-wise absolute value of X, with the same shape as the input
    - SQRT(X:np.array) -> np.array: Returns the element-wise square root of X, with the same shape as the input
    - EXP(X:np.array) -> np.array: Returns the element-wise exponential function value (e^x) of X, with the same shape as the input
    - LN(X:np.array) -> np.array: Returns the element-wise natural logarithm of X, with the same shape as the input
    - SIN(X:np.array) -> np.array: Returns the element-wise sine value (input in radians) of X, with the same shape as the input
    - COS(X:np.array) -> np.array: Returns the element-wise cosine value (input in radians) of X, with the same shape as the input
    
    ## Statistical Functions
    - MEAN(X:np.array) -> float: Returns the mean of all non-NaN values in X, returns a single float
    - STD(X:np.array) -> float: Returns the standard deviation of all non-NaN values in X, returns a single float
    - CORR(X:np.array, Y:np.array) -> float: Returns the Pearson correlation coefficient of X and Y, returns a single float, range [-1,1]
    
    ## Time Series Operations
    - DELAY(X:np.array, param:int) -> np.array: Shifts X backward by param steps, fills the first param positions with NaN, with the same shape as the input
    - TSMAX(X:np.array, param:int) -> np.array: Returns the maximum value for each position over the past param periods (including current), with the same shape as the input, the first param-1 positions are NaN
    - TSMIN(X:np.array, param:int) -> np.array: Returns the minimum value for each position over the past param periods (including current), with the same shape as the input, the first param-1 positions are NaN
    - CROSS(X:np.array, Y:np.array) -> np.array: Detects where X crosses above Y, returns a boolean array, 1 at crossing positions, 0 elsewhere, with the same shape as the input
    
    ## Moving Averages
    - SMA(X:np.array, period:int) -> np.array: Simple moving average, calculates the arithmetic mean of X over the past period periods, the first period-1 positions are NaN
    - EMA(X:np.array, period:int) -> np.array: Exponential moving average, uses 2/(period+1) as the smoothing factor, the first period-1 positions are NaN
    - WMA(X:np.array, period:int) -> np.array: Weighted moving average, weights decrease linearly, the first period-1 positions are NaN
    - DEMA(X:np.array, period:int) -> np.array: Double exponential moving average, calculates 2*EMA(X)-EMA(EMA(X)), reduces lag
    - TEMA(X:np.array, period:int) -> np.array: Triple exponential moving average, calculates 3*EMA-3*EMA(EMA)+EMA(EMA(EMA))
    - TRIMA(X:np.array, period:int) -> np.array: Triangular moving average, calculates one SMA of X and then another SMA
    - KAMA(X:np.array, period:int) -> np.array: Kaufman adaptive moving average, automatically adjusts the smoothing factor
    - MAMA(X:np.array, fast_limit:float=0.5, slow_limit:float=0.05) -> tuple: Returns MESA adaptive moving average tuple (MAMA, FAMA)
    - T3(X:np.array, period:int, vfactor:float=0.7) -> np.array: Tillson T3 moving average, reduces lag and noise
    - MA(X:np.array, period:int, ma_type:int=0) -> np.array: General moving average, ma_type is an integer from 0-8 to select different types
    
    ## Cumulative/Sliding Window Calculations
    - ROLLING_SUM(X:np.array, param:int) -> np.array: Calculates the sum of X for each position over the past param periods, the first param-1 positions are NaN
    - ROLLING_MEAN(X:np.array, param:int) -> np.array: Calculates the mean of X for each position over the past param periods, the first param-1 positions are NaN
    - EWM(X:np.array, alpha:float) -> float: Exponentially weighted mean, alpha is the smoothing factor (0-1), returns a single float
    - ROLLING_EWM(X:np.array, alpha:float) -> np.array: Rolling exponentially weighted mean, calculates the exponentially weighted mean up to each position

    # Important Notes
    1. Your code must maintain exactly the same algorithm logic and calculation steps as the C source code, including:
       - Exactly the same core algorithm conversion logic
       - Exactly the same sliding window calculation method
       - Exactly the same boundary condition handling
       - Exactly the same logical flow and branch judgments
       - Exactly the same mathematical calculation formulas and methods
       - Exactly the same variable accumulation properties and order
       - Exactly the same calculation loop structure
    
    2. Pay special attention to the following key points that must be precisely maintained:
       - Must fully comply with the unstable period (lookback period) handling method in the C source code, including any special initialization process
       - If there is Wilder smoothing in the C source code, must use the same smoothing method, the same formula, and apply it at the same position
       - Maintain the starting index of the output exactly as in TA-Lib, do not decide the output starting point yourself
       - Must use the same index calculation logic as the C source code to ensure data is correctly aligned
       - If the C source code uses += (accumulation) operations, must maintain the same accumulation logic and order in Python
       - If the C source code processes data in multiple loops, must maintain the same staged processing logic in Python
       - Strictly follow the variable processing flow, update frequency, and calculation order in the C source code
       - Ensure numerical precision is consistent with the C source code, add necessary floating-point precision protection (such as division by zero checks, using small thresholds like 1e-10)
       - For composite indicators that depend on other indicators (such as ADXR depending on ADX), must ensure that the calculation of the base indicator exactly matches the C source code
       - If the indicator has a specific unstable period (such as ADX's 25-period unstable period), must accurately implement this feature
    
    3. The implementation structure must be strictly divided into the following stages:
       - Initialization stage: Set up the correct lookback period, exactly corresponding to the C source code
       - Data validation stage: Ensure there are enough sample points to calculate the indicator
       - Warm-up period processing: Follow the warm-up process in the C source code to prepare for indicator calculation (no output)
       - Unstable period processing: Specifically process unstable period data after warm-up (if this logic exists in the C source code)
       - Main calculation stage: Perform the entire calculation process separately for each security (sec), output the final result
       - Ensure each stage is consistent with the TA-Lib source code flow, including loop structure and calculation order

    4. For indicators involving Wilder smoothing, must follow these calculation formulas:
       - Initial value = Simple average of the first N values
       - Subsequent values = (Previous smoothed value * (N-1) + Current value) / N
       - Ensure the smoothing factor, initialization logic, and application position are exactly the same as in TA-Lib
    
    5. For composite indicators (such as ADXR = (ADX + ADX from N periods ago)/2):
       - Must first fully calculate all values of the base indicator
       - Then combine these base indicators according to the C source code logic
       - Do not try to calculate the composite indicator while calculating the base indicator
       - Ensure the correct data index relationships are used (such as current value with the value from N periods ago)
       
    6. Most importantly, you must analyze the C source code line by line, understanding the meaning and function of each line of code:
       - Clarify the role of each variable and the source of its values
       - Understand the intention and impact of each conditional judgment
       - Master the purpose and boundary conditions of each loop
       - Note the order and priority of each mathematical operation
       - Pay attention to the lifecycle and value changes of each temporary variable
       - Identify each edge case and special handling
       - Fully understand the meaning and selection reason for all constants
       
    7. The conversion should be completely logically equivalent, even if there appears to be a better implementation method:
       - Maintain performance optimization techniques from the original C code
       - Maintain variable reuse patterns from the original C code
       - Maintain memory access patterns from the original C code
       - Do not use more advanced Python features to "improve" the algorithm unless they can produce exactly the same results as the C code
       - Even if you find possible errors or inefficiencies in the C code, preserve these characteristics as they are
       - The goal of the conversion is complete behavioral equivalence, not functional improvement or redesign

    # C Source Code
    ```
    {c_source_code}
    ```

    # Reference Example 1 - ATR Indicator
    @staticmethod
    @nb.njit
    def ATR(high, open, low, close, vol, oi, timeperiod=14):
        \"\"\"
        # ATR - Average True Range
        # The Average True Range is the maximum of the following three:
        # val1 = current day's high minus current day's low
        # val2 = absolute value of current day's high minus previous day's close
        # val3 = absolute value of current day's low minus previous day's close
        # Averages these values over the specified period using the Wilder method, which has an unstable period equivalent to an exponential moving average (EMA).
        \"\"\"
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        
        for sec in range(secs):
            # Precisely simulate TA-Lib's data processing method
            
            # Step 1: Create a mask for valid data
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
            
            # Step 2: Create continuous data sequences (without NaN)
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
            valid_indices = np.where(valid_mask)[0]
            
            # If there is not enough valid data, skip
            if len(valid_high) <= timeperiod:
                continue
            
            # Step 3: Calculate all TR values
            tr_values = np.zeros(len(valid_high))
            # The TR for the first point can only use high-low
            tr_values[0] = valid_high[0] - valid_low[0]
            
            # Calculate TR for remaining points
            for i in range(1, len(valid_high)):
                tr_1 = valid_high[i] - valid_low[i]
                tr_2 = abs(valid_close[i-1] - valid_high[i])
                tr_3 = abs(valid_close[i-1] - valid_low[i])
                tr_values[i] = max(tr_1, tr_2, tr_3)
            
            # Step 4: Calculate ATR
            atr_values = np.zeros(len(valid_high))
            # The first ATR value is the simple average of the first timeperiod TRs
            if timeperiod <= 1:
                # For timeperiod=1, ATR is just TR
                atr_values = tr_values
            else:
                # Calculate the first ATR (equal to the simple average of the first timeperiod TRs)
                first_atr = 0.0
                for i in range(timeperiod):
                    first_atr += tr_values[i]
                first_atr /= timeperiod
                atr_values[timeperiod-1] = first_atr
                
                # Use the Wilder smoothing formula to calculate the remaining ATR values
                for i in range(timeperiod, len(tr_values)):
                    atr_values[i] = (atr_values[i-1] * (timeperiod-1) + tr_values[i]) / timeperiod
            
            # Step 5: Map the results back to the original array
            # TA-Lib starts outputting ATR from the timeperiod-th point
            start_idx = timeperiod - 1 if timeperiod > 1 else 0
            for i in range(start_idx, len(valid_indices)):
                orig_idx = valid_indices[i]
                result[orig_idx, sec] = atr_values[i]
        
        return result

    # Reference Example 2 - CDLDOJI Indicator
    @staticmethod
    @nb.njit
    def CDLDOJI(high, open, low, close, vol, oi):
        \"\"\"
        CDLDOJI - Candlestick Doji Pattern
        
        # The CDLDOJI indicator is used to identify Doji (cross-line) candlestick patterns
        # Calculation method: When opening and closing prices are very close (body smaller than a certain percentage of the candle range), a cross-line pattern is formed
        # Usage: Used to identify market hesitation, may indicate a trend reversal
        \"\"\"
        # Get data dimensions
        tdts, secs = high.shape
        
        # Initialize result array
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        
        # BodyDoji average period, typically 3
        BodyDojiPeriod = 3
        
        for sec in range(secs):
            for ts in range(tdts):
                # Data validation
                if ts <= BodyDojiPeriod or close[ts, sec] != close[ts, sec]:
                    continue
                    
                # Data preparation
                _high = high[:ts + 1, sec]
                _open = open[:ts + 1, sec]
                _low = low[:ts + 1, sec]
                _close = close[:ts + 1, sec]
                _vol = vol[:ts + 1, sec]
                _oi = oi[:ts + 1, sec]
                
                # Use getavailabledata function to get available data
                myopen = getavailabledata(_open, ts + 1)
                myhigh = getavailabledata(_high, ts + 1)
                myclose = getavailabledata(_close, ts + 1)
                mylow = getavailabledata(_low, ts + 1)
                myvol = getavailabledata(_vol, ts + 1)
                myoi = getavailabledata(_oi, ts + 1)
                
                # Calculate real body size
                realbody = np.abs(myclose - myopen)
                
                # Calculate candlestick range (assuming BodyDoji type corresponds to a certain proportion of the high-low difference)
                candleRange = myhigh - mylow
                
                # Initialize BodyDojiPeriodTotal
                BodyDojiPeriodTotal = 0
                
                # Calculate the sum of candleRange for the previous BodyDojiPeriod periods
                for i in range(ts - BodyDojiPeriod, ts):
                    # Ensure data is valid
                    if i >= 0 and candleRange[i] == candleRange[i]:
                        BodyDojiPeriodTotal += candleRange[i]
                
                # Calculate average
                if BodyDojiPeriod > 0:
                    BodyDojiAverage = BodyDojiPeriodTotal / BodyDojiPeriod
                else:
                    BodyDojiAverage = 0
                    
                # Doji judgment: real body size is less than or equal to a certain proportion of the average range
                # Set a small coefficient, such as 0.1, indicating that the real body size does not exceed 10% of the average range
                DojiBodyCoef = 0.1
                
                # Determine if the current k-line is a Doji
                if realbody[ts] <= BodyDojiAverage * DojiBodyCoef:
                    result[ts, sec] = 100
                else:
                    result[ts, sec] = 0
                    
        return result

    # Reference Example 3 - ADXR Indicator
    @staticmethod
    @nb.njit
    def ADXR(high, open, low, close, vol, oi, timeperiod=14):
        tdts, secs = high.shape
        result = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        
        for sec in range(secs):
            # Create valid data mask
            valid_mask = np.zeros(tdts, dtype=np.bool_)
            for i in range(tdts):
                if (high[i, sec] == high[i, sec] and 
                    low[i, sec] == low[i, sec] and 
                    close[i, sec] == close[i, sec]):
                    valid_mask[i] = True
            
            valid_indices = np.where(valid_mask)[0]
            if len(valid_indices) <= (2 * timeperiod) + 24:  # Need enough data (ADX lookback + timeperiod - 1)
                continue
                
            # Extract valid data
            valid_high = high[valid_mask, sec]
            valid_low = low[valid_mask, sec]
            valid_close = close[valid_mask, sec]
            
            # Calculate ADX (based on ADX function logic in baselogicfactors)
            adx_values = np.zeros(len(valid_high))
            
            # Initialize variables
            prev_minus_dm = 0.0
            prev_plus_dm = 0.0
            prev_tr = 0.0
            prev_adx = 0.0
            unstable_period = 25  # TA-Lib default unstable period
            
            # Handle initialization of the first point
            prev_high = valid_high[0]
            prev_low = valid_low[0]
            prev_close = valid_close[0]
            
            # First loop: Initialize cumulative values for MinusDM, PlusDM, and TR
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
                
                # True Range calculation
                tr = max(valid_high[i] - valid_low[i], 
                        max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                sum_tr += tr
                prev_close = valid_close[i]
            
            # Initialize EMA values
            prev_plus_dm = sum_dm_plus
            prev_minus_dm = sum_dm_minus
            prev_tr = sum_tr
            
            # Second loop: Calculate initial sumDX value
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
                
                # True Range calculation
                tr = max(valid_high[i] - valid_low[i], 
                        max(abs(valid_high[i] - prev_close), abs(valid_low[i] - prev_close)))
                prev_tr = prev_tr - (prev_tr / timeperiod) + tr
                prev_close = valid_close[i]
                
                # Note: Use more precise zero value detection
                if prev_tr > 1e-10:
                    minus_di = 100.0 * (prev_minus_dm / prev_tr)
                    plus_di = 100.0 * (prev_plus_dm / prev_tr)
                    temp_real = minus_di + plus_di
                    if temp_real > 1e-10:
                        sum_dx += 100.0 * (abs(minus_di - plus_di) / temp_real)
            
            # Calculate initial ADX value
            prev_adx = sum_dx / timeperiod
            
            # Third loop: Process unstable period
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
                
                # True Range calculation
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
            
            # Main loop: Calculate and record remaining ADX values
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
                
                # True Range calculation
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
            
            # Calculate ADXR values: (current ADX + ADX from (timeperiod) days ago)/2
            adxr_values = np.zeros(len(valid_high))
            for i in range(timeperiod - 1, len(valid_high)):
                if i >= timeperiod + start_idx - 1:  # Ensure previous ADX values are available
                    adxr_values[i] = (adx_values[i] + adx_values[i - (timeperiod - 1)]) / 2.0
            
            # Map results back to the original array
            for i in range(len(valid_indices)):
                if i >= timeperiod + start_idx - 1:
                    orig_idx = valid_indices[i]
                    result[orig_idx, sec] = adxr_values[i]

        return result

    Now, based on the given C language core algorithm, according to the above requirements and reference examples, please implement the Python code for the {indicator_code} indicator. Pay special attention to maintaining exactly the same calculation logic, unstable period handling, index alignment, and data flow as the C source code.
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

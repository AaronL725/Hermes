import numpy as np
from numba import njit


@njit
def TSMAX(X:np.array, param:int) -> np.array:
    """
    Calculate the maximum value over a rolling window of size `param` for each element in the array X.

    This function takes a numpy array X and an integer parameter `param` as input. It returns a new array where each element is the maximum
    value observed within a sliding window of size `param` centered at that element (considering only valid elements without NaNs). If the window does not contain enough elements, it will be filled with NaN.

    Parameters:
        X (np.array): The input array.
        param (int): The size of the rolling window.

    Returns:
        np.array: A new array where each element is the maximum value over a rolling window centered at that element, considering only valid elements without NaNs.
                  If the window does not contain enough elements, it will be filled with NaN.

    Examples:
        >>> TSMAX(np.array([1, 2, 3, 4, 5]), 3)
        array([nan, nan, 3., 4., 5.])

        >>> TSMAX(np.array([1, 2, np.nan, 4, 5]), 3)
        array([nan, nan, nan, 4., 5.])
    """
    max = np.array([np.nan]*len(X))
    for i in range(param,len(X)):
        max[i] = np.nanmax(X[i-param+1:i+1])
    return max


@njit
def TSMIN(X:np.array, param:int) -> np.array:
    """
    Calculate the minimum value over a rolling window of size `param` for each element in the array X.

    This function takes a numpy array X and an integer parameter `param` as input. It returns a new array where each element is the minimum
    value observed within a sliding window of size `param` centered at that element (considering only valid elements without NaNs). If the window does not contain enough elements, it will be filled with NaN.

    Parameters:
        X (np.array): The input array.
        param (int): The size of the rolling window.

    Returns:
        np.array: A new array where each element is the minimum value over a rolling window centered at that element, considering only valid elements without NaNs.
                  If the window does not contain enough elements, it will be filled with NaN.

    Examples:
        >>> TSMIN(np.array([1, 2, 3, 4, 5]), 3)
        array([nan, nan, 1., 2., 3.])

        >>> TSMIN(np.array([1, 2, np.nan, 4, 5]), 3)
        array([nan, nan, nan, 1., 2.])
    """
    min = np.array([np.nan]*len(X))
    for i in range(param,len(X)):
        min[i] = np.nanmin(X[i-param+1:i+1])
    return min





@njit
def EWM(X:np.array,alpha:float)->float:
    """
    Calculate the exponential weighted moving average (EWM) of an array X with a given smoothing factor alpha.

    This function takes a numpy array X and a float parameter `alpha` as input. It returns the exponentially weighted moving average of X, where each element is calculated using the formula:
    EWMA(t) = alpha * X(t) + (1 - alpha) * EWMA(t-1), with the initial condition set to the first value of X if it exists and NaN otherwise.

    Parameters:
        X (np.array): The input array.
        alpha (float): The smoothing factor, ranging from 0 to 1. A higher value of alpha gives more weight to recent observations.

    Returns:
        float: The exponentially weighted moving average of the input array X. If an element is non-positive or if it does not exist in X, it will be replaced with NaN.

    Examples:
        >>> EWM(np.array([1, 2, 3, 4, 5]), 0.5)
        3.768905951452255

        >>> EWM(np.array([-1, -2, -3, -4, -5]), 0.5)
        NaN
    """
    x_num = 0
    for i in range(len(X)):
        if X[i]==X[i]:
            x_num+=1
    _X = [np.nan]*x_num
    _X_index=0
    for i in range(len(X)):
        if X[i]==X[i]:
            _X[_X_index]=X[i]
            _X_index+=1
    _X = np.array(_X)
    alpha_rev = 1 - alpha
    n = _X.shape[0]

    pows = alpha_rev ** (np.arange(n + 1))

    scale_arr = 1 / pows[:-1]

    offset =_X[0] * pows[1:]
    pw0 = alpha * alpha_rev ** (n - 1)

    mult = _X * pw0 * scale_arr

    cumsums = mult.cumsum()
    out = offset + cumsums * scale_arr[::-1]
    return out[-1]
@njit
def ROLLING_EWM(X:np.array,alpha:float)->np.array:
    """
    Calculate the rolling weighted mean of an array using a linear decay weighting scheme over a window of size `param`.

    This function takes a numpy array X and a float parameter `alpha` as input. It returns a new array where each element is the exponential weighted mean of values within a sliding window of size `param` centered at that element, calculated using an exponential decay weighting scheme with alpha as the smoothing factor. If the window does not contain enough elements, it will be filled with NaN.

    Parameters:
        X (np.array): The input array.
        alpha (float): The smoothing factor for the exponential weighted mean.

    Returns:
        np.array: A new array where each element is the exponential weighted mean over a rolling window centered at that element, calculated using an exponential decay weighting scheme with alpha as the smoothing factor. If the window does not contain enough elements, it will be filled with NaN.

    Examples:
        >>> ROLLING_EWM(np.array([1, 2, 3, 4, 5]), 0.5)
        array([nan, nan, nan, nan, 3.])
    """
    output = [np.nan]*len(X)
    for i in range(1,len(X)):
        output[i] = EWM(X[:i+1],alpha)
    return np.array(output)

@njit
def STD(X:np.array)->float:
    """
    Calculate the STD of an array X 
    """
    return np.nanstd(X)

@njit
def MEAN(X:np.array)->float:
    """
    Calculate the mean of an array X 
    This function takes a numpy array X and an integer N as input, and returns the mean of each element in X when considering a rolling window of size N centered at that element. If the window does not contain enough elements (i.e., if there are fewer than N/2 elements on either side), it will be filled with NaN.          
    """
    return np.nanmean(X)


@njit
def CORR(X:np.array,Y:np.array)->float:
    """
    Calculate the Pearson correlation coefficient between two arrays X and Y.

    This function takes two numpy arrays X and Y as input and returns the Pearson correlation coefficient, which measures the linear
    relationship between the two arrays. The result is a float value ranging from -1 to 1, where 1 indicates a perfect positive linear
    relationship, -1 indicates a perfect negative linear relationship, and 0 indicates no linear relationship.

    Parameters:
        X (np.array): The first input array.
        Y (np.array): The second input array.

    Returns:
        float: The Pearson correlation coefficient between the two arrays.

    Examples:
        >>> CORR(np.array([1, 2, 3]), np.array([4, 2, -1]))
        0.5

        >>> CORR(np.array([0, 0, 0]), np.array([-1, 2, 3]))
        0.0
    """
    return np.float32(np.corrcoef(X,Y)[0,1])



@njit
def DELAY(X:np.array,param:int)->np.array:
    """
    Calculate the delayed value of each element in the array X by shifting it back by `param` steps.

    This function takes a numpy array X and an integer parameter `param` as input. It returns a new array where each element is shifted back by `param` steps. If the shift goes beyond the start of the array, the value will be NaN.

    Parameters:
        X (np.array): The input array.
        param (int): The number of steps to shift back.

    Returns:
        np.array: A new array where each element is shifted back by `param` steps. If the shift goes beyond the start of the array, the value will be NaN.

    Examples:
        >>> DELAY(np.array([1, 2, 3, 4, 5]), 2)
        array([nan, nan, 1., 2., 3.])

        >>> DELAY(np.array([-1, -2, -3, -4, -5]), 3)
        array([nan, nan, nan, -1., -2.])
    """
    shifted_X = np.array([np.nan]*len(X))
    for i in range(param,len(X)):
        shifted_X[i] = X[i-param]
    return shifted_X


@njit
def ABS(X:np.array)->np.array:
    """
    Calculate the element-wise absolute value of each element in the array X.

    This function takes a numpy array X as input and returns a new array where each element is the absolute value of the corresponding element in X.

    Parameters:
        X (np.array): The input array.

    Returns:
        np.array: A new array where each element is the absolute value of the elements at the corresponding positions in X.

    Examples:
        >>> ABS(np.array([-1, -2, 3, -4]))
        array([1, 2, 3, 4])

        >>> ABS(np.array([0, 0, 0]))
        array([0, 0, 0])
    """
    return np.abs(X)

@njit
def ROLLING_MEAN(X,param):
    out = [np.nan]*len(X)
    for i in range(len(X)):
        if i>=param-1:
            out[i] = np.nanmean(X[i+1-param:i+1])
    return np.array(out)

@njit
def ADD(X:np.array, Y:np.array) -> np.array:
    """
    Calculate the element-wise addition between two arrays X and Y.

    This function takes two numpy arrays X and Y as input and returns a new array
    where each element is the sum of the corresponding elements in X and Y.

    Parameters:
        X (np.array): The first input array.
        Y (np.array): The second input array.

    Returns:
        np.array: A new array where each element is the sum of the elements at
                  the corresponding positions in X and Y.

    Examples:
        >>> ADD(np.array([1, 2, 3]), np.array([4, 2, -1]))
        array([5, 4, 2])

        >>> ADD(np.array([0, 0, 0]), np.array([-1, 2, 3]))
        array([-1, 2, 3])
    """
    return X + Y

@njit
def SUB(X:np.array, Y:np.array) -> np.array:
    """
    Calculate the element-wise subtraction between two arrays X and Y.

    This function takes two numpy arrays X and Y as input and returns a new array
    where each element is the result of subtracting the corresponding element in Y from X.

    Parameters:
        X (np.array): The first input array.
        Y (np.array): The second input array.

    Returns:
        np.array: A new array where each element is the result of X - Y at
                  the corresponding positions.

    Examples:
        >>> SUB(np.array([1, 2, 3]), np.array([4, 2, -1]))
        array([-3, 0, 4])

        >>> SUB(np.array([0, 0, 0]), np.array([-1, 2, 3]))
        array([1, -2, -3])
    """
    return X - Y

@njit
def MULT(X:np.array, Y:np.array) -> np.array:
    """
    Calculate the element-wise multiplication between two arrays X and Y.

    This function takes two numpy arrays X and Y as input and returns a new array
    where each element is the product of the corresponding elements in X and Y.

    Parameters:
        X (np.array): The first input array.
        Y (np.array): The second input array.

    Returns:
        np.array: A new array where each element is the product of the elements at
                  the corresponding positions in X and Y.

    Examples:
        >>> MULT(np.array([1, 2, 3]), np.array([4, 2, -1]))
        array([4, 4, -3])

        >>> MULT(np.array([0, 0, 0]), np.array([-1, 2, 3]))
        array([0, 0, 0])
    """
    return X * Y

@njit
def DIV(X:np.array, Y:np.array) -> np.array:
    """
    Calculate the element-wise division between two arrays X and Y.

    This function takes two numpy arrays X and Y as input and returns a new array
    where each element is the result of dividing the corresponding element in X by Y.

    Parameters:
        X (np.array): The first input array (numerator).
        Y (np.array): The second input array (denominator).

    Returns:
        np.array: A new array where each element is the result of X / Y at
                  the corresponding positions.

    Examples:
        >>> DIV(np.array([4, 4, -3]), np.array([2, 1, -1]))
        array([2, 4, 3])

        >>> DIV(np.array([0, 0, 0]), np.array([-1, 2, 3]))
        array([0, 0, 0])
    """
    return X / Y

@njit
def ROLLING_SUM(X:np.array, param:int) -> np.array:
    """
    Calculate the rolling sum over a window of size `param` for each element in the array X.

    This function takes a numpy array X and an integer parameter `param` as input. It returns a new array
    where each element is the sum of values within a sliding window of size `param` ending at that element.
    If the window does not contain enough elements, it will be filled with NaN.

    Parameters:
        X (np.array): The input array.
        param (int): The size of the rolling window.

    Returns:
        np.array: A new array where each element is the sum over a rolling window ending at that element.
                  If the window does not contain enough elements, it will be filled with NaN.

    Examples:
        >>> ROLLING_SUM(np.array([1, 2, 3, 4, 5]), 3)
        array([nan, nan, 6., 9., 12.])

        >>> ROLLING_SUM(np.array([1, 2, np.nan, 4, 5]), 3)
        array([nan, nan, nan, 7., 9.])
    """
    result = np.array([np.nan] * len(X))
    for i in range(param-1, len(X)):
        result[i] = np.nansum(X[i-param+1:i+1])
    return result

@njit
def SQRT(X:np.array) -> np.array:
    """
    Calculate the element-wise square root of each element in the array X.

    This function takes a numpy array X as input and returns a new array where each
    element is the square root of the corresponding element in X.

    Parameters:
        X (np.array): The input array.

    Returns:
        np.array: A new array where each element is the square root of the elements at
                  the corresponding positions in X.

    Examples:
        >>> SQRT(np.array([1, 4, 9, 16]))
        array([1.0, 2.0, 3.0, 4.0])

        >>> SQRT(np.array([0, 0, 0]))
        array([0.0, 0.0, 0.0])
    """
    return np.sqrt(X)

@njit
def CROSS(X:np.array, Y:np.array) -> np.array:
    """
    Detect crossover events between two arrays X and Y.

    This function takes two numpy arrays X and Y as input and returns a new array
    where each element is 1 if X crosses above Y at that position, 0 otherwise.
    A crossover is defined as X being below Y in the previous period and above Y in the current period.

    Parameters:
        X (np.array): The first input array.
        Y (np.array): The second input array.

    Returns:
        np.array: A new array where each element is 1 if X crosses above Y at that position, 0 otherwise.

    Examples:
        >>> CROSS(np.array([1, 3, 2, 4]), np.array([2, 2, 3, 3]))
        array([0, 1, 0, 1])

        >>> CROSS(np.array([1, 2, 3]), np.array([3, 2, 1]))
        array([0, 0, 1])
    """
    result = np.zeros(len(X))
    for i in range(1, len(X)):
        if X[i-1] <= Y[i-1] and X[i] > Y[i]:
            result[i] = 1
    return result

@njit
def EXP(X:np.array) -> np.array:
    """
    Calculate the element-wise exponential of each element in the array X.

    This function takes a numpy array X as input and returns a new array where each
    element is e raised to the power of the corresponding element in X.

    Parameters:
        X (np.array): The input array.

    Returns:
        np.array: A new array where each element is the exponential (e^x) of the elements at
                  the corresponding positions in X.

    Examples:
        >>> EXP(np.array([0, 1, 2]))
        array([1.0, 2.7182818, 7.3890561])

        >>> EXP(np.array([-1, 0, 1]))
        array([0.36787944, 1.0, 2.7182818])
    """
    return np.exp(X)

@njit
def LN(X:np.array) -> np.array:
    """
    Calculate the element-wise natural logarithm of each element in the array X.

    This function takes a numpy array X as input and returns a new array where each
    element is the natural logarithm (base e) of the corresponding element in X.

    Parameters:
        X (np.array): The input array.

    Returns:
        np.array: A new array where each element is the natural logarithm of the elements at
                  the corresponding positions in X.

    Examples:
        >>> LN(np.array([1, 2.7182818, 7.3890561]))
        array([0.0, 1.0, 2.0])

        >>> LN(np.array([0.36787944, 1.0, 2.7182818]))
        array([-1.0, 0.0, 1.0])
    """
    return np.log(X)

@njit
def SIN(X:np.array) -> np.array:
    """
    Calculate the element-wise sine of each element in the array X.

    This function takes a numpy array X as input and returns a new array where each
    element is the sine of the corresponding element in X (assumed to be in radians).

    Parameters:
        X (np.array): The input array with values in radians.

    Returns:
        np.array: A new array where each element is the sine of the elements at
                  the corresponding positions in X.

    Examples:
        >>> SIN(np.array([0, np.pi/2, np.pi]))
        array([0.0, 1.0, 0.0])

        >>> SIN(np.array([-np.pi/2, 0, np.pi/2]))
        array([-1.0, 0.0, 1.0])
    """
    return np.sin(X)

@njit
def COS(X:np.array) -> np.array:
    """
    Calculate the element-wise cosine of each element in the array X.

    This function takes a numpy array X as input and returns a new array where each
    element is the cosine of the corresponding element in X (assumed to be in radians).

    Parameters:
        X (np.array): The input array with values in radians.

    Returns:
        np.array: A new array where each element is the cosine of the elements at
                  the corresponding positions in X.

    Examples:
        >>> COS(np.array([0, np.pi/2, np.pi]))
        array([1.0, 0.0, -1.0])

        >>> COS(np.array([-np.pi, 0, np.pi]))
        array([-1.0, 1.0, -1.0])
    """
    return np.cos(X)

@njit
def SMA(X:np.array, period:int) -> np.array:
    """
    Simple Moving Average
    
    Calculates an unweighted moving average over the specified period.
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        
    Returns:
        np.array: Simple moving average
    """
    result = np.full(len(X), np.nan)
    
    # Return early if period is less than or equal to 1
    if period <= 1:
        return X.copy()
    
    # Calculate SMA
    for i in range(period-1, len(X)):
        # Use nanmean to handle any possible NaN values
        result[i] = np.nanmean(X[i-(period-1):i+1])
    
    return result

@njit
def EMA(X:np.array, period:int) -> np.array:
    """
    Exponential Moving Average
    
    Calculates an exponentially weighted moving average over the specified period.
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        
    Returns:
        np.array: Exponential moving average
    """
    result = np.full(len(X), np.nan)
    
    # Return early if period is less than or equal to 1
    if period <= 1:
        return X.copy()
    
    # Calculate the multiplier (k)
    k = 2.0 / (period + 1.0)
    one_minus_k = 1.0 - k
    
    # Initialize lookback
    lookback = period - 1
    
    # Find first valid value for initialization
    start_idx = 0
    while start_idx < len(X) and np.isnan(X[start_idx]):
        start_idx += 1
    
    if start_idx >= len(X):
        return result  # All input values are NaN
    
    # Initialize using SMA for the first value
    if start_idx + lookback < len(X):
        result[start_idx + lookback] = np.nanmean(X[start_idx:start_idx+period])
        
        # Calculate the rest of EMA values
        for i in range(start_idx + lookback + 1, len(X)):
            if np.isnan(X[i]):
                result[i] = result[i-1]  # Maintain previous value if current input is NaN
            else:
                result[i] = X[i] * k + result[i-1] * one_minus_k
    
    return result

@njit
def WMA(X:np.array, period:int) -> np.array:
    """
    Weighted Moving Average
    
    Calculates a linearly weighted moving average over the specified period.
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        
    Returns:
        np.array: Weighted moving average
    """
    result = np.full(len(X), np.nan)
    
    # Return early if period is less than or equal to 1
    if period <= 1:
        return X.copy()
    
    # Calculate denominator (sum of weights)
    denominator = period * (period + 1) / 2.0
    
    # Calculate WMA
    for i in range(period-1, len(X)):
        numerator = 0.0
        weight = 1.0
        
        for j in range(period):
            idx = i - (period - 1) + j
            if not np.isnan(X[idx]):
                numerator += X[idx] * weight
            weight += 1.0
        
        result[i] = numerator / denominator
    
    return result

@njit
def DEMA(X:np.array, period:int) -> np.array:
    """
    Double Exponential Moving Average
    
    Calculates a double exponential moving average over the specified period.
    DEMA = (2 * EMA(X, period)) - EMA(EMA(X, period), period)
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        
    Returns:
        np.array: Double exponential moving average
    """
    result = np.full(len(X), np.nan)
    
    # Return early if period is less than or equal to 1
    if period <= 1:
        return X.copy()
    
    # Calculate first EMA
    first_ema = EMA(X, period)
    
    # Calculate second EMA (EMA of the first EMA)
    second_ema = EMA(first_ema, period)
    
    # Calculate DEMA: 2 * first_ema - second_ema
    for i in range(len(X)):
        if not np.isnan(first_ema[i]) and not np.isnan(second_ema[i]):
            result[i] = 2.0 * first_ema[i] - second_ema[i]
    
    return result

@njit
def TEMA(X:np.array, period:int) -> np.array:
    """
    Triple Exponential Moving Average
    
    Calculates a triple exponential moving average over the specified period.
    TEMA = 3 * EMA1 - 3 * EMA2 + EMA3
    where:
        EMA1 = EMA(X, period)
        EMA2 = EMA(EMA1, period)
        EMA3 = EMA(EMA2, period)
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        
    Returns:
        np.array: Triple exponential moving average
    """
    result = np.full(len(X), np.nan)
    
    # Return early if period is less than or equal to 1
    if period <= 1:
        return X.copy()
    
    # Calculate first EMA
    ema1 = EMA(X, period)
    
    # Calculate second EMA (EMA of first EMA)
    ema2 = EMA(ema1, period)
    
    # Calculate third EMA (EMA of second EMA)
    ema3 = EMA(ema2, period)
    
    # Calculate TEMA: 3 * ema1 - 3 * ema2 + ema3
    for i in range(len(X)):
        if not np.isnan(ema1[i]) and not np.isnan(ema2[i]) and not np.isnan(ema3[i]):
            result[i] = 3.0 * ema1[i] - 3.0 * ema2[i] + ema3[i]
    
    return result

@njit
def TRIMA(X:np.array, period:int) -> np.array:
    """
    Triangular Moving Average
    
    Calculates a triangular moving average over the specified period.
    TRIMA is basically a double smoothed SMA with triangular weighting.
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        
    Returns:
        np.array: Triangular moving average
    """
    result = np.full(len(X), np.nan)
    
    # Return early if period is less than or equal to 1
    if period <= 1:
        return X.copy()
    
    # Determine the periods for the two SMAs
    if period % 2 == 0:
        period1 = period // 2
        period2 = period // 2 + 1
    else:
        period1 = (period + 1) // 2
        period2 = (period + 1) // 2
    
    # First SMA
    sma1 = SMA(X, period1)
    
    # Second SMA (on the result of the first SMA)
    for i in range(period2-1, len(X)):
        temp_sum = 0.0
        count = 0
        
        for j in range(period2):
            idx = i - (period2 - 1) + j
            if not np.isnan(sma1[idx]):
                temp_sum += sma1[idx]
                count += 1
        
        if count > 0:
            result[i] = temp_sum / count
    
    return result

@njit
def KAMA(X:np.array, period:int) -> np.array:
    """
    Kaufman Adaptive Moving Average
    
    Calculates a moving average that adapts to volatility, moving faster in trending markets 
    and slower in ranging markets.
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        
    Returns:
        np.array: Kaufman adaptive moving average
    """
    result = np.full(len(X), np.nan)
    
    # Return early if period is less than or equal to 1
    if period <= 1:
        return X.copy()
    
    # Constants for fastest and slowest EMA
    fast = 0.666  # 2/(2+1)
    slow = 0.0645  # 2/(30+1)
    
    # Find first valid data point
    start_idx = 0
    while start_idx < len(X) and np.isnan(X[start_idx]):
        start_idx += 1
    
    if start_idx >= len(X) - period:
        return result  # Not enough data
    
    # Initialize KAMA with the first valid data point
    current_kama = X[start_idx + period - 1]
    result[start_idx + period - 1] = current_kama
    
    # Process the rest of the data points
    for i in range(start_idx + period, len(X)):
        if np.isnan(X[i]):
            result[i] = result[i-1]  # Use previous value if current is NaN
            continue
        
        # Calculate direction (signal)
        direction = abs(X[i] - X[i-period])
        
        # Calculate noise (volatility)
        noise = 0.0
        for j in range(1, period + 1):
            if i-j >= 0 and i-j+1 >= 0 and not np.isnan(X[i-j]) and not np.isnan(X[i-j+1]):
                noise += abs(X[i-j+1] - X[i-j])
        
        # Calculate efficiency ratio
        if noise != 0:
            er = direction / noise
        else:
            er = 1.0  # If no noise, we have perfect efficiency
        
        # Calculate smoothing constant
        sc = (er * (fast - slow) + slow) ** 2
        
        # Update KAMA
        current_kama = current_kama + sc * (X[i] - current_kama)
        result[i] = current_kama
    
    return result

@njit
def MAMA(X:np.array, fast_limit:float=0.5, slow_limit:float=0.05) -> tuple:
    """
    MESA Adaptive Moving Average
    
    Calculates both MAMA (MESA Adaptive Moving Average) and FAMA (Following Adaptive Moving Average).
    Uses the Hilbert Transform to adapt to changing market conditions.
    
    Parameters:
        X (np.array): Input array
        fast_limit (float): Upper limit for alpha (default=0.5)
        slow_limit (float): Lower limit for alpha (default=0.05)
        
    Returns:
        tuple: (MAMA array, FAMA array)
    """
    length = len(X)
    mama = np.full(length, np.nan)
    fama = np.full(length, np.nan)
    
    # Constants
    pi = np.pi
    rad2deg = 180.0 / pi
    deg2rad = pi / 180.0
    
    # Smallest lookback needed (based on TA-Lib implementation)
    lookback = 32
    
    if length <= lookback:
        return mama, fama  # Not enough data
    
    # Temporary arrays for the calculations
    smooth = np.zeros(length)
    detrender = np.zeros(length)
    i1 = np.zeros(length)
    q1 = np.zeros(length)
    jI = np.zeros(length)
    jQ = np.zeros(length)
    i2 = np.zeros(length)
    q2 = np.zeros(length)
    re = np.zeros(length)
    im = np.zeros(length)
    period = np.zeros(length)
    
    phase = np.zeros(length)
    delta_phase = np.zeros(length)
    alpha = np.zeros(length)
    
    # Find first valid value
    start_idx = 0
    while start_idx < length and np.isnan(X[start_idx]):
        start_idx += 1
    
    if start_idx >= length - lookback:
        return mama, fama  # Not enough valid data
    
    # Initialize MAMA and FAMA
    mama[start_idx + lookback - 1] = X[start_idx + lookback - 1]
    fama[start_idx + lookback - 1] = X[start_idx + lookback - 1]
    
    # Calculate MAMA and FAMA for the rest of the data
    for i in range(start_idx + lookback, length):
        if np.isnan(X[i]):
            mama[i] = mama[i-1]
            fama[i] = fama[i-1]
            continue
        
        # Price smoothing
        smooth[i] = (4 * X[i] + 3 * X[i-1] + 2 * X[i-2] + X[i-3]) / 10.0
        
        # Detrender calculation
        detrender[i] = (0.0962 * smooth[i] + 0.5769 * smooth[i-2] - 0.5769 * smooth[i-4] - 0.0962 * smooth[i-6]) * (0.075 * period[i-1] + 0.54)
        
        # Hilbert Transform
        # Compute InPhase and Quadrature components
        q1[i] = (0.0962 * detrender[i] + 0.5769 * detrender[i-2] - 0.5769 * detrender[i-4] - 0.0962 * detrender[i-6]) * (0.075 * period[i-1] + 0.54)
        i1[i] = detrender[i-3]
        
        # Advance the phase of I1 and Q1 by 90 degrees
        jI[i] = (0.0962 * i1[i] + 0.5769 * i1[i-2] - 0.5769 * i1[i-4] - 0.0962 * i1[i-6]) * (0.075 * period[i-1] + 0.54)
        jQ[i] = (0.0962 * q1[i] + 0.5769 * q1[i-2] - 0.5769 * q1[i-4] - 0.0962 * q1[i-6]) * (0.075 * period[i-1] + 0.54)
        
        # Phasor addition for 3-bar averaging
        i2[i] = i1[i] - jQ[i]
        q2[i] = q1[i] + jI[i]
        
        # Smooth the I and Q components
        i2[i] = 0.2 * i2[i] + 0.8 * i2[i-1]
        q2[i] = 0.2 * q2[i] + 0.8 * q2[i-1]
        
        # Calculate Real and Imaginary parts
        re[i] = i2[i] * i2[i-1] + q2[i] * q2[i-1]
        im[i] = i2[i] * q2[i-1] - q2[i] * i2[i-1]
        
        # Calculate period
        if im[i] != 0.0 and re[i] != 0.0:
            period[i] = 2 * pi / np.arctan(im[i] / re[i])
        
        if period[i] > 1.5 * period[i-1]:
            period[i] = 1.5 * period[i-1]
        elif period[i] < 0.67 * period[i-1]:
            period[i] = 0.67 * period[i-1]
        
        if period[i] < 6:
            period[i] = 6
        elif period[i] > 50:
            period[i] = 50
        
        # Calculate phase
        if i2[i] != 0.0:
            phase[i] = np.arctan(q2[i] / i2[i]) * rad2deg
        
        # Calculate phase change
        delta_phase[i] = phase[i] - phase[i-1]
        if delta_phase[i] < 1:
            delta_phase[i] = 1
        
        # Calculate alpha
        alpha[i] = fast_limit / delta_phase[i]
        if alpha[i] < slow_limit:
            alpha[i] = slow_limit
        
        # Calculate MAMA and FAMA
        mama[i] = alpha[i] * X[i] + (1 - alpha[i]) * mama[i-1]
        fama[i] = 0.5 * alpha[i] * mama[i] + (1 - 0.5 * alpha[i]) * fama[i-1]
    
    return mama, fama

@njit
def T3(X:np.array, period:int, vfactor:float=0.7) -> np.array:
    """
    Triple Exponential Moving Average (T3)
    
    Calculates Tim Tillson's T3 moving average, which is a smoothed EMA with reduced lag.
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        vfactor (float): Volume factor between 0 and 1 (default=0.7)
        
    Returns:
        np.array: T3 moving average
    """
    length = len(X)
    result = np.full(length, np.nan)
    
    # Return early if period is less than or equal to 1
    if period <= 1:
        return X.copy()
    
    # Calculate the multiplier (k)
    k = 2.0 / (period + 1.0)
    
    # Prepare temporary arrays for intermediate EMAs
    e1 = np.full(length, np.nan)
    e2 = np.full(length, np.nan)
    e3 = np.full(length, np.nan)
    e4 = np.full(length, np.nan)
    e5 = np.full(length, np.nan)
    e6 = np.full(length, np.nan)
    
    # Calculate T3 components
    c1 = -vfactor * vfactor * vfactor
    c2 = 3 * vfactor * vfactor + 3 * vfactor * vfactor * vfactor
    c3 = -6 * vfactor * vfactor - 3 * vfactor - 3 * vfactor * vfactor * vfactor
    c4 = 1 + 3 * vfactor + vfactor * vfactor * vfactor + 3 * vfactor * vfactor
    
    # Find first valid value
    start_idx = 0
    while start_idx < length and np.isnan(X[start_idx]):
        start_idx += 1
    
    # Need at least 6 * (period-1) + 1 valid values
    lookback = 6 * (period - 1)
    if start_idx >= length - lookback:
        return result  # Not enough valid data
    
    # Calculate first valid EMA values using SMA
    if start_idx + period - 1 < length:
        e1[start_idx + period - 1] = np.nanmean(X[start_idx:start_idx + period])
        e2[start_idx + 2 * (period - 1)] = np.nanmean(e1[start_idx + period - 1:start_idx + 2 * period - 1])
        e3[start_idx + 3 * (period - 1)] = np.nanmean(e2[start_idx + 2 * (period - 1):start_idx + 3 * period - 2])
        e4[start_idx + 4 * (period - 1)] = np.nanmean(e3[start_idx + 3 * (period - 1):start_idx + 4 * period - 3])
        e5[start_idx + 5 * (period - 1)] = np.nanmean(e4[start_idx + 4 * (period - 1):start_idx + 5 * period - 4])
        e6[start_idx + 6 * (period - 1)] = np.nanmean(e5[start_idx + 5 * (period - 1):start_idx + 6 * period - 5])
        
        # Calculate first T3 value
        result[start_idx + lookback] = c1 * e6[start_idx + lookback] + c2 * e5[start_idx + lookback] + c3 * e4[start_idx + lookback] + c4 * e3[start_idx + lookback]
    
    # Calculate the rest of the EMA values
    for i in range(start_idx + period, length):
        if np.isnan(X[i]):
            # Propagate previous values if current input is NaN
            if i > 0:
                e1[i] = e1[i-1]
                if i > period - 1:
                    e2[i] = e2[i-1]
                    if i > 2 * (period - 1):
                        e3[i] = e3[i-1]
                        if i > 3 * (period - 1):
                            e4[i] = e4[i-1]
                            if i > 4 * (period - 1):
                                e5[i] = e5[i-1]
                                if i > 5 * (period - 1):
                                    e6[i] = e6[i-1]
                                    if i > lookback:
                                        result[i] = result[i-1]
        else:
            # Calculate e1 (first EMA)
            e1[i] = X[i] * k + e1[i-1] * (1.0 - k)
            
            # Calculate e2-e6 (cascaded EMAs) when sufficient data is available
            if i >= 2 * (period - 1):
                e2[i] = e1[i] * k + e2[i-1] * (1.0 - k)
                if i >= 3 * (period - 1):
                    e3[i] = e2[i] * k + e3[i-1] * (1.0 - k)
                    if i >= 4 * (period - 1):
                        e4[i] = e3[i] * k + e4[i-1] * (1.0 - k)
                        if i >= 5 * (period - 1):
                            e5[i] = e4[i] * k + e5[i-1] * (1.0 - k)
                            if i >= 6 * (period - 1):
                                e6[i] = e5[i] * k + e6[i-1] * (1.0 - k)
                                
                                # Calculate T3
                                result[i] = c1 * e6[i] + c2 * e5[i] + c3 * e4[i] + c4 * e3[i]
    
    return result

@njit
def MA(X:np.array, period:int, ma_type:int=0) -> np.array:
    """
    Moving Average
    
    Calculates a moving average of the specified type.
    
    Parameters:
        X (np.array): Input array
        period (int): Number of periods for the moving average
        ma_type (int): Type of moving average:
                       0 = SMA (Simple Moving Average) - default
                       1 = EMA (Exponential Moving Average)
                       2 = WMA (Weighted Moving Average)
                       3 = DEMA (Double Exponential Moving Average)
                       4 = TEMA (Triple Exponential Moving Average)
                       5 = TRIMA (Triangular Moving Average)
                       6 = KAMA (Kaufman Adaptive Moving Average)
                       7 = MAMA (MESA Adaptive Moving Average, returns only MAMA)
                       8 = T3 (Triple Exponential Moving Average T3)
        
    Returns:
        np.array: Moving average of the specified type
    """
    # Check for valid period
    if period <= 1:
        return X.copy()
    
    # Call the appropriate moving average function based on ma_type
    if ma_type == 0:
        # SMA
        return SMA(X, period)
    elif ma_type == 1:
        # EMA
        return EMA(X, period)
    elif ma_type == 2:
        # WMA
        return WMA(X, period)
    elif ma_type == 3:
        # DEMA
        return DEMA(X, period)
    elif ma_type == 4:
        # TEMA
        return TEMA(X, period)
    elif ma_type == 5:
        # TRIMA
        return TRIMA(X, period)
    elif ma_type == 6:
        # KAMA
        return KAMA(X, period)
    elif ma_type == 7:
        # MAMA (use default parameters, return only MAMA)
        mama, _ = MAMA(X)
        return mama
    elif ma_type == 8:
        # T3
        return T3(X, period)
    else:
        # Default to SMA if invalid ma_type
        return SMA(X, period)


    
import numba as nb
import numpy as np
from BaseLogicFactors.operators import *
import sys
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


class WrappedOperator:
    @staticmethod
    @nb.njit
    def Shift(X:np.array,N1_:int=5)->np.array:
        '''
        This function calculates the time series shift for a given numpy array X.
        The shift is calculated based on the available data up to each timestamp in the time series.

        Inputs@1:
            @X (np.array): A 2D numpy array where the first dimension represents time steps and the second dimension represents different variables.
            @N1_ (int, optional): The number of periods to shift backward. Default is 5.

        Outputs@1:
            np.array: A new numpy array with the same dimensions as X, where each element is the value from the original array shifted by N1_. If there is not enough data available for a particular timestamp, NaN is returned.
        @@:
            @N1_=[1,2,3,4,5,6,7,8,9,10,14,28,56,74,100,170,250]
        '''
        tdts, secs = X.shape
        newX =  np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec]:
                    continue
                _tfactors = X[:ts + 1, sec]
                myfactor = getavailabledata(_tfactors, N1_+1)
                newX[ts,sec] =myfactor[0]
        return newX


    
    @staticmethod
    @nb.njit
    def Diff(X:np.array,N1_=5)->np.array:
        '''
        This function calculates the first difference of a time series for a given numpy array X.
        The difference is calculated based on the available data up to each timestamp in the time series.

        Inputs@1:
            X (np.array): A 2D numpy array where the first dimension represents time steps and the second dimension represents different variables.
            N1_ (int, optional): The number of periods for which data should be available before calculating the difference. Default is 5.

        Outputs@1:
            np.array: A new numpy array with the same dimensions as X, where each element is the first difference from the original array. If there is not enough data available for a particular timestamp, NaN is returned.
        
        @@:
            @N1_=[1,2,3,4,5,6,7,8,9,10,14,28,56,74,100,170,250]
        '''
        tdts, secs = X.shape
        newX =  np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec]:
                    continue
                _tfactors = X[:ts + 1, sec]
                myfactor = getavailabledata(_tfactors, N1_)
                newX[ts,sec] =myfactor[-1] - myfactor[0]
        return newX


    @staticmethod
    @nb.njit
    def MA(X:np.array,N1_=5)->np.array:
        '''
        This function calculates the moving average (MA) of a time series for a given numpy array X.
        The moving average is calculated based on the available data up to each timestamp in the time series.

        Inputs@1:
            X (np.array): A 2D numpy array where the first dimension represents time steps and the second dimension represents different variables.
            N1_ (int, optional): The number of periods for which data should be available before calculating the moving average. Default is 5.

        Outputs@1:
            np.array: A new numpy array with the same dimensions as X, where each element is the moving average from the original array. If there is not enough data available for a particular timestamp, NaN is returned.
        @@:
            @N1_=[3,5,7,10,14,28,56,74,100,170,250]
        '''
        tdts, secs = X.shape
        newX =  np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec]:
                    continue
                _tfactors = X[:ts + 1, sec]
                myfactor = getavailabledata(_tfactors, N1_)
                newX[ts,sec] =MEAN(myfactor)
        return newX
    
    
    @staticmethod
    @nb.njit
    def MACD(X:np.array,N1_=26,N2_=9,N3_=12)->np.array:
        '''
        This function calculates the Moving Average Convergence Divergence (MACD) for a given numpy array X.

        Inputs@1:
            X (np.array): A 2D numpy array where the first dimension represents time steps and the second dimension represents different variables.
            N1_ (int, optional): The number of periods for the long EMA. Default is 26.
            N2_ (int, optional): The number of periods for the signal line (DEA). Default is 9.
            N3_ (int, optional): The number of periods for the short EMA. Default is 12.

        Outputs@3:
            dif (np.array): A new numpy array with the same dimensions as X, representing the difference between the short and long EMAs.
            dea (np.array): A new numpy array with the same dimensions as X, representing the signal line of the MACD.
            macd (np.array): A new numpy array with the same dimensions as X, representing the MACD line itself.
        @@:
            @N1_=[5,10,20,30,44]
            @N2_=[5,10,20,30,44]
            @N3_=[5,10,20,30,44]
        '''
        tdts, secs = X.shape
        dif = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        dea = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        macd = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec]:
                    continue
                N = N1_*3 if ts>=N1_*3 else ts
                _tfactors = X[:ts + 1, sec]
                myfactor = getavailabledata(_tfactors, N)
                long_ewm = ROLLING_EWM(myfactor,alpha=2/(N1_+1))
                short_ewm = ROLLING_EWM(myfactor,alpha=2/(N3_+1))
                _dif = short_ewm - long_ewm
                dif[ts, sec]  = _dif[-1]
                _dea = ROLLING_EWM(_dif,alpha=2/(N2_+1))
                dea[ts,sec] = _dea[-1]
                _macd = (_dif[-1] - _dea[-1]) * 2
                macd[ts, sec] = _macd
        return dif,dea,macd
    
    @staticmethod
    @nb.njit
    def CORR(X:np.array,Y:np.array,N1_=14)->np.array:
        '''
        This function calculates the time series correlation for a given numpy array X and Y.
        The correlation is calculated based on the available data up to each timestamp in the time series.

        Inputs@2:
            X (np.array): A 2D numpy array where the first dimension represents time steps and the second dimension represents different variables.
            Y (np.array): A 2D numpy array where the first dimension represents time steps and the second dimension represents different variables. It should have the same shape as X.
            N1_ (int, optional): The number of periods for which data should be available before calculating the correlation. Default is 14.

        Outputs@1:
            np.array: A new numpy array with the same dimensions as X and Y, where each element is the correlation coefficient from the original arrays. If there is not enough data available for a particular timestamp, NaN is returned.
        @@:
            @N1_=[5,10,14,28,56,74,100]
        '''
        tdts, secs = X.shape
        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec] or Y[ts,sec]!=Y[ts,sec]:
                    continue
                _X = X[:ts + 1, sec]
                _Y = Y[:ts+1,sec]
                myX = getavailabledata(_X, N1_)
                myY = getavailabledata(_Y, N1_)
                newX[ts,sec] = np.float32(np.corrcoef(myX,myY)[0,1])
        return newX

    
    @nb.njit
    def AccelerationRatio(X:np.array,N1_=14)->np.array:
        '''
        This function calculates the acceleration ratio (AR) for a given numpy array X.
        The acceleration ratio is calculated based on the available data up to each timestamp in the time series.

        Inputs@1:
            X (np.array): A 2D numpy array where the first dimension represents time steps and the second dimension represents different variables.
            N1_ (int, optional): The number of periods for which data should be available before calculating the acceleration ratio. Default is 14.

        Outputs@1:
            np.array: A new numpy array with the same dimensions as X, where each element is the acceleration ratio from the original array. If there is not enough data available for a particular timestamp, NaN is returned.
        @@:
            @N1_=[5,10,14,28,56]
        '''
        tdts, secs = X.shape

        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec] :
                    continue
                _X = X[:ts + 1, sec]
                N = N1_*3 if ts>=N1_*3 else ts
                myX = getavailabledata(_X, N)
                diffmyX = myX - DELAY(myX,1)

                newX[ts,sec]  = EWM(diffmyX,alpha=2/(N+1))/(myX[-1])  if myX[-1]!=0 else np.nan

        return newX

    @staticmethod
    @nb.njit
    def Trend(X:np.array,N1_=14,testp = 1/sys.float_info.epsilon )->np.array:
        '''
        This function calculates the trend for a given numpy array X using linear regression.

        Inputs@1:
            X (np.array): A 2D numpy array where the first dimension represents time steps and the second dimension represents different variables.
            N1_ (int, optional): The number of periods for which data should be available before calculating the trend. Default is 14.
            testp (float, optional): Tolerance parameter for condition checking in linear algebra operations. Default is 1/sys.float_info.epsilon.

        Outputs@1:
            np.array: A new numpy array with the same dimensions as X, where each element represents the trend coefficient calculated from a linear regression fit using the last N1_ data points for each variable. If there is not enough data available for a particular timestamp, NaN is returned.
        @@:
            @N1_=[5,10,14,28,56]
        '''
        tdts, secs = X.shape
        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts < N1_ or X[ts,sec] != X[ts,sec] or np.isinf(X[ts,sec]):
                    continue
                _X = X[:ts + 1, sec]
                myX = getavailabledata(_X, N1_)
                myXX = myX[~np.isnan(myX)]
                myNewX = np.vstack((np.ones(myXX.shape),myXX))

                XTX = (myNewX@myNewX.T)
                if np.linalg.cond(XTX) <testp:
                    XTX_inv = np.linalg.inv(XTX)
                else:
                    continue
                betas = XTX_inv @ myNewX @ np.array([np.float64(i) for i in range(len(myXX))])
                newX[ts,sec] = betas[-1]
        return newX

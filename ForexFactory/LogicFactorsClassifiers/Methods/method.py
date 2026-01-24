__doc__='''
Outout must be @1
'''
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

class WrappedMethod:
    @staticmethod
    @nb.njit
    def SectionDivideToNGroups(X:np.array,N1_:int=10,random_int_input = 99999)->np.array:
        """
        This function divides the input array X into N groups based on the number of available data points in each row.

        Inputs@1:
            X (np.array): The input 2D numpy array with shape (time_steps, sections).
            group_num (int): The desired number of groups to divide the data into. Default is 10.
            target_group (int): A placeholder parameter for future extension or customization. Default is 10.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or 0 based on the group assignment.
        @@:
            @N1_=[2,5,10]
        """
        if random_int_input ==99999:
            random_int = np.random.randint(1, N1_+1)
        else:
            random_int = int(random_int_input)
        tdts, secs = X.shape
        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for ts in range(tdts):
            _subX = X[ts, :]

            _available_num = 0
            for sec in range(secs):
                if ~np.isnan(_subX[sec]):
                    _available_num += 1
            if _available_num<N1_ :
                continue
            _subX_sorted,_subX_index = np.sort(_subX),np.argsort(_subX)
            group_size = int(_available_num/N1_)
            # _subX_sorted2 = _subX_sorted[:_available_num] # descending order
            # _subX_index2 = _subX_index[:_available_num] # index of sorted elements in original array

            for sec in range(N1_):
                if sec == N1_ - 1:
                    for ii in _subX_index[(sec * group_size):_available_num]:
                        newX[ts, ii] = sec + 1
                else:
                    for ii in _subX_index[(sec * group_size):(sec + 1) * group_size]:

                        newX[ts, ii] = sec + 1

        nnewX =   np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for ts in range(tdts):
            for sec in range(secs):
                
                if newX[ts,sec] ==random_int:
                    nnewX[ts,sec] = 1
                elif newX[ts,sec]==newX[ts,sec]:
                    nnewX[ts,sec] = 0
                else:
                    continue
        return nnewX,random_int



    @staticmethod
    @nb.njit
    def TimeSeriesDistribute(X:np.array,N1_=240,random_int_input = 99999)->np.array:
        """
        This function distributes the time series data based on specific factors derived from available data points in each row up to a certain point n.

        Inputs@1:
            X (np.array): The input 2D numpy array with shape (time_steps, sections).
            n (int): The number of time steps up to which the distribution is based. Default is 240.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or 0 based on the distribution criteria.
        @@:
            @N1_=[120,240]
        """
        if random_int_input ==99999:
            random_int = np.random.randint(1, N1_+1)
        else:
            random_int = int(random_int_input)
        tdts, secs = X.shape
        newX =  np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec]:
                    continue
                _tfactors = X[:ts + 1, sec]
                myfactor = getavailabledata(_tfactors, N1_)
                temp = (myfactor[-1] - np.nanmean(myfactor))/np.nanstd(myfactor) if np.nanstd(myfactor)!=0 else np.nan
                if random_int == 8 and temp>2:
                    newX[ts,sec] = 1
                elif random_int==7 and temp<=2 and temp>1:
                    newX[ts,sec] = 1
                elif random_int==6 and temp<=1 and temp>0.5:
                    newX[ts,sec] = 1
                elif random_int==5 and temp<=0.5 and temp>0:
                    newX[ts,sec] = 1
                elif random_int==4 and temp<=0 and temp>-0.5:
                    newX[ts,sec] = 1
                elif random_int==3 and temp<=-0.5 and temp>-1:
                    newX[ts,sec] = 1
                elif random_int==2 and temp<=-1 and temp>-2:
                    newX[ts,sec] = 1
                elif random_int==1 and temp<=-2:
                    newX[ts,sec] = 1
                else:
                    newX[ts,sec] = 0
        return newX,random_int



    

    
    @staticmethod
    @nb.njit
    def JC(X:np.array,Y:np.array,N1_:int=5)->np.array:
        """
        This function performs a comparison between two time series data arrays X and Y based on available data points in each row up to a certain point n.

        Inputs@2:
            X (np.array): The first input 2D numpy array with shape (time_steps, sections).
            Y (np.array): The second input 2D numpy array with the same shape as X.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or -1 based on the comparison result, or 0 if no significant difference is found.
        @@:
            @N1_=[1,2,3,4,5]
        """
        tdts, secs = X.shape
        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<2 or X[ts,sec]!=X[ts,sec] or Y[ts,sec]!=Y[ts,sec]:
                    continue
                _X = X[:ts + 1, sec]
                _Y = Y[:ts+1,sec]

                myX = getavailabledata(_X, 2)
                myY = getavailabledata(_Y, 2)
                # dif[ts, sec]  = _dif[-1]
                # dea[ts,sec] = _dea[-1]
                if myX[-1]>myY[-1]    and myX[-2]<=myY[-2]:
                    for i in range(N1_):
                        if ts+i<tdts:
                            newX[ts+i,sec] = 1
                    
                # elif  myX[-1]<myY[-1]  and myX[-2]>=myY[-2]:
                #     for i in range(N1_):
                #         if ts+i<tdts:
                #             newX[ts+i,sec] = -1

        return newX,np.nan

    @staticmethod
    @nb.njit
    def SC(X:np.array,Y:np.array,N1_:int=5)->np.array:
        """
        This function performs a comparison between two time series data arrays X and Y based on available data points in each row up to a certain point n.

        Inputs@2:
            X (np.array): The first input 2D numpy array with shape (time_steps, sections).
            Y (np.array): The second input 2D numpy array with the same shape as X.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or -1 based on the comparison result, or 0 if no significant difference is found.
        @@:
            @N1_=[1,2,3,4,5]
        """
        tdts, secs = X.shape
        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<2 or X[ts,sec]!=X[ts,sec] or Y[ts,sec]!=Y[ts,sec]:
                    continue
                _X = X[:ts + 1, sec]
                _Y = Y[:ts+1,sec]

                myX = getavailabledata(_X, 2)
                myY = getavailabledata(_Y, 2)
                # dif[ts, sec]  = _dif[-1]
                # dea[ts,sec] = _dea[-1]

                    
                if  myX[-1]<myY[-1]  and myX[-2]>=myY[-2]:
                    for i in range(N1_):
                        if ts+i<tdts:
                            newX[ts+i,sec] = 1
        return newX,np.nan
    
    @staticmethod
    @nb.njit
    def BeiLi(X:np.array,Y:np.array,N1_=14)->np.array:
        """
        This function performs a correlation-based comparison between two time series data arrays X and Y based on available data points in each row up to a certain point n.

        Inputs@2:
            X (np.array): The first input 2D numpy array with shape (time_steps, sections).
            Y (np.array): The second input 2D numpy array with the same shape as X.
            n (int): The number of time steps up to which the comparison is based. Default is 14.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or 0 based on the correlation-based comparison result.
        @@:
            @N1_=[14,30,70]
        """
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
                _cor = np.float32(np.corrcoef(myX, myY)[0, 1])
                if _cor < 0:
                    newX[ts, sec] = 1
                else:
                    newX[ts, sec] = 0
        return newX,np.nan


    @staticmethod
    @nb.njit
    def Acceleration(X:np.array,N1_=14)->np.array:
        """
        This function analyzes the acceleration of a time series based on available data points in each row up to a certain point n.

        Inputs@1:
            X (np.array): The input 2D numpy array with shape (time_steps, sections).
            n (int): The number of time steps up to which the acceleration is analyzed. Default is 14.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element indicates whether there is an upward or downward acceleration based on available data points.
        @@:
            @N1_=[14,30,70]
        """
        tdts, secs = X.shape

        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec]:
                    continue
                _X = X[:ts + 1, sec]
                myX = getavailabledata(_X, N1_*2)
                diffmyX = myX - DELAY(myX,1)
                if EWM(diffmyX,alpha=2/(N1_+1))   >0:
                    newX[ts,sec] =     1

                else:
                    newX[ts,sec] = 0
        return newX,np.nan
    @staticmethod
    @nb.njit
    def Deceleration(X:np.array,N1_=14)->np.array:
        """
        This function analyzes the acceleration of a time series based on available data points in each row up to a certain point n.

        Inputs@1:
            X (np.array): The input 2D numpy array with shape (time_steps, sections).
            n (int): The number of time steps up to which the acceleration is analyzed. Default is 14.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element indicates whether there is an upward or downward acceleration based on available data points.
        @@:
            @N1_=[14,30,70]
        """
        tdts, secs = X.shape

        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<N1_ or X[ts,sec]!=X[ts,sec]:
                    continue
                _X = X[:ts + 1, sec]
                myX = getavailabledata(_X, N1_*2)
                diffmyX = myX - DELAY(myX,1)

                if  EWM(diffmyX,alpha=2/(N1_+1))   <0:
                    newX[ts,sec] = 1
                else:
                    newX[ts,sec] = 0
        return newX,np.nan
    @staticmethod
    @nb.njit
    def ContinueUp(X:np.array,N1_=1,N2_=2)->np.array:
        """
        This function checks if the time series continues to increase over a specified number of consecutive steps starting from a given point in each row.

        Inputs@1:
            X (np.array): The input 2D numpy array with shape (time_steps, sections).
            N1_ (int): The minimum number of consecutive steps required for the series to be considered increasing. Default is 1.
            N2_ (int): The maximum number of consecutive steps to check. Default is 2.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element indicates whether the series continues to increase over the specified range.
        @@:
            @N1_=[1,2,3,4,5]
            @N2_=[1,2,3,4,5]
        """
        tdts, secs = X.shape

        ContinueKNum = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)

        for sec in range(secs):
            for ts in range(tdts):
                if ts <=N1_ or  X[ts,sec]!=X[ts,sec] or np.isinf(X[ts,sec]):
                    continue

                _X = X[:ts + 1, sec]
                myX = getavailabledata(_X, N1_+1)

                _n = 0
                for i in range(1,N1_+1):
                    if myX[i]>myX[i-1]:
                        _n +=1
                if _n == N1_:
                    for i in range(N2_):
                        if ts+i<tdts:
                            ContinueKNum[ts+i,sec] = 1
        return  ContinueKNum,np.nan
    @staticmethod
    @nb.njit
    def ContinueDown(X:np.array,N1_=1,N2_=2):
        """
        This function checks if the time series continues to increase over a specified number of consecutive steps starting from a given point in each row.

        Inputs@1:
            X (np.array): The input 2D numpy array with shape (time_steps, sections).
            N1_ (int): The minimum number of consecutive steps required for the series to be considered increasing. Default is 1.
            N2_ (int): The maximum number of consecutive steps to check. Default is 2.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element indicates whether the series continues to increase over the specified range.
        @@:
            @N1_=[1,2,3,4,5]
            @N2_=[1,2,3,4,5]
        """

        tdts, secs = X.shape

        ContinueKNum = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)

        for sec in range(secs):
            for ts in range(tdts):
                if ts <=N1_ or  X[ts,sec]!=X[ts,sec] or np.isinf(X[ts,sec]) :
                    continue

                _X = X[:ts + 1, sec]
                myX = getavailabledata(_X, N1_+1)
                
                _n = 0
                for i in range(1,N1_+1):
                    if myX[i]<myX[i-1]:
                        _n +=1
                if _n == N1_:
                    for i in range(N2_):
                        if ts+i<tdts:
                            ContinueKNum[ts+i,sec] = 1
        return  ContinueKNum,np.nan
    

    
    @staticmethod
    @nb.njit
    def tupoUP(X:np.array,Y:np.array,N1_=1)->np.array:
        """
        This function checks if the time series continues to increase over a specified number of consecutive steps starting from a given point in each row.

        Inputs@2:
            X (np.array): The first input 2D numpy array with shape (time_steps, sections).
            Y (np.array): The second input 2D numpy array with the same shape as X.
            N1_ (int): The minimum number of consecutive steps required for the series to be considered increasing. Default is 1.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element indicates whether the series continues to increase over the specified range.
        @@:
            @N1_=[1,2,3,4,5]
        """
        tdts, secs = X.shape

        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<2 or X[ts,sec]!=X[ts,sec] or Y[ts,sec]!=Y[ts,sec]:
                    continue
                _X = X[:ts + 1, sec]
                _Y = Y[:ts+1,sec]

                myX = getavailabledata(_X, 2)
                myY = getavailabledata(_Y, 2)
                # dif[ts, sec]  = _dif[-1]
                # dea[ts,sec] = _dea[-1]
                if myX[-1]>myY[-1]    and myX[-2]<=myY[-2]:
                    for i in range(N1_):
                        if ts+i<tdts:
                            newX[ts+i,sec] = 1
        return newX,np.nan

    @staticmethod
    @nb.njit
    def tupoDown(X,Y,N1_=1):
    # def tupoDown(X:np.array,Y:np.array,N1_=1)->np.array:
        """
        This function checks if the time series continues to decrease over a specified number of consecutive steps starting from a given point in each row.

        Inputs@2:
            X (np.array): The first input 2D numpy array with shape (time_steps, sections).
            Y (np.array): The second input 2D numpy array with the same shape as X.
            N1_ (int): The minimum number of consecutive steps required for the series to be considered decreasing. Default is 1.

        Outputs@1:
            np.array: A new 2D numpy array with shape (time_steps, sections) where each element indicates whether the series continues to decrease over the specified range.
        @@:
            @N1_=[1,2,3,4,5]
        """
        tdts, secs = X.shape

        newX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
        for sec in range(secs):
            for ts in range(tdts):
                if ts<2 or X[ts,sec]!=X[ts,sec] or Y[ts,sec]!=Y[ts,sec]:
                    continue
                _X = X[:ts + 1, sec]
                _Y = Y[:ts+1,sec]

                myX = getavailabledata(_X, 2)
                myY = getavailabledata(_Y, 2)
                # dif[ts, sec]  = _dif[-1]
                # dea[ts,sec] = _dea[-1]
                if myX[-1]>myY[-1]    and myX[-2]<=myY[-2]:
                    for i in range(N1_):
                        if ts+i<tdts:
                            newX[ts+i,sec] = 1


        return newX,np.nan
    
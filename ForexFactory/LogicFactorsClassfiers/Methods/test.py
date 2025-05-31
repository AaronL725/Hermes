import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import random 


def load_HOLCVO(level):
    script_dir = os.path.dirname(__file__)
    relative_data_path = os.path.join(script_dir, f"../../FutureData/{level}")
    path = os.path.abspath(relative_data_path)
    high = pd.read_csv(os.path.join(path,"high.csv"),index_col=[0])
    open = pd.read_csv(os.path.join(path,"open.csv"),index_col=[0])
    low = pd.read_csv(os.path.join(path,"low.csv"),index_col=[0])
    close = pd.read_csv(os.path.join(path,"close.csv"),index_col=[0])
    vol = pd.read_csv(os.path.join(path,"vol.csv"),index_col=[0])
    oi = pd.read_csv(os.path.join(path,"oi.csv"),index_col=[0])
    return high,open,low,close,vol,oi


from BaseLogicFactors.baselogicfactors import BaseLogicFactors
from Methods.operators import WrappedOperator
from Methods.method import WrappedMethod

class LogicFactorWrapper:

    @staticmethod
    def GetFuncOutputNum(doc):
        return eval(doc.split("Outputs@")[1].split(":")[0])

    @staticmethod
    def GetFuncInput(doc):
        # Check if the "@@:" marker exists in the docstring
        if "@@:" not in doc:
            # If not found, assume no dynamic inputs and return an empty list
            return []

        # Existing logic to parse dynamic inputs
        input_args =  doc.split("@@:")[-1].split("@")[1:]
        assert len(input_args)<=5,"Too Many Input Params"
        InputParams = []
        for i,_arg in enumerate(input_args):
            try:
                # compile(_arg,"",exec)
                ldict = {}
                exec(_arg,ldict)

                if i==0:
                    N1_ = random.choice(ldict['N1_'])
                    InputParams.append(N1_)
                if i==1:
                    N2_ = random.choice(ldict['N2_'])
                    InputParams.append(N2_)
                if i==2:
                    N3_ = random.choice(ldict['N3_'])
                    InputParams.append(N3_)
                if i==3:
                    N4_ = random.choice(ldict['N4_'])
                    InputParams.append(N4_)
                if i==4:
                    N5_ = random.choice(ldict['N5_'])
                    InputParams.append(N5_)    
            except Exception as e:
                raise ValueError("Error in GetFuncInput:",e)
        
        return InputParams

    def __init__(self,level):
        assert level in ["day","min60","min30","min15","min5"],f"Error Level arg: {level}"
        self.level = level
        high,open,low,close,vol,oi = load_HOLCVO(self.level)
        self.high  = high.to_numpy(dtype='float64')
        self.open = open.to_numpy(dtype='float64')
        self.low = low.to_numpy(dtype='float64')
        self.close = close.to_numpy(dtype='float64')
        self.vol = vol.to_numpy(dtype='float64')
        self.oi = oi.to_numpy(dtype='float64')
        self.method_list =  [func for func in dir(BaseLogicFactors) if callable(getattr(BaseLogicFactors, func)) and not func.startswith("__")]


    def _select_funnction(self):
        return getattr(BaseLogicFactors, random.choice(self.method_list))

    def iter(self,output_needed=1):
        # dice = random.choice([0,1])
        # if dice == 0:
        #     return None
        func_cond = True
        while func_cond:


            func = self._select_funnction()

            input_params = LogicFactorWrapper.GetFuncInput(func.__doc__)
            output_num = LogicFactorWrapper.GetFuncOutputNum(func.__doc__)
        
            if output_num>=output_needed:
                func_cond=False
        args = [self.high,self.open,self.low,self.close,self.vol,self.oi]
        args.extend(input_params)
        if output_num==1:
            _res1 = func(*args)
            res = random.sample([_res1],output_needed)
        elif output_num==2:
            _res1, _res2 = func(*args)
            res = random.sample([_res1,_res2],output_needed)
        elif output_num==3:  
            _res1, _res2, _res3 = func(*args)           
            res = random.sample([_res1,_res2,_res3],output_needed)
        else:
            raise ValueError("output_num must be 1,2 or 3")
        print(f"finished LogicFactorWrapper level:{self.level} func:{func.__name__} input_params:{input_params} output_num:{output_num}")
        return res

from Methods.method import *
if __name__=='__main__':
    LFM_day = LogicFactorWrapper(level='day')
    factors = LFM_day.iter(output_needed=2)
    res = WrappedMethod.JC(*factors)
    print(factors)





import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import random 
import numpy as np
from Mining.data_cache import load_HOLCVO_cached_by_path

def load_HOLCVO(path):
    return load_HOLCVO_cached_by_path(path)


from BaseLogicFactors.baselogicfactors import BaseLogicFactors
from Methods.operators import WrappedOperator
from Methods.method import WrappedMethod



class LogicFactorWrapper:

    @staticmethod
    def GetFuncOutputNum(doc):
        return eval(doc.split("Outputs@")[1].split(":")[0])

    @staticmethod
    def GetFuncInput(doc):
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
                raise ValueError("[Error] in GetFuncInput:",e)
        
        return InputParams

    def __init__(self,level):
        assert level in ["week","day","min60","min30","min15","min5"],f"[Error] Level arg: {level}"
        self.level = level
        high,open,low,close,vol,oi = load_HOLCVO(os.path.join(os.path.dirname(__file__), f"../../FutureData/{level}"))
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

            if "@@:" in func.__doc__:
                input_params = LogicFactorWrapper.GetFuncInput(func.__doc__)
            else:
                input_params = []
            output_num = LogicFactorWrapper.GetFuncOutputNum(func.__doc__)
        
            if output_num>=output_needed:
                func_cond=False

        args = [self.high,self.open,self.low,self.close,self.vol,self.oi]
        args.extend(input_params)
        res_index = []
        if output_num==1:
            _res1 = func(*args)
            res_index = [0]
            res = random.sample([_res1],output_needed)
        elif output_num==2: 
            _res1, _res2 = func(*args)
            res_index = random.sample([0,1],output_needed)
            res = []
            for ii in res_index:
                if ii ==0:
                    res.append(_res1)
                if ii ==1:
                    res.append(_res2)
        elif output_num==3:  
            _res1, _res2, _res3 = func(*args)           
            res_index = random.sample([0,1,2],output_needed)
            res = []
            for ii in res_index:
                if ii ==0:
                    res.append(_res1)
                if ii ==1:
                    res.append(_res2)
                if ii==2:
                    res.append(_res3)
        else:
            raise ValueError("output_num must be 1,2 or 3")
        # print(f"finished LogicFactorWrapper level:{self.level} func:{func.__name__} input_params:{input_params} output_num:{output_num}")
        myargs = f"LogicFactorWrapper_level:{self.level}_func:{func.__name__}_inputparams:{input_params}_outputparams:{res_index}"
        return myargs,res

class OperatorWrapper:
    
    @staticmethod
    def GetFuncInputNum(doc):
        return eval(doc.split("Inputs@")[1].split(":")[0])

    @staticmethod
    def GetFuncOutputNum(doc):
        return eval(doc.split("Outputs@")[1].split(":")[0])

    @staticmethod
    def GetFuncInput(doc):
        input_args =  doc.split("@@:")[-1].split("@")[1:]
        assert len(input_args)<=5,"[ERROR] Too Many Input Params"
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


    def __init__(self, level):
        self.level = level
        self.method_list =  [func for func in dir(WrappedOperator) if callable(getattr(WrappedOperator, func)) and not func.startswith("__")]
        self.LFM = LogicFactorWrapper(level=self.level)

    def _select_funnction(self):
        return getattr(WrappedOperator, random.choice(self.method_list))
 
    def iter(self,output_needed=1):

        
        dice = random.choice([0,1])
        
        if dice == 0:

            return self.LFM.iter(output_needed = output_needed)
        
        func_cond = True
        while func_cond:


            func = self._select_funnction()
            if "@@:" in func.__doc__:
                input_params = OperatorWrapper.GetFuncInput(func.__doc__)
            else:
                input_params = []
            output_num = OperatorWrapper.GetFuncOutputNum(func.__doc__)
        
            if output_num>=output_needed:
                func_cond=False
        
        input_num = OperatorWrapper.GetFuncInputNum(func.__doc__) 
        input_params = OperatorWrapper.GetFuncInput(func.__doc__)
        output_num = OperatorWrapper.GetFuncOutputNum(func.__doc__)
        assert input_num<=2,"[ERROR] input num must less than 2"
        if input_num==1:
            myargs,args = self.LFM.iter(output_needed=input_num)
        elif input_num==2:
            dice = random.choice([0,1])
            if dice==0:
                myargs,args = self.LFM.iter(output_needed=input_num)
            else:
                myargs1,args1 = self.LFM.iter(output_needed=1)
                myargs2,args2 = self.LFM.iter(output_needed=1)
                assert len(args1)==1 and len(args2)==1,"[ERROR] OperatorWrapper args1 len {0} args2 len {1}".format(len(args1),len(args2))
                args = [args1[0],args2[0]]
                myargs = myargs1+"@OW@" + myargs2
        args.extend(input_params)
        if output_num==1:
            _res1 = func(*args)
            res_index = random.sample([0],output_needed)
            res = []
            for ii in res_index:
                if ii ==0:
                    res.append(_res1)
        elif output_num==2:
            _res1, _res2 = func(*args)
            res_index = random.sample([0,1],output_needed)
            res = []
            for ii in res_index:
                if ii ==0:
                    res.append(_res1)
                if ii ==1:
                    res.append(_res2)
        elif output_num==3:  
            _res1, _res2, _res3 = func(*args)
            res_index = random.sample([0,1,2],output_needed)
            res = []
            for ii in res_index:
                if ii ==0:
                    res.append(_res1)
                if ii ==1:
                    res.append(_res2)
                if ii==2:
                    res.append(_res3)
        else:
            raise ValueError("output_num must be 1,2 or 3")
        # print(f"finished OperatorWrapper level:{self.level} func:{func.__name__} input_params:{input_params} output_num:{output_num}")
        myargs += f";OperatorWrapper_level:{self.level}_func:{func.__name__}_inputparams:{input_params}_outputparams:{res_index}"
        return myargs,res




class MethodWrapper:
    
    @staticmethod
    def GetFuncInputNum(doc):
        return eval(doc.split("Inputs@")[1].split(":")[0])

    @staticmethod
    def GetFuncOutputNum(doc):
        return eval(doc.split("Outputs@")[1].split(":")[0])

    @staticmethod
    def GetFuncInput(doc):
        input_args =  doc.split("@@:")[-1].split("@")[1:]
        assert len(input_args)<=5,"[ERROR] Too Many Input Params"
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
    def _select_funnction(self):
        return getattr(WrappedMethod, random.choice(self.method_list))
 
    def __init__(self,level):
        self.level = level
        self.method_list =  [func for func in dir(WrappedMethod) if callable(getattr(WrappedMethod, func)) and not func.startswith("__")]
        self.OW = OperatorWrapper(level=self.level)
        self.high,_,_,_,_,_ = load_HOLCVO(os.path.join(os.path.dirname(__file__), f"../../FutureData/{level}"))

    def iter(self):
        

        cond = True
        while cond:

            func = self._select_funnction()
            input_num = MethodWrapper.GetFuncInputNum(func.__doc__) 
            input_params = MethodWrapper.GetFuncInput(func.__doc__)
            output_num = MethodWrapper.GetFuncOutputNum(func.__doc__)
            
            assert output_num==1,"[ERROR] Method Output Must 1"
            
            if input_num == 1:
                myargs,args = self.OW.iter(output_needed=1)

                if len(pd.Series(args[0].flatten()).unique())<=3 and 1 in args[0]:
                    dice = random.choice([0,1])
                    if dice==0:
                        return myargs,pd.DataFrame(args[0],index=self.high.index,columns=self.high.columns)

            elif input_num == 2:
                dice = random.choice([0,1])
                if dice==0:
                    myargs,args = self.OW.iter(output_needed=2)
                else:
                    myargs1,args1 = self.OW.iter(output_needed=1)
                    myargs2,args2 = self.OW.iter(output_needed=1)
                    assert len(args1)==1 and len(args2)==1,"[ERROR] MethodWrapper args1 len {0} args2 len {1}".format(len(args1),len(args2))
                    args = [args1[0],args2[0]]
                    myargs = myargs1 + "@MW@" + myargs2

            args.extend(input_params)
            res,randomparams = func(*args)
            assert len(res.shape)==2,f"[ERROR] MethodWrapper res shape:{res.shape}"
            print(f"finished MethodWrapper level:{self.level} func:{func.__name__} input_num:{input_num} output_num:{output_num}")
            if np.nansum(res)>0:
                cond = False
        assert  len(pd.Series(res.flatten()).unique())<=3 and 1 in res,"[ERROR] MethodWrapper return value error"
        myargs += f";MethodWrapper_level:{self.level}_func:{func.__name__}_inputparams:{input_params}_randomparams:{randomparams}"
        return myargs,pd.DataFrame(res,index=self.high.index,columns=self.high.columns)

if __name__=='__main__':
    # MW_week = MethodWrapper(level='week')

    # MW_day = MethodWrapper(level='day')
    # MW_min60 = MethodWrapper(level='min60')
    # MW_min30 = MethodWrapper(level='min30')
    # MW_min15 = MethodWrapper(level='min15')
    # MW_min5 = MethodWrapper(level='min5')

    # while True:
    #     MW_week.iter()
        # MW_day.iter()
        # MW_min60.iter()
        # MW_min30.iter()
        # MW_min15.iter()
        # MW_min5.iter()
    # OW_day = OperatorWrapper(level='day')
    # OW_min60 = OperatorWrapper(level='min60')
    # OW_min30 = OperatorWrapper(level='min30')
    # OW_min15 = OperatorWrapper(level='min15')
    # OW_min5 = OperatorWrapper(level='min5')

    # while True:
    #     res_day = OW_day.iter()
    #     res_min60 = OW_min60.iter()
    #     res_min30 = OW_min30.iter()
    #     res_min15 = OW_min15.iter()
    #     res_min5 = OW_min5.iter()
    LFM_day = LogicFactorWrapper(level='day')
    LFM_min60 = LogicFactorWrapper(level='min60')
    LFM_min30 = LogicFactorWrapper(level='min30')
    LFM_min15 = LogicFactorWrapper(level='min15')
    LFM_min5 = LogicFactorWrapper(level='min5')


    while True:
        res_day = LFM_day.iter()
        res_min60 = LFM_min60.iter()
        res_min30 = LFM_min30.iter()
        res_min15 = LFM_min15.iter()
        res_min5 = LFM_min5.iter()
    
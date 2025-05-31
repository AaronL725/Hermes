from Mining.base import MethodWrapper
import numpy as np
import pandas as pd
import random 
import numba as nb
from backtest.RuleBackTest import RunRuleBackTest
import uuid
import matplotlib.pyplot as plt
import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # 设置日志级别

# 获取当前脚本的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 设置输出路径为相对路径
output_path = os.path.join(current_dir, 'RuleStrategy', '20250520')

# 确保目录存在
os.makedirs(os.path.join(output_path, 'log'), exist_ok=True)
os.makedirs(os.path.join(output_path, 'plot'), exist_ok=True)

# 创建一个handler，用于写入日志文件
file_handler = logging.FileHandler(os.path.join(output_path, 'log', 'mylog.log'))
file_handler.setLevel(logging.DEBUG) 
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  # 设置输出到控制台的日志级别（例如仅错误及以上）
 
# 创建formatter并添加到handler中
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
 
# 将handler添加到logger中
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def load_HOLCVO(level):
    script_dir = os.path.dirname(__file__)
    # 构建相对于脚本文件位置的数据路径：向上回退一级，进入FutureData，再进入level
    data_path = os.path.join(script_dir, "..", "FutureData", level)

    high = pd.read_csv(os.path.join(data_path,"high.csv"),index_col=[0])
    open = pd.read_csv(os.path.join(data_path,"open.csv"),index_col=[0])
    low = pd.read_csv(os.path.join(data_path,"low.csv"),index_col=[0])
    close = pd.read_csv(os.path.join(data_path,"close.csv"),index_col=[0])
    vol = pd.read_csv(os.path.join(data_path,"vol.csv"),index_col=[0])
    oi = pd.read_csv(os.path.join(data_path,"oi.csv"),index_col=[0])

    return high,open,low,close,vol,oi


def reformCloseHolidng(x):
    sec = []
    opendatetime = []
    holdingdays = []
    closedatetime = []
    pctchg = []
    closetype = []
    for i in x:
        sec.append(i[0])
        opendatetime.append(i[1])
        holdingdays.append(i[2])
        closedatetime.append(i[3])
        pctchg.append(i[4])
        closetype.append(i[5])
    return pd.DataFrame( {"sec":sec,"opendatetime":opendatetime,"holdingdays":holdingdays,"closedatetime":closedatetime,"pctchg":pctchg,"closetype":closetype},columns=["sec","opendatetime","holdingdays","closedatetime","pctchg","closetype"],index=range(len(sec)))


class OpenCloseSignal:

    def __init__(self, level_max_iter, use_limit_data=True):
        self.levels = ['min5','min15','min30','min60','day']
        self.level_max_iter = level_max_iter
        self.FactorGenerators = {"min5":MethodWrapper(level='min5'),"min15":MethodWrapper(level='min15'),"min30":MethodWrapper(level='min30'),
                                 "min60":MethodWrapper(level='min60'),"day":MethodWrapper(level='day')}

        self.pctchg = {}
        self.close = {}
        self.limit = {}
        self.use_limit_data = use_limit_data

        # 获取当前脚本的目录
        script_dir = os.path.dirname(os.path.abspath(__file__))

        for level in self.levels:
            # 直接将级别字符串传递给 load_HOLCVO
            _,_,_,close,_,_ = load_HOLCVO(level)
            self.close[level] = close.copy(deep=True)

            close = close.ffill()
            pctchg =  close/(close.shift(1))-1
            pctchg  = pctchg.fillna(0)
            self.pctchg[level] = pctchg

            if self.use_limit_data:
                # 构建 limitdata.csv 的完整路径，相对于脚本文件位置
                limit_data_file = os.path.join(script_dir, "..", "FutureData", level, "limitdata.csv")

                if os.path.exists(limit_data_file):
                     self.limit[level] = pd.read_csv(limit_data_file,index_col=[0])
                else:
                     logger.warning(f"limitdata.csv not found for level {level} at {limit_data_file}. Using zeros for limit data.")
                     self.limit[level] = pd.DataFrame(0.0,index=self.close[level].index,columns=self.close[level].columns)
            else:
                 self.limit[level] = pd.DataFrame(0.0,index=self.close[level].index,columns=self.close[level].columns)

            assert len(self.limit[level])==len(self.close[level])
    def _getSignal(self):
        target_levels = []

        while len(target_levels)==0:
            for level in self.levels:
                if level != 'week':
                    dice = random.choice([0,1])
                    if dice ==1:
                        target_levels.append(level)
                else:
                    dice = random.random()
                    if dice < 0.25:
                        target_levels.append(level)

        LEVELS = {}
        for level in target_levels:
            if level=='week':
                LEVELS[level] = 1
            else:
                LEVELS[level] = random.choice(list(range(1,self.level_max_iter+1)))

        ARGS = []
        Factors = {}
        for level in LEVELS.keys():
            times = LEVELS[level]
            _Factors = np.nan
            for i in range(times):
                myargs,factor = self.FactorGenerators[level].iter()
                if i==0:
                    _Factors = factor==1
                    ARGS.append(myargs)

                else:
                    temp = _Factors & (factor==1)
                    if temp.sum().sum()>(len(temp)*0.01):
                        _Factors = temp
                        ARGS.append(myargs)
            Factors[level] = _Factors
        print("所有因子生成完成，即将开始跨时间级别信号组合...")
        min_level = self.levels[np.min([self.levels.index(i) for i in Factors.keys()])]
        FACTORS = Factors[min_level]
        for level in Factors.keys():
            if level==min_level:
                continue
            _Factors = Factors[level]
            
            _NewFactos = pd.DataFrame(np.nan,index=FACTORS.index,columns=FACTORS.columns).to_numpy()
            assert sum([1 if i in FACTORS.index else 0 for i in _Factors.index  ])==len(_Factors),"[ERROR] OpenCloseSignal index dones't match"
            _ifchangeTS = np.array([1 if i in _Factors.index else 0 for i in FACTORS.index])
            _OldFactors = _Factors.to_numpy()
            _NewFactors = self._reform(_NewFactos,_ifchangeTS,_OldFactors)
            NewFactors = pd.DataFrame(_NewFactors,index=FACTORS.index,columns=FACTORS.columns)
            temp = FACTORS&NewFactors
            FACTORS = temp
        return ARGS,FACTORS

    
    def GetOpenSignal(self):
        print("进入 GetOpenSignal 方法...")
        cond1 = True
        cond2 = True
        while cond1:
            print("进入第一个信号生成循环...")
            try:
                print("尝试生成 signals1...")
                args1,signals1 = self._getSignal()
                print(f"signals1 生成完成. 信号总和: {signals1.sum().sum()}, 信号长度: {len(signals1)}")

                if signals1.sum().sum()>(len(signals1)*0.01):
                    print("signals1 满足条件，退出第一个循环.")
                    cond1= False
                else:
                    print("signals1 不满足条件，继续生成...")
            except Exception as e:
                print(e)
        while cond2:
            print("进入第二个信号生成循环...")
            try:
                print("尝试生成 signals2...")
                args2,signals2 = self._getSignal()
                print(f"signals2 生成完成. 信号总和: {signals2.sum().sum()}, 信号长度: {len(signals2)}")

                if signals2.sum().sum()>(len(signals2)*0.01):
                    print("signals2 满足条件，退出第二个循环.")
                    cond2= False
                else:
                    print("signals2 不满足条件，继续生成...")
            except Exception as e:
                print(e)
        if len(signals1)!=len(signals2):
            signals = [signals1,signals2]
            args = [args1,args2]
            # lens_signals = [len(x) for x in signals]
            min_levels = [self._get_minium_level(x) for x in args]
            min_level = self.levels[np.min(min_levels)]
            min_level_index = min_levels.index(np.min(min_levels))
            high_level_signal = signals[min_level_index]
            low_level_signal = signals[1-min_level_index]

            _new_low_level_signal = pd.DataFrame(np.nan,index=high_level_signal.index,columns=high_level_signal.columns).to_numpy()
            _ifchangeTS = np.array([1 if i in low_level_signal.index else 0 for i in high_level_signal.index])
            _old_low_level_signal = low_level_signal.to_numpy()
            _new_low_level_signal = self._reform(_new_low_level_signal,_ifchangeTS,_old_low_level_signal)
            new_low_level_signal = pd.DataFrame(_new_low_level_signal,index=high_level_signal.index,columns=high_level_signal.columns)
            
            signals[1-min_level_index] = new_low_level_signal
            longargs = args[0]
            shortargs = args[1]
            longsignal = signals[0]
            shortsignal = signals[1]
            print(f"信号生成完成，正在进行回测 (信号长度不同)...")

        else:
            longargs = args1 
            shortargs = args2
            longsignal = signals1
            shortsignal = signals2
            min_level = self.levels[self._get_minium_level(longargs)]
            print(f"信号生成完成，正在进行回测 (信号长度相同)...")
        assert len(longsignal) == len(shortsignal),"[ERROR] The length of long signal and short signal are not equal!"

        close = self.close[min_level]
        pctchg = self.pctchg[min_level]
        limit = self.limit[min_level]
        ifdaychange = np.array([1 if x[11:]=='15:00:00' else 0 for x in longsignal.index])
        maxium_day_holding = np.random.choice([1,2,3,4,5])
        
        print(f"准备执行回测 - 数据形状: close{close.shape}, pctchg{pctchg.shape}, limit{limit.shape}")
        print(f"信号形状: longsignal{longsignal.shape}, shortsignal{shortsignal.shape}")
        print(f"最大持仓天数: {maxium_day_holding}")
        
        try:
            Holding,ClosedHolding,PorfolioPctchg = RunRuleBackTest(close.to_numpy(dtype='float64'),pctchg.to_numpy(dtype='float64'), limit.to_numpy(dtype='float64'),longsignal.to_numpy(dtype='float64'),shortsignal.to_numpy(dtype='float64'),ifdaychange,maxium_day_holding=maxium_day_holding)
            print("第一次回测执行完成")
        except Exception as e:
            print(f"第一次回测执行失败: {str(e)}")
            import traceback
            print(traceback.format_exc())
            return
        PorfolioPctchg2 = pd.Series(PorfolioPctchg,index=self.close[min_level].index)
        day_index =[x[:10] for x in  PorfolioPctchg2.index]
        PorfolioPctchgDay = PorfolioPctchg2.groupby(day_index).apply(lambda x: x.sum() if sum(x!=x)!=len(x) else np.nan)
        myClosedHolding = reformCloseHolidng(ClosedHolding)
        opendays = len(PorfolioPctchgDay[PorfolioPctchgDay==PorfolioPctchgDay])
        dailyaverage = PorfolioPctchgDay.sum()/opendays if opendays > 0 else 0
        
        # 显示第一次回测的基本信息
        avg_return = myClosedHolding['pctchg'].mean() if len(myClosedHolding) > 0 else 0
        print(f"第一次回测结果 - 交易次数: {len(myClosedHolding)}, 平均收益率: {avg_return:.6f}, 开仓天数: {opendays}, 日均收益率: {dailyaverage:.6f}")
        
        if   abs(avg_return)>0.001 and opendays>=400 and abs(dailyaverage)>=0.0008:
            args = "LONG:{0};SHORT:{1};MAXHOLDING:{2};Tpctchg:{3};Dpctchg:{4}".format("@OS@".join(longargs),"@OS@".join(shortargs),maxium_day_holding,int(abs(dailyaverage)*1000000)/100,int(abs(avg_return)*1000000)/100)
            namespace = uuid.NAMESPACE_DNS
            unique_id = uuid.uuid3(namespace, args)

            logger.info(str(unique_id) + f":{args}")

            PorfolioPctchgDay.cumsum().plot()
            plt.savefig(os.path.join(output_path, 'plot', f'{unique_id}.png'))
            plt.close()
            print(f"回测完成并保存结果: {unique_id}")
        else:
            print(f"第一次回测结果不符合保存条件 - 交易次数: {len(myClosedHolding)}, 平均收益率: {avg_return:.6f}, 开仓天数: {opendays}, 日均收益率: {dailyaverage:.6f}")
            print(f"筛选要求: 平均收益率绝对值 > 0.001 ({abs(avg_return):.6f}), 开仓天数 >= 400 ({opendays}), 日均收益率绝对值 >= 0.0008 ({abs(dailyaverage):.6f})")

        # 进行反向回测
        print("开始反向回测...")
        try:
            Holding,ClosedHolding,PorfolioPctchg = RunRuleBackTest(close.to_numpy(dtype='float64'),pctchg.to_numpy(dtype='float64'), limit.to_numpy(dtype='float64'),shortsignal.to_numpy(dtype='float64'),longsignal.to_numpy(dtype='float64'),ifdaychange,maxium_day_holding=maxium_day_holding)
            print("反向回测执行完成")
        except Exception as e:
            print(f"反向回测执行失败: {str(e)}")
            import traceback
            print(traceback.format_exc())
            return
        PorfolioPctchg2 = pd.Series(PorfolioPctchg,index=self.close[min_level].index)
        day_index =[x[:10] for x in  PorfolioPctchg2.index]
        PorfolioPctchgDay = PorfolioPctchg2.groupby(day_index).apply(lambda x: x.sum() if sum(x!=x)!=len(x) else np.nan)
        myClosedHolding = reformCloseHolidng(ClosedHolding)
        opendays = len(PorfolioPctchgDay[PorfolioPctchgDay==PorfolioPctchgDay])
        dailyaverage = PorfolioPctchgDay.sum()/opendays if opendays > 0 else 0
        
        # 显示第二次（反向）回测的基本信息
        avg_return = myClosedHolding['pctchg'].mean() if len(myClosedHolding) > 0 else 0
        print(f"反向回测结果 - 交易次数: {len(myClosedHolding)}, 平均收益率: {avg_return:.6f}, 开仓天数: {opendays}, 日均收益率: {dailyaverage:.6f}")
        
        if   abs(avg_return)>0.001 and opendays>=400 and abs(dailyaverage)>=0.0008:
            args = "LONG:{0};SHORT:{1};MAXHOLDING:{2};Tpctchg:{3};Dpctchg:{4}".format("@OS@".join(shortargs),"@OS@".join(longargs),maxium_day_holding,int(abs(dailyaverage)*1000000)/100,int(abs(avg_return)*1000000)/100)
            namespace = uuid.NAMESPACE_DNS
            unique_id = uuid.uuid3(namespace, args)

            logger.info(str(unique_id) + f":{args}")

            PorfolioPctchgDay.cumsum().plot()
            plt.savefig(os.path.join(output_path, 'plot', f'{unique_id}.png'))
            plt.close()
            print(f"回测完成并保存结果 (反向): {unique_id}")
        else:
            print(f"反向回测结果不符合保存条件 - 交易次数: {len(myClosedHolding)}, 平均收益率: {avg_return:.6f}, 开仓天数: {opendays}, 日均收益率: {dailyaverage:.6f}")
            print(f"筛选要求: 平均收益率绝对值 > 0.001 ({abs(avg_return):.6f}), 开仓天数 >= 400 ({opendays}), 日均收益率绝对值 >= 0.0008 ({abs(dailyaverage):.6f})")
        print("回测流程结束，开始新的一轮...")
        print("-" * 50)

    def _get_minium_level(self,args:list):
        min_levels = []
        for arg in args:
            temp = arg.split(";")
            min_levels.append( np.min([self.levels.index(x.split("level:")[1].split("_")[0]) for x in temp ]))
        return np.min(min_levels)
    @staticmethod
    @nb.njit
    def _reform(_NewFactos, _ifchangeTS,_OldFactors):
        tdts,secs = _NewFactos.shape
        init = -1
        for ts in range(tdts):
            ifchangts = _ifchangeTS[ts]                        
            if ifchangts==1:
                init +=1
                values = _OldFactors[init,:]
            if init == -1:
                continue
            for sec in range(secs):
                _NewFactos[ts,sec] = values[sec]
        return _NewFactos


    
if __name__=='__main__':
    # 设置这个变量为 True 来使用 limitdata，设置为 False 则不使用
    USE_LIMIT_DATA_SWITCH = False

    print("程序开始运行...")

    while True:
        print("正在生成新的交易信号...")
        try:
            # 根据开关状态创建 OpenCloseSignal 实例
            OCS = OpenCloseSignal(4, use_limit_data=USE_LIMIT_DATA_SWITCH)
            print("OpenCloseSignal 实例已创建...")
            OCS.GetOpenSignal()
        except Exception as e:
            import traceback
            print(f"发生异常: {str(e)}")
            print("详细错误信息:")
            print(traceback.format_exc())
            print("=" * 60)
            
    MW_day = MethodWrapper(level='day')
    MW_min60 = MethodWrapper(level='min60')
    MW_min30 = MethodWrapper(level='min30')
    MW_min15 = MethodWrapper(level='min15')
    MW_min5 = MethodWrapper(level='min5')

    while True:
        MW_day.iter()
        MW_min60.iter()
        MW_min30.iter()
        MW_min15.iter()
        MW_min5.iter()
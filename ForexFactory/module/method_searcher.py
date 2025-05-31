'''
如程序中断，继续运行请使用 --resume
& A:/Python312/python.exe f:/Hermes/ForexFactory/module/method_searcher.py --resume
'''

import os
import json
import re
import time
from datetime import datetime
from typing import List, Dict, Set, Tuple, Optional
import chromadb
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_xai import ChatXAI
import tiktoken
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CollectionMethodAnalyzer:
    def __init__(self):
        """初始化集合方法分析器"""
        # 获取当前脚本文件所在的目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # 获取脚本文件所在目录的上一级目录
        parent_dir = os.path.dirname(script_dir)

        # 从method_searcher.py复制的核心组件
        self.technical_indicators = {
            'AD', 'ADOSC', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'ATR', 'AVGPRICE',
            'BBANDS', 'BETA', 'BOP', 'CCI', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE',
            'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS',
            'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY',
            'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK',
            'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI',
            'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE',
            'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS',
            'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON',
            'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING',
            'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE',
            'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR',
            'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN',
            'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR',
            'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH',
            'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER',
            'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'CMO', 'CORREL', 'DEMA', 'DX',
            'EMA', 'HT_DCPERIOD', 'HT_DCPHASE', 'HT_PHASOR', 'HT_SINE', 'HT_TRENDMODE',
            'KAMA', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE',
            'MA', 'MACD', 'MACDEXT', 'MACDFIX', 'MAMA', 'MAVP', 'MAX', 'MAXINDEX', 'MEDPRICE',
            'MFI', 'MIDPOINT', 'MIDPRICE', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MINUS_DI',
            'MINUS_DM', 'MOM', 'NATR', 'OBV', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP',
            'ROCR', 'ROCR100', 'RSI', 'SAR', 'SAREXT', 'SMA', 'STDDEV', 'STOCH', 'STOCHF',
            'STOCHRSI', 'SUM', 'T3', 'TEMA', 'TRANGE', 'TRIMA', 'TRIX', 'TSF', 'TYPPRICE',
            'ULTOSC', 'VAR', 'WCLPRICE', 'WILLR', 'WMA'
        }

        self.indicator_aliases = {
            'MACD': ['moving average convergence divergence', 'macd', 'Moving Average Convergence/Divergence'],
            'RSI': ['relative strength index', 'rsi', 'Relative Strength Index'],
            'EMA': ['exponential moving average', 'ema', 'Exponential Moving Average'],
            'SMA': ['simple moving average', 'sma', 'Simple Moving Average'],
            'BBANDS': ['bollinger bands', 'bollinger', 'Bollinger Bands'],
            'STOCH': ['stochastic', 'stoch', 'Stochastic'],
            'ADX': ['average directional movement index', 'adx', 'Average Directional Movement Index'],
            'ATR': ['average true range', 'atr', 'Average True Range'],
            'CCI': ['commodity channel index', 'cci', 'Commodity Channel Index'],
            'MFI': ['money flow index', 'mfi', 'Money Flow Index'],
            'OBV': ['on balance volume', 'obv', 'On Balance Volume'],
            'SAR': ['parabolic sar', 'sar', 'Parabolic SAR'],
            'WILLR': ['williams %r', 'williams r', "Williams' %R"],
            'WMA': ['weighted moving average', 'wma', 'Weighted Average'],
            'DEMA': ['double exponential moving average', 'dema'],
            'TEMA': ['triple exponential moving average', 'tema'],
            'T3': ['triple exponential moving average t3', 't3'],
            'KAMA': ['kaufman adaptive moving average', 'kama'],
            'MAMA': ['mesa adaptive moving average', 'mama']
        }
        self.trading_method_keywords = {
            # --- 经典方法名称 ---
            'crossover', 'crossunder', 'golden cross', 'death cross', 'bullish cross', 'bearish cross',
            'breakout', 'breakdown', 'divergence', 'convergence', 'overbought', 'oversold',
            'reversal', 'continuation', 'support', 'resistance', 'trend following',
            'mean reversion', 'scalping', 'swing trading', 'position trading',
            'price action', 'candlestick pattern',
            # --- 信号/触发词 ---
            'signal', 'trigger', 'alert', 'confirmation', 'entry', 'exit',
            'buy', 'sell', 'long', 'short', 'trade', 'position',
            'indicator shows', 'generates a signal', 'points to', 'confirms that',
            'entry point', 'exit point', 'stop loss', 'take profit',
            # --- 行为动词 ---
            'crosses', 'breaking', 'breaks above', 'breaks below', 'touches', 'tests',
            'bounces', 'rejects', 'respects', 'holds',
            'moves above', 'moves below', 'dips below', 'rallies above',
            'turns up', 'turns down', 'hooks up', 'hooks down',
            'accelerates', 'decelerates', 'expands', 'contracts', 'squeezes',
            'forms a peak', 'forms a trough', 'bottoms out', 'tops out',
            'diverges from', 'converges with',
            'holds above', 'holds below', 'fails to break', 'unable to break',
            'ranges', 'consolidates', 'trends', 'trending',
            # --- 条件/规则短语 ---
            'if', 'when', 'once', 'after', 'as soon as',
            'look for', 'watch for', 'wait for', 'expect',
            'as long as', 'provided that', 'on condition that', 'only if',
            'consider ... when', 'strategy is to', 'my rule is', 'the system dictates',
            'criterion', 'criteria', 'condition is met', 'requirements are fulfilled',
            # --- 模式/设置描述词 ---
            'pattern', 'setup', 'formation', 'structure', 'scenario', 'configuration',
            'opportunity', 'potential', 'indication',
            # --- 关系/应用短语 ---
            'indicates', 'suggests', 'implies', 'signifies',
            'use ... for', 'apply ... when', 'based on', 'according to',
            'combined with', 'in conjunction with', 'alongside',
            'key level', 'important zone', 'significant area'
        }

        # ChromaDB设置 - 路径相对于脚本文件目录的父目录
        self.db_path = os.path.join(parent_dir, "database")
        # 输出路径 - 路径相对于脚本文件目录的父目录
        self.output_path = os.path.join(parent_dir, "mediumdata")
        self.client = None
        
        # LLM设置
        self.llm = None
        self.encoding = tiktoken.get_encoding("cl100k_base")
        
        # 查询字符串
        self.query = """
        technical indicator trading signals, indicator crossover methods, golden cross death cross,
        indicator calculation code, numba implementation, indicator divergence detection,
        trading method code implementation, technical indicator breakout strategies,
        indicator continuation patterns, technical indicator python implementation,
        indicator trending patterns, acceleration deceleration signals, trading method formulas,
        indicator parameter optimization, continuation patterns, breakout patterns, divergence patterns
        """
        
        # 进度跟踪
        self.processed_collections = set()  # 存储已处理的集合名称集合
        self.log_file = None
        self.output_file = None
        
    def is_collection_processed(self, collection_name: str) -> bool:
        """检查集合是否已被处理过 (基于内存中的已处理集合set)
        """
        return collection_name in self.processed_collections
    
    def initialize_connections(self):
        """初始化LLM连接并确保输出目录存在"""
        try:
            # 创建输出目录
            os.makedirs(self.output_path, exist_ok=True)
            
            # **始终**初始化ChromaDB客户端
            try:
                self.client = chromadb.PersistentClient(path=self.db_path)
                self.log_progress(f"连接到ChromaDB: {self.db_path}")
            except Exception as e:
                print(f"❌ 连接到ChromaDB失败: {e}")
                self.log_progress(f"❌ 连接到ChromaDB失败: {e}")
                return False
            
            # 初始化LLM
            xai_api_key = os.getenv("XAI_API_KEY_WT")
            if not xai_api_key:
                raise ValueError("XAI_API_KEY not found")
                
            self.llm = ChatXAI(
                model="grok-3-latest",
                temperature=0.4,
                api_key=xai_api_key
            )
            self.log_progress("连接到XAI Grok-3模型")
            
            # 初始化日志文件 (如果不存在)
            if not os.path.exists(self.log_file):
                 with open(self.log_file, 'w', encoding='utf-8') as f:
                     pass # 创建空文件
                 self.log_progress(f"创建日志文件: {self.log_file}")
            
            # 输出文件的头部在run_workflow中根据是否恢复处理
            
            return True
            
        except Exception as e:
            error_msg = f"❌ 初始化失败: {e}"
            print(error_msg)
            self.log_progress(error_msg)
    
    # 修改方法：记录已完成处理的集合名称，更新整个日志文件
    def log_completed_collection(self, collection_name: str):
        """记录已完成处理的集合名称，并以指定格式更新整个日志文件"""
        if not self.log_file:
            print("❌ 日志文件路径未设置，无法记录已完成集合")
            return

        try:
            # 将新完成的集合添加到内存中的集合集
            self.processed_collections.add(collection_name)

            # 构建新的日志内容字符串
            completed_names_formatted = ", ".join([f"[{name}]" for name in sorted(list(self.processed_collections))])
            log_content = f"{{\n{completed_names_formatted}\n}}"

            # 写入更新后的日志文件
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write(log_content)
                
            print(f"✓ 已记录完成集合到日志: {collection_name}。当前日志内容格式已更新")
            
        except Exception as e:
            error_msg = f"❌ 记录完成集合 {collection_name} 到日志失败: {e}"
            print(error_msg)
            self.log_progress(error_msg) # 使用原有的log_progress记录错误

    def write_output_header(self):
        """写入输出文件的头部信息"""
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(f"# 交易方法分析报告\n\n")
                f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("=" * 80 + "\n\n")
            self.log_progress(f"写入输出文件头部: {os.path.basename(self.output_file)}")
        except Exception as e:
            print(f"❌ 写入输出文件头部失败: {e}")
            self.log_progress(f"❌ 写入输出文件头部失败: {e}")
    
    def get_all_collections(self) -> List[str]:
        """获取所有集合并按名称排序"""
        if not self.client:
            print("❌ ChromaDB客户端未初始化")
            self.log_progress("❌ ChromaDB客户端未初始化，请确保已调用initialize_connections()或在run_workflow中初始化客户端")
            return []
        
        try:
            collection_names = self.client.list_collections()
            
            # 获取每个集合的名称
            collections = []
            for collection in collection_names:
                collections.append(collection)
                
            # 按名称排序
            collections.sort()

            print(f"发现 {len(collections)} 个集合")
            self.log_progress(f"发现 {len(collections)} 个集合: {collections[:10] if collections else '[]'}...")

            return collections

        except Exception as e:
            print(f"❌ 获取集合列表失败: {e}")
            self.log_progress(f"❌ 获取集合列表失败: {e}")
            return []
    
    # 辅助方法：检查文本中是否存在技术指标
    def _find_indicators_in_text(self, text):
        text_lower = text.lower()
        found_indicators = set()
        for indicator in self.technical_indicators:
            if indicator.lower() in text_lower:
                found_indicators.add(indicator)
        for main_indicator, aliases in self.indicator_aliases.items():
            for alias in aliases:
                if alias.lower() in text_lower:
                    found_indicators.add(main_indicator)
        return found_indicators

    # 辅助方法：检查文本中是否存在交易方法关键词
    def _has_trading_method_keyword(self, text):
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.trading_method_keywords)

    def filter_with_indicators_and_keywords(self, documents: List[str], metadatas: List[Dict]) -> Tuple[List[str], List[Dict]]:
        filtered_docs = []
        filtered_metas = []
        for doc, meta in zip(documents, metadatas):
            has_indicator = bool(self._find_indicators_in_text(doc))
            has_method_keyword = self._has_trading_method_keyword(doc)
            if has_indicator or has_method_keyword:
                filtered_docs.append(doc)
                filtered_metas.append(meta)
        return filtered_docs, filtered_metas
    
    def split_into_batches(self, documents: List[str], metadatas: List[Dict]) -> List[Tuple[List[str], List[Dict]]]:
        """
        将文档分成批次。
        如果文档总数大于400，则分成两个批次，每批数量约为总数的一半。
        如果文档总数小于等于400，则作为一个批次。
        """
        total_docs = len(documents)
        batches = []

        if total_docs > 400:
            # 分成两批
            half_size = total_docs // 2
            # 确保第一个批次包含额外的文档如果总数是奇数
            batch1_size = half_size + (total_docs % 2)
            batch2_size = total_docs - batch1_size

            batch1_docs = documents[:batch1_size]
            batch1_metas = metadatas[:batch1_size]
            batches.append((batch1_docs, batch1_metas))
            self.log_progress(f"分成两批: 批次1 包含 {len(batch1_docs)} 个文档")


            batch2_docs = documents[batch1_size:]
            batch2_metas = metadatas[batch1_size:]
            batches.append((batch2_docs, batch2_metas))
            self.log_progress(f"分成两批: 批次2 包含 {len(batch2_docs)} 个文档")

        else:
            # 作为单个批次处理
            batches.append((documents, metadatas))
            self.log_progress(f"文档数量 <= 400，作为单个批次处理")

        return batches

    def analyze_with_llm(self, documents: List[str], collection_name: str, batch_num: int = 1) -> str:
        """使用LLM分析文档"""
        
        # 将批次中的所有文档合并成一个长字符串，用双换行分隔
        batch_text = "\n\n".join(documents)
        
        # 初始化tiktoken编码器，用于计算token数量
        try:
            encoding = self.encoding
        except Exception:
            print("无法获取编码器，尝试使用默认编码器...")
            encoding = tiktoken.get_encoding("cl100k_base")

        # 定义模型的最大token限制和为系统提示及其他用途预留的token
        MAX_TOKENS = 131072  # Grok模型的最大上下文窗口大小
        RESERVED_TOKENS = 20000  # 预留给系统提示、输出等
        TEMPLATE_TOKENS = 1000  # 预估提示模板本身的token数
        AVAILABLE_TOKENS = MAX_TOKENS - RESERVED_TOKENS - TEMPLATE_TOKENS  # 留给文档内容的可用token数

        # 将文档合并为用于模型输入的上下文
        context = batch_text
        # 计算当前上下文（文档内容）的token数量
        context_tokens = len(encoding.encode(context))

        # 如果上下文的token数量超出可用限制
        if context_tokens > AVAILABLE_TOKENS:
            print(f"批次 token 数 ({context_tokens}) 超出可用限制 ({AVAILABLE_TOKENS})，进行截断处理...")
            truncated_docs = []
            current_tokens = 0
            
            # 逐个文档添加到截断列表，直到达到token限制
            for doc in documents:
                doc_tokens = len(encoding.encode(doc))
                # 如果当前文档加上已有的文档 token 数不超过可用限制，则添加当前文档
                if current_tokens + doc_tokens <= AVAILABLE_TOKENS:
                    truncated_docs.append(doc)
                    current_tokens += doc_tokens
                else:
                    # 如果添加当前文档会超出限制，则停止添加
                    break

            # 使用截断后的文档重新构建上下文
            context = "\n\n".join(truncated_docs)
            print(f"截断后包含 {len(truncated_docs)} 个文档，token 数: {current_tokens}。")
            
        # 定义用于指导大语言模型提取交易方法的提示模板
        examples = {
            "example1": """
@staticmethod
@nb.njit
def JC(X:np.array,Y:np.array,N1_:int=5)->np.array:
    \"\"\"
    This function performs a comparison between two time series data arrays X and Y based on available data points in each row up to a certain point n.

    Inputs@2:
        X (np.array): The first input 2D numpy array with shape (time_steps, sections).
        Y (np.array): The second input 2D numpy array with the same shape as X.

    Outputs@1:
        np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or -1 based on the comparison result, or 0 if no significant difference is found.
    @@:
        @N1_=[1,2,3,4,5]
    \"\"\"
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
            if myX[-1]>myY[-1] and myX[-2]<=myY[-2]:
                for i in range(N1_):
                    if ts+i<tdts:
                        newX[ts+i,sec] = 1
    return newX,np.nan
""",
            "example2": """
@staticmethod
@nb.njit
def SectionDivideToNGroups(X:np.array,N1_:int=10,random_int_input = 99999)->np.array:
    \"\"\"
    This function divides the input array X into N groups based on the number of available data points in each row.

    Inputs@1:
        X (np.array): The input 2D numpy array with shape (time_steps, sections).
        group_num (int): The desired number of groups to divide the data into. Default is 10.
        target_group (int): A placeholder parameter for future extension or customization. Default is 10.

    Outputs@1:
        np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or 0 based on the group assignment.
    @@:
        @N1_=[2,5,10]
    \"\"\"
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

    nnewX = np.array([np.float64(np.nan)] * (tdts * secs)).reshape(tdts, secs)
    for ts in range(tdts):
        for sec in range(secs):
            if newX[ts,sec] == random_int:
                nnewX[ts,sec] = 1
            elif newX[ts,sec]==newX[ts,sec]:
                nnewX[ts,sec] = 0
            else:
                continue
    return nnewX,random_int
""",
            "example3": """
@staticmethod
@nb.njit
def BeiLi(X:np.array,Y:np.array,N1_=14)->np.array:
    \"\"\"
    This function performs a correlation-based comparison between two time series data arrays X and Y based on available data points in each row up to a certain point n.

    Inputs@2:
        X (np.array): The first input 2D numpy array with shape (time_steps, sections).
        Y (np.array): The second input 2D numpy array with the same shape as X.
        n (int): The number of time steps up to which the comparison is based. Default is 14.

    Outputs@1:
        np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or 0 based on the correlation-based comparison result.
    @@:
        @N1_=[14,30,70]
    \"\"\"
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
""",
            "example4": """
@staticmethod
@nb.njit
def TimeSeriesDistribute(X:np.array,N1_=240,random_int_input = 99999)->np.array:
    \"\"\"
    This function distributes the time series data based on specific factors derived from available data points in each row up to a certain point n.

    Inputs@1:
        X (np.array): The input 2D numpy array with shape (time_steps, sections).
        n (int): The number of time steps up to which the distribution is based. Default is 240.

    Outputs@1:
        np.array: A new 2D numpy array with shape (time_steps, sections) where each element is either 1 or 0 based on the distribution criteria.
    @@:
        @N1_=[120,240]
    \"\"\"
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
"""
        }

        template = f"""
# EXPERT SYSTEM ACTIVATION

作为顶级量化交易架构师，你拥有15年技术指标开发经验，专精将复杂交易逻辑转化为高性能numba优化代码。你的核心能力：精准识别技术指标模式、零容错代码实现、严格质量控制。

**使命目标**: 从论坛内容中提取符合规范的技术指标交易方法，生成production-ready代码

=======================================================================================================

## EXECUTION PROTOCOL

执行以下4阶段精确分析流程，每阶段必须达到PASS标准才能进入下一阶段：

### >> PHASE 1: SCAN & IDENTIFY
**目标**: 定位技术指标相关内容
**执行**: 
- 扫描识别技术指标名称 (MACD/RSI/EMA/SMA/BBANDS/STOCH/ADX/ATR等)
- 查找相关交易规则、信号描述、策略说明
**决策**: 发现技术指标描述 → 进入PHASE 2 | 无技术指标 → 终止

### >> PHASE 2: EXTRACT & ANALYZE  
**目标**: 提取可实现的交易逻辑
**执行**:
- 识别信号类型: 交叉/突破/背离/超买超卖/趋势确认等等
- 提取参数设定、数值条件、时间参数、阈值设定
- 理解前置条件和触发机制
**决策**: 逻辑基本可理解且具备实现潜力 → 进入PHASE 3 | 逻辑完全模糊不可实现 → 舍弃

### >> PHASE 3: VALIDATE & VERIFY
**目标**: 确保生成代码符合技术规范
**执行**: 对每个通过筛选的方法验证其代码实现的合规性
- 生成代码时的参数命名规范 (X/Y/Z, N1_/N2_/N3_, random_int_input)
- 生成代码时的参数总数限制 (≤5个)
- 生成代码时的输出格式要求 ((数据,参数)或(数据,np.nan))
- 生成代码时的numba兼容性
**决策**: 全部符合规范 → 进入PHASE 4 | 任一不符合 → 舍弃该方法

### >> PHASE 4: IMPLEMENT & GENERATE
**目标**: 生成完整代码实现
**执行**: 
- 设计数据处理流程
- 实现边界条件处理
- 生成完整docstring文档
- 应用性能优化
**决策**: 代码完整可用 → 输出 | 有缺陷 → 舍弃

=======================================================================================================

## TECHNICAL SPECIFICATIONS

### MANDATORY CONSTRAINTS

**生成代码时必须遵循的参数命名规范** (100%严格):
```
• 输入数组: X, Y, Z (形状: time_steps×sections, 必须是技术指标数据，可以是一个或多个)
• 数值参数: N1_, N2_, N3_ (如: N1_=14, N2_=30)  
• 随机整数: random_int_input=99999（可选使用）
• 总参数数: ≤5个 (包括所有类型)
```

**代码生成时的输出格式要求** (100%严格执行):
```
• 输出格式: 
    - 格式1 (数据,参数): 返回计算结果 + 随机参数
    - 格式2 (数据,np.nan): 返回计算结果 + np.nan
• 数据类型: np.array, 元素类型: np.float64
• 数据形状: (time_steps, sections)
```

**代码生成时的技术要求**:
```
• 装饰器: @staticmethod + @nb.njit
• 导入禁止: 代码块内禁止任何import语句
• 异常处理: 正确处理np.nan、边界条件、数组索引
• 性能优化: numba兼容，适合大规模数据
```

### 生成代码时强制使用的DOCSTRING格式
```python
\"\"\"
This function [英文功能描述].

Inputs@[数量]:
    参数名 (类型): 参数描述。

Outputs@[数量]:  
    返回值类型: 返回值描述。
@@:
    @参数名_=[可选值列表]
\"\"\"
```

=======================================================================================================

## SUCCESS PATTERNS

以下4个实现模板展示proven成功模式，严格遵循这些模式：

### 模式A: 双指标交叉检测
```python
{examples["example1"]}
```
**核心特征**: 双时间序列比较，交叉点检测，持续信号生成

### 模式B: 单指标分组分析  
```python
{examples["example2"]}
```
**核心特征**: 横截面分组，排序位置信号，随机分组支持

### 模式C: 相关性背离检测
```python
{examples["example3"]}
```
**核心特征**: 滑动窗口相关系数，负相关状态检测

### 模式D: 统计分布分析
```python
{examples["example4"]}
```
**核心特征**: 历史统计特征，标准化分值，分层信号

=======================================================================================================

## VALIDATION PROTOCOL

**执行强制验证流程** - 确保生成的代码符合规范:

### CHECKPOINT 1: 基础验证
```
[ ] 基于技术指标？        [ ] 逻辑可实现？         [ ] numba兼容？
[ ] 边界条件处理？        [ ] 文档完整？
```

### CHECKPOINT 2: 代码规范验证  
```
[ ] X/Y/Z命名？          [ ] N1_/N2_/N3_命名？    [ ] 参数≤5个？
[ ] 输出格式正确？        [ ] np.float64类型？       
```

### CHECKPOINT 3: 代码格式验证
```
[ ] docstring格式？      [ ] Inputs@/Outputs@？   [ ] @@:配置？
[ ] 参数值列表？
```

**CRITICAL**: 如果任一验证失败，必须舍弃该方法。宁可输出0个方法，不输出1个不合规方法。

=======================================================================================================

## OUTPUT DIRECTIVE

**生成格式** (严格遵循):

```markdown
**Method Name:** [英文函数名]

**Description:** [详细中文描述：技术指标+交易逻辑+适用场景+预期效果]

**Main Indicator Type:** [主要指标类型]

**Signal Type:** [信号类型]

**Key Parameters:** [关键参数说明]

**Code:**

```python
[完整Python代码实现，包含完整docstring，无import语句]
```

---
```

**CRITICAL OUTPUT RULES**:
- 输出纯Markdown内容，无其他文本
- 无markdown代码块标记 (如```markdown)
- 多个方法用"---"分隔
- 如无符合规范方法，输出："未发现完全符合规范要求的交易方法。"

=======================================================================================================

**ANALYSIS TARGET:**
{{context}}

=======================================================================================================

**EXECUTION ORDER**: 
1. 执行PHASE 1-4分析流程
2. 对每个候选方法执行CHECKPOINT 1-3验证  
3. 生成符合OUTPUT DIRECTIVE的Markdown内容
4. 应用最终质量过滤

**START ANALYSIS NOW**
        """

        # 从模板字符串创建ChatPromptTemplate对象
        prompt = ChatPromptTemplate.from_template(template)
        
        # 构建LangChain处理链
        chain = (
            {"context": lambda _: context, "batch_number": lambda _: batch_num}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        try:
            # 调用LLM
            result = chain.invoke({})
            print(f"✓ 批次 {batch_num} 处理完成")
            return result
            
        except Exception as e:
            error_msg = f"❌ LLM分析失败: {e}"
            print(error_msg)
            return error_msg
    
    def save_results(self, collection_name: str, analysis_result: str, batch_num: int = 1):
        """将分析结果追加到单一输出文件中"""
        if not self.output_file:
            self.log_progress("❌ 输出文件未初始化，无法保存结果")
            return
            
        try:
            with open(self.output_file, 'a', encoding='utf-8') as f:
                f.write(f"\n## 集合名称: {collection_name} (批次 {batch_num})\n\n")
                f.write(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(analysis_result)
                f.write("\n\n" + "=" * 80 + "\n\n")
                
            self.log_progress(f"结果已追加到输出文件: {os.path.basename(self.output_file)}")
            
        except Exception as e:
            error_msg = f"❌ 保存结果失败: {e}"
            print(error_msg)
            self.log_progress(error_msg)
    
    def log_progress(self, message: str):
        """记录进度日志 (只输出到终端)"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        
        print(log_entry)
    
    def process_collection(self, collection_name: str) -> bool:
        """处理单个集合"""
        try:
            # 首先检查是否已经处理过该集合
            if self.is_collection_processed(collection_name):
                self.log_progress(f"跳过已处理过的集合: {collection_name}")
                # 将集合添加到已处理列表中，以防重复处理
                self.processed_collections.add(collection_name)
                return True
                
            self.log_progress(f"开始处理集合: {collection_name}")
            
            # 获取集合
            collection = self.client.get_collection(name=collection_name)
            
            # 第一轮筛选：使用query获取最相关的文档
            results = collection.query(
                query_texts=[self.query],
                n_results=min(800, collection.count()) # 增加获取的文档数量
            )
            
            if not results['documents'] or not results['documents'][0]:
                self.log_progress(f"集合 {collection_name} 没有找到相关文档")
                return True
            
            documents = results['documents'][0]
            metadatas = results['metadatas'][0] if results['metadatas'] else [{}] * len(documents)
            
            self.log_progress(f"第一轮筛选得到 {len(documents)} 个文档")
            
            # 第二轮筛选：使用技术指标和交易关键词
            filtered_docs, filtered_metas = self.filter_with_indicators_and_keywords(documents, metadatas)
            
            if not filtered_docs:
                self.log_progress(f"集合 {collection_name} 第二轮筛选后没有相关文档")
                return True
            
            self.log_progress(f"第二轮筛选得到 {len(filtered_docs)} 个文档")
            
            # 将筛选后的文档分成批次 (根据数量自动决定1批还是2批)
            batches = self.split_into_batches(filtered_docs, filtered_metas)
            
            self.log_progress(f"处理 {len(batches)} 个批次")
            
            for i, (batch_docs, batch_metas) in enumerate(batches, 1):
                self.log_progress(f"处理批次 {i}/{len(batches)}，包含 {len(batch_docs)} 个文档")
                
                # LLM分析
                analysis_result = self.analyze_with_llm(batch_docs, collection_name, i)
                
                # 保存结果
                self.save_results(collection_name, analysis_result, i)
                
                # 批次间稍作休息
                time.sleep(2)
            
            # 标记集合已处理
            self.processed_collections.add(collection_name)
            self.log_progress(f"✓ 集合 {collection_name} 处理完成")
            
            return True
            
        except Exception as e:
            error_msg = f"处理集合 {collection_name} 失败: {e}"
            self.log_progress(f"❌ {error_msg}")
            return False
    
    # 修改方法：从指定格式的日志文件加载已处理的集合列表
    def load_existing_log(self, log_path):
        """从指定格式 ({ [name1], [name2] }) 的日志文件加载已处理的集合列表"""
        processed = set()
        try:
            if not os.path.exists(log_path):
                return processed
                
            with open(log_path, 'r', encoding='utf-8') as f:
                log_content = f.read().strip()
                
            # 解析格式: { [name1], [name2] }
            # 移除 {} 和换行符，按逗号分割，移除 [] 和空白
            if log_content.startswith('{') and log_content.endswith('}'):
                content = log_content[1:-1].strip()
                if content:
                    # 使用正则表达式匹配 [name]
                    matches = re.findall(r'\[(.*?)\]', content)
                    processed = set(matches)
                    
            if processed:
                self.log_progress(f"从日志文件加载了 {len(processed)} 个已处理的集合: {list(processed)[:5]}...")
            else:
                 # 如果文件存在但解析后为空，说明日志文件是空的 {} 或格式错误，按没有已处理的集合处理
                 self.log_progress(f"日志文件存在但未找到已处理的集合记录，可能为空或格式错误")
                
            return processed
        except Exception as e:
            self.log_progress(f"❌ 读取或解析日志文件失败: {e}")
            return set() # 返回空集合，防止错误导致跳过
            
    def run_workflow(self, resume_from_log=None):
        """运行完整的工作流，可选择从现有日志恢复"""
        print("🚀 启动集合方法分析工作流")
        
        # 设置日志文件和输出文件的固定名称，基于已确定的self.output_path
        self.log_file = os.path.join(self.output_path, "method_log.log")
        self.output_file = os.path.join(self.output_path, "method_output.txt")
        
        # 创建输出目录，确保日志和输出文件目录存在
        os.makedirs(self.output_path, exist_ok=True)
        
        # **始终**初始化ChromaDB客户端
        try:
            self.client = chromadb.PersistentClient(path=self.db_path)
            self.log_progress(f"连接到ChromaDB: {self.db_path}")
        except Exception as e:
            print(f"❌ 连接到ChromaDB失败: {e}")
            self.log_progress(f"❌ 连接到ChromaDB失败: {e}")
            return

        # 初始化LLM连接
        if not self.initialize_connections():
            return # 如果初始化失败则停止工作流

        # 处理恢复逻辑和输出文件头部
        if resume_from_log and os.path.exists(self.log_file):
            # 从日志加载已处理的集合列表
            self.processed_collections = self.load_existing_log(self.log_file)
            self.log_progress(f"正在从日志文件恢复状态: {self.log_file}")
            # 如果输出文件不存在，创建并写入头部（这不应该发生如果日志存在且恢复，但以防万一）
            if not os.path.exists(self.output_file):
                 self.write_output_header()
                 self.log_progress(f"创建新的输出文件进行恢复: {os.path.basename(self.output_file)}")
            else:
                 self.log_progress(f"将继续向现有输出文件写入: {os.path.basename(self.output_file)}")
        else:
            # 如果不恢复或日志文件不存在，创建新的输出文件并写入头部
            self.write_output_header()
            self.processed_collections = set() # 确保已处理集合列表为空
            # 创建日志文件并写入空集合 {} 表示未处理任何集合
            try:
                with open(self.log_file, 'w', encoding='utf-8') as f:
                    f.write("{}")
                print(f"创建新的日志文件并初始化为空集合: {os.path.basename(self.log_file)}") # 直接使用print，不使用log_progress避免写入日志文件
            except Exception as e:
                print(f"❌ 创建或写入新的日志文件失败: {e}") # 直接使用print

            self.log_progress(f"未指定恢复或日志文件不存在，开始新的工作流，创建新的输出文件: {os.path.basename(self.output_file)}")

        
        # 获取所有集合
        collections = self.get_all_collections()
        if not collections:
            self.log_progress("❌ 没有找到任何集合")
            return
        
        # 逐个处理集合
        total_collections = len(collections)
        successful_count = 0
        skipped_count = 0
        
        for i, collection_name in enumerate(collections, 1):
            self.log_progress(f"进度: {i}/{total_collections} - 处理集合: {collection_name}")
            
            # 检查是否已处理
            if self.is_collection_processed(collection_name):
                self.log_progress(f"跳过已处理的集合: {collection_name}")
                skipped_count += 1
                continue
                
            if self.process_collection(collection_name):
                successful_count += 1
                # 在成功处理完一个集合的所有批次后，记录到日志文件
                self.log_completed_collection(collection_name)
            
            # 集合间稍作休息
            time.sleep(1)
        
        # 完成总结
        self.log_progress(f"工作流完成！成功处理 {successful_count}/{total_collections - skipped_count} 个新集合，跳过 {skipped_count} 个已处理集合") # 统计成功处理的是新集合数量
        print(f"🎉 工作流完成！成功处理 {successful_count}/{total_collections - skipped_count} 个新集合，跳过 {skipped_count} 个已处理集合")
        print(f"📊 结果文件: {self.output_file}")
        print(f"📝 日志文件: {self.log_file}")

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Collection Method Analyzer')
    parser.add_argument('--resume', '-r', help='Resume from existing progress', action='store_true')
    parser.add_argument('--debug', '-d', help='Enable debug mode with more verbose output', action='store_true')
    args = parser.parse_args()
    
    analyzer = CollectionMethodAnalyzer()
    
    # 设置日志文件路径
    log_file = os.path.join(analyzer.output_path, "method_log.log")
    
    # 运行工作流
    # 只有指定了 --resume 且日志文件存在时才尝试恢复
    resume_arg = args.resume and os.path.exists(log_file)
    if resume_arg:
        print(f"正在从日志文件恢复: {log_file}")
        
    analyzer.run_workflow(resume_arg)

if __name__ == "__main__":
    main()
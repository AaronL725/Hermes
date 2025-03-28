import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_xai import ChatXAI
import chromadb
import re
from dotenv import load_dotenv
import tiktoken
from datetime import datetime

class ForexIndicatorAnalyzer:
    def __init__(self):
        # 初始化基础路径
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.root_dir = os.path.dirname(self.current_dir)  # 获取项目根目录
        self.vectorized_data_path = os.path.join(self.root_dir, "database")
        
        # 加载环境变量
        load_dotenv(os.path.join(self.current_dir, '.env'))
        self.xai_api_key = os.environ.get("XAI_API_KEY_WT")
        
        if not self.xai_api_key:
            raise ValueError("在.env文件中未找到XAI_API_KEY")

    def create_retrieval_chain(self, collection):
        """创建检索链，从指定集合中提取技术指标相关信息"""
        # 初始化大语言模型
        llm = ChatXAI(
            api_key=self.xai_api_key,
            model="grok-2-latest",
            temperature=0.4,
            max_tokens=16000
        )
        
        # 构建精简但高度相关的查询
        query = """
        RSI, MACD, Bollinger Bands, Stochastic, Moving Average, EMA, SMA, ATR, Fibonacci,
        indicator parameters, technical indicators, trading rules, entry signals, exit signals,
        indicator combinations, indicator reliability, confirmation signals,

        quantitative factors, statistical edge, signal generation, algorithmic rules,
        mean reversion, trend following, breakout strategies, volatility trading,
        win rate, profit factor, parameter optimization, signal filtering,
        alpha generation, signal threshold, feature extraction, multi-timeframe analysis
        """
        
        # 初始化token计数器
        try:
            encoding = tiktoken.get_encoding("cl100k_base")
        except:
            encoding = tiktoken.encoding_for_model("gpt-4")
        
        # 设置Grok模型的token限制参数
        MAX_TOKENS = 131072
        RESERVED_TOKENS = 20000
        TEMPLATE_TOKENS = 1000
        AVAILABLE_TOKENS = MAX_TOKENS - RESERVED_TOKENS - TEMPLATE_TOKENS
        
        # 第一阶段：获取前50个最相关片段
        initial_results = collection.query(
            query_texts=[query],
            n_results=50
        )
        
        # 检查是否找到有效文档
        if not initial_results["documents"] or not initial_results["documents"][0]:
            return "未找到有效讨论内容"
        
        # 提取文档和相似度分数
        documents = initial_results["documents"][0]
        distances = initial_results["distances"][0]
        
        # 计算当前文档的token数量
        token_counts = [len(encoding.encode(doc)) for doc in documents]
        total_tokens = sum(token_counts)
        
        print(f"前50个片段的总token数: {total_tokens}")
        
        # 第二阶段：如果还有剩余token空间，获取更多相关片段
        remaining_tokens = AVAILABLE_TOKENS - total_tokens
        
        if remaining_tokens > 1000:
            # 计算平均每个文档占用的token数
            avg_token_per_doc = total_tokens / len(documents) if documents else 0
            # 估算可以添加的额外文档数量
            additional_docs = int(remaining_tokens / avg_token_per_doc) if avg_token_per_doc > 0 else 0
            # 限制最多添加200个额外片段
            additional_docs = min(additional_docs, 200)
            
            if additional_docs > 0:
                print(f"尝试添加额外的 {additional_docs} 个片段...")
                
                # 获取更多文档
                more_results = collection.query(
                    query_texts=[query],
                    n_results=50 + additional_docs
                )
                
                # 处理新获取的文档
                if more_results["documents"] and more_results["documents"][0]:
                    # 只取新增的文档（跳过前50个）
                    additional_documents = more_results["documents"][0][50:]
                    additional_distances = more_results["distances"][0][50:]
                    
                    # 计算新文档的token数
                    additional_token_counts = [len(encoding.encode(doc)) for doc in additional_documents]
                    
                    # 动态选择能容纳的额外文档
                    selected_docs = []
                    selected_distances = []
                    current_additional_tokens = 0
                    
                    # 在token限制内添加尽可能多的文档
                    for i, (doc, tokens, distance) in enumerate(zip(additional_documents, additional_token_counts, additional_distances)):
                        if current_additional_tokens + tokens <= remaining_tokens:
                            selected_docs.append(doc)
                            selected_distances.append(distance)
                            current_additional_tokens += tokens
                        else:
                            break
                    
                    # 合并所有文档
                    documents.extend(selected_docs)
                    distances.extend(selected_distances)
                    
                    print(f"成功添加了 {len(selected_docs)} 个额外片段，总token数: {total_tokens + current_additional_tokens}")
        
        # 将所有检索到的文档合并为一个上下文文本
        context = "\n\n".join(documents)
        
        # 最终检查token数量
        final_token_count = len(encoding.encode(context))
        print(f"最终上下文的token数: {final_token_count}")
        
        # 创建提示模板，指导模型对内容进行分析
        template = """
        You are a professional forex market quantitative analyst, analyzing trading discussions from ForexFactory forums with the goal of extracting valuable information that can be converted into quantitative factors. Based on the following content:

        {context}

        Please provide a concise technical analysis summary WITH THE OUTPUT IN CHINESE using this format:

        SUMMARY:

        1. Core Quantitative Indicators/Signals:
           - List all indicators or signals that could be used for quantification
           - Include relationship or priority between indicators
           - Note which indicators are acknowledged by most traders

        2. Indicator Parameters and Calculation Methods:
           - Provide detailed explanation of specific parameter settings for each indicator (periods, thresholds, etc.)
           - Describe calculation methods or formulas (if mentioned)
           - How indicators are adjusted under different market conditions

        3. Trading Rules and Trigger Conditions:
           - Clear definition of entry conditions (e.g., breakouts, crossovers, thresholds)
           - Exit conditions and stop-loss settings
           - Risk management rules (position sizing, risk ratios)

        4. Indicator Effectiveness Evaluation:
           - Traders' assessment of each indicator's reliability
           - Potential failure scenarios or error sources
           - Performance differences in specific market environments

        5. Potential Quantitative Factor Construction Directions:
           - Suggestions for indicator data transformation or combination
           - Possible time series processing methods
           - Signal filtering or confirmation mechanisms

        Note:
        • Focus only on content specifically related to quantitative trading
        • Keep the format concise and clear
        • If no relevant content is found, respond with "未找到可用于量化因子构建的有效信息"
        • Do not add additional analysis or speculation
        • YOUR ENTIRE RESPONSE MUST BE IN CHINESE
        """
        
        # 创建提示对象
        prompt = ChatPromptTemplate.from_template(template)
        
        # 构建完整的处理链
        chain = (
            {"context": lambda _: context}  # 注入上下文
            | prompt                        # 应用提示模板
            | llm                           # 发送到LLM处理
            | StrOutputParser()             # 解析输出为字符串
        )
        
        # 执行链并返回结果
        try:
            return chain.invoke({})
        except Exception as e:
            print(f"处理集合时出错: {str(e)}")
            return "处理过程中出现错误"

    def _get_latest_summary_file(self):
        """获取最近的摘要文件"""
        # 查找根目录下所有的summary文件
        summary_files = []
        for file in os.listdir(self.root_dir):
            if file.startswith("summary_") and file.endswith(".md"):
                file_path = os.path.join(self.root_dir, file)
                summary_files.append(file_path)
        
        # 如果没有找到摘要文件，返回None
        if not summary_files:
            return None
        
        # 按文件修改时间排序，获取最新的文件
        summary_files.sort(key=os.path.getmtime, reverse=True)
        return summary_files[0]

    def _get_analyzed_collections(self, file_path):
        """从摘要文件中提取已分析过的集合名称"""
        analyzed_collections = set()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 使用正则表达式匹配所有标题格式为 ## xxx 的内容
            # 排除第一个总览标题
            titles = re.findall(r'## ([^\n]+)', content)
            if len(titles) > 1:  # 第一个是"总览"，我们要跳过
                analyzed_collections = set(titles[1:])  # 转换为集合提高查找效率
                print(f"发现之前已分析 {len(analyzed_collections)} 个集合")
        except Exception as e:
            print(f"读取之前摘要文件时出错: {str(e)}")
        
        return analyzed_collections

    def analyze_indicators(self):
        """分析所有文档集合中的交易指标信息并返回摘要"""
        try:
            # 连接到ChromaDB客户端
            client = chromadb.PersistentClient(path=self.vectorized_data_path)
            # 获取所有集合名称
            collection_names = client.list_collections()
            
            # 获取最新的摘要文件
            latest_summary = self._get_latest_summary_file()
            already_analyzed = set()
            
            # 如果存在之前的摘要文件，读取已分析过的集合
            if latest_summary:
                print(f"找到之前的摘要文件: {os.path.basename(latest_summary)}")
                already_analyzed = self._get_analyzed_collections(latest_summary)
            
            # 准备存储分析结果
            results = []
            total_collections = len(collection_names)
            
            print(f"开始处理 {total_collections} 个集合...")
            
            # 处理每个集合
            for idx, collection_name in enumerate(collection_names, 1):
                # 清理集合名称，移除时间戳后缀
                title = re.sub(r'_\d{8}_\d{6}$', '', collection_name)
                
                # 检查是否已经分析过此集合
                if title in already_analyzed:
                    print(f"跳过已分析过的集合 [{idx}/{total_collections}]: {title}")
                    continue
                
                print(f"正在处理第 {idx}/{total_collections} 个集合: {collection_name}")
                
                # 获取集合对象
                collection = client.get_collection(name=collection_name)
                
                # 分析当前集合内容
                summary = self.create_retrieval_chain(collection)
                
                # 添加到结果列表
                results.append({
                    "title": title,
                    "summary": summary
                })
                
                print(f"完成处理: {title}")
            
            # 如果存在之前的摘要，将其内容也添加到结果中
            if latest_summary and already_analyzed:
                print("将之前分析的结果合并到当前报告...")
                with open(latest_summary, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 解析之前文件中的每个章节
                sections = re.split(r'## ', content)
                if len(sections) > 1:  # 确保有章节
                    for section in sections[2:]:  # 跳过文件头和总览部分
                        section_parts = section.split('\n', 1)
                        if len(section_parts) >= 2:
                            title = section_parts[0].strip()
                            summary_content = section_parts[1].split('---')[0].strip()
                            
                            if title and title in already_analyzed:
                                results.append({
                                    "title": title,
                                    "summary": summary_content
                                })
            
            return results
        
        except Exception as e:
            print(f"分析指标时出错: {str(e)}")
            return []

    def _format_output(self, results):
        """格式化分析结果为可读文本"""
        if not results:
            return "未找到任何内容。"
        
        # 创建输出文本
        output = f"# 技术指标分析报告\n\n"
        output += f"## 总览\n共处理 {len(results)} 个thread\n\n"
        for result in results:
            output += f"## {result['title']}\n"
            output += f"{result['summary']}\n"
            output += "---\n\n"
        
        return output

    def _delete_chroma_cache(self):
        """删除ChromaDB的缓存文件以释放空间"""
        try:
            import shutil
            from pathlib import Path
            
            # 获取用户主目录
            home_dir = Path.home()
            # ChromaDB缓存目录
            cache_dir = home_dir / ".cache" / "chroma"
            
            # 如果缓存目录存在则删除
            if cache_dir.exists():
                print("正在删除Chroma缓存...")
                shutil.rmtree(cache_dir)
                print("Chroma缓存已删除")
            else:
                print("未找到Chroma缓存目录")
        except Exception as e:
            print(f"删除Chroma缓存时出错: {str(e)}")

    def analyze(self):
        """
        执行分析并生成报告的主方法
        返回: 生成的报告文件路径
        """
        print("正在分析所有文档中的指标信息...")
        
        # 执行指标分析
        results = self.analyze_indicators()
        
        # 格式化结果
        output = self._format_output(results)
        
        # 生成文件名和路径
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # 修改为简化的命名规则
        filename = f"summary_{timestamp}.md"
        # 修改为保存到根目录
        output_path = os.path.join(self.root_dir, filename)
        
        # 写入文件
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)
        
        print(f"分析报告已保存至: {filename}")
        
        # 删除或注释下面这行代码
        # self._delete_chroma_cache()
        
        return output_path

# 为了方便使用，提供一个简单的函数接口
def analyze_threads():
    """
    分析Forex指标并生成报告的简单接口
    返回: 生成的报告文件路径
    """
    analyzer = ForexIndicatorAnalyzer()
    return analyzer.analyze()

if __name__ == "__main__":
    analyze_threads()

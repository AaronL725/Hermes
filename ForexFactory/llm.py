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
        self.vectorized_data_path = os.path.join(self.current_dir, "vectorized_data")
        
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
        
        # 构建包含所有技术指标相关术语的查询
        query = """
        technical indicators, trading indicators, indicator settings, indicator parameters, 
        trading strategies using indicators, buy signals, sell signals, 
        RSI, MACD, Bollinger Bands, Stochastic, Moving Average, EMA, SMA, ATR, Fibonacci, 
        pivot points, support resistance, overbought, oversold, divergence, 
        indicator combinations, indicator setup, trading rules, entry points, exit points,
        indicator optimization, backtesting indicators, custom indicators, proprietary indicators,
        indicator reliability, false signals, confirmation signals, trend indicators, momentum indicators
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
        You are a professional forex market analyst analyzing trading discussions related to indicators and their usage from ForexFactory forums. Based on the following context:

        {context}

        Provide a concise technical analysis summary based on the content of discussions WITH THE OUTPUT IN CHINESE using this format:

        SUMMARY:

        1. Technical Indicators:
           - List all key technical indicators mentioned

        2. Usage and Settings of These Indicators:
           - Detailed explanation of specific parameter settings for each indicator
           - Explanation of how indicators are used and what trading signals they generate
           - If there are specific trading rules, list them

        Note:
        • Focus only on technical indicator related content
        • Keep the format concise and clear
        • If no technical indicator related content is found, respond with "未找到技术指标相关内容"
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

    def analyze_indicators(self):
        """分析所有文档集合中的交易指标信息并返回摘要"""
        try:
            # 连接到ChromaDB客户端
            client = chromadb.PersistentClient(path=self.vectorized_data_path)
            # 获取所有集合名称
            collection_names = client.list_collections()
            
            # 准备存储分析结果
            results = []
            total_collections = len(collection_names)
            
            print(f"开始处理 {total_collections} 个集合...")
            
            # 处理每个集合
            for idx, collection_name in enumerate(collection_names, 1):
                print(f"正在处理第 {idx}/{total_collections} 个集合: {collection_name}")
                
                # 获取集合对象
                collection = client.get_collection(name=collection_name)
                # 清理集合名称，移除时间戳后缀
                title = re.sub(r'_\d{8}_\d{6}$', '', collection_name)
                
                # 分析当前集合内容
                summary = self.create_retrieval_chain(collection)
                
                # 添加到结果列表
                results.append({
                    "title": title,
                    "summary": summary
                })
                
                print(f"完成处理: {title}")
            
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
        filename = f"summary({len(results)})_{timestamp}.md"
        output_path = os.path.join(self.current_dir, filename)
        
        # 写入文件
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)
        
        print(f"分析报告已保存至: {filename}")
        
        # 清理缓存
        self._delete_chroma_cache()
        
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

import os
import chromadb
from chromadb.utils import embedding_functions
import shutil
import re
from tqdm import tqdm
import concurrent.futures

class ForexVectorDB:
    def __init__(self):
        # 初始化路径
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.unextracted_files_dir = os.path.join(self.current_dir, "unextracted_files")
        self.vectorized_data_dir = os.path.join(self.current_dir, "vectorized_data")
        self.client = None

    def _split_into_chunks(self, text, max_length=800, overlap=80):
        # 智能文本分块函数，优先按帖子结构分割
        posts = []
        post_markers = re.findall(r'\* \[#\d+\].*?(?=\* \[#\d+\]|\Z)', text, re.DOTALL)
        
        if post_markers and len(post_markers) > 2:
            # 存在多个帖子标记时，按帖子进行分割
            for post in post_markers:
                # 对长帖子进行进一步分块
                if len(post) > max_length:
                    post_chunks = self._split_text_by_semantic(post, max_length, overlap)
                    posts.extend(post_chunks)
                else:
                    # 短帖子保持完整
                    posts.append(post)
            return posts
        else:
            # 无法识别帖子结构时，使用语义分块
            return self._split_text_by_semantic(text, max_length, overlap)

    def _split_text_by_semantic(self, text, max_length=800, overlap=80):
        # 按语义边界智能分割文本的内部函数
        if len(text) <= max_length:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = min(start + max_length, len(text))
            
            # 分割优先级：帖子边界 > 段落边界 > 列表项边界 > 句子边界 > 空白字符
            if end < len(text):
                post_boundary = text.rfind("* [#", start, end)
                if post_boundary > start + max_length // 2:
                    end = post_boundary
                else:
                    paragraph_boundary = text.rfind("\n\n", start, end)
                    if paragraph_boundary > start + max_length // 2:
                        end = paragraph_boundary + 2
                    else:
                        list_boundary = max(
                            text.rfind("\n- ", start, end),
                            text.rfind("\ni - ", start, end),
                            text.rfind("\nii- ", start, end)
                        )
                        if list_boundary > start + max_length // 2:
                            end = list_boundary
                        else:
                            sentence_boundary = max(
                                text.rfind(". ", start, end),
                                text.rfind("? ", start, end),
                                text.rfind("! ", start, end)
                            )
                            if sentence_boundary > start + max_length // 2:
                                end = sentence_boundary + 2
                            else:
                                # 无合适边界时，在空白处分割
                                while end > start + max_length - overlap and not text[end].isspace():
                                    end -= 1
                                
                                if end <= start + max_length - overlap:
                                    end = start + max_length
            
            chunks.append(text[start:end])
            start = end - overlap if end < len(text) else end
        
        return chunks

    def create_database(self):
        """创建并返回向量数据库"""
        # 清理并重建向量数据库目录
        if os.path.exists(self.vectorized_data_dir):
            shutil.rmtree(self.vectorized_data_dir)
        os.makedirs(self.vectorized_data_dir, exist_ok=True)
        
        # 初始化客户端
        self.client = chromadb.PersistentClient(path=self.vectorized_data_dir)
        embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction()
        
        # 获取待处理的markdown文件列表
        md_files = [f for f in os.listdir(self.unextracted_files_dir) if f.endswith('.md')]
        
        # 使用 ThreadPoolExecutor 进行并发处理, 并添加tqdm显示进度
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:  # 根据你的CPU核心数调整
            futures = [executor.submit(self._process_file, md_file, embedding_function) for md_file in md_files]
            
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(md_files)):
                try:
                    future.result()  # 获取结果，如果有异常会在这里抛出
                except Exception as e:
                    print(f"处理文件时发生错误: {e}")
        
        print(f"向量数据库已成功创建，存储在 {self.vectorized_data_dir} 目录中")
        return self.client

    def _process_file(self, md_file, embedding_function):
        """处理单个文件"""
        print(f"处理文件: {md_file}")
        
        # 清理集合名称
        collection_name = os.path.splitext(md_file)[0]
        collection_name = re.sub(r'[^a-zA-Z0-9_-]', '_', collection_name)  # 替换非法字符为下划线
        collection_name = re.sub(r'^[^a-zA-Z]+', '', collection_name)  # 确保以字母开头
        collection_name = re.sub(r'__+', '_', collection_name)  # 将连续的下划线替换为单个下划线
        collection_name = re.sub(r'\.\.+', '.', collection_name)  # 将连续的句点替换为单个句点
        
        # 确保集合名称长度在 3 到 63 个字符之间
        if len(collection_name) > 63:
            collection_name = collection_name[:63]
        if len(collection_name) < 3:
            collection_name = collection_name.ljust(3, '0')  # 补足到 3 个字符

        # 确保集合名称以字母或数字结尾
        if not collection_name[-1].isalnum():
            collection_name = collection_name[:-1] + '0'

        # 确保集合名称不以连字符或下划线结尾
        if collection_name[-1] in ['-', '_']:
            collection_name = collection_name[:-1] + '0'

        # 创建向量集合
        collection = self.client.create_collection(
            name=collection_name,
            embedding_function=embedding_function,
            metadata={
                "hnsw:space": "cosine",
                "hnsw:construction_ef": 200,
                "hnsw:search_ef": 200
            }
        )
        
        # 读取文件内容
        file_path = os.path.join(self.unextracted_files_dir, md_file)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='gbk') as file:
                content = file.read()
        
        # 分块
        chunks = self._split_into_chunks(content, max_length=1000)
        
        # 批量处理
        batch_size = 32  # 根据你的内存大小调整
        for i in range(0, len(chunks), batch_size):
            batch_chunks = chunks[i:i + batch_size]
            batch_ids = [f"{collection_name}_chunk_{i + j}" for j in range(len(batch_chunks))]
            
            collection.add(
                documents=batch_chunks,
                ids=batch_ids,
                metadatas=[{"source": md_file, "chunk_index": i + j} for j in range(len(batch_chunks))]
            )
        
        print(f"已将文件 {md_file} 添加到向量数据库中，共 {len(chunks)} 个块")

    def query(self, document_name, query_text, n_results=5, where_filter=None):
        """查询文档"""
        if not self.client:
            self.client = chromadb.PersistentClient(path=self.vectorized_data_dir)
            
        collection_name = document_name
        if collection_name.endswith('.md'):
            collection_name = os.path.splitext(collection_name)[0]
        
        # 尝试获取集合
        try:
            collection = self.client.get_collection(name=collection_name)
        except ValueError:
            print(f"未找到文档 {document_name} 的集合")
            return None
        
        # 执行相似度查询
        results = collection.query(
            query_texts=[query_text],
            n_results=n_results,
            where=where_filter  # 可选的过滤条件
        )
        
        return results

if __name__ == "__main__":
    # 创建单例实例
    vector_db = ForexVectorDB()
    vector_db.create_database()

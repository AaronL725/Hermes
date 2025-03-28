import os
import re
import random
import asyncio

# 设置 Windows 环境下的异步事件循环策略，避免默认策略在 Windows 上的兼容性问题
if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import aiohttp
import cloudscraper
from typing import List, Tuple

# 多种浏览器的用户代理字符串集合，用于模拟不同设备的浏览请求
MY_HEADERS = [
    # 桌面Chrome浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # 桌面Firefox浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
    # 桌面Safari浏览器
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    # 桌面Edge浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    # 桌面Opera浏览器
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    # 移动设备浏览器
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36"
]

class ForexFileDownloader:
    @staticmethod
    def get_random_headers():
        """生成随机HTTP请求头，模拟正常浏览器行为，避免被目标网站识别为爬虫"""
        return {
            'User-Agent': random.choice(MY_HEADERS),
            'Referer': 'https://www.forexfactory.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        }

    @staticmethod
    def extract_download_links(text_file):
        """从文本文件中提取下载链接和对应文件名
        
        参数:
            text_file: 包含下载链接信息的文本文件路径
            
        返回:
            列表，每项包含(文件名, 下载链接)的元组，仅包含文本类型文件
        """
        links = []
        # 定义要处理的文本类型文件后缀
        text_extensions = ['.txt', '.doc', '.docx', '.pdf', '.md']
        
        with open(text_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # 检查并定位附件下载链接部分
            if "===== 附件下载链接 =====" in content:
                # 切分出附件下载链接部分的文本
                attachment_section = content.split("===== 附件下载链接 =====")[1].strip()
                
                # 使用正则表达式匹配"文件名: 链接"格式的内容
                pattern = r'([^:]+): (https?://[^\s]+)'
                matches = re.finditer(pattern, attachment_section)
                
                for match in matches:
                    file_name = match.group(1).strip()
                    download_url = match.group(2).strip()
                    
                    # 过滤，仅保留文本类型文件
                    file_ext = os.path.splitext(file_name)[1].lower()
                    if file_ext in text_extensions:
                        links.append((file_name, download_url))
        
        return links

    @staticmethod
    async def download_file_async(session, scraper, url, filename, save_dir):
        """异步下载单个文件，采用双重下载机制确保成功率
        
        首先尝试使用cloudscraper下载（绕过网站反爬机制），失败后再用aiohttp尝试
        
        参数:
            session: aiohttp会话对象
            scraper: cloudscraper会话对象
            url: 文件下载链接
            filename: 保存的文件名
            save_dir: 保存目录
        """
        try:
            os.makedirs(save_dir, exist_ok=True)
            save_path = os.path.join(save_dir, filename)
            
            # 检查文件是否已存在，避免重复下载
            if os.path.exists(save_path):
                print(f"文件已存在，跳过下载: {filename}")
                return
            
            headers = ForexFileDownloader.get_random_headers()
            
            # 处理并标准化URL格式，确保包含完整域名
            if url.startswith('/'):
                download_url = f"https://www.forexfactory.com{url}"
            elif not url.startswith(('http://', 'https://')):
                download_url = f"https://www.forexfactory.com/{url}"
            else:
                download_url = url
            
            # 转换为附件下载格式的URL
            download_url = download_url.replace('thread/', 'attachment.php?attachment/')
            
            # 方法一：使用cloudscraper尝试下载（能绕过CloudFlare防护）
            scraper_response = scraper.get(download_url, headers=headers, allow_redirects=True)
            if scraper_response.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(scraper_response.content)
                print(f"成功下载: {filename}")
                return
            
            # 方法二：使用aiohttp尝试下载（如果cloudscraper失败）
            cookies = scraper.cookies.get_dict()
            async with session.get(download_url, headers=headers, cookies=cookies) as response:
                response.raise_for_status()
                with open(save_path, 'wb') as f:
                    async for chunk in response.content.iter_chunked(8192):
                        if chunk:
                            f.write(chunk)
            print(f"成功下载: {filename}")
        
        except Exception as e:
            print(f"下载失败 {filename}: {str(e)}")

    @staticmethod
    async def download_files(files: List[Tuple[str, str]], save_dir: str):
        """并发下载多个文件，控制并发数和下载频率以避免触发反爬机制
        
        参数:
            files: 包含(文件名,下载链接)元组的列表
            save_dir: 文件保存目录
        """
        scraper = cloudscraper.create_scraper(
            browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False},
            ecdhCurve='secp384r1'  # 使用高强度加密曲线，避免SSL握手错误
        )
        
        async with aiohttp.ClientSession(
            cookies=scraper.cookies.get_dict(),
            connector=aiohttp.TCPConnector(limit=5),  # 限制最大并发连接数为5
            timeout=aiohttp.ClientTimeout(total=60)   # 设置60秒超时
        ) as session:
            tasks = []
            for filename, url in files:
                # 清理文件名，移除Windows文件系统不支持的字符
                clean_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
                task = asyncio.create_task(
                    ForexFileDownloader.download_file_async(session, scraper, url, clean_filename, save_dir)
                )
                tasks.append(task)
                await asyncio.sleep(0.3)  # 添加延迟，控制请求频率避免被封
            await asyncio.gather(*tasks)  # 等待所有下载任务完成

    @staticmethod
    async def run():
        """执行下载器主流程，处理rawdata目录中的所有txt文件，提取并下载其中的附件"""
        # 获取项目根目录路径
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # 设置输入和输出目录的路径
        rawdata_dir = os.path.join(project_root, 'rawdata')  # 原始数据目录
        thread_doc_dir = os.path.join(project_root, 'thread_doc')  # 下载文件保存目录
        
        # 确保输出目录存在
        os.makedirs(thread_doc_dir, exist_ok=True)
        
        # 遍历处理所有txt文件
        for file in os.listdir(rawdata_dir):
            if file.endswith('.txt'):
                links = ForexFileDownloader.extract_download_links(os.path.join(rawdata_dir, file))
                if links:
                    await ForexFileDownloader.download_files(links, thread_doc_dir)

# 创建并导出下载器单例实例，方便其他模块直接使用
downloader = ForexFileDownloader()

if __name__ == "__main__":
    asyncio.run(downloader.run())

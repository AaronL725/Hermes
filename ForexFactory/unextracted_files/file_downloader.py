import os
import re
import random
import asyncio
import aiohttp
import cloudscraper
from typing import List, Tuple

# 浏览器UA列表
MY_HEADERS = [
    # 桌面Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # 桌面Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
    # 桌面Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    # 桌面Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    # 桌面Opera
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    # 移动设备
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36"
]

class ForexFileDownloader:
    @staticmethod
    def get_random_headers():
        """随机生成请求头"""
        return {
            'User-Agent': random.choice(MY_HEADERS),
            'Referer': 'https://www.forexfactory.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        }

    @staticmethod
    def extract_download_links(markdown_file):
        """从md文件提取下载链接和文件名"""
        links = []
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
            pattern = r'!\[File Type: (pdf|doc|txt|xls|xlsx)\].*?\((.*?)\) \[(.*?)\]\((.*?)\)'
            matches = re.finditer(pattern, content)
            for match in matches:
                file_name = match.group(3)
                download_url = match.group(4).replace('</','').replace('>','').replace('thread/','')
                links.append((file_name, download_url))
        return links

    @staticmethod
    async def download_file_async(session, scraper, url, filename, save_dir):
        """异步下载单个文件，先用cloudscraper尝试，失败后用aiohttp"""
        try:
            os.makedirs(save_dir, exist_ok=True)
            save_path = os.path.join(save_dir, filename)
            headers = ForexFileDownloader.get_random_headers()
            
            # 确保URL格式正确，添加域名
            if url.startswith('/'):
                download_url = f"https://www.forexfactory.com{url}"
            elif not url.startswith(('http://', 'https://')):
                download_url = f"https://www.forexfactory.com/{url}"
            else:
                download_url = url
            
            download_url = download_url.replace('thread/', 'attachment.php?attachment/')
            
            # cloudscraper下载
            scraper_response = scraper.get(download_url, headers=headers, allow_redirects=True)
            if scraper_response.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(scraper_response.content)
                print(f"成功下载: {filename}")
                return
            
            # aiohttp下载
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
        """并发下载多个文件，限制并发数为5"""
        scraper = cloudscraper.create_scraper(
            browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False},
            ecdhCurve='secp384r1'  # 使用更强的加密曲线避免SSL错误
        )
        
        async with aiohttp.ClientSession(
            cookies=scraper.cookies.get_dict(),
            connector=aiohttp.TCPConnector(limit=5),
            timeout=aiohttp.ClientTimeout(total=60)
        ) as session:
            tasks = []
            for filename, url in files:
                clean_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
                task = asyncio.create_task(
                    ForexFileDownloader.download_file_async(session, scraper, url, clean_filename, save_dir)
                )
                tasks.append(task)
                await asyncio.sleep(0.3)  # 限制请求频率
            await asyncio.gather(*tasks)

    @staticmethod
    async def run():
        """运行下载器"""
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        thread_docs_dir = os.path.join(os.path.dirname(current_dir), 'thread_docs')
        
        for file in os.listdir(current_dir):
            if file.endswith('.md'):
                links = ForexFileDownloader.extract_download_links(os.path.join(current_dir, file))
                await ForexFileDownloader.download_files(links, thread_docs_dir)

# 导出单例实例
downloader = ForexFileDownloader()

if __name__ == "__main__":
    downloader.run()

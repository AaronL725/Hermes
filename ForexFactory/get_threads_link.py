import asyncio
import json
import sys
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, BrowserConfig

async def get_threads_link(start_page=1, end_page=1, max_concurrent=3):
    """
    从ForexFactory论坛爬取指定页码范围内的交易系统线程链接
    """
    async def extract_thread_links(url, crawler, config):
        """
        从单个论坛页面提取线程链接
        """
        result = await crawler.arun(url=url, config=config)
        
        if not result.success:
            return {}
        
        html_content = result.html if hasattr(result, 'html') else result.cleaned_html
        
        soup = BeautifulSoup(html_content, 'html.parser')
        all_links = soup.find_all('a', href=True)
        
        thread_links = {}
        link_count = 0
        max_links = 40  # 每页最多获取40个链接
        
        for link in all_links:
            if link_count >= max_links:
                break
                
            href = link.get('href')
            title = link.text.strip()
            
            if not title:
                continue
            
            if href and not href.startswith('http'):
                href = f"https://www.forexfactory.com{href}"
            
            if (href and 
                href.startswith("https://www.forexfactory.com/thread/") and 
                not href.startswith("https://www.forexfactory.com/thread/post/")):
                
                if href not in thread_links.values():
                    thread_links[title] = href
                    link_count += 1
        
        return thread_links

    # 存储所有页面的线程信息
    all_threads = []
    
    # 配置无头浏览器
    browser_config = BrowserConfig(
        headless=True,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )
    
    # 初始化爬虫实例
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()
    
    try:
        # 生成所有目标页面URL
        urls = []
        for page in range(start_page, end_page + 1):
            forum_url = f"https://www.forexfactory.com/forum/71-trading-systems?sort=replycount&order=desc&page={page}"
            urls.append(forum_url)
        
        # 分批并发爬取页面
        for i in range(0, len(urls), max_concurrent):
            batch = urls[i:i + max_concurrent]
            tasks = []
            
            for j, url in enumerate(batch):
                # 为每个任务创建唯一会话ID
                session_id = f"page_session_{i + j}"
                config = CrawlerRunConfig(
                    cache_mode=CacheMode.BYPASS,
                    session_id=session_id
                )
                
                task = extract_thread_links(url, crawler, config)
                tasks.append(task)
            
            # 并发执行当前批次的爬取任务
            results = await asyncio.gather(*tasks)
            
            # 处理并整合爬取结果
            for url, thread_links in zip(batch, results):
                if thread_links:
                    page_threads = [{"title": title, "link": url} for title, url in thread_links.items()]
                    all_threads.extend(page_threads)
    
    finally:
        # 关闭爬虫资源
        await crawler.close()
    
    # 转换为JSON输出
    return json.dumps(all_threads, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # 处理命令行参数
    start_page = 1
    end_page = 3
    max_concurrent = 15
    
    if len(sys.argv) > 1:
        try:
            start_page = int(sys.argv[1])
            if start_page < 1:
                start_page = 1
        except ValueError:
            pass
    
    if len(sys.argv) > 2:
        try:
            end_page = int(sys.argv[2])
            if end_page < start_page:
                end_page = start_page
        except ValueError:
            end_page = start_page
    
    if len(sys.argv) > 3:
        try:
            max_concurrent = int(sys.argv[3])
            if max_concurrent < 1:
                max_concurrent = 1
        except ValueError:
            pass
    
    # 执行爬虫并输出结果
    async def run():
        json_result = await get_threads_link(start_page=1, end_page=3)
        print(json_result)
    
    asyncio.run(run())



# 输出格式示例
'''
[
  {
    "title": "Trading Made Simple",
    "link": "https://www.forexfactory.com/thread/291622-trading-made-simple"
  },
  {
    "title": "Supernova GBP/JPY Mini Trend Catcher",
    "link": "https://www.forexfactory.com/thread/44216-supernova-gbpjpy-mini-trend-catcher"
  },
  {
    "title": "Come Surfing Fx With Me System",
    "link": "https://www.forexfactory.com/thread/527711-come-surfing-fx-with-me-system"
  },
  {
    "title": "Roadmap - A Way To Read Markets",
    "link": "https://www.forexfactory.com/thread/993524-roadmap-a-way-to-read-markets"
  }
]
'''

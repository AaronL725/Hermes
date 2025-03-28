import undetected_chromedriver as uc
import time
import os
import re
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from bs4 import BeautifulSoup
import datetime
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

class ForexFactoryCrawler:
    def __init__(self, thread_link, thread_title):
        # 初始化爬虫实例
        self.driver = None
        self.base_url = thread_link
        self.thread_title = thread_title
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.dirname(self.script_dir)
        self.output_dir = os.path.join(self.project_dir, "rawdata")
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # 页码和解析设置
        self.max_page = None
        self.parser = 'lxml'  # 使用更快的lxml解析器
        self.parsed_urls = []  # 预解析URL存储列表

    def start_browser(self):
        # 启动优化的Chrome浏览器实例
        print("开始初始化浏览器...")
        options = uc.ChromeOptions()
        
        # 核心性能选项
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--blink-settings=imagesEnabled=false")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-breakpad")
        options.add_argument("--disable-hang-monitor")
        options.add_argument("--disable-component-update")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--single-process")
        
        try:
            self.driver = uc.Chrome(options=options)
            print("Chrome实例已创建")
            self.driver.maximize_window()
            time.sleep(1)
        except Exception as e:
            print(f"创建浏览器实例失败: {e}")
            # 失败后使用最小配置
            if self.driver is None:
                print("尝试使用最小配置重新启动浏览器...")
                minimal_options = uc.ChromeOptions()
                minimal_options.add_argument("--no-sandbox")
                self.driver = uc.Chrome(options=minimal_options)
                print("使用最小配置成功创建Chrome实例")

    def visit_url(self, url):
        # 访问URL并等待内容加载
        try:
            start_time = time.time()
            
            try:
                self.driver.get(url)
            except:
                # 备用导航方法
                self.driver.execute_script(f"window.location='{url}';")
            
            # 等待内容加载
            self.wait_for_content()
            
            print(f"页面访问总耗时: {time.time() - start_time:.2f} 秒")
            return True
        except Exception as e:
            print(f"导航到URL时出错: {e}")
            # 尝试备用方案
            try:
                self.driver.get('about:blank')
                self.driver.execute_script(f"window.location.href = '{url}';")
                return self.wait_for_content()
            except:
                return False

    def wait_for_content(self):
        # 智能等待页面内容加载完成
        start_time = time.time()
        
        # 添加调试日志
        print("开始等待页面内容加载...")
        
        # 扩展和更新选择器列表
        selectors = [
            # 原有选择器
            "document.querySelectorAll('.threadpost-content__message').length > 0",
            "document.querySelectorAll('div[id^=\"post_message_\"]').length > 0",
            "document.querySelectorAll('div[id^=\"td_post_\"]').length > 0",
            "document.querySelectorAll('.threadpost-header').length > 0",
            "document.querySelectorAll('.flexposts__attachments-frame').length > 0",
            # 新增更宽泛的选择器
            "document.getElementsByClassName('threadpost-content').length > 0",
            "document.getElementsByClassName('postbit').length > 0",
            "document.querySelector('#content') !== null",
            "document.querySelector('.posts') !== null",
            "document.querySelector('.thread') !== null"
        ]
        
        while True:
            # 输出当前页面源码长度，作为调试信息
            try:
                source_len = len(self.driver.page_source)
                if time.time() - start_time > 5 and time.time() - start_time < 5.5:
                    print(f"当前页面源码长度: {source_len} 字节")
            except:
                pass
            
            # 尝试多种选择器检测页面内容
            for selector_check in selectors:
                try:
                    result = self.driver.execute_script(f"return {selector_check}")
                    if result:
                        print(f"内容已加载 (选择器: {selector_check})，用时 {time.time() - start_time:.2f} 秒")
                        return True
                except Exception as e:
                    # 输出JavaScript执行错误
                    if "is not defined" in str(e) or "Cannot read property" in str(e):
                        continue
            
            # 文本特征备用检测 - 增加更多关键词
            try:
                page_text = self.driver.page_source
                markers = ["Support/Resistance", "threadpost-content", "post_message", 
                          "content-main", "page-content", "thread-container", "forum-posts"]
                found_markers = [m for m in markers if m in page_text]
                if found_markers:
                    print(f"内容已通过文本特征检测 ({found_markers[0]})，用时 {time.time() - start_time:.2f} 秒")
                    return True
            except:
                pass
            
            # 尝试通过iframe检测内容
            try:
                iframes = self.driver.find_elements("tag name", "iframe")
                if iframes:
                    for i, iframe in enumerate(iframes):
                        try:
                            self.driver.switch_to.frame(iframe)
                            # 检查iframe内容
                            iframe_content = self.driver.page_source
                            if any(marker in iframe_content for marker in ["post", "thread", "content"]):
                                print(f"在iframe #{i}中检测到内容，用时 {time.time() - start_time:.2f} 秒")
                                self.driver.switch_to.default_content()
                                return True
                            self.driver.switch_to.default_content()
                        except:
                            self.driver.switch_to.default_content()
            except:
                pass
            
            # 尝试基于视觉元素检测
            try:
                if time.time() - start_time > 5:
                    body_height = self.driver.execute_script("return document.body.scrollHeight")
                    if body_height > 500:  # 如果页面有一定高度，可能已加载
                        print(f"检测到页面高度为 {body_height}px，内容可能已加载，用时 {time.time() - start_time:.2f} 秒")
                        return True
            except:
                pass
            
            time.sleep(0.1)  # 减少CPU占用
            
            # 超时处理
            if time.time() - start_time > 5:
                print(f"检测超时，强制继续执行，用时 {time.time() - start_time:.2f} 秒")
                return True

    def get_page_content(self, page_num):
        # 获取指定页码的内容，优先使用预解析URL
        url = None
        
        # 查找预解析URL
        for pnum, purl in self.parsed_urls:
            if pnum == page_num:
                url = purl
                break
        
        # 如果未找到预解析URL，动态生成
        if not url:
            parsed_url = list(urlparse(self.base_url))
            query_dict = parse_qs(parsed_url[4])
            query_dict['page'] = [str(page_num)]
            parsed_url[4] = urlencode(query_dict, doseq=True)
            url = urlunparse(parsed_url)
        
        # 获取内容
        self.visit_url(url)
        return self.driver.page_source

    def detect_max_page(self, html_content):
        # 检测帖子最大页码
        soup = BeautifulSoup(html_content, self.parser)
        
        last_page_link = soup.find('a', title='Last Page')
        if last_page_link:
            max_page = int(last_page_link.text.strip())
            print(f"检测到最大页码: {max_page}")
            return max_page
        
        print("未检测到最大页码，将使用指定的结束页码")
        return None
    
    def prepare_urls(self, start_page, end_page):
        # 高效预解析所有页面URL
        print(f"预解析从第 {start_page} 页到第 {end_page} 页的URL...")
        self.parsed_urls = []
        
        # 仅解析一次基础URL组件
        parsed_base = list(urlparse(self.base_url))
        query_dict = parse_qs(parsed_base[4])
        
        # 批量生成所有页面URL
        for page_num in range(start_page, end_page + 1):
            page_query = query_dict.copy()
            page_query['page'] = [str(page_num)]
            
            page_parsed = parsed_base.copy()
            page_parsed[4] = urlencode(page_query, doseq=True)
            
            url = urlunparse(page_parsed)
            self.parsed_urls.append((page_num, url))
        
        print(f"已预解析 {len(self.parsed_urls)} 个URL")
        return self.parsed_urls
    
    def process_content(self, page_content, page_num):
        # 使用高效方法处理页面内容
        soup = BeautifulSoup(page_content, self.parser)
        posts = soup.find_all('div', class_='threadpost-content__message')
        
        # 计算帖子编号起点
        start_post_num = (page_num - 1) * len(posts) + 1
        result_texts = []
        
        for i, post in enumerate(posts):
            # 直接字符串处理替代DOM操作，提高性能
            post_html = str(post)
            
            # 高效正则表达式清理引用内容
            post_html = re.sub(r'<div\s+class=["\'](?:quote|quotecontainer)["\'][^>]*>.*?</div>', '', 
                              post_html, flags=re.DOTALL)
            post_html = re.sub(r'<div\s+class=["\']frame["\'][^>]*>.*?<blockquote.*?</blockquote>.*?</div>', '', 
                              post_html, flags=re.DOTALL)
            
            # 直接替换HTML元素为文本
            post_html = re.sub(r'<br\s*/?>', '\n', post_html)
            post_html = re.sub(r'<[^>]+>', ' ', post_html)
            
            # 规范化文本格式
            post_text = re.sub(r'\s+', ' ', post_html)
            post_text = re.sub(r'\n{3,}', '\n\n', post_text)
            
            lines = [line.strip() for line in post_text.split('\n')]
            post_text = '\n'.join(lines)
            post_text = re.sub(r'\n{3,}', '\n\n', post_text)
            post_text = post_text.strip()
            
            if post_text:
                result_texts.append(f"--- 帖子 #{start_post_num + i} ---\n{post_text}\n\n")
        
        return "".join(result_texts)

    def crawl_pages(self, start_page=1, end_page=10000):
        # 爬取指定页码范围的所有页面
        output_file = None
        
        # Monkey patch解决Chrome析构问题
        original_del = uc.Chrome.__del__
        def safe_del(self_chrome):
            try:
                if hasattr(self_chrome, 'service') and hasattr(self_chrome.service, 'process'):
                    self_chrome.service.process = None
                if hasattr(self_chrome, '_proc'):
                    self_chrome._proc = None
                original_del(self_chrome)
            except:
                pass
        uc.Chrome.__del__ = safe_del
        
        try:
            self.start_browser()
            
            # 获取最大页码并处理第一页
            start_time = time.time()
            first_page_content = self.get_page_content(start_page)
            self.max_page = self.detect_max_page(first_page_content)
            
            if self.max_page and end_page > self.max_page:
                end_page = self.max_page
            
            # 创建输出文件
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            cleaned_title = re.sub(r'[<>:"/\\|?*]', '', self.thread_title)
            output_file = os.path.join(self.output_dir, f"{cleaned_title}_{current_time}_extracted.txt")
            
            # 处理第一页内容
            first_page_processed = self.process_content(first_page_content, start_page)
            
            # 同步开始URL解析
            with ThreadPoolExecutor(max_workers=1) as url_executor:
                # 在后台线程中预解析所有URL
                urls_future = url_executor.submit(self.prepare_urls, start_page, end_page)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write("===== 帖子内容 =====\n\n")
                    
                    # 写入第一页内容
                    f.write(first_page_processed)
                    
                    # 等待URL解析完成
                    urls_to_fetch = urls_future.result()
                    
                    # 收集剩余页面内容
                    page_contents = {}
                    for i, (page_num, url) in enumerate(self.parsed_urls[1:], 1):
                        page_start_time = time.time()
                        print(f"正在爬取第 {page_num} 页 ({i}/{len(self.parsed_urls)-1})")
                        
                        content = self.get_page_content(page_num)
                        page_contents[page_num] = content
                        
                        print(f"第 {page_num} 页内容获取完成，耗时 {time.time() - page_start_time:.2f} 秒")
                    
                    # 并行处理所有页面内容
                    print("开始并行处理页面内容...")
                    process_start_time = time.time()
                    
                    # 动态确定线程数
                    max_workers = min(5, os.cpu_count() * 2 if os.cpu_count() else 4)
                    print(f"使用 {max_workers} 个线程处理内容")
                    
                    processed_results = {}
                    with ThreadPoolExecutor(max_workers=max_workers) as executor:
                        # 提交所有处理任务
                        future_to_page = {
                            executor.submit(self.process_content, content, page_num): page_num
                            for page_num, content in page_contents.items()
                        }
                        
                        # 收集处理结果
                        for future in concurrent.futures.as_completed(future_to_page):
                            page_num = future_to_page[future]
                            try:
                                processed_results[page_num] = future.result()
                            except Exception as exc:
                                print(f"处理第 {page_num} 页时出错: {exc}")
                    
                    print(f"所有内容并行处理完成，耗时 {time.time() - process_start_time:.2f} 秒")
                    
                    # 按页码顺序写入结果
                    for page_num in sorted(processed_results.keys()):
                        f.write(processed_results[page_num])
                        f.flush()
                    
                    # 写入附件链接
                    f.write("\n===== 附件下载链接 =====\n\n")
            
            print(f"所有页面爬取完成，总耗时 {time.time() - start_time:.2f} 秒")
            print(f"内容已保存到: {output_file}")
            
        except Exception as e:
            print(f"爬取过程中出现错误: {e}")
            if output_file and os.path.exists(output_file):
                try:
                    os.remove(output_file)
                    print(f"已删除未完成的文件: {output_file}")
                except Exception as del_err:
                    print(f"删除文件失败: {del_err}")
            raise

        finally:
            self.close_browser()

    def close_browser(self):
        # 安全关闭浏览器实例
        if self.driver:
            driver = self.driver
            self.driver = None  # 防止重复关闭
            
            try:
                # 阻止析构函数错误
                if hasattr(driver, 'service') and hasattr(driver.service, 'process'):
                    driver.service.process = None
                if hasattr(driver, '_proc'):
                    driver._proc = None
                    
                driver.close()
                print("已关闭浏览器窗口")
            except Exception as e:
                print(f"关闭窗口时出错: {e}")
            
            try:
                driver.quit()
                print("已关闭浏览器驱动")
            except Exception as e:
                print(f"关闭驱动程序时出错: {e}")

def crawl_thread(thread_data):
    # 爬取单个帖子
    cleaned_title = re.sub(r'[<>:"/\\|?*]', '', thread_data['title'])
    
    # 确定输出路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    rawdata_dir = os.path.join(project_dir, "rawdata")
    
    if not os.path.exists(rawdata_dir):
        os.makedirs(rawdata_dir)
    
    # 检查是否已爬取过
    if os.path.exists(rawdata_dir):
        for filename in os.listdir(rawdata_dir):
            if filename.startswith(cleaned_title + "_") and filename.endswith("_extracted.txt"):
                print(f"跳过已爬取的帖子: {thread_data['title']}")
                return
    
    # 开始爬取
    print(f"开始爬取新帖子: {thread_data['title']}")
    crawler = ForexFactoryCrawler(thread_data['link'], thread_data['title'])
    crawler.crawl_pages()

if __name__ == "__main__":
    # 测试入口
    threads_list = [
        {
            "title": "Gold (XAU/USD) with BiteFX",
            "link": "https://www.forexfactory.com/thread/1328362-gold-xauusd-with-bitefx"
        },
        {
            "title": "New Variation on 7 am to 9 am Breakout Strategy",
            "link": "https://www.forexfactory.com/thread/171613-new-variation-on-7-am-to-9-am"
        }
    ]
    
    for thread in threads_list:
        print(f"\n开始爬取: {thread['title']}")
        crawl_thread(thread)
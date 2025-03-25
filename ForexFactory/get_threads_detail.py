import undetected_chromedriver as uc
import time
import os
import re
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import html2text
from bs4 import BeautifulSoup
import datetime
import psutil

class ForexFactoryCrawler:
    def __init__(self, thread_link, thread_title):
        # 初始化爬虫对象，设置基础URL和输出目录
        self.driver = None
        self.base_url = thread_link
        self.thread_title = thread_title
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_dir = os.path.join(self.script_dir, "unextracted_files")
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # 设置HTML转Markdown配置
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0  # 不限制行宽
        self.max_page = None

    def start_browser(self):
        print("开始初始化浏览器...")
        options = uc.ChromeOptions()
        
        # 基础必要选项
        options.add_argument("--disable-dev-shm-usage")  # 防止Linux下内存问题
        options.add_argument("--no-sandbox")  # 避免沙箱安全问题
        
        # 加速选项 - 保留这些
        options.add_argument("--disable-gpu")  # 禁用GPU
        options.add_argument("--blink-settings=imagesEnabled=false")  # 禁用图片加载
        options.add_argument("--disable-extensions")  # 禁用扩展
        
        # 有效的性能优化
        options.add_argument("--disable-infobars")  # 禁用信息栏
        options.add_argument("--disable-notifications")  # 禁用通知
        options.add_argument("--disable-popup-blocking")  # 禁用弹窗阻止
        options.add_argument("--disable-default-apps")  # 禁用默认应用
        
        # 有助于减少资源使用的选项
        options.add_argument("--disable-background-networking")  # 禁用后台网络
        options.add_argument("--disable-breakpad")  # 禁用崩溃报告
        
        # 添加一些内存优化
        options.add_argument("--disable-hang-monitor")
        options.add_argument("--disable-component-update")
        options.add_argument("--disable-client-side-phishing-detection")
        
        # 添加进程限制，防止内存泄漏
        options.add_argument("--single-process")
        
        print("创建Chrome实例...")
        try:
            self.driver = uc.Chrome(options=options)
            print("Chrome实例已创建")
            self.driver.maximize_window()
            print("浏览器窗口已最大化")
            time.sleep(1)  # 减少启动等待时间
        except Exception as e:
            print(f"创建浏览器实例失败: {e}")
            # 备用尝试：最小配置
            if self.driver is None:
                print("尝试使用最小配置重新启动浏览器...")
                minimal_options = uc.ChromeOptions()
                minimal_options.add_argument("--no-sandbox")
                self.driver = uc.Chrome(options=minimal_options)
                print("使用最小配置成功创建Chrome实例")

    def visit_url(self, url):
        try:
            # 移除页面加载超时设置，允许完整加载
            start_time = time.time()
            
            try:
                # 常规导航方式
                self.driver.get(url)
            except:
                # 备用导航方式
                self.driver.execute_script(f"window.location='{url}';")
            
            # 等待内容加载，现在会无限等待直到检测到内容
            result = self.wait_for_content()
            
            print(f"页面访问总耗时: {time.time() - start_time:.2f} 秒")
            return result
        except Exception as e:
            print(f"导航到URL时出错: {e}")
            # 备用方案
            try:
                self.driver.get('about:blank')
                self.driver.execute_script(f"window.location.href = '{url}';")
                return self.wait_for_content()
            except Exception as e2:
                print(f"备用导航也失败: {e2}")
                return False

    def wait_for_content(self, max_wait=None):
        # 根据HTML结构优化选择器，无限等待直到检测到内容
        start_time = time.time()
        selectors = [
            # 主要内容容器
            "document.querySelectorAll('.threadpost-content__message').length > 0",
            # 带ID的帖子消息
            "document.querySelectorAll('div[id^=\"post_message_\"]').length > 0",
            # 帖子容器
            "document.querySelectorAll('div[id^=\"td_post_\"]').length > 0",
            # 帖子头部
            "document.querySelectorAll('.threadpost-header').length > 0",
            # 附件框架
            "document.querySelectorAll('.flexposts__attachments-frame').length > 0"
        ]
        
        # 无限循环，直到检测到内容
        while True:
            for selector_check in selectors:
                try:
                    result = self.driver.execute_script(f"return {selector_check}")
                    if result:
                        # 内容已加载，继续处理
                        print(f"内容已加载(检测到特定元素)，用时 {time.time() - start_time:.2f} 秒")
                        return True
                except:
                    pass
            
            # 检查页面文本特征，作为内容检测的备选方法
            try:
                page_text = self.driver.page_source
                if ("Support/Resistance" in page_text or 
                    "threadpost-content" in page_text or
                    "post_message" in page_text):
                    print(f"内容已通过文本特征检测，用时 {time.time() - start_time:.2f} 秒")
                    return True
            except:
                pass
            
            # 每100毫秒检查一次
            time.sleep(0.1)
            
            # 可选：显示等待时间，帮助调试
            if time.time() - start_time > 10 and (time.time() - start_time) % 5 < 0.1:
                print(f"已等待 {time.time() - start_time:.0f} 秒，继续等待内容加载...")

    def get_page_content(self, page_num):
        # 获取指定页码的页面内容
        parsed_url = list(urlparse(self.base_url))
        query_dict = parse_qs(parsed_url[4])
        query_dict['page'] = [str(page_num)]
        parsed_url[4] = urlencode(query_dict, doseq=True)
        url = urlunparse(parsed_url)
        
        print(f"解析后的URL: {parsed_url}")
        print(f"构建的完整URL: {url}")
        
        self.visit_url(url)
        
        content = self.driver.page_source
        return content

    def convert_to_markdown(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 只保留帖子内容区域，减少处理量
        content_area = soup.find('div', id='thread-content') or soup
        
        # 一次性移除所有无关元素
        for selector in ['script', 'style', 'iframe', '.navigation', '.menu', '.footer']:
            for element in content_area.select(selector):
                element.decompose()
            
        markdown = self.h2t.handle(str(content_area))
        return markdown

    def detect_max_page(self, html_content):
        # 从页面内容中检测最大页码
        soup = BeautifulSoup(html_content, 'html.parser')
        
        last_page_link = soup.find('a', title='Last Page')
        if last_page_link:
            max_page = int(last_page_link.text.strip())
            print(f"检测到最大页码: {max_page}")
            return max_page
        
        print("未检测到最大页码，将使用指定的结束页码")
        return None

    def crawl_pages(self, start_page=1, end_page=10000):
        try:
            self.start_browser()
            
            # 获取最大页码
            start_time = time.time()
            first_page_content = self.get_page_content(start_page)
            self.max_page = self.detect_max_page(first_page_content)
            
            if self.max_page and end_page > self.max_page:
                end_page = self.max_page
            
            # 准备URL列表
            urls = []
            for page in range(start_page, end_page + 1):
                parsed_url = list(urlparse(self.base_url))
                query_dict = parse_qs(parsed_url[4])
                query_dict['page'] = [str(page)]
                parsed_url[4] = urlencode(query_dict, doseq=True)
                urls.append(urlunparse(parsed_url))
            
            # 保存第一页内容
            all_content = [first_page_content]
            
            # 实现预加载机制
            if len(urls) > 2:  # 如果有足够的页面
                # 预加载第二个页面，但不使用有问题的容器代码
                self.driver.execute_script(f"""
                    try {{
                        var preloader = document.createElement('iframe');
                        preloader.style.display = 'none';
                        preloader.src = '{urls[1]}';
                        document.body.appendChild(preloader);
                    }} catch(e) {{
                        console.log('预加载错误: ' + e.message);
                    }}
                """)
            
            total_pages = len(urls[1:])
            for i, url in enumerate(urls[1:]):
                page_start_time = time.time()
                print(f"正在爬取: {url} ({i+1}/{total_pages})")
                
                # 修改预加载逻辑，确保安全追加到body
                if i+2 < len(urls):
                    try:
                        # 创建一个隐藏的iframe预加载下一页
                        self.driver.execute_script(f"""
                            try {{
                                var preloader = document.createElement('iframe');
                                preloader.style.display = 'none';
                                preloader.src = '{urls[i+2]}';
                                if (document.body) {{
                                    document.body.appendChild(preloader);
                                }}
                            }} catch(e) {{
                                console.log('预加载错误: ' + e.message);
                            }}
                        """)
                    except:
                        pass
                
                self.visit_url(url)
                all_content.append(self.driver.page_source)
                print(f"第 {i+2} 页爬取完成，耗时 {time.time() - page_start_time:.2f} 秒")
            
            print(f"所有页面爬取完成，总耗时 {time.time() - start_time:.2f} 秒")
            
            combined_html = '\n'.join(all_content)
            
            markdown_content = self.convert_to_markdown(combined_html)
            
            cleaned_markdown = self.clean_markdown(markdown_content)
            
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # 清理文件名，移除非法字符
            cleaned_title = re.sub(r'[<>:"/\\|?*]', '', self.thread_title)
            filename = f"{cleaned_title}_{current_time}.md" if cleaned_title else f"thread_content_{current_time}.md"
            output_file = os.path.join(self.output_dir, filename)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_markdown)
            
            print(f"爬取完成！内容已保存到: {output_file}")
            
        finally:
            # 确保浏览器进程被彻底关闭
            if self.driver:
                try:
                    self.driver.close()
                except:
                    pass
                
                try:
                    for proc in psutil.process_iter():
                        try:
                            if "chrome" in proc.name().lower():
                                cmdline = " ".join(proc.cmdline()).lower()
                                if "--remote-debugging-port" in cmdline:
                                    proc.terminate()
                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                            pass
                except:
                    pass
                
                self.driver = None

    def clean_markdown(self, markdown_content):
        # 合并所有正则表达式为一个大正则，提高处理速度
        combined_pattern = '|'.join([
            r"^.*\[ Home \].*$",
            r"^.*\[ Forums \].*$",
            r"^.*\[ Trades \].*$", 
            r"^.*\[ News \].*$",
            r"^.*\[ Calendar \].*$",
            r"^.*\[ Market \].*$",
            r"^.*\[ Brokers \].*$",
            r"^.*\[\]\(/login\).*$",
            r"^.*Menu \[ \]\(/\).*$",
            r"^.*\[ Login \].*$",
            r"^.*\[ Create Account \].*$",
            r"^.*\[ \]\(/\).*$",
            r"^.*\[\]\(javascript:void.*\).*$",
            r"^.*\[Print Thread\].*$",
            r"^.*\[Cancel\].*$",
            r"^.*\[Exit Attachments\].*$",
            r"^.*\[Last Post\].*$",
            r"^.*\[First Page\].*$",
            r"^.*\[Last Page\].*$",
            r"^.*\[Quote\].*$",
            r"^.*\[Reply to Thread\].*$",
            r"^.*\[Subscribe\].*$",
            r"^.*\[Page \d+\].*$",
            r"^.*\d+ trader.*viewing now.*$",
            r"^.*Top of Page.*$",
            r"^.*\[Facebook\].*$",
            r"^.*\[X\].*$",
            r"^.*\*\*About FF\*\*.*$",
            r"^.*\*\*FF Products\*\*.*$",
            r"^.*\*\*FF Website\*\*.*$",
            r"^.*\*\*Follow FF\*\*.*$",
            r"^.*FF Sister Sites:.*$",
            r"^.*\[Metals Mine\].*$",
            r"^.*\[Energy EXCH\].*$",
            r"^.*\[Crypto Craft\].*$",
            r"^.*Forex Factory.*$",
            r"^.*\[Terms of Service\].*$",
            r"^.*\[Mission\].*$",
            r"^.*\[Products\].*$",
            r"^.*\[User Guide\].*$",
            r"^.*\[Media Kit\].*$",
            r"^.*\[Blog\].*$",
            r"^.*\[Contact\].*$",
            r"^.*\[Trade Explorer\].*$",
            r"^.*\[Homepage\].*$",
            r"^.*\[Search\].*$",
            r"^.*\[Traders\].*$",
            r"^.*\[Report a Bug\].*$",
            r"^.*Options.*$",
            r"^.*Bookmark Thread.*$",
            r"^.*First Unread.*$",
            r"^.*Similar Threads.*$",
            r"^.*\[Login\].*$",
            r"^.*\[Create Account\].*$",
            r"^.*User/Email.*$",
            r"^.*\(/timezone.*$"
        ])
        
        # 一次性替换所有匹配项
        cleaned_content = re.sub(combined_pattern, '', markdown_content, flags=re.MULTILINE)
        cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)
        
        return cleaned_content

def crawl_thread(thread_data):
    """
    爬取单个论坛帖子的内容
    
    Args:
        thread_data (dict): 包含帖子信息的字典，必须包含 'title' 和 'link' 键
    """
    # 清理标题中的非法字符
    cleaned_title = re.sub(r'[<>:"/\\|?*]', '', thread_data['title'])
    
    # 检查是否已经爬取过
    script_dir = os.path.dirname(os.path.abspath(__file__))
    unextracted_dir = os.path.join(script_dir, "unextracted_files")
    
    # 检查文件夹中是否存在以该标题开头的文件
    if os.path.exists(unextracted_dir):
        for filename in os.listdir(unextracted_dir):
            if filename.startswith(cleaned_title + "_") and filename.endswith(".md"):
                print(f"跳过已爬取的帖子: {thread_data['title']}")
                return
    
    # 如果没有爬取过，则开始爬取
    print(f"开始爬取新帖子: {thread_data['title']}")
    crawler = ForexFactoryCrawler(thread_data['link'], thread_data['title'])
    crawler.crawl_pages()

if __name__ == "__main__":
    # 批量爬取示例
    threads_list = [
        {
            "title": "Update v.1 sniper rishijay trading system new arrow in arsenal",
            "link": "https://www.forexfactory.com/thread/692194-update-v1-sniper-rishijay-trading-system-new-arrow"
        },
        {
            "title": "Opening price US30", 
            "link": "https://www.forexfactory.com/thread/1064458-opening-price-us30"
        }
    ]
    
    for thread in threads_list:
        print(f"\n开始爬取: {thread['title']}")
        crawl_thread(thread)

import json
import sys
import undetected_chromedriver as uc
import time
from bs4 import BeautifulSoup
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 定义并添加到模块初始化时
def patched_quit(self):
    try:
        if hasattr(self, 'service') and self.service.process:
            try:
                self.service.stop()
            except:
                pass
    except:
        pass
    
    try:
        # 跳过time.sleep()调用，这是导致错误的根源
        self.original_command_executor._conn.close()
    except:
        pass

# 应用monkey patch
original_quit = uc.Chrome.quit
uc.Chrome.quit = patched_quit

class ForumLinkCrawler:
    def __init__(self):
        """
        初始化爬虫实例
        """
        self.driver = None
    
    def start_browser(self):
        """
        启动无头Chrome浏览器
        """
        options = uc.ChromeOptions()
        
        # 核心选项
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        
        # 性能优化
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        
        # 内存优化
        options.add_argument("--disable-hang-monitor")
        options.add_argument("--disable-component-update")
        
        try:
            self.driver = uc.Chrome(options=options)
            self.driver.maximize_window()
            return True
        except Exception as e:
            print(f"创建浏览器实例失败: {e}")
            traceback.print_exc()
            
            # 尝试最小配置
            try:
                if self.driver is None:
                    minimal_options = uc.ChromeOptions()
                    minimal_options.add_argument("--no-sandbox")
                    self.driver = uc.Chrome(options=minimal_options)
                    return True
            except Exception as e2:
                print(f"使用最小配置创建浏览器也失败: {e2}")
                return False
    
    def wait_for_content(self, timeout=10):
        """
        动态等待页面内容加载
        """
        start_time = time.time()
        print("等待页面内容加载...")
        
        # 定义可能的内容指示器元素列表
        possible_indicators = [
            (By.CLASS_NAME, "thread-title"),
            (By.CLASS_NAME, "threadlist"),
            (By.CLASS_NAME, "pagination"),
            (By.TAG_NAME, "table"),  # 论坛通常用表格显示帖子列表
            (By.CLASS_NAME, "threadbit"),  # 一些论坛使用的帖子容器
            (By.CLASS_NAME, "threadlisthead"),  # 帖子列表头部
            (By.CLASS_NAME, "post"),  # 帖子元素
            (By.CLASS_NAME, "topic"),  # 主题元素
        ]
        
        # 轮询检查各种可能的指示器
        for selector_type, selector_value in possible_indicators:
            try:
                WebDriverWait(self.driver, timeout/len(possible_indicators)).until(
                    EC.presence_of_element_located((selector_type, selector_value))
                )
                print(f"找到 {selector_value} 元素，内容加载完成，耗时: {time.time() - start_time:.2f}秒")
                return True
            except Exception:
                continue
        
        # 如果所有指示器都没找到，检查链接数量作为后备方案
        try:
            all_links = self.driver.find_elements(By.TAG_NAME, 'a')
            if len(all_links) > 30:  # 假设至少有30个链接的页面已加载
                print(f"检测到足够的链接，内容可能已加载，耗时: {time.time() - start_time:.2f}秒")
                return True
        except:
            pass
        
        # 最后检查页面标题或URL变化
        try:
            # 等待页面标题非空
            if self.driver.title:
                print(f"页面有标题，内容可能已加载，耗时: {time.time() - start_time:.2f}秒")
                return True
        except:
            pass
        
        print(f"等待超时，内容未完全加载，耗时: {time.time() - start_time:.2f}秒")
        return False
    
    def visit_url(self, url):
        """
        访问指定URL并等待内容加载
        """
        if not self.driver:
            print("浏览器未初始化，无法访问URL")
            return False
            
        try:
            print(f"正在访问: {url}")
            self.driver.get(url)
            return self.wait_for_content()
        except Exception as e:
            print(f"访问URL时出错: {e}")
            return False
    
    def extract_thread_links(self, url):
        """
        从单个论坛页面提取线程链接
        """
        if not self.visit_url(url):
            return {}
        
        html_content = self.driver.page_source
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
    
    def close(self):
        """
        关闭浏览器和资源 - 强制结束所有Chrome进程
        """
        import os
        import signal
        import psutil
        
        driver_ref = self.driver
        self.driver = None  # 先断开引用
        
        # 1. 尝试常规的清理方法
        if driver_ref:
            try:
                driver_ref.delete_all_cookies()
            except:
                pass
            
            try:
                driver_ref.quit()
            except:
                pass
        
        # 2. 强制结束所有相关Chrome进程
        try:
            # 查找并终止所有Chrome和ChromeDriver进程
            current_pid = os.getpid()
            for proc in psutil.process_iter():
                try:
                    # 跳过当前Python进程
                    if proc.pid == current_pid:
                        continue
                        
                    # 寻找Chrome相关进程
                    if any(name in proc.name().lower() for name in ["chrome", "chromedriver"]):
                        # 输出将要终止的进程信息
                        print(f"强制终止进程: {proc.name()} (PID: {proc.pid})")
                        
                        # 尝试正常终止
                        proc.terminate()
                        
                        # 不等待，立即继续
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                    print(f"处理进程时出错: {e}")
                    continue
        except Exception as e:
            print(f"强制终止Chrome进程失败: {e}")

def get_threads_link(start_page=1, end_page=1):
    """
    从ForexFactory论坛爬取指定页码范围内的交易系统线程链接
    """
    all_threads = []
    crawler = ForumLinkCrawler()
    
    try:
        print("正在初始化浏览器...")
        if not crawler.start_browser():
            print("无法初始化浏览器，爬虫终止")
            return json.dumps(all_threads, ensure_ascii=False, indent=2)
        print("浏览器初始化成功")
        
        # 单线程顺序爬取每个页面
        for page in range(start_page, end_page + 1):
            forum_url = f"https://www.forexfactory.com/forum/71-trading-systems?sort=replycount&order=desc&page={page}"
            print(f"正在尝试访问页面: {forum_url}")
            
            thread_links = crawler.extract_thread_links(forum_url)
            page_threads = [{"title": title, "link": url} for title, url in thread_links.items()]
            all_threads.extend(page_threads)
            
            print(f"第 {page} 页爬取完成，获取到 {len(page_threads)} 个线程链接")
            
            # 不再使用固定等待时间，直接进入下一页爬取
    
    except Exception as e:
        print(f"爬取过程中发生错误: {e}")
        traceback.print_exc()
    
    finally:
        # 确保资源被正确关闭
        crawler.close()
    
    # 转换为JSON输出
    return json.dumps(all_threads, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    # 处理命令行参数
    start_page = 1
    end_page = 1
    
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
    
    # 执行爬虫并输出结果
    print(f"开始爬取从第 {start_page} 页到第 {end_page} 页的线程链接...")
    json_result = get_threads_link(start_page, end_page)
    print(json_result)

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
  }
]
'''

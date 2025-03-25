import json
import asyncio
import sys
from get_threads_link import get_threads_link
from get_threads_detail import crawl_thread
from unextracted_files.file_downloader import downloader
from vectorization import ForexVectorDB
from llm import analyze_threads

if sys.platform.startswith('win'):
    asyncio.set_event_loop(asyncio.ProactorEventLoop())

async def run_option_1():
    # 获取线程链接并保存
    json_result = await get_threads_link(start_page=3, end_page=10)
    threads_data = json.loads(json_result)
    
    # 批量抓取内容
    for thread in threads_data:
        crawl_thread(thread)

async def run_option_2():
    await downloader.run()

def run_option_3():
    try:
        vector_db = ForexVectorDB()
        vector_db.create_database()
        print("向量化数据已完成。")
    except Exception as e:
        print(f"向量化数据时发生错误: {e}")

def run_option_4():
    analyze_threads()

def show_menu():
    print("\n请选择要执行的操作：")
    print("1. 批量获取链接并抓取内容")
    print("2. 下载文件")
    print("3. 向量化数据")
    print("4. 运行LLM分析")
    print("5. 退出")

async def main():
    while True:
        show_menu()
        choice = input("请输入选项 (1-5): ")
        
        if choice == "1":
            await run_option_1()
        elif choice == "2":
            await run_option_2()
        elif choice == "3":
            run_option_3()
        elif choice == "4":
            run_option_4()
        elif choice == "5":
            print("程序已退出")
            break
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    asyncio.run(main())

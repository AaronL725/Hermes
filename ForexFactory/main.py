import json
from module.get_threads_link import get_threads_link
from module.get_threads_detail import crawl_thread
from module.file_downloader import downloader
from module.vectorization import ForexVectorDB
from module.llm import analyze_threads
import asyncio

def run_option_1():
    try:
        print("开始获取线程链接...")
        json_result = get_threads_link(start_page=3, end_page=20)
        threads_data = json.loads(json_result)
        print(f"成功获取到 {len(threads_data)} 个线程链接")
        
        # 批量抓取内容
        for thread in threads_data:
            try:
                crawl_thread(thread)
            except Exception as e:
                print(f"抓取线程时出错: {e}")
                continue
        
        print("所有线程抓取完成")
    except Exception as e:
        print(f"获取线程链接时发生错误: {e}")

def run_option_2():
    asyncio.run(downloader.run())

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

def main():
    while True:
        show_menu()
        choice = input("请输入选项 (1-5): ")
        
        if choice == "1":
            run_option_1()
        elif choice == "2":
            run_option_2()
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
    main()

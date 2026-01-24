@echo off
rem 将当前目录切换到批处理文件所在的目录
cd /d "%~dp0"
rem 使用相对路径执行 Python 脚本，指定解释器路径
A:\Python312\python312.exe main_mining.py

#!/usr/bin/env python3
import os
import re
import sys

def find_indicator_file(indicator_name, directory='ta_func'):
    """
    查找实现给定指标的C文件。
    
    参数:
        indicator_name (str): 指标的名称（例如 'RSI'）
        directory (str): 要搜索的目录
        
    返回:
        str: 实现该指标的C文件的路径
    """
    # 转换为大写以便一致匹配
    indicator_name = indicator_name.upper()
    
    # 查找 ta_INDICATOR.c 文件
    indicator_file = f"ta_{indicator_name}.c"
    full_path = os.path.join(directory, indicator_file)
    
    if os.path.exists(full_path):
        return full_path
    
    # 如果没有直接找到，搜索可能包含它的文件
    for filename in os.listdir(directory):
        if filename.lower().endswith('.c') and indicator_name in filename.upper():
            return os.path.join(directory, filename)
    
    return None

def remove_c_comments(code):
    """
    从代码中删除C风格的注释。
    
    参数:
        code (str): 带有注释的C代码
        
    返回:
        str: 没有注释的C代码
    """
    # 删除多行注释 (/* ... */)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    
    # 删除单行注释 (// ...)
    code = re.sub(r'//.*?$', '', code, flags=re.MULTILINE)
    
    # 清理空行和多余的空白
    code = re.sub(r'\n\s*\n', '\n', code)
    return code.strip()

def extract_core_algorithm(file_path):
    """
    从TA-Lib C文件中提取核心算法。
    
    参数:
        file_path (str): C文件的路径
        
    返回:
        str: 提取的核心算法代码（已删除注释）
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 查找主函数实现
    # 这通常在GENCODE SECTION 3和GENCODE SECTION 5之间
    pattern = r'/\*\*\*\* END GENCODE SECTION 3[^\n]*\*\*\*\*/.*?/\*\*\*\* START GENCODE SECTION 5'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # 如果第一个模式不匹配，尝试另一种方法
        pattern = r'/\* Insert TA function code here\. \*/.*?VALUE_HANDLE_DEREF\(outNBElement\) = outIdx;'
        match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # 如果仍然没有匹配，提取GENCODE SECTION 3后的第一个函数实现
        pattern = r'/\*\*\*\* END GENCODE SECTION 3[^\n]*\*\*\*\*/.*?\{(.*?)return '
        match = re.search(pattern, content, re.DOTALL)
    
    if match:
        algorithm_code = match.group(0)
        
        # 检查是否有指示核心算法的注释
        core_comment = "/* Insert TA function code here. */"
        if core_comment in algorithm_code:
            # 从注释后提取
            algorithm_code = algorithm_code.split(core_comment)[1]
        
        # 清理代码
        algorithm_code = algorithm_code.strip()
        
        # 如果包含GENCODE SECTION 5的开始部分，则删除尾部
        if '/**** START GENCODE SECTION 5' in algorithm_code:
            algorithm_code = algorithm_code.split('/**** START GENCODE SECTION 5')[0].strip()
        
        # 删除C风格的注释
        algorithm_code = remove_c_comments(algorithm_code)
        
        return algorithm_code
    
    return "无法提取核心算法。"

def main():
    if len(sys.argv) != 2:
        print("用法: python extract.py <indicator_name>")
        print("示例: python extract.py RSI")
        sys.exit(1)
    
    indicator_name = sys.argv[1]
    file_path = find_indicator_file(indicator_name)
    
    if not file_path:
        print(f"找不到指标'{indicator_name}'的C文件")
        sys.exit(1)
    
    algorithm_code = extract_core_algorithm(file_path)
    print(algorithm_code)

if __name__ == "__main__":
    main()

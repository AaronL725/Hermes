import os
import sys
import re
from langchain_xai import ChatXAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json
from tqdm import tqdm
from dotenv import load_dotenv

def analyze_indicator_function(function_code, function_name, api_key):
    """
    分析指标函数是否使用未来数据及其防止机制。
    
    返回值:
        int: 如果没有使用未来数据且有防止机制则返回1，否则返回0
    """
    system_prompt = """You are a senior code review expert with 10 years of experience in quantitative trading system development, specializing in financial time series data processing. Your task is to strictly review indicator function code to determine if it uses future data or lacks safety mechanisms to prevent the use of future data.

【Future Data】: Using t+1 or later data when calculating the indicator at time t, such as:
- Direct access to future index: data[t+1], data[ts+offset] where offset>0
- Forward reference in loops: for i in range(len(data)-1): result[i] = data[i+1]
- Negative parameter shift: np.roll(data, -1), DELAY(close, -1)

【Effective Prevention Mechanisms】
Effective prevention mechanisms include but are not limited to:
- Historical length check: if ts <= N: continue
- Correct slicing: data[:ts+1]
- Data validity: if close[ts,sec] != close[ts,sec]

【Judgment Criteria】
Output "1": No future data is used AND at least one prevention mechanism is implemented
Output "0": Future data is used OR lack of prevention mechanisms

Only answer 0 or 1. Do not explain the reason.
"""
    
    # Use explicit placeholders in the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "Function name: {func_name_placeholder}\n\n```python\n{func_code_placeholder}\n```")
    ])
    
    llm = ChatXAI(
        api_key=api_key,
        model="grok-3-latest",
        temperature=0,
        max_tokens=1000
    )
    
    chain = prompt | llm | StrOutputParser()
    
    try:
        # Provide the actual values for the placeholders in the invoke call
        result = chain.invoke({
            "func_name_placeholder": function_name,
            "func_code_placeholder": function_code
        })
        # 确保结果是0或1
        if result.strip() in ["0", "1"]:
            return int(result.strip())
        else:
            print(f"警告: {function_name}的结果异常: {result}")
            return 0  # 默认返回0表示不符合要求
    except Exception as e:
        print(f"分析函数{function_name}时出错: {e}")
        return 0  # 出错时默认返回0表示不符合要求

def extract_indicator_functions(file_path):
    """
    从BaseLogicFactors类中提取所有指标函数。
    
    返回值:
        dict: 函数名和函数代码的字典
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取BaseLogicFactors类
    class_match = re.search(r'class BaseLogicFactors:.*?(?=class|\Z)', content, re.DOTALL)
    if not class_match:
        raise ValueError("未找到BaseLogicFactors类")
    
    class_content = class_match.group(0)
    
    # 查找所有静态方法/指标函数
    function_pattern = r'@staticmethod\s+@nb\.njit\s+def\s+([A-Za-z0-9_]+)\s*\(.*?\):.*?(?=\s+@staticmethod|\s*$)'
    functions = re.findall(function_pattern, class_content, re.DOTALL)
    
    # 提取每个函数的完整代码
    indicator_functions = {}
    for func_name in functions:
        func_pattern = r'@staticmethod\s+@nb\.njit\s+def\s+' + func_name + r'\s*\(.*?\):.*?(?=\s+@staticmethod|\s*$)'
        func_match = re.search(func_pattern, class_content, re.DOTALL)
        if func_match:
            indicator_functions[func_name] = func_match.group(0)
    
    return indicator_functions

def get_xai_api_key():
    """获取XAI API密钥从module/.env文件"""
    # 获取当前文件目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 获取项目根目录
    root_dir = os.path.dirname(current_dir)
    # 设置.env文件路径
    env_path = os.path.join(root_dir, "module", ".env")
    
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"未找到.env文件: {env_path}")
    
    # 加载环境变量
    load_dotenv(env_path)
    xai_api_key = os.environ.get("XAI_API_KEY_Aaron")
    
    if not xai_api_key:
        raise ValueError("在.env文件中未找到XAI_API_KEY")
    
    return xai_api_key

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'baselogicfactors.py')
    
    if not os.path.exists(file_path):
        print(f"错误: 未找到文件 {file_path}")
        sys.exit(1)
    
    # 获取XAI API密钥
    try:
        api_key = get_xai_api_key()
        print("成功获取XAI API密钥")
    except Exception as e:
        print(f"获取API密钥失败: {str(e)}")
        sys.exit(1)
    
    print("正在提取指标函数...")
    indicator_functions = extract_indicator_functions(file_path)
    print(f"找到 {len(indicator_functions)} 个指标函数。")
    
    results = {}
    failing_indicators = []
    print("正在分析指标函数是否使用未来数据...")
    for func_name, func_code in tqdm(indicator_functions.items(), desc="分析中"):
        result = analyze_indicator_function(func_code, func_name, api_key)
        results[func_name] = result

        # 如果不满足要求，添加到失败列表
        if result == 0:
            failing_indicators.append(func_name)
    
    # 计算失败函数数量
    failing_count = len(failing_indicators)
    passing_count = len(results) - failing_count

    # 打印摘要
    print(f"\n分析完成!")
    print(f"指标函数总数: {len(results)}")
    print(f"符合要求的函数数量: {passing_count}")
    print(f"不符合要求的函数数量: {failing_count}")
    if failing_indicators:
        print("不符合要求的函数名：")
        for func_name in failing_indicators:
            print(func_name)
    return failing_count

if __name__ == "__main__":
    failing_count = main()
    print(f"不符合要求的函数数量: {failing_count}")

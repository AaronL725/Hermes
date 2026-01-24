import numpy as np
import numba as nb
import pandas as pd
import random
import sys
import os

# 添加项目路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backtest.RuleBackTest import RunRuleBackTest

@nb.jit
def generate_random_signals(time_steps, securities, num_signals):
    """生成随机开仓和平仓信号"""
    open_signals = np.zeros((time_steps, securities), dtype=np.int32)
    close_signals = np.zeros((time_steps, securities), dtype=np.int32)
    
    # 生成随机开仓信号
    for _ in range(num_signals):
        t = np.random.randint(0, time_steps)
        s = np.random.randint(0, securities)
        open_signals[t, s] = 1
    
    # 生成随机平仓信号（比开仓信号稍少）
    for _ in range(num_signals // 2):
        t = np.random.randint(0, time_steps)
        s = np.random.randint(0, securities)
        close_signals[t, s] = 1
        
    return open_signals, close_signals

@nb.jit
def create_mock_data(time_steps=2000, securities=50):
    """创建模拟市场数据"""
    # 生成收盘价数据（随机游走模式）
    np.random.seed(42)  # 固定随机种子保证可重复
    base_price = 100.0
    close = np.zeros((time_steps, securities), dtype=np.float64)
    pctchg = np.zeros((time_steps, securities), dtype=np.float64)
    
    # 初始化第一天价格
    for s in range(securities):
        close[0, s] = base_price + np.random.normal(0, 10)
    
    # 生成后续价格和涨跌幅
    for t in range(1, time_steps):
        for s in range(securities):
            # 生成日收益率（正态分布，均值0，标准差2%）
            daily_return = np.random.normal(0, 0.02)
            pctchg[t, s] = daily_return
            close[t, s] = close[t-1, s] * (1 + daily_return)
            
            # 添加一些NaN值模拟停牌
            if np.random.random() < 0.01:  # 1%概率停牌
                close[t, s] = np.nan
                pctchg[t, s] = np.nan
    
    # 生成涨跌停限制（大部分时候不涨跌停）
    limit = np.zeros((time_steps, securities), dtype=np.int32)
    
    # 生成换日标记（每20个时间点算一天，模拟日内多个时间点）
    ifdaychange = np.zeros(time_steps, dtype=np.int32)
    for t in range(0, time_steps, 20):
        if t < time_steps:
            ifdaychange[t] = 1
    
    return close, pctchg, limit, ifdaychange

def test_backtest_function():
    """测试回测函数的完整流程"""
    print("开始测试RuleBackTest函数...")
    
    # 创建测试数据
    time_steps = 2000
    securities = 50
    num_signals = 100
    
    print(f"生成测试数据: {time_steps}个时间点, {securities}个证券, {num_signals}个信号")
    
    # 生成模拟数据
    close, pctchg, limit, ifdaychange = create_mock_data(time_steps, securities)
    
    # 生成随机信号
    np.random.seed(123)  # 固定随机种子
    opensignal, closesignal = generate_random_signals(time_steps, securities, num_signals)
    
    print(f"开仓信号总数: {opensignal.sum()}")
    print(f"平仓信号总数: {closesignal.sum()}")
    
    # 运行回测
    print("开始运行回测...")
    holding, closed_holding, portfolio_pctchg = RunRuleBackTest(
        close=close,
        pctchg=pctchg, 
        limit=limit,
        opensignal=opensignal,
        closesignal=closesignal,
        ifdaychange=ifdaychange,
        maxium_day_holding=5
    )
    
    print("回测完成，开始验证结果...")
    
    # 验证结果
    assert isinstance(holding, list), "当前持仓应该是list类型"
    assert isinstance(closed_holding, list), "已平仓记录应该是list类型" 
    assert isinstance(portfolio_pctchg, list), "组合收益率应该是list类型"
    assert len(portfolio_pctchg) == time_steps, f"组合收益率长度应该等于时间步数: {len(portfolio_pctchg)} vs {time_steps}"
    
    # 验证持仓记录格式
    print(f"当前持仓数量: {len(holding)}")
    if len(holding) > 0:
        sample_holding = holding[0]
        assert len(sample_holding) == 3, f"持仓记录应该包含3个元素: [证券ID, 开仓时间, 持仓天数], 实际: {len(sample_holding)}"
        assert isinstance(sample_holding[0], (int, np.integer, float, np.floating)), "证券ID应该是数字类型"
        assert isinstance(sample_holding[1], (int, np.integer, float, np.floating)), "开仓时间应该是数字类型"
        assert isinstance(sample_holding[2], (int, np.integer, float, np.floating)), "持仓天数应该是数字类型"
        print(f"持仓记录示例: {sample_holding}")
    
    # 验证已平仓记录格式
    print(f"已平仓记录数量: {len(closed_holding)}")
    if len(closed_holding) > 0:
        sample_closed = closed_holding[0]
        assert len(sample_closed) == 6, f"已平仓记录应该包含6个元素: [证券ID, 开仓时间, 持仓天数, 平仓时间, 收益率, 平仓原因], 实际: {len(sample_closed)}"
        assert isinstance(sample_closed[0], (int, np.integer, float, np.floating)), "证券ID应该是数字类型"
        assert isinstance(sample_closed[1], (int, np.integer, float, np.floating)), "开仓时间应该是数字类型"
        assert isinstance(sample_closed[2], (int, np.integer, float, np.floating)), "持仓天数应该是数字类型"
        assert isinstance(sample_closed[3], (int, np.integer, float, np.floating)), "平仓时间应该是数字类型"
        assert isinstance(sample_closed[4], (float, np.floating)), "收益率应该是浮点数"
        assert sample_closed[5] in [1, 2], f"平仓原因应该是1(信号平仓)或2(时间平仓), 实际: {sample_closed[5]}"
        print(f"已平仓记录示例: {sample_closed}")
    
    # 统计分析
    valid_returns = [r for r in portfolio_pctchg if not np.isnan(r)]
    if len(valid_returns) > 0:
        avg_return = np.mean(valid_returns)
        std_return = np.std(valid_returns)
        print(f"组合平均日收益率: {avg_return:.6f}")
        print(f"组合收益率标准差: {std_return:.6f}")
        print(f"有效收益率天数: {len(valid_returns)}/{len(portfolio_pctchg)}")
    
    # 验证平仓原因统计
    if len(closed_holding) > 0:
        close_by_signal = sum(1 for trade in closed_holding if trade[5] == 1)
        close_by_time = sum(1 for trade in closed_holding if trade[5] == 2)
        print(f"信号平仓次数: {close_by_signal}")
        print(f"时间平仓次数: {close_by_time}")
        
        # 计算平均持仓期
        holding_periods = [trade[2] for trade in closed_holding]
        avg_holding_period = np.mean(holding_periods)
        print(f"平均持仓天数: {avg_holding_period:.2f}")
    
    print("✅ 所有测试通过！回测函数工作正常。")
    return True

def performance_test():
    """性能测试"""
    print("\n开始性能测试...")
    import time
    
    # 较大数据集
    time_steps = 2000
    securities = 100
    num_signals = 100
    
    close, pctchg, limit, ifdaychange = create_mock_data(time_steps, securities)
    np.random.seed(456)
    opensignal, closesignal = generate_random_signals(time_steps, securities, num_signals)
    
    start_time = time.time()
    holding, closed_holding, portfolio_pctchg = RunRuleBackTest(
        close=close,
        pctchg=pctchg,
        limit=limit, 
        opensignal=opensignal,
        closesignal=closesignal,
        ifdaychange=ifdaychange,
        maxium_day_holding=5
    )
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"性能测试 - 数据规模: {time_steps}x{securities}, 执行时间: {execution_time:.4f}秒")
    print(f"处理速度: {time_steps * securities / execution_time:.0f} 数据点/秒")

if __name__ == "__main__":
    # 运行基础功能测试
    try:
        test_backtest_function()
        
        # 运行性能测试
        performance_test()
        
        print("\n🎉 所有测试完成！RuleBackTest函数运行正常。")
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()

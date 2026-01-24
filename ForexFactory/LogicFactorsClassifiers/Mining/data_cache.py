import os
import pandas as pd
import pickle
from typing import Tuple, Dict, Any, Optional
import logging

# 设置日志 - 只显示WARNING及以上级别的消息
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

class DataCache:
    """数据缓存管理器，用于缓存期货数据到磁盘并提供快速访问"""
    
    def __init__(self):
        # 项目根目录
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.future_data_dir = os.path.join(self.base_dir, "..", "FutureData")
        
        # 数据级别
        self.levels = ['day', 'min5', 'min15', 'min30', 'min60']
        
        # 数据类型 (包含所有需要缓存的数据类型)
        self.data_types = ['high', 'open', 'low', 'close', 'vol', 'oi']
    
    def _get_csv_path(self, level: str, data_type: str) -> str:
        """获取CSV文件路径"""
        return os.path.join(self.future_data_dir, level, f"{data_type}.csv")
    
    def _get_cache_path(self, level: str, data_type: str) -> str:
        """获取缓存文件路径"""
        return os.path.join(self.future_data_dir, level, f"{data_type}_cache.pkl")
    
    def _is_cache_valid(self, level: str, data_type: str) -> bool:
        """检查缓存是否有效（比原始CSV文件新）"""
        csv_path = self._get_csv_path(level, data_type)
        cache_path = self._get_cache_path(level, data_type)
        
        if not os.path.exists(cache_path):
            return False
        
        if not os.path.exists(csv_path):
            return False
        
        csv_mtime = os.path.getmtime(csv_path)
        cache_mtime = os.path.getmtime(cache_path)
        
        return cache_mtime >= csv_mtime
    
    def _load_csv_data(self, level: str, data_type: str) -> pd.DataFrame:
        """从CSV文件加载数据"""
        csv_path = self._get_csv_path(level, data_type)
        logger.info(f"Loading CSV: {csv_path}")
        return pd.read_csv(csv_path, index_col=[0])
    
    def _save_cache(self, data: pd.DataFrame, level: str, data_type: str) -> None:
        """保存数据到缓存文件"""
        cache_path = self._get_cache_path(level, data_type)
        logger.info(f"Saving cache: {cache_path}")
        
        # 确保目录存在
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        
        with open(cache_path, 'wb') as f:
            pickle.dump(data, f)
    
    def _load_cache(self, level: str, data_type: str) -> pd.DataFrame:
        """从缓存文件加载数据"""
        cache_path = self._get_cache_path(level, data_type)
        logger.info(f"Loading cache: {cache_path}")
        
        with open(cache_path, 'rb') as f:
            return pickle.load(f)
    
    def get_data(self, level: str, data_type: str) -> pd.DataFrame:
        """获取数据，优先从缓存获取，如果缓存无效则重新加载并缓存"""
        if self._is_cache_valid(level, data_type):
            return self._load_cache(level, data_type)
        else:
            # 缓存无效，重新加载并缓存
            data = self._load_csv_data(level, data_type)
            self._save_cache(data, level, data_type)
            return data
    
    def cache_all_data(self) -> None:
        """缓存所有级别的所有数据类型"""
        logger.info("Starting to cache all data...")
        
        for level in self.levels:
            logger.info(f"Caching level: {level}")
            
            # 缓存HOLCVO数据
            holcvo_types = ['high', 'open', 'low', 'close', 'vol', 'oi']
            for data_type in holcvo_types:
                try:
                    csv_path = self._get_csv_path(level, data_type)
                    if os.path.exists(csv_path):
                        data = self._load_csv_data(level, data_type)
                        self._save_cache(data, level, data_type)
                        logger.info(f"Successfully cached {level}/{data_type}")
                    else:
                        logger.warning(f"CSV file not found: {csv_path}")
                except Exception as e:
                    logger.error(f"Error caching {level}/{data_type}: {e}")
        
        logger.info("Finished caching all data!")
    
    def clear_cache(self, level: str = None, data_type: str = None) -> None:
        """清除缓存文件"""
        if level and data_type:
            # 清除特定缓存
            cache_path = self._get_cache_path(level, data_type)
            if os.path.exists(cache_path):
                os.remove(cache_path)
                logger.info(f"Cleared cache: {cache_path}")
        elif level:
            # 清除特定级别的所有缓存
            for dt in self.data_types:
                cache_path = self._get_cache_path(level, dt)
                if os.path.exists(cache_path):
                    os.remove(cache_path)
                    logger.info(f"Cleared cache: {cache_path}")
        else:
            # 清除所有缓存
            for lv in self.levels:
                for dt in self.data_types:
                    cache_path = self._get_cache_path(lv, dt)
                    if os.path.exists(cache_path):
                        os.remove(cache_path)
                        logger.info(f"Cleared cache: {cache_path}")


# 全局缓存实例
_cache_instance = None

def get_cache_instance() -> DataCache:
    """获取全局缓存实例（单例模式）"""
    global _cache_instance
    if _cache_instance is None:
        _cache_instance = DataCache()
    return _cache_instance


def load_HOLCVO_cached(level: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    使用缓存加载HOLCVO数据
    返回: (high, open, low, close, vol, oi)
    """
    cache = get_cache_instance()
    
    high = cache.get_data(level, 'high')
    open_data = cache.get_data(level, 'open')
    low = cache.get_data(level, 'low')
    close = cache.get_data(level, 'close')
    vol = cache.get_data(level, 'vol')
    oi = cache.get_data(level, 'oi')
    
    return high, open_data, low, close, vol, oi


def load_HOLCVO_cached_by_path(path: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    根据路径使用缓存加载HOLCVO数据（兼容原有接口）
    """
    # 从路径中提取级别
    level = os.path.basename(path)
    return load_HOLCVO_cached(level)


if __name__ == "__main__":
    # 缓存所有数据
    cache = get_cache_instance()
    cache.cache_all_data()
    
    # 测试缓存效果
    print("Testing cache...")
    high, open_data, low, close, vol, oi = load_HOLCVO_cached('day')
    print(f"Day close data shape: {close.shape}")
    print(f"Day close data head:\n{close.head()}")
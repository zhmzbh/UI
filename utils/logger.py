import time  # 添加这一行
import logging
import os

# 确保日志目录存在
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 配置日志
log_filename = f"{log_dir}/test_{time.strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%H:%M:%S',
    handlers=[
        logging.StreamHandler(),  # 控制台输出
        logging.FileHandler(log_filename, encoding='utf-8')  # 文件输出
    ]
)

def get_logger():
    """获取日志记录器"""
    return logging.getLogger(__name__)

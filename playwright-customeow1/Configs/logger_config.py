# # logger_config.py
# import logging
# import sys
# from pathlib import Path
#
#
# def configure_logger(name: str, log_level: str = "INFO", log_file: Path = None) -> logging.Logger:
#     """
#     配置日志记录器
#
#     参数：
#     name: 日志器名称（通常为模块名 __name__）
#     log_level: 日志级别（DEBUG/INFO/WARNING/ERROR）
#     log_file: 日志文件路径（可选）
#
#     返回：
#     logging.Logger 实例
#     """
#     logger = logging.getLogger(name)
#     logger.setLevel(log_level)
#
#     # 定义日志格式
#     formatter = logging.Formatter(
#         "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S"
#     )
#
#     # 控制台处理器
#     console_handler = logging.StreamHandler(sys.stdout)
#     console_handler.setFormatter(formatter)
#     logger.addHandler(console_handler)
#
#     # 文件处理器（如果指定了日志文件）
#     if log_file:
#         file_handler = logging.FileHandler(log_file)
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)
#
#     return logger


# configs/logger_config.py
import logging
import sys
from pathlib import Path
from typing import Optional


def configure_logger(
        name: str,
        log_level: str = "INFO",
        log_file: Optional[Path] = None,
        format_str: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
) -> logging.Logger:
    """
    配置并返回一个日志记录器

    参数：
    name (str): 日志记录器名称（通常使用 __name__）
    log_level (str): 日志级别（DEBUG/INFO/WARNING/ERROR）
    log_file (Path): 日志文件路径（可选）
    format_str (str): 日志格式字符串

    返回：
    logging.Logger: 配置好的日志记录器
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # 避免重复添加处理器
    if logger.handlers:
        return logger

    formatter = logging.Formatter(format_str, datefmt="%Y-%m-%d %H:%M:%S")

    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 文件处理器（如果提供了日志文件路径）
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)  # 创建目录
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
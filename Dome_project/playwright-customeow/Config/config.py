import os
import logging
import configparser
from logging.handlers import TimedRotatingFileHandler

# 项目根目录
BASE_PATH = os.path.abspath(os.path.join(os.getcwd(), "."))

class ConfigParser:
    """
    简单封装 configparser，读取配置项
    """
    def __init__(self, file_name: str):
        self.config = configparser.ConfigParser()
        file_path = os.path.join(BASE_PATH, file_name)
        self.config.read(file_path, encoding='utf-8')

    def read_str_value(self, section: str, option: str) -> str:
        return self.config.get(section, option)

    def read_int_value(self, section: str, option: str) -> int:
        return self.config.getint(section, option)

LOG_LEVEL_MAP = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}

class MyLog:
    """
    日志封装类：支持控制台输出 + 文件切割保存
    """
    def __init__(self, name: str = 'root', level: str = 'info'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(LOG_LEVEL_MAP.get(level.lower(), logging.INFO))

        if not self.logger.handlers:
            self._add_stream_handler(level)
            self._add_file_handler(level)

    def _get_formatter(self) -> logging.Formatter:
        fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
        return logging.Formatter(fmt=fmt)

    def _add_stream_handler(self, level: str):
        """ 添加控制台输出 """
        console_handler = logging.StreamHandler()
        console_handler.setLevel(LOG_LEVEL_MAP.get(level.lower(), logging.INFO))
        console_handler.setFormatter(self._get_formatter())
        self.logger.addHandler(console_handler)

    def _add_file_handler(self, level: str):
        """ 添加文件输出（按天切割） """
        log_dir = os.path.join(BASE_PATH, "OutPut", "Log")
        os.makedirs(log_dir, exist_ok=True)
        file_path = os.path.join(log_dir, "product.Log")

        file_handler = TimedRotatingFileHandler(
            filename=file_path,
            when="D",  # 每天切割
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setLevel(LOG_LEVEL_MAP.get(level.lower(), logging.INFO))
        file_handler.setFormatter(self._get_formatter())
        self.logger.addHandler(file_handler)

    def get_log(self) -> logging.Logger:
        return self.logger

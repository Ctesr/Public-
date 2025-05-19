import json
from pathlib import Path


class EnvConfig:
    """环境配置工具类"""

    def __init__(self, env="env_BETA"):
        # 默认环境为 prod，如果没有传入则使用 prod 环境
        self.env = env
        config_path = Path(__file__).parent.parent / "Configs" / "env_config.json"
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def get_base_url(self):
        """根据当前环境获取基础 URL"""
        # 获取当前环境的配置，默认返回 prod 环境的配置
        if self.env not in self.config:
            raise ValueError(f"未找到环境 '{self.env}' 的配置")

        url = self.config[self.env]["base_url"]
        print(f"当前环境: {self.env}, URL: {url}")
        return url

    def set_env(self, env):
        """切换环境"""
        self.env = env

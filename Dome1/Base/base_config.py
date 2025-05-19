from Config.config import ConfigParser

cfg = ConfigParser('config.ini')
browser = cfg.read_str_value('config', 'Browser')
url = cfg.read_str_value('config', 'URL')

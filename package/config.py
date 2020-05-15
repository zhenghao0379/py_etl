# 配置文件获取

import configparser
# 生成ConfigParser对象
config = configparser.ConfigParser()
# 读取配置文件
config_file = r'config\config.ini'
config.read(config_file, encoding='utf-8')

class config_val:
    def __init__(self, config):
        self.config = config

    def get_value(self, p):
        self.config.GetInteger(p)

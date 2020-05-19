# 配置文件获取

import configparser

# # 生成ConfigParser对象
# config = configparser.ConfigParser()
# # 读取配置文件
# config_file = r'config\config.ini'
# config.read(config_file, encoding='utf-8')

class CONFIG:
    def __init__(self, config_file_path=r'config\config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path, encoding='utf-8')

    def get_value(self, section, item):
        return self.config.get(section, item)

    def get_value(self, section, item):
        return self.config.get(section, item)


CONFIG = CONFIG()

import configparser
# 生成ConfigParser对象
config = configparser.ConfigParser()
# 读取配置文件
config_file = r'config\config.ini'
config.read(config_file, encoding='utf-8')

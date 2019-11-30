# 环境文件

# 载入工具包
import numpy as np
import pandas as pd
import mysql.connector
import pymongo
import datetime


# 公共函数
import source.public_fun
import source.sql_connect


# 全局变量
# 时间
DATE = datetime.datetime.now().strftime("%Y-%m-%d")
print("DATE:",DATE)
DATETIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("DATETIME:",DATETIME)
import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../../'))

print(sys.path)

# import pandas as pd
# 全局变量 与 自定义函数
from package.env import *
from package.source.sql_connect import mysql_on

conn = mysql_on("tinydata","sakila")

print(conn)

data = pd.read_sql("select * from film", conn)

print(data.head())

print(DATE)

data.to_sql()

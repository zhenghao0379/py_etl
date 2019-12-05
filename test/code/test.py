import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../../'))

# import pandas as pd
# 全局变量 与 自定义函数
from package.env import *
from package.source.sql_connect import mysql_on
from package.source.sql_connect import mysql_engine

conn = mysql_engine("tinydata","sakila")
conn1 = mysql_engine("tinydata","test")

import pandas as pd


for day in DAYS:
    for rpt_type in RPT_TYPES:

        data = pd.read_sql("select * from film", conn)

        data.to_sql("film",conn1,if_exists="append",index=False)

        data.dtypes

        data["last_update2"] = pd.to_datetime(data["last_update"], format='%Y-%m-%d %H:%m:%s')

# 定位到工作根目录
import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../../'))

# 载入工具包和自定义工具包
import numpy as np
import pandas as pd

from package.env import *
from package.source.sql_connect import *

# 获取连接
dev()
conn, engine = mysql_on("sakila")

# sql
df_address = pd.read_sql("select * from address", engine).drop(['last_update'],axis=1)
df_city = pd.read_sql("select * from city", engine).drop(['last_update'],axis=1)
df_country = pd.read_sql("select * from country", engine).drop(['last_update'],axis=1)

df_address["location_text"] = df_address["location"]
df_address["lat"] = df_address["location_text"].
df_address["lng"] = df_address["location_text"].

# 载入数据
df_data = df_address.merge(df_city, how="left", on="city_id")
df_data_2 = df_data.merge(df_country, how="left", on="country_id")

# 载入数据
conn, engine = mysql_on("test")
mysql_upload(df_data_2,"dim_address",conn,engine,type="r")

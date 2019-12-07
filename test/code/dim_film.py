# 定位到工作目录
import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../..'))

# 载入工具包和自定义工具包
import numpy as np
import pandas as pd
from package.env import *
from package.source.sql_connect import *

# 获取连接
test()
conn, engine = mysql_on("sakila")

# sql
sql = "select * from film".format_map(vars())

# 
df_data = pd.read_sql(sql, engine)

print(df_data.head())

# 载入数据
conn, engine = mysql_on("sakila")
# df_data.to_sql("",engine)


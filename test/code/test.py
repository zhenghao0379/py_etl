import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../..'))

# import pandas as pd
# 全局变量 与 自定义函数
import pandas as pd
from package.env import *
from package.source.sql_connect import *

dev()
conn,engine = mysql_on("sakila")

for day in DAYS:
    for rpt_type in RPT_TYPES:

        print(day)

        print(rpt_type)

        # sql = "select * from {table} where day = '{day}' and rpt_type='{RPT_TYPE}'"

        # data = pd.read_sql(sql, conn)

        # data.to_sql("film",conn,if_exists="append",index=False)

        # data.dtypes

        # data["last_update2"] = pd.to_datetime(data["last_update"], format='%Y-%m-%d %H:%m:%s')

a = "R"
a == "R" or "r"
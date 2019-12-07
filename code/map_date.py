# 生成日期


import pandas as pd
import datetime as dt

from package.env import *
from package.source.sql_connect import *

# 
df_index = pd.date_range(dt.date(2010,1,1),dt.date(2030,1,1))

df_date = pd.DataFrame()

df_date["date"] = df_index.strftime("%F")
df_date["year"] = df_index.strftime("%Y")
df_date["month"] = df_index.strftime("%m")
df_date["day"] = df_index.strftime("%d")
df_date["week"] = df_index.strftime("%w")
df_date["week"] = df_date["week"].replace("0", "7")
df_date["month_full_name"] = df_index.strftime("%B")
df_date["month_short_name"] = df_index.strftime("%b")
df_date["week_full_name"] = df_index.strftime("%A")
df_date["week_short_name"] = df_index.strftime("%a")

# 审核周期 上周五到本周四，返回本周日
df_date["dt_date"] = (df_index + dt.timedelta(3)).shift(0,freq="w").strftime("%F")

df_date["upload_time"] = DATETIME

# 载入数据
dev()
conn, engine = mysql_on("test")



# 
cursor = conn.cursor()
sql = "DELETE FROM map_date"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

df_date.to_sql("map_date",engine,if_exists="append",index=False)
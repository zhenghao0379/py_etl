import pandas as pd
import pymysql
import sqlalchemy
from package.env import DATETIME

# 定义连接的全局变量
CONNS = ""
MYSQL_USER = ""
CONN = ""
ENGINE = ""

# 测试环境
def test():
    global CONNS
    db = pd.read_csv("config/db.csv")
    CONNS = db.loc[db['state']=='test']
    print("it is test env now!")
# 正式环境
def dev():
    global CONNS
    db = pd.read_csv("config/db.csv")
    CONNS = db.loc[db['state']=='dev']
    print("it is dev env now!")

# 选择数据库
def mysql_on(db_name="test"):
    global CONNS,MYSQL_USER,CONN,ENGINE
    MYSQL_USER = {
        "host":CONNS.loc[CONNS["db_name"] == db_name,"host"].item(),
        "port":CONNS.loc[CONNS["db_name"] == db_name,"port"].item(),
        "user":CONNS.loc[CONNS["db_name"] == db_name,"user"].item(),
        "password":CONNS.loc[CONNS["db_name"] == db_name,"password"].item(),
        "db_name":db_name
    }
    mysql_user = MYSQL_USER
    # CONN
    CONN = pymysql.connect(
        host=mysql_user["host"],
        user=mysql_user["user"],
        passwd=mysql_user["password"],
        database=db_name,
        charset='utf8'
    )
    print(CONN)
    # ENGINE
    url = "mysql+pymysql://"+ str(mysql_user["user"]) +":"+ str(mysql_user["password"]) +"@"+ str(mysql_user["host"])+":"+ str(mysql_user["port"]) +"/"+ db_name + "?charset=utf8"
    print(url)
    ENGINE = sqlalchemy.create_engine(url,echo=False,encoding='utf-8')
    print(ENGINE)



# 获取数据
def mysql_download(table_name,sql,day,rpt_type):
    global CONN
    sql = "select * from where day = {day} and rpt_type = {rpt_type}"

    df_data = pd.read_sql(sql,CONN)

    return df_data


# 载入数据
def mysql_upload(df,talbe_name,conn,if_exists="append"):

    if (if_exists == "replace"):
        # 先清空表

        df.to_sql(talbe_name,conn,if_exists="append")
    else:
        df.to_sql(talbe_name,conn,if_exists="append")

    return print("success")

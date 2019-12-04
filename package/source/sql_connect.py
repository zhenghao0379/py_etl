import pandas as pd
import mysql.connector
import pymysql
import sqlalchemy


# Mysql
# 创建链接
def mysql_on(name, db_name = "sakila"):
    # 选择账户
    db = pd.read_csv("config/db.csv")
    mysql_user = {
        "host":db.loc[db["name"] == name,"host"].item(),
        "port":db.loc[db["name"] == name,"port"].item(),
        "user":db.loc[db["name"] == name,"name"].item(),
        "password":db.loc[db["name"] == name,"password"].item(),
    }
    print(mysql_user)
    print(db_name)
    # 选择数据库
    conn = mysql.connector.connect(
        host=mysql_user["host"],
        user=mysql_user["user"],
        passwd=mysql_user["password"],
        database=db_name
    )
    return conn

def mysql_engine(name, db_name="sakila"):
    # 选择账户
    db = pd.read_csv("config/db.csv")
    mysql_user = {
        "host":db.loc[db["name"] == name,"host"].item(),
        "port":db.loc[db["name"] == name,"port"].item(),
        "user":db.loc[db["name"] == name,"name"].item(),
        "password":db.loc[db["name"] == name,"password"].item(),
    }
    print(mysql_user)
    url = "mysql+pymysql://"+ str(mysql_user["user"]) +":"+ str(mysql_user["password"]) +"@"+ str(mysql_user["host"])+":"+ str(mysql_user["port"]) +"/"+ db_name + "?charset=utf8"
    print(url)
    engine = sqlalchemy.create_engine(url,echo=False,encoding='utf-8')

    return engine

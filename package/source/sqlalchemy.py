import sqlalchemy
import pymysql

url = "mysql+pymysql://tinydata:3990240Zz.@192.168.23.3:3306/sakila?charset=utf8"

engine = sqlalchemy.create_engine(url,echo=False,encoding='utf-8')


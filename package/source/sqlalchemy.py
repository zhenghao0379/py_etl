import sqlalchemy
import pymysql

url_sakila = "mysql+pymysql://tinydata:3990240Zz.@192.168.23.3:3306/sakila?charset=utf8"
url_test = "mysql+pymysql://tinydata:3990240Zz.@192.168.23.3:3306/test?charset=utf8"

engine = sqlalchemy.create_engine(url_test,echo=True,encoding='utf-8')

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

from sqlalchemy.ext.declarative import declarative_base

# 创建基础类
BaseModel = declarative_base()

sqlalchemy.__version__
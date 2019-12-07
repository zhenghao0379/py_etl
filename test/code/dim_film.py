import numpy as np
import pandas as pd

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../..'))
print(sys.path)

from package.env import *
from package.source.sql_connect import *

dev()
mysql_on("sakila")

print(CONN)
print(ENGINE)

table = "film"
sql2 = "select * from {table}".format_map(vars())
print(sql2)

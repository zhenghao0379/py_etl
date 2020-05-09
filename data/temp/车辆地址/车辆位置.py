# 定位到工作根目录
import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../../'))

# 载入工具包和自定义工具包
import numpy as np
import pandas as pd

data = pd.read_excel('')


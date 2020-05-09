# 终端执行传递参数 apgparse
# 官方快速文档：https://docs.python.org/zh-cn/3/howto/argparse.html
# 官方详细文档：https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse
# 文档： https://pymotw.com/3/argparse/index.html#module-argparse

# 终端执行
# D:
# cd 

import argparse
import datetime

def get_DAYS(start, end):
    start = datetime.datetime.fromisoformat(start)
    end = datetime.datetime.fromisoformat(end)

    days = [start + datetime.timedelta(days=x) for x in range((end-start).days + 1)]
    days = [i.strftime("%F") for i in days]

    return days

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-D', '--DAYS', help='运行日期，默认为昨天')
parser.add_argument('-S', '--START', help='起始日期，默认为昨天')
parser.add_argument('-E', '--END', help='终止日期，默认为昨天')
parser.add_argument('-T', '--RPT_TYPE', help='循环周期类型')

args = parser.parse_args()

yesterday = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%F")

if args.DAYS:
    DAYS = args.DAYS.split(',')
else:
    DAYS = [yesterday]

if args.START:
    START = args.START
else:
    START = yesterday

if args.END:
    END = args.START
else:
    END = yesterday

if START < min(DAYS):
    DAYS = get_DAYS(START, END)

if args.RPT_TYPE:
    RPT_TYPE = list(args.RPT_TYPE)
else:
    RPT_TYPE = ['D']

print('DAYS =', DAYS)
print('START =', START)
print('END =', END)
print('RPT_TYPE =', RPT_TYPE)
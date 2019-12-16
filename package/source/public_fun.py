import numpy as np
import pandas as pd
import datetime

# 百度地图API 从经纬度获取省市区
import requests
# AK = "eCMzKQzCMnunc3R9Gt1gGMQsL0R5PqpV"
def get_address_api(lng, lat, *AK):
    AK = "eCMzKQzCMnunc3R9Gt1gGMQsL0R5PqpV"
    url = "http://api.map.baidu.com/reverse_geocoding/v3/?"
    ak = "ak=" + AK
    output = "&output=json"
    coordtype = "&coordtype=wgs84ll"
    location = "&location=" + str(lat) + "," + str(lng)
    
    url_all = url + ak + output + coordtype + location
    print(url_all)
    
    response = requests.get(url = url_all)
    
    if response.status_code == 200:
        try:
            # time.sleep(0.25)
            output = response.json()
            return output
        except Exception as e:
            print("Exception in amp_geocode",e)
            # time.sleep(5)
            return None
    else:
        print("========>", response.status_code)
        # time.sleep(5)
        return None

def get_day_start_end(day, rpt_type):
    day = datetime.datetime.strptime(day, "%Y-%m-%d")
    start = {
        "D":day.strftime("%F"),
        "W":(day+pd.tseries.offsets.MonthBegin).strftime("%F"),
        "M":day.shift(0,freq="m").strftime("%F"),
        "Y":day.shift(0,freq="y").strftime("%F"),
    }.get(rpt_type,"error")

    end = {
        "D":day.strftime("%F"),
        "W":day.shift(0,freq="w").strftime("%F"),
        "M":day.shift(0,freq="m").strftime("%F"),
        "Y":day.shift(0,freq="y").strftime("%F"),
    }.get(rpt_type,"error")
    return start, end

start, end = get_day_start_end("2019-12-12", "D")
print(start)
print(end)
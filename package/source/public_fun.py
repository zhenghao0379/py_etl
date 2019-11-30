# 百度地图API 从经纬度获取省市区
AK = "eCMzKQzCMnunc3R9Gt1gGMQsL0R5PqpV"

def get_city_api(AK, lng, lat):
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
            time.sleep(5)
            return None
    else:
        print("========>", response.status_code)
        time.sleep(5)
        return None
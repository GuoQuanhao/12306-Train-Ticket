import requests
import re
import os


# 获取地名信息
def getStation():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9142'
    response = requests.get(url, verify=True)
    # 返回中文与大写字母
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    stations = dict(stations)
    stations = str(stations)
    write(stations)


# 站点文件写入
def write(item):
    with open('stations.txt', 'w', encoding='utf-8') as f:
        f.write(item)


# 站点文件读取
def read():
    with open('stations.txt', 'r', encoding='utf-8') as f:
        data = f.readline()

    return data


# 判断站点文件是否存在
def isStations():
    isStations = os.path.exists('stations.txt')

    return isStations
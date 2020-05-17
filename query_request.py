from get_stations import *


'''5-7目的地，3车次，6出发地，8出发时间，9到达时间，10历时，26无坐，29硬座，
   24软座，28硬卧，33动卧，23软卧，21高级软卧，30二等座，31一等座，32商务座特等座
'''

data = []  # 用于保存整理好的所有车次信息
type_data = []  # 保存车次分类后最后的数据


def query(date, from_station, to_station):
    print(date, from_station, to_station)
    data.clear()  # 清空数据
    type_data.clear()  # 清空车次分类保存的数据
    # 设置cookie
    cookie = 'JSESSIONID=245782306A8F72B197AE2ADA05F463A8; BIGipServerotn=1708720394.50210.0000; RAIL_EXPIRATION=1589844843366; RAIL_DEVICEID=R0B-jSpnTZ4NSWa2MVZNuBUvmwAoHG22Rqb8eQm0qu7ZUWdpbKElaHY3oqEUR8AG2ooarmYVW3kNP98Lkhn5YqoPa5KUUB8IMjRdPEZ-iZbqgyh-gOFgMNRRpieZq3GBI36yzGkOErVsDyR9NWWrDJY_EThOSJ5f; BIGipServerpassport=921174282.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_fromStation=%u5317%u4EAC%2C{}; _jc_save_toStation=%u4E0A%u6D77%2C{}; _jc_save_fromDate={}; _jc_save_toDate={}; _jc_save_wfdc_flag=dc'.format(
        from_station, to_station, date, date)
    # 设置标头
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
        'Cookie': cookie}
    # 查询请求地址
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station)
    # 发送查询请求
    response = requests.get(url, headers=headers)
    # 修改编码格式
    response.encoding = 'utf-8'
    # 将json数据转换为字典类型，通过键值对取数据
    result = response.json()
    result = result['data']['result']
    # 判断车站文件是否存在
    if isStations() == True:
        # 读取所有车站并转换为dic类型，eval()获取字符串值
        stations = eval(read())
        if len(result) != 0:  # 判断返回数据是否为空
            for i in result:
                # 分割数据并添加到列表中
                tmp_list = i.split('|')
                # 因为查询结果中出发站和到达站为站名的缩写字母，所以需要在车站库中找到对应的车站名称
                from_station = list(stations.keys())[list(stations.values()).index(tmp_list[6])]
                to_station = list(stations.keys())[list(stations.values()).index(tmp_list[7])]
                # 创建座位数组，由于返回的座位数据中含有空既“”，所以将空改成--这样好识别
                seat = [tmp_list[3], from_station, to_station, tmp_list[8], tmp_list[9], tmp_list[10]
                    , tmp_list[32], tmp_list[31], tmp_list[30], tmp_list[21]
                    , tmp_list[23], tmp_list[33], tmp_list[28], tmp_list[24], tmp_list[29], tmp_list[26]]
                newSeat = []
                # 循环将座位信息中的空改成--
                for s in seat:
                    if s == "":
                        s = "--"
                    else:
                        s = s
                    newSeat.append(s)  # 保存新的座位信息
                data.append(newSeat)
        return data   # 返回整理好的车次信息


# 获取高铁信息的方法
def g_vehicle():
    if len(data) != 0:
        for g in data:  # 循环所有火车数据
            i = g[0].startswith('G')  # 判断车次首字母是不是高铁
            if i:  # 如果是将该条信息添加到高铁数据中
                type_data.append(g)


# 移除高铁信息的方法
def r_g_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for g in data:
            i = g[0].startswith('G')
            if i:  # 移除高铁信息
                type_data.remove(g)


# 获取动车信息的方法
def d_vehicle():
    if len(data) != 0:
        for d in data:  # 循环所有火车数据
            i = d[0].startswith('D')  # 判断车次首字母是不是动车
            if i == True:  # 如果是将该条信息添加到动车数据中
                type_data.append(d)


# 移除动车信息的方法
def r_d_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for d in data:
            i = d[0].startswith('D')
            if i == True:  # 移除动车信息
                type_data.remove(d)


# 获取直达车信息的方法
def z_vehicle():
    if len(data) != 0:
        for z in data:  # 循环所有火车数据
            i = z[0].startswith('Z')  # 判断车次首字母是不是直达
            if i == True:  # 如果是将该条信息添加到直达数据中
                type_data.append(z)


# 移除直达车信息的方法
def r_z_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for z in data:
            i = z[0].startswith('Z')
            if i == True:  # 移除直达车信息
                type_data.remove(z)


# 获取特快车信息的方法
def t_vehicle():
    if len(data) != 0:
        for t in data:  # 循环所有火车数据
            i = t[0].startswith('T')  # 判断车次首字母是不是特快
            if i == True:  # 如果是将该条信息添加到特快车数据中
                type_data.append(t)


# 移除特快车信息的方法
def r_t_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for t in data:
            i = t[0].startswith('T')
            if i == True:  # 移除特快车信息
                type_data.remove(t)


# 获取快速车数据的方法
def k_vehicle():
    if len(data) != 0:
        for k in data:  # 循环所有火车数据
            i = k[0].startswith('K')  # 判断车次首字母是不是快车
            if i == True:  # 如果是将该条信息添加到快车数据中
                type_data.append(k)


# 移除快速车数据的方法
def r_k_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for k in data:
            i = k[0].startswith('K')
            if i == True:  # 移除快车信息
                type_data.remove(k)
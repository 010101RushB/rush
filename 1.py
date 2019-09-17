import re
import json
import os

province_zhixia = ['北京', '天津', '上海', '重庆']

def get_phone(can):
    ret = re.search(r'\d{11}', can)
    if ret == None:
        return ""
    else:
        return ret.group(0)


def get_province(can):
    if(can[0:2] in province_zhixia):
        ret = can[0:2]
        return ret
    else:
        if(re.search(("(.*?省)|(.*?自治区)"), can) != None):
            ret = re.search(("(.*?省)|(.*?自治区)"), can)
        else:
            if(can[0:3] == "黑龙江"):
                return "黑龙江"
            else:
                return (can[0:2])
    return ret.group(0)


def get_city(can):
    if(re.search(".*?市", can) != None):
        return (re.search(".*?市", can)).group(0)
    else:
        return ''


def get_qu(can):
    if(re.search(("(.*?区)|(.*?县)|(.*?区)"), can) != None):
        return (re.search(("(.*?区)|(.*?县)|(.*?区)"), can)).group(0)
    else:
        return ''


def get_zheng(can):
    if(re.search(("(.*?街道)|(.*?镇)|(.*?乡)"), can) != None):
        return (re.search(("(.*?街道)|(.*?镇)|(.*?乡)"), can)).group(0)
    else:
        return ''


def get_lu(can):
    if(re.search(".*?路", can) != None):
        return (re.search(".*?路", can)).group(0)
    else:
        return ''


def get_hao(can):
    if(re.search(".*?号", can) != None):
        return (re.search(".*?号", can)).group(0)
    else:
        return ''

shuru = input()
flag = shuru[0]
ans = {}
place = []
sp = shuru.split(',')
ans['姓名'] = sp[0][2:4]  # 导出姓名
res = sp[1]
phone = get_phone(res)
res = res.replace(phone, '')
ans['电话'] = phone
province = get_province(res)  # 导出省
l = len(province)
if(res[0:2] in province_zhixia or l >= 5):
    province_t = province
else:
    if(province[-1] != '省'):
        province_t = province + '省'
    else:
        province_t = province
place.append(province_t)
if(res[0:2] not in province_zhixia):
    res = res.replace(province, '')
city = get_city(res)  # 导出市
place.append(city)
res = res.replace(city, '')
qu = get_qu(res)  # 导出区/县/县级市
place.append(qu)
res = res.replace(qu, '')
zheng = get_zheng(res)  # 导出街道/镇/乡
place.append(zheng)
res = res.replace(zheng, '')
if(flag != '1'):
    lu = get_lu(res)  # 导出路
    place.append(lu)
    res = res.replace(lu, '')
    hao = get_hao(res)  # 导出门牌号
    place.append(hao)
    res = res.replace(hao, '')
place.append(res)
ans['地址'] = place
# print(res)
# print(place)
# print(province)
print(ans)

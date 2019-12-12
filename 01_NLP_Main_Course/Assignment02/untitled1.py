# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:27:11 2019

@author: yihua
"""

from urllib import parse
import json
import requests

def get_geo(loc='中关村'):
    '''
    输入一个地理位置，返回百度地图中搜索该位置的排第一的地理坐标
    '''
    queryUrl = "http://api.map.baidu.com/"
    queryParams = {
      "qt": "s",
      "c": "131",
      "wd": "",
      "rn": "10",
      "ie": "utf-8",
      "oue": "1",
      "fromproduct": "jsapi",
      "res": "api",
      "callback": "",
      "ak": "E4805d16520de693a3fe707cdc962045"
    }
    queryHeaders = {
      "Host": "api.map.baidu.com",
      "Connection": "keep-alive",
      "Sec-Fetch-Mode": "no-cors",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
      "Accept": "*/*",
      "Sec-Fetch-Site": "cross-site",
      "Referer": "http://api.map.baidu.com/lbsapi/getpoint/index.html",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    }
    queryParams['wd'] = parse.quote(loc)
    a = requests.get(queryUrl, params=queryParams, headers=queryHeaders)
    a = json.loads(a.text)
    return a['content'][0]['x']/100, a['content'][0]['y']/100


def get_bus_uid(bus='308路 苏州'):
    '''
    输入一个公交线路，返回该线路的uid，供后面使用
    '''
    queryUrl = "https://map.baidu.com/"
    queryParams = {
      "newmap": "1",
      "reqflag": "pcmap",
      "biz": "1",
      "from": "webmap",
      "da_par": "direct",
      "pcevaname": "pc4.1",
      "qt": "s",
      "da_src": "searchBox.button",
      "wd": bus,
      "c": "224",
      "src": "0",
      "wd2": "",
      "pn": "0",
      "sug": "0",
      "l": "13",
      "biz_forward": "{%22scaler%22:2,%22styles%22:%22pl%22}",
      "sug_forward": "",
      "auth": "Rf9AJZYfFDcVLNWKOA0AKFgcvV4D7XOEuxHNzEzETNztDpnSCE%40%40By1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3Guxtdw8E62qvOuUbNB9AUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVteuztghxehwzJPBGBGVJ4vtx77IbHzeeaCE",
      "device_ratio": "2",
      "tn": "B_NORMAL_MAP",
      "nn": "0",
      "u_loc": "13441417,3646685",
      "ie": "utf-8",
      "t": "1572424978726"
    }
    queryHeaders = {
      "Host": "map.baidu.com",
      "Connection": "keep-alive",
      "Upgrade-Insecure-Requests": "1",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
      "Sec-Fetch-Mode": "navigate",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
      "Sec-Fetch-Site": "none",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6"
    }
    
    a = requests.get(queryUrl, params=queryParams, headers=queryHeaders)
    b = a.url
    a = json.loads(a.text)
    return a['content'][0]['name'], a['content'][0]['uid'], b

def get_bus_stations(bus='308路 苏州'):
    '''
    输入一条公交，自动获取uid，然后进一步获取该公交的路线信息
    '''
    url = "http://map.baidu.com/"
    p = {
      "qt": "bsl",
      "tps": "",
      "newmap": "1",
      "uid": get_bus_uid(bus=bus)[1],
      "c": "224"
    }
    hd = {
      "Host": "map.baidu.com",
      "Connection": "keep-alive",
      "Sec-Fetch-Mode": "cors",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
      "Accept": "*/*",
      "Sec-Fetch-Site": "same-origin",
      "Referer": "https://map.baidu.com/search/"+parse.quote(bus)+"/@13418480.824453374,3647843.66,13.6z?querytype=s&da_src=shareurl&wd="+parse.quote(bus)+"&c=224&src=0&pn=0&sug=0&l=13&b=(13402217.399630222,3640199.003279743;13434744.249276526,3655488.3167202575)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&device_ratio=2",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
    }
    b = requests.get(url, params=p, headers=hd)
    b = json.loads(b.text)
    return b['content'][0]['stations']
    

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2017/3/21'
# ----------Dragon be here!----------
              ┏━┓      ┏━┓
            ┏━┛ ┻━━━━━━┛ ┻━━┓
            ┃       ━       ┃
            ┃  ━┳━┛   ┗━┳━  ┃
            ┃       ┻       ┃
            ┗━━━┓      ┏━━━━┛
                ┃      ┃神兽保佑
                ┃      ┃永无BUG！
                ┃      ┗━━━━━━━━━┓
                ┃                ┣━┓
                ┃                ┏━┛
                ┗━━┓ ┓ ┏━━━┳━┓ ┏━┛
                   ┃ ┫ ┫   ┃ ┫ ┫
                   ┗━┻━┛   ┗━┻━┛
"""
import requests

# 1.登录页面获取cookies
Get_cookies = requests.get("http://dig.chouti.com/help/service")
# 2.用户登录，携带上一次的cookies，后台对cookies中的gpsd进行授权
Login = requests.post(
	url = "http://dig.chouti.com/login",
	data = {
		'phone':"86手机号",
		'password':"密码",
		'oneMonth':""
	},
	cookies = Get_cookies.cookies.get_dict()
)

# 3.点赞（只需要已被授权的gpsd即可）
gpsd = Get_cookies.cookies.get_dict()['gpsd']
Dianzan = requests.post(
	url = "http://dig.chouti.com/link/vote?linksId=109",
	cookies = {'gpsd':gpsd}
)

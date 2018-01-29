#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2018/1/29'
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
from wsgiref.simple_server import make_server

def return_index():
	f = open('../index.html',mode='rb')
	data = f.read()
	f.close()

	return [data,]

def return_date():
	return ['<h1>hello date</h1>'.encode('utf-8')]

URL_DICT={
	"/index": return_index,
	"/date": return_date,}

def RunServer(environ,start_response):

	#返回html
	# start_response封装返回给客户的数据，响应头状态
	start_response('200 OK', [('Content-Type', 'text/html')])
	#environ客户发来的数据
	current_url = environ['PATH_INFO']
	func = None
	if current_url in URL_DICT:
		func= URL_DICT[current_url]
	if func:
		return func()
	else:
		return ['<h1>404</h1>'.encode('utf-8')]

	# 第三种方式，如果url过多，依然在编写dict的时候有很大工作量，一般就涉及到使用正则来编写，比如分页
	#URL_DICT = {"/index\d+": return_index,"/date": return_date, }



if __name__ == '__main__':
	httpd = make_server('',8000,RunServer)
	print('Serving Http on port 8000')
	httpd.serve_forever()
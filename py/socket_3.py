#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2018/1/25'
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
	return ['<h1>hello index</h1>'.encode('utf-8')]

def return_date():
	return ['<h1>hello date</h1>'.encode('utf-8')]

URL_DICT={
	"/index": return_index,
	"/date": return_date,}

def RunServer(environ,start_response):
	# #第一种方式
	# # start_response封装返回给客户的数据，响应头状态
	# start_response('200 OK', [('Content-Type', 'text/html')])
	# #environ客户发来的数据
	# if environ['PATH_INFO']=='/index':
	# 	return ['<h1>hello index</h1>'.encode('utf-8')]
	# elif environ['PATH_INFO']=='/date':
	# 	return ['<h1>hello date</h1>'.encode('utf-8')]
	# else:
	# 	return ['<h1>404</h1>'.encode('utf-8')]

	# #第二种方式，将方法绑定到return上
	# # start_response封装返回给客户的数据，响应头状态
	# start_response('200 OK', [('Content-Type', 'text/html')])
	# #environ客户发来的数据
	# current_url = environ['PATH_INFO']
	# if current_url == '/index':
	# 	return return_index()
	# elif current_url == '/date':
	# 	return return_date()
	# else:
	# 	return ['<h1>404</h1>'.encode('utf-8')]

	#第三种方式，更加进化，因为如果有成百上千的url，不能去写那么多elif，所以讲方法放到一个dict映射中。
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
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2018/1/24'
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

# python2.7
from wsgiref.simple_server import make_server

def RunServer(environ,start_response):
	#environ客户发来的数据
	#start_response封装返回给客户的数据，响应头状态
	start_response('200 OK',[('Content-Type','text/html')])
	return '<h1>hello web</h1>'


if __name__ == '__main__':
	httpd = make_server('',8000,RunServer)
	print 'Serving Http on port 8000'
	httpd.serve_forever()
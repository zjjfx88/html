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


import socket

def handle_request(clinet):
	buf = clinet.recv(1024)
	clinet.send("HTTP/1.1 200 OK\r\n\r\n")
	clinet.send("hello world")


def main():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('localhost',8000))
	sock.listen(5)

	while True:
		connection,address = sock.accept()
		handle_request(connection)
		connection.close()

if __name__ == '__main__':
	main()

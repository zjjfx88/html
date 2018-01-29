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
#python2
import hashlib
#python2中的写法
m= hashlib.md5()
m.update('fffff')
ret = m.hexdigest()
print(ret)

#python3中如果还是上述代码则会报错，需要修改如下，不能直接传字符串，因为没有unicode
import hashlib
m= hashlib.md5()
#三种方式
#1.info=b'fffff'
#2.info=bytes('fffff',coding='utf-8')
#3.info='fffff'.encode('utf-8')
m.update(info)
ret = m.hexdigest()
print(ret)
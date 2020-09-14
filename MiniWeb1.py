"""
版本：1-显示固定页面
日期：2020年9月14日
作者：王铭东
email：dong4716138@163.com
运行本版本的命令：gunicorn -w 1 -b 127.0.0.1:8080 MiniWeb1:application
"""

import time


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response(status.encode("utf-8"), response_headers)
    response = '欢迎来到到真正的MiniWeb框架，当前时间是： %s' % time.ctime()
    return [response.encode("utf-8")]

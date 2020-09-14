"""
版本：2-获取指定页面（添加模板的操作）
日期：2020年9月14日
作者：王铭东
email：dong4716138@163.com
运行本版本的命令：gunicorn -w 1 -b 127.0.0.1:8080 MiniWeb2:application
"""

import time

# 配置模板文件路径
TEMPLATES_ROOT = "./templates/"
# 配置资源的路径
RESOURCE_ROOT = "./static/"


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response(status.encode("utf-8"), response_headers)
    response = '欢迎来到到真正的MiniWeb框架，当前时间是： %s' % time.ctime()

    # 打印测试传递过来的信息
    # print("environ--->", environ.keys())  # 打印WSGI协议传递过来的字典信息
    # 获取文件名字
    file_name = environ['PATH_INFO']  # 这里就是浏览器输入网址中的path，例如 http://127.0.0.1:8080/index.html，此时就是/index.html
    print("请求的path--->", file_name)

    try:
        if file_name.endswith(".html"):
            file_root_path = TEMPLATES_ROOT
        else:
            file_root_path = RESOURCE_ROOT

        with open(file_root_path + file_name, "r") as f:
            response = f.read()
    except Exception as ret:
        response = "%s" % ret

    return [response.encode("utf-8")]

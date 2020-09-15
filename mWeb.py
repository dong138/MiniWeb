"""
作者：王铭东
email：dong4716138@163.com
运行本版本的命令：gunicorn -w 1 -b 127.0.0.1:8080 mWeb:application
"""
import sys

from distutils import dirname
from os.path import abspath

# 配置视图函数存放的路径
VIEWS_ROOT = "app.views"


def application(environ, start_response):
    # 获取path info
    file_name = environ['PATH_INFO']  # 这里就是浏览器输入网址中的path，例如 http://127.0.0.1:8080/index.html，此时就是/index.html
    print("请求的path--->", file_name)

    # 设置app路径为可以直接import的路径
    sys.path.append(dirname(abspath(__file__)) + "/app")
    # 如下代码实现了"路由表"的制作
    views = __import__(VIEWS_ROOT)

    # 导入路由表
    from MiniWeb.route import URL_FUNC
    print("路由表--->", URL_FUNC)

    try:
        # 根据"路由表"，调用对应的视图函数
        response = URL_FUNC[file_name]()
        status = '200 OK'
    except Exception as ret:
        status = '404 NOT FOUND'
        response = "我是404页面<br>您访问的页面不存在，请检查URL或者路由装饰是否正确"

    # 回调服务器函数，设置response header
    response_headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)

    # 将response body返回
    return [response.encode("utf-8")]

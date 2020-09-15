"""
作者：王铭东
email：dong4716138@163.com
运行本版本的命令：gunicorn -w 1 -b 127.0.0.1:8080 mWeb:application
"""
import sys

from distutils import dirname
from os.path import abspath

from configobj import ConfigObj
from MiniWeb.utils import G_MINIWEB  # 这全局变量用来存放相关的配置、浏览器等信息


def application(environ, start_response):
    config = ConfigObj("alembic.ini", encoding='UTF8')

    # 将配置的URL驱动添加到对象中
    G_MINIWEB.sqlalchemy_url = config['alembic']['sqlalchemy.url']
    # 将服务器传递归来的参数字添加到对象中
    G_MINIWEB.env = environ

    # 获取path info
    file_name = environ['PATH_INFO']  # 这里就是浏览器输入网址中的path，例如 http://127.0.0.1:8080/index.html，此时就是/index.html
    print("请求的path--->", file_name)

    # 设置app路径为可以直接import的路径
    sys.path.append(dirname(abspath(__file__)) + "/app")
    # 如下代码实现了"路由表"的制作
    views_root = "app.views"  # 配置视图函数存放的路径
    views = __import__(views_root)

    # 导入路由表
    from MiniWeb.route import URL_FUNC
    print("路由表--->", URL_FUNC)

    # 回调服务器函数，设置response header
    response_headers = list()

    try:
        # 根据"路由表"，调用对应的视图函数
        response_body = URL_FUNC[file_name]().encode("utf-8")
        status = '200 OK'
        response_headers.append(('Content-Type', 'text/html; charset=utf-8'))
    except Exception as ret:
        status = '404 NOT FOUND'
        response_body = "我是404页面<br>您访问的页面不存在，请检查URL或者路由装饰是否正确".encode("utf-8")

        if file_name.startswith("/static"):
            try:
                with open("./app" + file_name, "rb") as f:
                    response_body = f.read()
                    status = '200 OK'

                    for file_type in [".jpg", ".png", "jpeg", "gif"]:
                        if file_name.lower().endswith(file_type):
                            response_headers.append(('Content-Type', 'image/%s' % file_type[1:]))
            except Exception as ret:
                pass

    start_response(status, response_headers)

    # 将response body返回
    return [response_body]

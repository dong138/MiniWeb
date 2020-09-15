"""
日期：2020年9月14日
作者：王铭东
email：dong4716138@163.com
运行本版本的命令：gunicorn -w 1 -b 127.0.0.1:8080 mWeb:application
"""
import sys
import time

from distutils import dirname
from os.path import abspath

# 配置模板文件路径
TEMPLATES_ROOT = "./app/templates"
# 配置资源的路径
RESOURCE_ROOT = "./app/static"
# 配置视图函数存放的路径
VIEWS_ROOT = "app.views"
# 配置
# MODEL_ROOT = "app.models"


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

    # 设置app路径为可以直接import的路径
    sys.path.append(dirname(abspath(__file__)) + "/app")

    # 如下代码实现了"路由表"的制作
    views = __import__(VIEWS_ROOT)

    # 导入模型
    # models = __import__(MODEL_ROOT)

    # 导入路由表
    from MiniWeb.route import URL_FUNC
    print("URL_FUNC--->", URL_FUNC)

    try:
        # 根据"路由表"，调用对应的视图函数
        response = URL_FUNC[file_name]()
    except Exception as ret:
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

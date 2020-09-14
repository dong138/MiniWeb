"""
版本：3-添加view（视图操作）
日期：2020年9月14日
作者：王铭东
email：dong4716138@163.com
运行本版本的命令：gunicorn -w 1 -b 127.0.0.1:8080 MiniWeb3:application
"""
import sys
import time

# 配置模板文件路径
from distutils import dirname
from os.path import abspath

TEMPLATES_ROOT = "./templates/"
# 配置资源的路径
RESOURCE_ROOT = "./static/"
# 配置视图函数存放的路径
VIEWS_ROOT = "views"


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

    # 导入视图包
    # sys.path.append(dirname(dirname(abspath(__file__))))
    web_frame = __import__(VIEWS_ROOT)

    from MiniWeb.route import URL_FUNC
    print("URL_FUNC--->", URL_FUNC)

    try:
        # /index.html
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

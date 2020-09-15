"""
这里存放的是与首页相关的视图函数
"""
from os.path import dirname, abspath

print("---这是views/index.py---")

from MiniWeb.route import route
from models.user import User
from jinja2 import PackageLoader, Environment, FileSystemLoader


@route("/")
def index():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # 1. 链接数据库等准备工作
    engine = create_engine('mysql+pymysql://root:python@localhost:3306/19python')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # 2. 查询
    user = session.query(User).first()
    # 3. 关闭session
    session.close()

    env = Environment(loader=FileSystemLoader(dirname(dirname(abspath(__file__)))))
    template = env.get_template('templates/index.html')  # 获取一个模板文件
    response = template.render(teacher=user.username)  # 渲染

    return response

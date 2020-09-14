"""
这里存放的是与首页相关的视图函数
"""

print("---这是views/index.py---")

from MiniWeb.route import route
from models.user import User


@route("/index.html")
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

    return "我是views/index.py下的index视图函数,,,%s" % user

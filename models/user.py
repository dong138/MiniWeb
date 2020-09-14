from sqlalchemy import Column, Integer, String

from . import Base


# 2. 创建数据表对应的类
class User(Base):
    # 对应MySQL中数据表的名字
    __tablename__ = 'users'

    # 创建字段
    id = Column(Integer, primary_key=True)  # users表中的id字段(主键)
    username = Column(String(64), nullable=False)  # users表中的username字段
    password = Column(String(64), nullable=False)  # users表中的password字段
    email = Column(String(64), nullable=False, index=True)  # users表中的email字段(有索引)
    address = Column(String(200), nullable=True)  # users表中的address字段

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)


print("---这是 models/user.py---")

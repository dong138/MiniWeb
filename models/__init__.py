from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from . import user

print("---这是 models/__init__.py---")

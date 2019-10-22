from sqlalchemy import Table, Column, String, Integer

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Friends(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    spider = Column(String, nullable=True)
    friends = Column(String, nullable=True)
    user = Column(String, nullable=True)
    deep = Column(String, nullable=True)

    def __init__(self, **kwargs):
        self.friends = kwargs.get('friends')
        self.spider = kwargs.get('spider')
        self.user = kwargs.get('user')
        self.deep = kwargs.get('deep')

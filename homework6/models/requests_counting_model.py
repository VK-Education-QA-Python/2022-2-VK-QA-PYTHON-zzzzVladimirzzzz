from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalNumberRequests(Base):
    __tablename__ = 'requests_counting'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'requests_counting id={self.id}, number_of_requests={self.number_of_requests}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_requests = Column(Integer, nullable=False)

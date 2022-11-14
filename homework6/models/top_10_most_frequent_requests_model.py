from sqlalchemy import Column, VARCHAR, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Top10MostFrequentRequests(Base):
    __tablename__ = 'top_10_most_frequent_requests'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'top_10_most_frequent_requests id={self.id}, url= {self.url}, ' \
               f'number_of_requests={self.number_of_requests}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(255), nullable=False)
    number_of_requests = Column(Integer, nullable=False)

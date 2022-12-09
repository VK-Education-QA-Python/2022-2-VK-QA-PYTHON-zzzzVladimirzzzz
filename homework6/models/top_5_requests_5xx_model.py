from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, Integer

Base = declarative_base()


class Top5Requests5xx(Base):

    __tablename__ = 'top_5_requests_5xx'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'top_5_requests_5xx id={self.id}, ip_address= {self.ip_address}, ' \
               f'number_of_requests={self.number_of_requests}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(VARCHAR(50), nullable=False)
    number_of_requests = Column(Integer, nullable=False)

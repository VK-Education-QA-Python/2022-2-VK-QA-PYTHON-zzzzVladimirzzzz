from sqlalchemy import Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalNumberRequestsByType(Base):
    __tablename__ = 'requests_counting_by_type'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'requests_counting_by_type id={self.id}, method={self.method}, ' \
               f'number_of_requests={self.number_of_requests} '

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(CHAR(50), nullable=False)
    number_of_requests = Column(Integer, nullable=True)

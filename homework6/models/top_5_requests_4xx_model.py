from sqlalchemy import Column, VARCHAR, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Top5Requests4xx(Base):
    __tablename__ = 'top_5_requests_4xx'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'top_5_requests_4xx id={self.id}, url={self.url}, status_code={self.status_code},' \
               f'bytes_sent={self.bytes_sent}, ip_address={self.ip_address},'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(CHAR(255), nullable=False)
    status_code = Column(VARCHAR(50), nullable=False)
    bytes_sent = Column(VARCHAR(50), nullable=False)
    ip_address = Column(VARCHAR(50), nullable=False)

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models.request_counting_by_type_model import TotalNumberRequestsByType
from models.requests_counting_model import TotalNumberRequests
from models.top_10_most_frequent_requests_model import Top10MostFrequentRequests
from models.top_5_requests_4xx_model import Top5Requests4xx
from models.top_5_requests_5xx_model import Top5Requests5xx


class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = user
        self.port = '3306'
        self.password = password
        self.host = '127.0.0.1'
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')
        self.execute_query(f'CREATE database {self.db_name}')

    def create_table_total_requests(self):
        if not sqlalchemy.inspect(self.engine).has_table('requests_counting'):
            TotalNumberRequests.metadata.tables['requests_counting'].create(self.engine)

    def create_table_total_requests_by_type(self):
        if not sqlalchemy.inspect(self.engine).has_table('requests_counting_by_type'):
            TotalNumberRequestsByType.metadata.tables['requests_counting_by_type'].create(self.engine)

    def create_top_5_requests_5xx(self):
        if not sqlalchemy.inspect(self.engine).has_table('top_5_requests_5xx'):
            Top5Requests5xx.metadata.tables['top_5_requests_5xx'].create(self.engine)

    def create_top_5_requests_4xx(self):
        if not sqlalchemy.inspect(self.engine).has_table('top_5_requests_4xx'):
            Top5Requests4xx.metadata.tables['top_5_requests_4xx'].create(self.engine)

    def create_top_10_most_frequent_requests(self):
        if not sqlalchemy.inspect(self.engine).has_table('top_10_most_frequent_requests'):
            Top10MostFrequentRequests.metadata.tables['top_10_most_frequent_requests'].create(self.engine)

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

import pytest

from models.request_counting_by_type_model import TotalNumberRequestsByType
from models.requests_counting_model import TotalNumberRequests
from models.top_10_most_frequent_requests_model import Top10MostFrequentRequests
from models.top_5_requests_4xx_model import Top5Requests4xx
from models.top_5_requests_5xx_model import Top5Requests5xx
from mysql.client import MysqlClient
from utils.builder import MysqlBuilder


class MyTest:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.client)

    def get_total_requests(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TotalNumberRequests).filter_by(**filters).all()

    def get_total_requests_by_type(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TotalNumberRequestsByType).filter_by(**filters).all()

    def get_top_5_requests_5xx(self, **filters):
        self.client.session.commit()
        return self.client.session.query(Top5Requests5xx).filter_by(**filters).all()

    def get_top_10_most_frequent_requests_5xx(self, **filters):
        self.client.session.commit()
        return self.client.session.query(Top10MostFrequentRequests).filter_by(**filters).all()

    def get_top_5_requests_4xx(self, **filters):
        self.client.session.commit()
        return self.client.session.query(Top5Requests4xx).filter_by(**filters).all()


class TestMysql(MyTest):
    def test_request_counting(self):
        self.builder.create_total_number_of_requests()
        total_number_of_requests = self.get_total_requests()
        assert len(total_number_of_requests) == 1
        assert total_number_of_requests[0].number_of_requests == 225133

    def test_request_counting_by_type(self):
        self.builder.create_total_number_of_requests_by_type()
        total_number_of_requests_by_type = self.get_total_requests_by_type()
        assert len(total_number_of_requests_by_type) == 9

    def test_top_5_requests_5xx(self):
        self.builder.create_top_5_requests_5xx(number_of_requests=5)
        top_5_requests_5xx = self.get_top_5_requests_5xx()
        assert len(top_5_requests_5xx) == 5

    def test_top_10_most_frequent_requests(self):
        self.builder.create_top_10_most_frequent_requests_5xx(number_of_requests=10)
        top_10_most_frequent_request = self.get_top_10_most_frequent_requests_5xx()
        assert len(top_10_most_frequent_request) == 10

    def test_top_5_requests_4xx(self):
        self.builder.create_top_5_requests_4xx(number_of_requests=5)
        top_5_requests_4xx = self.get_top_5_requests_4xx()
        assert len(top_5_requests_4xx) == 5

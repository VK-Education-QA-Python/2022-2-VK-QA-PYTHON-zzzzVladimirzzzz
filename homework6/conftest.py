import pytest
from sqlalchemy.orm import close_all_sessions

from mysql.client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)

    if not hasattr(config, 'workerinput'):
        mysql_client.create_table_total_requests()
        mysql_client.create_table_total_requests_by_type()
        mysql_client.create_top_5_requests_5xx()
        mysql_client.create_top_10_most_frequent_requests()
        mysql_client.create_top_5_requests_4xx()

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    close_all_sessions()

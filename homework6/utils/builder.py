from scripts.request_counting_by_type_script import request_counting_by_type
from scripts.request_counting_script import total_number_of_requests_func
from scripts.top_10_most_frequent_requests import top_10_most_frequent_requests
from scripts.top_5_requests_4xx import top_requests_4xx
from scripts.top_5_requests_5xx import top_requests_5xx


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_total_number_of_requests(self):
        number_of_requests = total_number_of_requests_func()
        self.client.execute_query(
            f'insert into `requests_counting` (`number_of_requests`) values ("{number_of_requests}")')

    def create_total_number_of_requests_by_type(self):
        requests_dict = request_counting_by_type()
        for i in requests_dict:
            self.client.execute_query(
                f'insert into `requests_counting_by_type` (`method`,`number_of_requests`) '
                f'values ("{i}", "{int(requests_dict[i])}")'
            )

    def create_top_5_requests_5xx(self, number_of_requests):
        requests_dict = top_requests_5xx(number_of_requests=number_of_requests)
        for i in requests_dict.keys():
            self.client.execute_query(
                f'insert into `top_5_requests_5xx` (`ip_address`,`number_of_requests`) '
                f'values ("{i}", "{int(requests_dict[i])}")'
            )

    def create_top_10_most_frequent_requests_5xx(self, number_of_requests):
        requests_dict = top_10_most_frequent_requests(number_of_requests=number_of_requests)
        for i in requests_dict.keys():
            self.client.execute_query(
                f'insert into `top_10_most_frequent_requests` (`url`,`number_of_requests`) '
                f'values ("{i}", "{int(requests_dict[i])}")'
            )

    def create_top_5_requests_4xx(self, number_of_requests):
        requests_list = top_requests_4xx(number_of_requests=number_of_requests)
        for i in requests_list:
            self.client.execute_query(
                f'insert into `top_5_requests_4xx` (`url`,`status_code`,`bytes_sent`,`ip_address`) '
                f'values ("{str(i[0][:20])}","{i[1]}","{i[2]}","{i[3]}")'
            )

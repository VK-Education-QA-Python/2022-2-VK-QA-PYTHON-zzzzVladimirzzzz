import os
import re

path = os.path.abspath(os.path.join(__file__, os.path.pardir))


def total_number_of_requests_func():
    total_number_of_requests = 0
    with open(path + '/files/access.logs', "r") as f:
        for line in f:
            line_list = re.split(' ', line)
            if re.search(r'POST|GET|PUT|HEAD|DELETE|CONNECT|OPTIONS|TRACE|PATCH', line_list[5]) is not None:
                total_number_of_requests += 1
    return total_number_of_requests

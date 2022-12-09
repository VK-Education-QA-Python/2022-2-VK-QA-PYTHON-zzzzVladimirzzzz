import re
import os

path = os.path.abspath(os.path.join(__file__, os.path.pardir))


def request_counting_by_type():
    post_result = 0
    get_result = 0
    put_result = 0
    head_result = 0
    delete_result = 0
    connect_result = 0
    options_result = 0
    trace_result = 0
    patch_result = 0
    with open(path + '/files/access.logs',
              "r") as f:
        for line in f:
            line_list = re.split(' ', line)
            if re.search(r'POST', line_list[5]) is not None:
                post_result += 1
            if re.search(r'GET', line_list[5]) is not None:
                get_result += 1
            if re.search(r'PUT', line_list[5]) is not None:
                put_result += 1
            if re.search(r'HEAD', line_list[5]) is not None:
                head_result += 1
            if re.search(r'DELETE', line_list[5]) is not None:
                delete_result += 1
            if re.search(r'CONNECT', line_list[5]) is not None:
                connect_result += 1
            if re.search(r'OPTIONS', line_list[5]) is not None:
                options_result += 1
            if re.search(r'TRACE', line_list[5]) is not None:
                trace_result += 1
            if re.search(r'PATCH', line_list[5]) is not None:
                patch_result += 1
    dict_total_number_of_requests = {"POST REQUESTS": post_result, 'GET REQUESTS': get_result,
                                     'PUT REQUESTS': put_result, 'HEAD REQUESTS': head_result,
                                     'DELETE REQUESTS': delete_result,
                                     'CONNECT REQUESTS': connect_result,
                                     'OPTIONS REQUESTS': options_result,
                                     'TRACE REQUESTS': trace_result,
                                     'PATCH REQUESTS': patch_result}
    return dict_total_number_of_requests

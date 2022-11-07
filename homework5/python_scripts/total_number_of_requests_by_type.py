import argparse
import json
import re

POST_RESULT = 0
GET_RESULT = 0
PUT_RESULT = 0
HEAD_RESULT = 0
DELETE_RESULT = 0
CONNECT_RESULT = 0
OPTIONS_RESULT = 0
TRACE_RESULT = 0
PATCH_RESULT = 0

with open(
        "access.log",
        "r") as f:
    for line in f:
        line_list = re.split(' ', line)
        if re.search(r'POST', line_list[5]) is not None:
            POST_RESULT += 1
        if re.search(r'GET', line_list[5]) is not None:
            GET_RESULT += 1
        if re.search(r'PUT', line_list[5]) is not None:
            PUT_RESULT += 1
        if re.search(r'HEAD', line_list[5]) is not None:
            HEAD_RESULT += 1
        if re.search(r'DELETE', line_list[5]) is not None:
            DELETE_RESULT += 1
        if re.search(r'CONNECT', line_list[5]) is not None:
            CONNECT_RESULT += 1
        if re.search(r'OPTIONS', line_list[5]) is not None:
            OPTIONS_RESULT += 1
        if re.search(r'TRACE', line_list[5]) is not None:
            TRACE_RESULT += 1
        if re.search(r'PATCH', line_list[5]) is not None:
            PATCH_RESULT += 1
parser = argparse.ArgumentParser()
parser.add_argument('--json', default=True)
dict_total_number_of_requests = {"Количество POST запросов:": POST_RESULT, 'Количество GET запросов:': GET_RESULT,
                                 'Количество PUT запросов:': PUT_RESULT, 'Количество HEAD запросов:': HEAD_RESULT,
                                 'Количество DELETE запросов:': DELETE_RESULT,
                                 'Количество CONNECT запросов:': CONNECT_RESULT,
                                 'Количество OPTIONS запросов:': OPTIONS_RESULT,
                                 'Количество TRACE запросов:': TRACE_RESULT, 'Количество PATCH запросов:': PATCH_RESULT}
args = parser.parse_args()
if args.json:
    with open('results_python.txt', 'w') as f:
        json.dump(dict_total_number_of_requests, f)
else:
    with open("results_python.txt", "w") as f:
        f.write(dict_total_number_of_requests)

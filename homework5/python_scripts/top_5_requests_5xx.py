import argparse
import json
import re
from collections import Counter

line_nginx_full = re.compile(
    r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""",
    re.IGNORECASE)
list_status_code_500 = []
with open(
        "access.log",
        "r") as f:
    for line in f:
        data = re.search(line_nginx_full, line)
        if data:
            datadict = data.groupdict()
            ip = datadict["ipaddress"]
            status = datadict["statuscode"]
            if status[0] == '5':
                list_status_code_500.append(ip)

dict_status_code_500 = dict((Counter(list_status_code_500)))
sorted_dict_status_code_500 = dict(sorted(dict_status_code_500.items(), key=lambda x: int(x[1]),reverse=True)[:5])
parser = argparse.ArgumentParser()
parser.add_argument('--json', default=True)
args = parser.parse_args()
if args.json:
    with open('results_python.txt', 'w') as f:
        f.write('Топ 5 пользователей по количеству запросов,которые завершились серверной (5xx) ошибкой \n')
        json.dump(sorted_dict_status_code_500, f)
else:
    with open("results_python.txt", "w") as f:
        f.write(f'Топ 5 пользователей по количеству запросов,которые завершились серверной '
                f'(5xx) ошибкой :\n{sorted_dict_status_code_500}')

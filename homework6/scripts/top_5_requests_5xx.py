import os
import re
from collections import Counter

path = os.path.abspath(os.path.join(__file__, os.path.pardir))


def top_requests_5xx(number_of_requests):
    line_nginx_full = re.compile(
        r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""",
        re.IGNORECASE)
    list_status_code_500 = []
    with open(path + '/files/access.logs', "r") as f:
        for line in f:
            data = re.search(line_nginx_full, line)
            if data:
                datadict = data.groupdict()
                ip = datadict["ipaddress"]
                status = datadict["statuscode"]
                if status[0] == '5':
                    list_status_code_500.append(ip)

    dict_status_code_500 = dict((Counter(list_status_code_500)))
    sorted_dict_status_code_500 = dict(
        sorted(dict_status_code_500.items(), key=lambda x: int(x[1]), reverse=True)[:number_of_requests])
    return sorted_dict_status_code_500

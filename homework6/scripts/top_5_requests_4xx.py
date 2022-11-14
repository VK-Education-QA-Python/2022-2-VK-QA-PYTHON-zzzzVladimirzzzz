import os
import re
from operator import itemgetter

path = os.path.abspath(os.path.join(__file__, os.path.pardir))


def top_requests_4xx(number_of_requests):
    line_nginx_full = re.compile(
        r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""",
        re.IGNORECASE)
    list_status_code_400 = []
    with open(
            path + '/files/access.logs',
            "r") as f:
        for line in f:
            data = re.search(line_nginx_full, line)
            list_request = []
            if data:
                datadict = data.groupdict()
                url = datadict["url"]
                status = datadict["statuscode"]
                bytessent = datadict["bytessent"]
                ip = datadict["ipaddress"]
                list_request.append(url)
                list_request.append(status)
                list_request.append(int(bytessent))
                list_request.append(ip)
                if list_request[1][0] == '4':
                    list_status_code_400.append(list_request)
    sorted_list = sorted(list_status_code_400, key=itemgetter(2), reverse=True)
    return sorted_list[:number_of_requests]

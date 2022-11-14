import os
import re
from collections import Counter
from urllib.parse import urlparse

path = os.path.abspath(os.path.join(__file__, os.path.pardir))


def top_10_most_frequent_requests(number_of_requests):
    path_list = []
    line_nginx_full = re.compile(
        r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""",
        re.IGNORECASE)
    with open(
            path + '/files/access.logs',
            "r") as f:
        for line in f:
            data = re.search(line_nginx_full, line)
            if data:
                datadict = data.groupdict()
                url = datadict["url"]
                path_list.append(urlparse(url).path)
    dict_path = dict((Counter(path_list)))
    sorted_dict_path = dict(sorted(dict_path.items(), key=lambda x: int(x[1]), reverse=True)[:number_of_requests])
    return sorted_dict_path

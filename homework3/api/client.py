from urllib.parse import urljoin

import requests


class ApiClientException(Exception):
    ...


class ResponseStatusCodeException(Exception):
    pass


class RespondErrorException(Exception):
    pass


class ApiClient:
    def __init__(self, base_url: str, login: str, password: str):
        self.base_url = base_url

        self.login = login
        self.password = password

        self.session = requests.Session()

    def post_login(self):
        data = {'login': self.login, 'password': self.password}
        headers = {'Referer': 'https://target-sandbox.my.com/'}

        location = urljoin('https://auth-ac.my.com/', 'auth?lang=ru&nosavelogin=0')
        login_request = self._request(method='POST', location=location, headers=headers, data=data, expected_status=302)
        return login_request

    def get_mc_token(self):
        headers = self.post_login().headers['Set-Cookie'].split(';')

        mc_token = [mc for mc in headers if 'mc']
        if not mc_token:
            raise ApiClientException('Expected mc_token in Set-Cookie')
        mc_token = mc_token[0].split('=')[-1]
        return mc_token

    def login_and_get_tokens(self):
        mc_token = self.get_mc_token()
        headers = {'Cookie': f'mc={mc_token}'}
        tokens = self._request(method='GET', location='csrf', headers=headers, expected_status=200,
                               allow_redirects=True)
        return tokens

    def _request(self, method, location, headers, data=None, params=None, allow_redirects=False, expected_status=200,
                 jsonify=False, json=None):
        url = urljoin(self.base_url, location)

        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params,
                                        allow_redirects=allow_redirects, json=json)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Expected {expected_status}, but got {response.status_code}')
        if jsonify:
            json_response: dict = response.json()
            return json_response
        return response

    def post_create_campaign(self, name: str, sex: list, age_list: list, pads: list):
        headers = {'X-CSRFToken': f'{self.session.cookies["csrftoken"]}', }
        data = {"name": name, "read_only": False, "objective": "special",
                "targetings": {"sex": sex, "age": {"age_list": age_list, "expand": False}, "pads": pads},
                "mixing": "fastest", "price": "0.01", "max_price": "0", "package_id": 2266}
        request = self._request(method='POST', location='api/v2/campaigns.json', headers=headers, json=data,
                                jsonify=True)
        return request

    def get_campaigns(self, campaign_id):
        headers = {'Cookie': f'csrftoken={self.session.cookies["csrftoken"]};'
                             f'mc={self.session.cookies["mc"]};'
                             f'sdc={self.session.cookies["sdc"]};', }
        request = self._request(method='GET', location=f'api/v2/campaigns.json?_status=active&_id={campaign_id}',
                                headers=headers)
        return request

    def delete_campaign(self, campaign_id):
        headers = {'X-CSRFToken': f'{self.session.cookies["csrftoken"]}', }

        request = self._request(method='DELETE', location=f'api/v2/campaigns/{campaign_id}.json', headers=headers,
                                expected_status=204)
        return request

    def post_create_segment(self, name: str, object_type: str, params: dict, pass_condition: int):
        headers = {'X-CSRFToken': f'{self.session.cookies["csrftoken"]}', }
        data = {"name": name, "pass_condition": pass_condition,
                "relations": [{"object_type": object_type, "params": params}], "logicType": "or"}
        request = self._request(method='POST', location='api/v2/remarketing/segments.json', headers=headers, json=data,
                                jsonify=True)
        return request

    def delete_segment(self, segment_id):
        headers = {'X-CSRFToken': f'{self.session.cookies["csrftoken"]}', }

        request = self._request(method='DELETE', location=f'api/v2/remarketing/segments/{segment_id}.json',
                                headers=headers, expected_status=204)
        return request

    def get_segments(self):
        headers = {'Cookie': f'csrftoken={self.session.cookies["csrftoken"]};'
                             f'mc={self.session.cookies["mc"]};'
                             f'sdc={self.session.cookies["sdc"]};'}
        return self._request(method='GET', location=f'api/v2//remarketing/segments.json?limit=100', headers=headers)

    def get_object_id(self, group_link: str):
        headers = {'Cookie': f'csrftoken={self.session.cookies["csrftoken"]};'
                             f'mc={self.session.cookies["mc"]};'
                             f'sdc={self.session.cookies["sdc"]};'}
        return self._request(method='GET', location=f'api/v2/vk_groups.json?_q={group_link}', headers=headers)

    def post_create_data_source(self, object_id: int):
        headers = {'X-CSRFToken': f'{self.session.cookies["csrftoken"]}', }
        data = {"object_id": object_id}

        return self._request(method='POST', location='api/v2/remarketing/vk_groups.json', headers=headers, json=data,
                             expected_status=201)

    def delete_created_data_source(self, data_source_id):
        headers = {'X-CSRFToken': f'{self.session.cookies["csrftoken"]}', }

        return self._request(method='DELETE', location=f'api/v2/remarketing/vk_groups/{data_source_id}.json',
                             headers=headers, expected_status=204)

    def get_data_sources_list(self):
        headers = {'Cookie': f'csrftoken={self.session.cookies["csrftoken"]};'
                             f'mc={self.session.cookies["mc"]};'
                             f'sdc={self.session.cookies["sdc"]};'}

        return self._request(method='GET', location=f'api/v2/remarketing/vk_groups.json', headers=headers,
                             expected_status=200)

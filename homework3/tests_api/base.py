import pytest


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        if self.authorize:
            self.api_client.login_and_get_tokens()

    def created_campaign(self):
        created_campaign = self.api_client.post_create_campaign(name='test1', sex=["female"],
                                                                age_list=[0, 12, 13, 14, 15, 16, 17, 18,
                                                                          19, 20, 21, 22, 23, 24],
                                                                pads=[784699, 784700, 806001,
                                                                      846252, 846321, 887946, 1220843])
        return created_campaign

    def check_campaign_in_campaigns_list(self, campaign_id):
        campaigns_list = self.api_client.get_campaigns(campaign_id=campaign_id).json()['items']
        found = False
        for campaign in campaigns_list:
            if campaign['id'] == campaign_id:
                found = True
                break
        return found

    def delete_campaign(self, campaign_id):
        campaign_deleted = self.api_client.delete_campaign(campaign_id=campaign_id)
        return campaign_deleted

    def created_segment_games(self):
        created_segment = self.api_client.post_create_segment(name='test2', object_type='remarketing_game_player',
                                                              params={"game": "supercity", "type": "positive",
                                                                      "left": 365, "right": 0}, pass_condition=1)
        return created_segment

    def check_segment_in_segment_list(self, segment_id):
        segment_list = self.api_client.get_segments().json()['items']
        found = False
        for segment in segment_list:
            if segment['id'] == segment_id:
                found = True
                break
        return found

    def delete_segment(self, segment_id):
        segment_deleted = self.api_client.delete_segment(segment_id=segment_id)
        return segment_deleted

    def group_object_id(self):
        object_group_request = self.api_client.get_object_id(group_link='https://vk.com/vkedu').json()['items'][0]
        return object_group_request['id']

    def create_data_source(self):
        object_id = self.group_object_id()
        created_data_source = self.api_client.post_create_data_source(object_id=object_id).json()
        return created_data_source

    def delete_data_source(self, data_source_id):
        data_source_deleted = self.api_client.delete_created_data_source(data_source_id=data_source_id)
        return data_source_deleted

    def check_groups_in_data_sources(self, data_source_id):
        data_sources_list = self.api_client.get_data_sources_list().json()['items']
        found = False
        for data_source in data_sources_list:
            if data_source['id'] == data_source_id:
                found = True
                break
        return found

    def created_segment_vk_groups(self):
        created_segment = self.api_client.post_create_segment(name='test3', object_type='remarketing_vk_group',
                                                              params={'source_id':
                                                                      self.create_data_source()['object_id'],
                                                                      "type": 'positive',
                                                                      "left": 365, "right": 0}, pass_condition=1)
        return created_segment

import pytest

from base import ApiBase


@pytest.mark.API
class TestHomework3(ApiBase):
    def test_create_delete_campaign(self):
        campaign_id = self.created_campaign()['id']
        assert self.check_campaign_in_campaigns_list(campaign_id=campaign_id)
        self.delete_campaign(campaign_id=campaign_id)
        assert self.check_campaign_in_campaigns_list(campaign_id=campaign_id) is False

    def test_create_delete_segment(self):
        segment_id = self.created_segment_games()['id']
        assert self.check_segment_in_segment_list(segment_id=segment_id)
        self.delete_segment(segment_id=segment_id)
        assert self.check_segment_in_segment_list(segment_id=segment_id) is False

    def test_create_delete_segment_and_data_source(self):
        segment_id = self.created_segment_vk_groups()['id']
        source_id = self.create_data_source()['id']
        assert self.check_segment_in_segment_list(segment_id=segment_id)
        assert self.check_groups_in_data_sources(data_source_id=source_id)
        self.delete_segment(segment_id=segment_id)
        self.delete_data_source(data_source_id=source_id)
        assert self.check_segment_in_segment_list(segment_id=segment_id) is False
        assert self.check_groups_in_data_sources(data_source_id=source_id) is False

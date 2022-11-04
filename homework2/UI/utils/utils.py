import uuid
import os


def generate_campaign_name(base_campaign_name):
    return base_campaign_name + str(uuid.uuid4())


def generate_segments_name(base_segment_name):
    return base_segment_name + str(uuid.uuid4())


def generate_file_path(file_name, repo_root):
    return os.path.join(repo_root, 'UI', 'static', file_name)

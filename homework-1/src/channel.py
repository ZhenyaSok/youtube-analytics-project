import json
import os
from googleapiclient.discovery import build


class Channel:

    api_key: str = os.getenv('YOUTUBE_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id):
        self.channel_id = channel_id

    def print_info(self):
        print(json.dumps(self.youtube.channels().list(
            part='snippet, contentDetails, statistics',
            id=self.channel_id).execute(), indent=2, ensure_ascii=False))

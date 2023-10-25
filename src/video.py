import  os
from googleapiclient.discovery import build




class Video:
    api_key: str = os.getenv('YOUTUBE_KEY')
    url_str = 'https://youtu.be/'

    def __init__(self,id_video):
        self.__id_video = id_video
        self.title = self.video_response()['items'][0]['snippet']['title']
        self.view_count = self.video_response()['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response()['items'][0]['statistics']['likeCount']
        self.url = Video.url_str + self.__id_video

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    @property
    def id_video(self):
        return self.__id_video


    def video_response(self):
        """Метод для получения информации о видео"""
        video = Video.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=self.__id_video
                                                  ).execute()
        return video

    def __str__(self):
        return self.title


class PLVideo(Video):
    """Класс для видео из плейлиста"""

    def __init__(self, id_video, pl_id):
        super().__init__(id_video)
        self.__pl_id = pl_id

    @property
    def pl_id(self):
        return self.__pl_id


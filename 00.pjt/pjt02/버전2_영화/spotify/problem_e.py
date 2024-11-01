import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_recommended_tracks(track, artist, genre):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    pass


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_recommended_tracks('HypeBoy', 'BTS', 'k-pop,acoustic'))

from typing import List, Dict
from soundcloud.converter import download_opus, opus2mp3
from soundcloud.utils import request,  parse_username
from soundcloud.endpoints import *

from pprint import pprint

class SoundCloudList:
    def __init__(self, client_id, oauth_token, playlist_name) -> None:
        self.client_id = client_id
        self.oauth_token = oauth_token
        self.playlist_name = playlist_name
        self.tracks = {}
        self.list_names = {}

    def rq(self, url, params: Dict = None):
        return request(url, self.client_id, self.oauth_token, params)

    def fetch_user_id(self, username: str) -> int:
        pms = {"q": username, "limit": 1}
        r = self.rq(SEARCH_USER, pms)
        return int(r['collection'][0]['id'])

    def add_likes(self, url: str) -> str:
        track_list = []

        username = parse_username(url)
        user_id = self.fetch_user_id(username)
        url_likes = USER_LIKES(user_id)
        params = {"limit": "100"}
        first_response = self.rq(url_likes, params)
        next_href = first_response['next_href']
        track_list.extend(first_response['collection'])
        while (next_href):
            params = {"limit": "100"}
            response = self.rq(next_href, params)
            next_href = response['next_href']
            track_list.extend(response['collection'])
        playlist_tag = f"{username}/likes"
        self.tracks[playlist_tag] = track_list
        return playlist_tag

    def download_tracks(self, playlist_tags: List[str] = None):
        if not playlist_tags:
            for playlist in self.tracks:
                for t in self.tracks[playlist]:
                    for i in range(len(t['track']['media']['transcodings'])):
                        treasure_url = t['track']['media']['transcodings'][i]['url']
                        t_id = t['track']['id']
                        r = self.rq(treasure_url)
                        file_url = r['url']
                        # pprint(t['track']['media']['transcodings'])
                        fn = download_opus(file_url, i)
                        opus2mp3(fn)

        else:
            pass

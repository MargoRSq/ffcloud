import os
import requests
from typing import Dict, List
from urllib.parse import urlparse

from soundcloud.endpoints import *


def request(url: str, client_id: str, oauth_token: str, pms: Dict | None) -> Dict:
    headers = {"Authorization": f"OAuth {oauth_token}"}
    params = {"client_id": client_id}
    if pms:
        params.update(pms)
    tries = 10
    status = 403
    response = None
    while (status != 200 and tries and not response):
        response = requests.get(url, headers=headers, params=params)
        status = response.status_code
        tries -= 1
    if response.status_code != 200:
        raise requests.RequestException(response)
    else:
        return response.json()


def parse_username(url: str) -> str:
    up = urlparse(url)
    username = up.path.split('/')[1]
    return username


def create_m3u(tracks: List[str]) -> str:
    text = u"""\\
    #EXTM3U"""
    for file in files:
            text += f"""\n#EXTINF:
    file:{os.getcwd()}/{file}"""

    print(text)

from soundcloud.sclist import SoundCloudList
from config.config import *


def main():
    scl = SoundCloudList(CLIENT_ID, OAUTH_TOKEN, "likes")
    scl.add_likes("https://soundcloud.com/egqys5isic3w/likes")
    scl.download_tracks()

if __name__ == "__main__":
    main()
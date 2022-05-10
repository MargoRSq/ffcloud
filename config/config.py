from starlette.config import Config

config = Config(".env")

CLIENT_ID = config("CLIENT_ID")
OAUTH_TOKEN = config("OAUTH_TOKEN")
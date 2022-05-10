
API_SERVER = "https://api-v2.soundcloud.com"

SEARCH_USER = API_SERVER + "/search/users"

USERS = API_SERVER + "/users"

USER_LIKES = lambda u_id: USERS + "/" + str(u_id) + "/likes"


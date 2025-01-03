# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sibyl_core_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    USERS = "/users"
    USERS_ID = "/users/{id}"
    USERS_TELEGRAM_TELEGRAM_ID = "/users/telegram/{telegram_id}"

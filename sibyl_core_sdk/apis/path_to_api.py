import typing_extensions

from sibyl_core_sdk.paths import PathValues
from sibyl_core_sdk.apis.paths.users import Users
from sibyl_core_sdk.apis.paths.users_id import UsersId
from sibyl_core_sdk.apis.paths.users_telegram_telegram_id import UsersTelegramTelegramId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.USERS: Users,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS_TELEGRAM_TELEGRAM_ID: UsersTelegramTelegramId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.USERS: Users,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS_TELEGRAM_TELEGRAM_ID: UsersTelegramTelegramId,
    }
)

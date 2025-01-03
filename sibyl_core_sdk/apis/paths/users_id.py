from sibyl_core_sdk.paths.users_id.get import ApiForget
from sibyl_core_sdk.paths.users_id.put import ApiForput
from sibyl_core_sdk.paths.users_id.delete import ApiFordelete


class UsersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass

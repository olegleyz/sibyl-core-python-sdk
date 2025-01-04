# UsersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**telegram_id** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**profile** | **str** |  | [optional] 
**reading** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sibyl_core_sdk.models.users_post_request import UsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPostRequest from a JSON string
users_post_request_instance = UsersPostRequest.from_json(json)
# print the JSON string representation of the object
print(UsersPostRequest.to_json())

# convert the object into a dict
users_post_request_dict = users_post_request_instance.to_dict()
# create an instance of UsersPostRequest from a dict
users_post_request_from_dict = UsersPostRequest.from_dict(users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



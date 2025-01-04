# sibyl_core_sdk.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_id_delete**](DefaultApi.md#users_id_delete) | **DELETE** /users/{id} | Delete user by UUID
[**users_id_get**](DefaultApi.md#users_id_get) | **GET** /users/{id} | Get user by UUID
[**users_id_put**](DefaultApi.md#users_id_put) | **PUT** /users/{id} | Update user by UUID
[**users_post**](DefaultApi.md#users_post) | **POST** /users | Create a new user
[**users_telegram_telegram_id_get**](DefaultApi.md#users_telegram_telegram_id_get) | **GET** /users/telegram/{telegram_id} | Get user by Telegram ID
[**users_telegram_telegram_id_put**](DefaultApi.md#users_telegram_telegram_id_put) | **PUT** /users/telegram/{telegram_id} | Update user by Telegram ID


# **users_id_delete**
> users_id_delete(id)

Delete user by UUID

### Example

* Api Key Authentication (AWS_IAM):

```python
import sibyl_core_sdk
from sibyl_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sibyl_core_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AWS_IAM
configuration.api_key['AWS_IAM'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AWS_IAM'] = 'Bearer'

# Enter a context with an instance of the API client
with sibyl_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sibyl_core_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete user by UUID
        api_instance.users_id_delete(id)
    except Exception as e:
        print("Exception when calling DefaultApi->users_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[AWS_IAM](../README.md#AWS_IAM)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User deleted successfully |  -  |
**400** | Invalid request |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_get**
> UsersPostRequest users_id_get(id)

Get user by UUID

### Example

* Api Key Authentication (AWS_IAM):

```python
import sibyl_core_sdk
from sibyl_core_sdk.models.users_post_request import UsersPostRequest
from sibyl_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sibyl_core_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AWS_IAM
configuration.api_key['AWS_IAM'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AWS_IAM'] = 'Bearer'

# Enter a context with an instance of the API client
with sibyl_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sibyl_core_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get user by UUID
        api_response = api_instance.users_id_get(id)
        print("The response of DefaultApi->users_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UsersPostRequest**](UsersPostRequest.md)

### Authorization

[AWS_IAM](../README.md#AWS_IAM)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User found |  -  |
**400** | Invalid request |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_put**
> UsersPostRequest users_id_put(id, users_post_request)

Update user by UUID

### Example

* Api Key Authentication (AWS_IAM):

```python
import sibyl_core_sdk
from sibyl_core_sdk.models.users_post_request import UsersPostRequest
from sibyl_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sibyl_core_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AWS_IAM
configuration.api_key['AWS_IAM'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AWS_IAM'] = 'Bearer'

# Enter a context with an instance of the API client
with sibyl_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sibyl_core_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 
    users_post_request = sibyl_core_sdk.UsersPostRequest() # UsersPostRequest | 

    try:
        # Update user by UUID
        api_response = api_instance.users_id_put(id, users_post_request)
        print("The response of DefaultApi->users_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **users_post_request** | [**UsersPostRequest**](UsersPostRequest.md)|  | 

### Return type

[**UsersPostRequest**](UsersPostRequest.md)

### Authorization

[AWS_IAM](../README.md#AWS_IAM)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User updated successfully |  -  |
**400** | Invalid request |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> UsersPostRequest users_post(users_post_request)

Create a new user

### Example

* Api Key Authentication (AWS_IAM):

```python
import sibyl_core_sdk
from sibyl_core_sdk.models.users_post_request import UsersPostRequest
from sibyl_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sibyl_core_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AWS_IAM
configuration.api_key['AWS_IAM'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AWS_IAM'] = 'Bearer'

# Enter a context with an instance of the API client
with sibyl_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sibyl_core_sdk.DefaultApi(api_client)
    users_post_request = sibyl_core_sdk.UsersPostRequest() # UsersPostRequest | 

    try:
        # Create a new user
        api_response = api_instance.users_post(users_post_request)
        print("The response of DefaultApi->users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_post_request** | [**UsersPostRequest**](UsersPostRequest.md)|  | 

### Return type

[**UsersPostRequest**](UsersPostRequest.md)

### Authorization

[AWS_IAM](../README.md#AWS_IAM)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created successfully |  -  |
**400** | Invalid request |  -  |
**409** | User with the same telegram_id already exists |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_telegram_telegram_id_get**
> UsersPostRequest users_telegram_telegram_id_get(telegram_id)

Get user by Telegram ID

### Example

* Api Key Authentication (AWS_IAM):

```python
import sibyl_core_sdk
from sibyl_core_sdk.models.users_post_request import UsersPostRequest
from sibyl_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sibyl_core_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AWS_IAM
configuration.api_key['AWS_IAM'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AWS_IAM'] = 'Bearer'

# Enter a context with an instance of the API client
with sibyl_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sibyl_core_sdk.DefaultApi(api_client)
    telegram_id = 'telegram_id_example' # str | 

    try:
        # Get user by Telegram ID
        api_response = api_instance.users_telegram_telegram_id_get(telegram_id)
        print("The response of DefaultApi->users_telegram_telegram_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_telegram_telegram_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telegram_id** | **str**|  | 

### Return type

[**UsersPostRequest**](UsersPostRequest.md)

### Authorization

[AWS_IAM](../README.md#AWS_IAM)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User found |  -  |
**400** | Invalid request |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_telegram_telegram_id_put**
> UsersPostRequest users_telegram_telegram_id_put(telegram_id, users_post_request)

Update user by Telegram ID

### Example

* Api Key Authentication (AWS_IAM):

```python
import sibyl_core_sdk
from sibyl_core_sdk.models.users_post_request import UsersPostRequest
from sibyl_core_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sibyl_core_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AWS_IAM
configuration.api_key['AWS_IAM'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AWS_IAM'] = 'Bearer'

# Enter a context with an instance of the API client
with sibyl_core_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sibyl_core_sdk.DefaultApi(api_client)
    telegram_id = 'telegram_id_example' # str | 
    users_post_request = sibyl_core_sdk.UsersPostRequest() # UsersPostRequest | 

    try:
        # Update user by Telegram ID
        api_response = api_instance.users_telegram_telegram_id_put(telegram_id, users_post_request)
        print("The response of DefaultApi->users_telegram_telegram_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_telegram_telegram_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telegram_id** | **str**|  | 
 **users_post_request** | [**UsersPostRequest**](UsersPostRequest.md)|  | 

### Return type

[**UsersPostRequest**](UsersPostRequest.md)

### Authorization

[AWS_IAM](../README.md#AWS_IAM)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User updated successfully |  -  |
**400** | Invalid request |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


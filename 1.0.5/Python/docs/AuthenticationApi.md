# swagger_client.AuthenticationApi

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_post**](AuthenticationApi.md#v1_auth_post) | **POST** /v1/auth | Authenticate through our API

# **v1_auth_post**
> InlineResponse200 v1_auth_post(body)

Authenticate through our API

Allow user to authenticate through our API and retrieve a JWT token that need to be used within all requests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.Auth() # Auth | Authenticate user and retrieve JWT token

try:
    # Authenticate through our API
    api_response = api_instance.v1_auth_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->v1_auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Auth**](Auth.md)| Authenticate user and retrieve JWT token | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


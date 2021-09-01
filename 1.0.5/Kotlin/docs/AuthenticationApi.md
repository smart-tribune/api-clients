# AuthenticationApi

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1AuthPost**](AuthenticationApi.md#v1AuthPost) | **POST** /v1/auth | Authenticate through our API

<a name="v1AuthPost"></a>
# **v1AuthPost**
> InlineResponse200 v1AuthPost(body)

Authenticate through our API

Allow user to authenticate through our API and retrieve a JWT token that need to be used within all requests

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = AuthenticationApi()
val body : Auth =  // Auth | Authenticate user and retrieve JWT token
try {
    val result : InlineResponse200 = apiInstance.v1AuthPost(body)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthenticationApi#v1AuthPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthenticationApi#v1AuthPost")
    e.printStackTrace()
}
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


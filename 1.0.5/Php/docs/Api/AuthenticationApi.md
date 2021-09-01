# Swagger\Client\AuthenticationApi

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1AuthPost**](AuthenticationApi.md#v1authpost) | **POST** /v1/auth | Authenticate through our API

# **v1AuthPost**
> \Swagger\Client\Model\InlineResponse200 v1AuthPost($body)

Authenticate through our API

Allow user to authenticate through our API and retrieve a JWT token that need to be used within all requests

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\AuthenticationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\Auth(); // \Swagger\Client\Model\Auth | Authenticate user and retrieve JWT token

try {
    $result = $apiInstance->v1AuthPost($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AuthenticationApi->v1AuthPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\Auth**](../Model/Auth.md)| Authenticate user and retrieve JWT token |

### Return type

[**\Swagger\Client\Model\InlineResponse200**](../Model/InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)


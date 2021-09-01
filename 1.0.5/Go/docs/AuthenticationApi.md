# {{classname}}

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1AuthPost**](AuthenticationApi.md#V1AuthPost) | **Post** /v1/auth | Authenticate through our API

# **V1AuthPost**
> InlineResponse200 V1AuthPost(ctx, body)
Authenticate through our API

Allow user to authenticate through our API and retrieve a JWT token that need to be used within all requests

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**Auth**](Auth.md)| Authenticate user and retrieve JWT token | 

### Return type

[**InlineResponse200**](inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


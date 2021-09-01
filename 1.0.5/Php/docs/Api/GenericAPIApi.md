# Swagger\Client\GenericAPIApi

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1KnowledgeBasesGet**](GenericAPIApi.md#v1knowledgebasesget) | **GET** /v1/knowledge-bases | Fetch allowed Knowledge bases
[**v1KnowledgeBasesIdContactsGet**](GenericAPIApi.md#v1knowledgebasesidcontactsget) | **GET** /v1/knowledge-bases/{id}/contacts | Fetch available Contact methods
[**v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet**](GenericAPIApi.md#v1knowledgebasesidquestionsquestionidchannelschannelidresponsesget) | **GET** /v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses | Fetch Response related to a specified Question for a specific Channel
[**v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost**](GenericAPIApi.md#v1knowledgebasesidquestionsquestionidresponsesresponseidresponsessatisfactionspost) | **POST** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions | Post a Response Satisfaction on a specified Response
[**v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch**](GenericAPIApi.md#v1knowledgebasesidquestionsquestionidresponsesresponseidresponsessatisfactionssatisfactionidpatch) | **PATCH** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId} | Update a Response Satisfaction on a specified Response to provide a Reason
[**v1KnowledgeBasesIdReasonCommentsGet**](GenericAPIApi.md#v1knowledgebasesidreasoncommentsget) | **GET** /v1/knowledge-bases/{id}/reason-comments | Fetch available comments for negative vote Reasons
[**v1KnowledgeBasesIdReasonsGet**](GenericAPIApi.md#v1knowledgebasesidreasonsget) | **GET** /v1/knowledge-bases/{id}/reasons | Fetch available negative vote Reasons

# **v1KnowledgeBasesGet**
> \Swagger\Client\Model\InlineResponse2003 v1KnowledgeBasesGet($accept_language)

Fetch allowed Knowledge bases

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\GenericAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$accept_language = "accept_language_example"; // string | Language locale to filter api results

try {
    $result = $apiInstance->v1KnowledgeBasesGet($accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GenericAPIApi->v1KnowledgeBasesGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **string**| Language locale to filter api results |

### Return type

[**\Swagger\Client\Model\InlineResponse2003**](../Model/InlineResponse2003.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1KnowledgeBasesIdContactsGet**
> \Swagger\Client\Model\InlineResponse2009 v1KnowledgeBasesIdContactsGet($id, $accept_language)

Fetch available Contact methods

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\GenericAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 56; // int | The Knowledgebase id that needs to be fetched.
$accept_language = "accept_language_example"; // string | Language locale to filter api results

try {
    $result = $apiInstance->v1KnowledgeBasesIdContactsGet($id, $accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GenericAPIApi->v1KnowledgeBasesIdContactsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Knowledgebase id that needs to be fetched. |
 **accept_language** | **string**| Language locale to filter api results |

### Return type

[**\Swagger\Client\Model\InlineResponse2009**](../Model/InlineResponse2009.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet**
> \Swagger\Client\Model\InlineResponse2004 v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet($id, $question_id, $channel_id, $accept_language)

Fetch Response related to a specified Question for a specific Channel

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\GenericAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 56; // int | The Knowledgebase id that needs to be fetched.
$question_id = 56; // int | The Question id that needs to be fetched.
$channel_id = 56; // int | The Channel id that needs to be fetched.
$accept_language = "accept_language_example"; // string | Language locale to filter api results

try {
    $result = $apiInstance->v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet($id, $question_id, $channel_id, $accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GenericAPIApi->v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Knowledgebase id that needs to be fetched. |
 **question_id** | **int**| The Question id that needs to be fetched. |
 **channel_id** | **int**| The Channel id that needs to be fetched. |
 **accept_language** | **string**| Language locale to filter api results |

### Return type

[**\Swagger\Client\Model\InlineResponse2004**](../Model/InlineResponse2004.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost**
> \Swagger\Client\Model\InlineResponse2005 v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost($accept_language, $id, $question_id, $response_id, $body)

Post a Response Satisfaction on a specified Response

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\GenericAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$accept_language = "accept_language_example"; // string | Language locale to filter api results
$id = 56; // int | The knowledgebase id that needs to be fetched.
$question_id = 56; // int | The Question id that needs to be fetched.
$response_id = 56; // int | The Response id that needs to be fetched.
$body = new \Swagger\Client\Model\ResponseIdResponsessatisfactionsBody(); // \Swagger\Client\Model\ResponseIdResponsessatisfactionsBody | 

try {
    $result = $apiInstance->v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost($accept_language, $id, $question_id, $response_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GenericAPIApi->v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **string**| Language locale to filter api results |
 **id** | **int**| The knowledgebase id that needs to be fetched. |
 **question_id** | **int**| The Question id that needs to be fetched. |
 **response_id** | **int**| The Response id that needs to be fetched. |
 **body** | [**\Swagger\Client\Model\ResponseIdResponsessatisfactionsBody**](../Model/ResponseIdResponsessatisfactionsBody.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2005**](../Model/InlineResponse2005.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch**
> \Swagger\Client\Model\InlineResponse2008 v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch($accept_language, $id, $question_id, $response_id, $satisfaction_id, $body)

Update a Response Satisfaction on a specified Response to provide a Reason

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\GenericAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$accept_language = "accept_language_example"; // string | Language locale to filter api results
$id = 56; // int | The knowledgebase id that needs to be fetched.
$question_id = 56; // int | The Question id that needs to be fetched.
$response_id = 56; // int | The Response id that needs to be fetched.
$satisfaction_id = 56; // int | The Response satisfaction id that needs to be fetched.
$body = new \Swagger\Client\Model\ResponsessatisfactionsSatisfactionIdBody(); // \Swagger\Client\Model\ResponsessatisfactionsSatisfactionIdBody | 

try {
    $result = $apiInstance->v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch($accept_language, $id, $question_id, $response_id, $satisfaction_id, $body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GenericAPIApi->v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **string**| Language locale to filter api results |
 **id** | **int**| The knowledgebase id that needs to be fetched. |
 **question_id** | **int**| The Question id that needs to be fetched. |
 **response_id** | **int**| The Response id that needs to be fetched. |
 **satisfaction_id** | **int**| The Response satisfaction id that needs to be fetched. |
 **body** | [**\Swagger\Client\Model\ResponsessatisfactionsSatisfactionIdBody**](../Model/ResponsessatisfactionsSatisfactionIdBody.md)|  | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2008**](../Model/InlineResponse2008.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1KnowledgeBasesIdReasonCommentsGet**
> \Swagger\Client\Model\InlineResponse2007 v1KnowledgeBasesIdReasonCommentsGet($id, $accept_language, $start_date, $channel, $extended)

Fetch available comments for negative vote Reasons

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\GenericAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 56; // int | The Knowledgebase id that needs to be fetched.
$accept_language = "accept_language_example"; // string | Language locale to filter api results
$start_date = "start_date_example"; // string | Start Date in yyyy-mm-dd format. Comments fetched are created at startDate (between 00:00:00 and 23:59:59)
$channel = "channel_example"; // string | The channel name of the responses affected by comments
$extended = true; // bool | used to display additional information : thematics list and response content associated to the question

try {
    $result = $apiInstance->v1KnowledgeBasesIdReasonCommentsGet($id, $accept_language, $start_date, $channel, $extended);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GenericAPIApi->v1KnowledgeBasesIdReasonCommentsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Knowledgebase id that needs to be fetched. |
 **accept_language** | **string**| Language locale to filter api results |
 **start_date** | **string**| Start Date in yyyy-mm-dd format. Comments fetched are created at startDate (between 00:00:00 and 23:59:59) |
 **channel** | **string**| The channel name of the responses affected by comments |
 **extended** | **bool**| used to display additional information : thematics list and response content associated to the question | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2007**](../Model/InlineResponse2007.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1KnowledgeBasesIdReasonsGet**
> \Swagger\Client\Model\InlineResponse2006 v1KnowledgeBasesIdReasonsGet($id, $accept_language)

Fetch available negative vote Reasons

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\GenericAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 56; // int | The Knowledgebase id that needs to be fetched.
$accept_language = "accept_language_example"; // string | Language locale to filter api results

try {
    $result = $apiInstance->v1KnowledgeBasesIdReasonsGet($id, $accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GenericAPIApi->v1KnowledgeBasesIdReasonsGet: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Knowledgebase id that needs to be fetched. |
 **accept_language** | **string**| Language locale to filter api results |

### Return type

[**\Swagger\Client\Model\InlineResponse2006**](../Model/InlineResponse2006.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)


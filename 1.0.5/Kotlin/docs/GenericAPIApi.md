# GenericAPIApi

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1KnowledgeBasesGet**](GenericAPIApi.md#v1KnowledgeBasesGet) | **GET** /v1/knowledge-bases | Fetch allowed Knowledge bases
[**v1KnowledgeBasesIdContactsGet**](GenericAPIApi.md#v1KnowledgeBasesIdContactsGet) | **GET** /v1/knowledge-bases/{id}/contacts | Fetch available Contact methods
[**v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet**](GenericAPIApi.md#v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet) | **GET** /v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses | Fetch Response related to a specified Question for a specific Channel
[**v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost**](GenericAPIApi.md#v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost) | **POST** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions | Post a Response Satisfaction on a specified Response
[**v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch**](GenericAPIApi.md#v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch) | **PATCH** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId} | Update a Response Satisfaction on a specified Response to provide a Reason
[**v1KnowledgeBasesIdReasonCommentsGet**](GenericAPIApi.md#v1KnowledgeBasesIdReasonCommentsGet) | **GET** /v1/knowledge-bases/{id}/reason-comments | Fetch available comments for negative vote Reasons
[**v1KnowledgeBasesIdReasonsGet**](GenericAPIApi.md#v1KnowledgeBasesIdReasonsGet) | **GET** /v1/knowledge-bases/{id}/reasons | Fetch available negative vote Reasons

<a name="v1KnowledgeBasesGet"></a>
# **v1KnowledgeBasesGet**
> InlineResponse2003 v1KnowledgeBasesGet(acceptLanguage)

Fetch allowed Knowledge bases

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = GenericAPIApi()
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
try {
    val result : InlineResponse2003 = apiInstance.v1KnowledgeBasesGet(acceptLanguage)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling GenericAPIApi#v1KnowledgeBasesGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GenericAPIApi#v1KnowledgeBasesGet")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="v1KnowledgeBasesIdContactsGet"></a>
# **v1KnowledgeBasesIdContactsGet**
> InlineResponse2009 v1KnowledgeBasesIdContactsGet(id, acceptLanguage)

Fetch available Contact methods

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = GenericAPIApi()
val id : kotlin.Int = 56 // kotlin.Int | The Knowledgebase id that needs to be fetched.
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
try {
    val result : InlineResponse2009 = apiInstance.v1KnowledgeBasesIdContactsGet(id, acceptLanguage)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling GenericAPIApi#v1KnowledgeBasesIdContactsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GenericAPIApi#v1KnowledgeBasesIdContactsGet")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| The Knowledgebase id that needs to be fetched. |
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet"></a>
# **v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet**
> InlineResponse2004 v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet(id, questionId, channelId, acceptLanguage)

Fetch Response related to a specified Question for a specific Channel

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = GenericAPIApi()
val id : kotlin.Int = 56 // kotlin.Int | The Knowledgebase id that needs to be fetched.
val questionId : kotlin.Int = 56 // kotlin.Int | The Question id that needs to be fetched.
val channelId : kotlin.Int = 56 // kotlin.Int | The Channel id that needs to be fetched.
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
try {
    val result : InlineResponse2004 = apiInstance.v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet(id, questionId, channelId, acceptLanguage)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling GenericAPIApi#v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GenericAPIApi#v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| The Knowledgebase id that needs to be fetched. |
 **questionId** | **kotlin.Int**| The Question id that needs to be fetched. |
 **channelId** | **kotlin.Int**| The Channel id that needs to be fetched. |
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost"></a>
# **v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost**
> InlineResponse2005 v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost(acceptLanguage, id, questionId, responseId, body)

Post a Response Satisfaction on a specified Response

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = GenericAPIApi()
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
val id : kotlin.Int = 56 // kotlin.Int | The knowledgebase id that needs to be fetched.
val questionId : kotlin.Int = 56 // kotlin.Int | The Question id that needs to be fetched.
val responseId : kotlin.Int = 56 // kotlin.Int | The Response id that needs to be fetched.
val body : ResponseIdResponsessatisfactionsBody =  // ResponseIdResponsessatisfactionsBody | 
try {
    val result : InlineResponse2005 = apiInstance.v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost(acceptLanguage, id, questionId, responseId, body)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling GenericAPIApi#v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GenericAPIApi#v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |
 **id** | **kotlin.Int**| The knowledgebase id that needs to be fetched. |
 **questionId** | **kotlin.Int**| The Question id that needs to be fetched. |
 **responseId** | **kotlin.Int**| The Response id that needs to be fetched. |
 **body** | [**ResponseIdResponsessatisfactionsBody**](ResponseIdResponsessatisfactionsBody.md)|  | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch"></a>
# **v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch**
> InlineResponse2008 v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch(acceptLanguage, id, questionId, responseId, satisfactionId, body)

Update a Response Satisfaction on a specified Response to provide a Reason

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = GenericAPIApi()
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
val id : kotlin.Int = 56 // kotlin.Int | The knowledgebase id that needs to be fetched.
val questionId : kotlin.Int = 56 // kotlin.Int | The Question id that needs to be fetched.
val responseId : kotlin.Int = 56 // kotlin.Int | The Response id that needs to be fetched.
val satisfactionId : kotlin.Int = 56 // kotlin.Int | The Response satisfaction id that needs to be fetched.
val body : ResponsessatisfactionsSatisfactionIdBody =  // ResponsessatisfactionsSatisfactionIdBody | 
try {
    val result : InlineResponse2008 = apiInstance.v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch(acceptLanguage, id, questionId, responseId, satisfactionId, body)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling GenericAPIApi#v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GenericAPIApi#v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |
 **id** | **kotlin.Int**| The knowledgebase id that needs to be fetched. |
 **questionId** | **kotlin.Int**| The Question id that needs to be fetched. |
 **responseId** | **kotlin.Int**| The Response id that needs to be fetched. |
 **satisfactionId** | **kotlin.Int**| The Response satisfaction id that needs to be fetched. |
 **body** | [**ResponsessatisfactionsSatisfactionIdBody**](ResponsessatisfactionsSatisfactionIdBody.md)|  | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="v1KnowledgeBasesIdReasonCommentsGet"></a>
# **v1KnowledgeBasesIdReasonCommentsGet**
> InlineResponse2007 v1KnowledgeBasesIdReasonCommentsGet(id, acceptLanguage, startDate, channel, extended)

Fetch available comments for negative vote Reasons

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = GenericAPIApi()
val id : kotlin.Int = 56 // kotlin.Int | The Knowledgebase id that needs to be fetched.
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
val startDate : kotlin.String = startDate_example // kotlin.String | Start Date in yyyy-mm-dd format. Comments fetched are created at startDate (between 00:00:00 and 23:59:59)
val channel : kotlin.String = channel_example // kotlin.String | The channel name of the responses affected by comments
val extended : kotlin.Boolean = true // kotlin.Boolean | used to display additional information : thematics list and response content associated to the question
try {
    val result : InlineResponse2007 = apiInstance.v1KnowledgeBasesIdReasonCommentsGet(id, acceptLanguage, startDate, channel, extended)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling GenericAPIApi#v1KnowledgeBasesIdReasonCommentsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GenericAPIApi#v1KnowledgeBasesIdReasonCommentsGet")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| The Knowledgebase id that needs to be fetched. |
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |
 **startDate** | **kotlin.String**| Start Date in yyyy-mm-dd format. Comments fetched are created at startDate (between 00:00:00 and 23:59:59) |
 **channel** | **kotlin.String**| The channel name of the responses affected by comments |
 **extended** | **kotlin.Boolean**| used to display additional information : thematics list and response content associated to the question | [optional]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="v1KnowledgeBasesIdReasonsGet"></a>
# **v1KnowledgeBasesIdReasonsGet**
> InlineResponse2006 v1KnowledgeBasesIdReasonsGet(id, acceptLanguage)

Fetch available negative vote Reasons

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = GenericAPIApi()
val id : kotlin.Int = 56 // kotlin.Int | The Knowledgebase id that needs to be fetched.
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
try {
    val result : InlineResponse2006 = apiInstance.v1KnowledgeBasesIdReasonsGet(id, acceptLanguage)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling GenericAPIApi#v1KnowledgeBasesIdReasonsGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling GenericAPIApi#v1KnowledgeBasesIdReasonsGet")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **kotlin.Int**| The Knowledgebase id that needs to be fetched. |
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


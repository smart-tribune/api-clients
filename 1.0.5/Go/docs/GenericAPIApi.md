# {{classname}}

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1KnowledgeBasesGet**](GenericAPIApi.md#V1KnowledgeBasesGet) | **Get** /v1/knowledge-bases | Fetch allowed Knowledge bases
[**V1KnowledgeBasesIdContactsGet**](GenericAPIApi.md#V1KnowledgeBasesIdContactsGet) | **Get** /v1/knowledge-bases/{id}/contacts | Fetch available Contact methods
[**V1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet**](GenericAPIApi.md#V1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet) | **Get** /v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses | Fetch Response related to a specified Question for a specific Channel
[**V1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost**](GenericAPIApi.md#V1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost) | **Post** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions | Post a Response Satisfaction on a specified Response
[**V1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch**](GenericAPIApi.md#V1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch) | **Patch** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId} | Update a Response Satisfaction on a specified Response to provide a Reason
[**V1KnowledgeBasesIdReasonCommentsGet**](GenericAPIApi.md#V1KnowledgeBasesIdReasonCommentsGet) | **Get** /v1/knowledge-bases/{id}/reason-comments | Fetch available comments for negative vote Reasons
[**V1KnowledgeBasesIdReasonsGet**](GenericAPIApi.md#V1KnowledgeBasesIdReasonsGet) | **Get** /v1/knowledge-bases/{id}/reasons | Fetch available negative vote Reasons

# **V1KnowledgeBasesGet**
> InlineResponse2003 V1KnowledgeBasesGet(ctx, acceptLanguage)
Fetch allowed Knowledge bases

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **acceptLanguage** | **string**| Language locale to filter api results | 

### Return type

[**InlineResponse2003**](inline_response_200_3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **V1KnowledgeBasesIdContactsGet**
> InlineResponse2009 V1KnowledgeBasesIdContactsGet(ctx, id, acceptLanguage)
Fetch available Contact methods

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**| The Knowledgebase id that needs to be fetched. | 
  **acceptLanguage** | **string**| Language locale to filter api results | 

### Return type

[**InlineResponse2009**](inline_response_200_9.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **V1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet**
> InlineResponse2004 V1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet(ctx, id, questionId, channelId, acceptLanguage)
Fetch Response related to a specified Question for a specific Channel

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**| The Knowledgebase id that needs to be fetched. | 
  **questionId** | **int32**| The Question id that needs to be fetched. | 
  **channelId** | **int32**| The Channel id that needs to be fetched. | 
  **acceptLanguage** | **string**| Language locale to filter api results | 

### Return type

[**InlineResponse2004**](inline_response_200_4.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **V1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost**
> InlineResponse2005 V1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost(ctx, id, questionId, responseId, acceptLanguage, optional)
Post a Response Satisfaction on a specified Response

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**| The knowledgebase id that needs to be fetched. | 
  **questionId** | **int32**| The Question id that needs to be fetched. | 
  **responseId** | **int32**| The Response id that needs to be fetched. | 
  **acceptLanguage** | **string**| Language locale to filter api results | 
 **optional** | ***GenericAPIApiV1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a GenericAPIApiV1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPostOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **body** | [**optional.Interface of ResponseIdResponsessatisfactionsBody**](ResponseIdResponsessatisfactionsBody.md)|  | 

### Return type

[**InlineResponse2005**](inline_response_200_5.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **V1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch**
> InlineResponse2008 V1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch(ctx, id, questionId, responseId, satisfactionId, acceptLanguage, optional)
Update a Response Satisfaction on a specified Response to provide a Reason

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**| The knowledgebase id that needs to be fetched. | 
  **questionId** | **int32**| The Question id that needs to be fetched. | 
  **responseId** | **int32**| The Response id that needs to be fetched. | 
  **satisfactionId** | **int32**| The Response satisfaction id that needs to be fetched. | 
  **acceptLanguage** | **string**| Language locale to filter api results | 
 **optional** | ***GenericAPIApiV1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatchOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a GenericAPIApiV1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatchOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





 **body** | [**optional.Interface of ResponsessatisfactionsSatisfactionIdBody**](ResponsessatisfactionsSatisfactionIdBody.md)|  | 

### Return type

[**InlineResponse2008**](inline_response_200_8.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **V1KnowledgeBasesIdReasonCommentsGet**
> InlineResponse2007 V1KnowledgeBasesIdReasonCommentsGet(ctx, id, acceptLanguage, startDate, channel, optional)
Fetch available comments for negative vote Reasons

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**| The Knowledgebase id that needs to be fetched. | 
  **acceptLanguage** | **string**| Language locale to filter api results | 
  **startDate** | **string**| Start Date in yyyy-mm-dd format. Comments fetched are created at startDate (between 00:00:00 and 23:59:59) | 
  **channel** | **string**| The channel name of the responses affected by comments | 
 **optional** | ***GenericAPIApiV1KnowledgeBasesIdReasonCommentsGetOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a GenericAPIApiV1KnowledgeBasesIdReasonCommentsGetOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **extended** | **optional.Bool**| used to display additional information : thematics list and response content associated to the question | 

### Return type

[**InlineResponse2007**](inline_response_200_7.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **V1KnowledgeBasesIdReasonsGet**
> InlineResponse2006 V1KnowledgeBasesIdReasonsGet(ctx, id, acceptLanguage)
Fetch available negative vote Reasons

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**| The Knowledgebase id that needs to be fetched. | 
  **acceptLanguage** | **string**| Language locale to filter api results | 

### Return type

[**InlineResponse2006**](inline_response_200_6.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


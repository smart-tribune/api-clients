# {{classname}}

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1KnowledgeBasesIdFilteredQuestionsPost**](FilteredAPIApi.md#V1KnowledgeBasesIdFilteredQuestionsPost) | **Post** /v1/knowledge-bases/{id}/filtered/questions | Fetch a (list of) Question(s) depend on specified Filters
[**V1KnowledgeBasesIdFilteredThematicsPost**](FilteredAPIApi.md#V1KnowledgeBasesIdFilteredThematicsPost) | **Post** /v1/knowledge-bases/{id}/filtered/thematics | Fetch a (list of) Thematic(s) depend on specified Filters

# **V1KnowledgeBasesIdFilteredQuestionsPost**
> InlineResponse2001 V1KnowledgeBasesIdFilteredQuestionsPost(ctx, id, acceptLanguage, optional)
Fetch a (list of) Question(s) depend on specified Filters

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**| The knowledgebase Id that needs to be fetched. | 
  **acceptLanguage** | **string**| Language locale to filter api results | 
 **optional** | ***FilteredAPIApiV1KnowledgeBasesIdFilteredQuestionsPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a FilteredAPIApiV1KnowledgeBasesIdFilteredQuestionsPostOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of FilteredQuestionsPayload**](FilteredQuestionsPayload.md)| **Example of payloads to fetch** :

 * Promoted Questions within Smart FAQ Channel
     &#x60;&#x60;&#x60;javascript
      {
        &quot;channel&quot;: &quot;faq&quot;,
        &quot;promoted&quot;: true
      }
     &#x60;&#x60;&#x60;

 * Frequent Questions within Smart FAQ Channel
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot;: &quot;faq&quot;,
       &quot;frequent&quot;: true
     }
     &#x60;&#x60;&#x60;

 * Related questions within Smart FAQ channel for thematic systemName &quot;how-to-make-booking-987&quot; and Question id 19
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot; : &quot;faq&quot;,
       &quot;excludedQuestions&quot; : [19],
       &quot;searchFilters&quot;: [
           {
               &quot;name&quot;: &quot;thematic-system-name-859&quot;,
               &quot;type&quot;: &quot;thematic&quot;
           }
       ]
     }
     &#x60;&#x60;&#x60;

 * Search results within Smart FAQ Channel
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot;: &quot;faq&quot;,
       &quot;query&quot;: &quot;my search query&quot;
       &quot;useSuggester&quot;: true
     }
     &#x60;&#x60;&#x60;

 * Single Question by slug
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot;: &quot;faq&quot;,
       &quot;questionSlug&quot;: &quot;my-question-slug&quot;
     }
     &#x60;&#x60;&#x60;

 * Questions filtered by Thematic with slug &quot;my-thematic&quot;
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot;: &quot;faq&quot;,
       &quot;searchFilters&quot;: [
           {
               &quot;slug&quot;: &quot;my-thematic-slug&quot;,
               &quot;type&quot;: &quot;thematic&quot;
           }
       ]
     }
     &#x60;&#x60;&#x60;
  * Questions filtered using Tags with name &quot;my-tag-1&quot; OR &quot;my-tag-2&quot;
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot;: &quot;faq&quot;,
       &quot;searchFilters&quot;: [
           {
               &quot;name&quot;: &quot;my-tag-1&quot;,
               &quot;type&quot;: &quot;tag&quot;
           },
           {
               &quot;name&quot;: &quot;my-tag-2&quot;,
               &quot;type&quot;: &quot;tag&quot;
           }
       ],
       &quot;searchFiltersOperators&quot;: [
          { &quot;tag&quot; : &quot;OR&quot; }
        ]
     }
     &#x60;&#x60;&#x60;
 * Questions filtered by Thematic with systemName &quot;tag-system-name-568&quot; AND Tag with systemName &quot;my-tag-14&quot;
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot;: &quot;faq&quot;,
       &quot;searchFilters&quot;: [
           {
               &quot;name&quot;: &quot;thematic-system-name-859&quot;,
               &quot;type&quot;: &quot;thematic&quot;
           },
           {
               &quot;name&quot;: &quot;tag-system-name-568&quot;,
               &quot;type&quot;: &quot;tag&quot;
           }
       ]
     }
     &#x60;&#x60;&#x60;
 | 
 **page** | **optional.**| Page identifier | 
 **limit** | **optional.**| Items per page | 

### Return type

[**InlineResponse2001**](inline_response_200_1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **V1KnowledgeBasesIdFilteredThematicsPost**
> InlineResponse2002 V1KnowledgeBasesIdFilteredThematicsPost(ctx, id, acceptLanguage, optional)
Fetch a (list of) Thematic(s) depend on specified Filters

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**| The knowledgebase Id that needs to be fetched. | 
  **acceptLanguage** | **string**| Language locale to filter api results | 
 **optional** | ***FilteredAPIApiV1KnowledgeBasesIdFilteredThematicsPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a FilteredAPIApiV1KnowledgeBasesIdFilteredThematicsPostOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of FilteredThematicsPayload**](FilteredThematicsPayload.md)| **Example of payloads to fetch** :

  * Thematics filtered by SystemName &quot;how-to-make-booking-987&quot;
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot;: &quot;faq&quot;,
       &quot;searchFilters&quot;: [
           {
               &quot;name&quot;: &quot;how-to-make-booking-987&quot;,
               &quot;type&quot;: &quot;thematic&quot;
           }
       ]
     }
      &#x60;&#x60;&#x60;

  * Thematics filtered by slug &quot;my-thematic&quot;
     &#x60;&#x60;&#x60;javascript
     {
       &quot;channel&quot;: &quot;faq&quot;,
       &quot;searchFilters&quot;: [
           {
               &quot;slug&quot;: &quot;my-thematic-slug&quot;,
               &quot;type&quot;: &quot;thematic&quot;
           }
       ]
     }
      &#x60;&#x60;&#x60;
 | 
 **page** | **optional.**| Page identifier | 
 **limit** | **optional.**| Items per page | 

### Return type

[**InlineResponse2002**](inline_response_200_2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


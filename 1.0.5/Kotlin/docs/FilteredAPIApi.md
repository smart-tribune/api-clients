# FilteredAPIApi

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1KnowledgeBasesIdFilteredQuestionsPost**](FilteredAPIApi.md#v1KnowledgeBasesIdFilteredQuestionsPost) | **POST** /v1/knowledge-bases/{id}/filtered/questions | Fetch a (list of) Question(s) depend on specified Filters
[**v1KnowledgeBasesIdFilteredThematicsPost**](FilteredAPIApi.md#v1KnowledgeBasesIdFilteredThematicsPost) | **POST** /v1/knowledge-bases/{id}/filtered/thematics | Fetch a (list of) Thematic(s) depend on specified Filters

<a name="v1KnowledgeBasesIdFilteredQuestionsPost"></a>
# **v1KnowledgeBasesIdFilteredQuestionsPost**
> InlineResponse2001 v1KnowledgeBasesIdFilteredQuestionsPost(acceptLanguage, id, body, page, limit)

Fetch a (list of) Question(s) depend on specified Filters

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = FilteredAPIApi()
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
val id : kotlin.Int = 56 // kotlin.Int | The knowledgebase Id that needs to be fetched.
val body : FilteredQuestionsPayload =  // FilteredQuestionsPayload | **Example of payloads to fetch** :

 * Promoted Questions within Smart FAQ Channel
     ```javascript
      {
        "channel": "faq",
        "promoted": true
      }
     ```

 * Frequent Questions within Smart FAQ Channel
     ```javascript
     {
       "channel": "faq",
       "frequent": true
     }
     ```

 * Related questions within Smart FAQ channel for thematic systemName "how-to-make-booking-987" and Question id 19
     ```javascript
     {
       "channel" : "faq",
       "excludedQuestions" : [19],
       "searchFilters": [
           {
               "name": "thematic-system-name-859",
               "type": "thematic"
           }
       ]
     }
     ```

 * Search results within Smart FAQ Channel
     ```javascript
     {
       "channel": "faq",
       "query": "my search query"
       "useSuggester": true
     }
     ```

 * Single Question by slug
     ```javascript
     {
       "channel": "faq",
       "questionSlug": "my-question-slug"
     }
     ```

 * Questions filtered by Thematic with slug "my-thematic"
     ```javascript
     {
       "channel": "faq",
       "searchFilters": [
           {
               "slug": "my-thematic-slug",
               "type": "thematic"
           }
       ]
     }
     ```
  * Questions filtered using Tags with name "my-tag-1" OR "my-tag-2"
     ```javascript
     {
       "channel": "faq",
       "searchFilters": [
           {
               "name": "my-tag-1",
               "type": "tag"
           },
           {
               "name": "my-tag-2",
               "type": "tag"
           }
       ],
       "searchFiltersOperators": [
          { "tag" : "OR" }
        ]
     }
     ```
 * Questions filtered by Thematic with systemName "tag-system-name-568" AND Tag with systemName "my-tag-14"
     ```javascript
     {
       "channel": "faq",
       "searchFilters": [
           {
               "name": "thematic-system-name-859",
               "type": "thematic"
           },
           {
               "name": "tag-system-name-568",
               "type": "tag"
           }
       ]
     }
     ```

val page : kotlin.Int = 56 // kotlin.Int | Page identifier
val limit : kotlin.Int = 56 // kotlin.Int | Items per page
try {
    val result : InlineResponse2001 = apiInstance.v1KnowledgeBasesIdFilteredQuestionsPost(acceptLanguage, id, body, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling FilteredAPIApi#v1KnowledgeBasesIdFilteredQuestionsPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling FilteredAPIApi#v1KnowledgeBasesIdFilteredQuestionsPost")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |
 **id** | **kotlin.Int**| The knowledgebase Id that needs to be fetched. |
 **body** | [**FilteredQuestionsPayload**](FilteredQuestionsPayload.md)| **Example of payloads to fetch** :

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
 | [optional]
 **page** | **kotlin.Int**| Page identifier | [optional]
 **limit** | **kotlin.Int**| Items per page | [optional] [enum: ]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="v1KnowledgeBasesIdFilteredThematicsPost"></a>
# **v1KnowledgeBasesIdFilteredThematicsPost**
> InlineResponse2002 v1KnowledgeBasesIdFilteredThematicsPost(acceptLanguage, id, body, page, limit)

Fetch a (list of) Thematic(s) depend on specified Filters

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = FilteredAPIApi()
val acceptLanguage : kotlin.String = acceptLanguage_example // kotlin.String | Language locale to filter api results
val id : kotlin.Int = 56 // kotlin.Int | The knowledgebase Id that needs to be fetched.
val body : FilteredThematicsPayload =  // FilteredThematicsPayload | **Example of payloads to fetch** :

  * Thematics filtered by SystemName "how-to-make-booking-987"
     ```javascript
     {
       "channel": "faq",
       "searchFilters": [
           {
               "name": "how-to-make-booking-987",
               "type": "thematic"
           }
       ]
     }
      ```

  * Thematics filtered by slug "my-thematic"
     ```javascript
     {
       "channel": "faq",
       "searchFilters": [
           {
               "slug": "my-thematic-slug",
               "type": "thematic"
           }
       ]
     }
      ```

val page : kotlin.Int = 56 // kotlin.Int | Page identifier
val limit : kotlin.Int = 56 // kotlin.Int | Items per page
try {
    val result : InlineResponse2002 = apiInstance.v1KnowledgeBasesIdFilteredThematicsPost(acceptLanguage, id, body, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling FilteredAPIApi#v1KnowledgeBasesIdFilteredThematicsPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling FilteredAPIApi#v1KnowledgeBasesIdFilteredThematicsPost")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acceptLanguage** | **kotlin.String**| Language locale to filter api results |
 **id** | **kotlin.Int**| The knowledgebase Id that needs to be fetched. |
 **body** | [**FilteredThematicsPayload**](FilteredThematicsPayload.md)| **Example of payloads to fetch** :

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
 | [optional]
 **page** | **kotlin.Int**| Page identifier | [optional]
 **limit** | **kotlin.Int**| Items per page | [optional] [enum: ]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


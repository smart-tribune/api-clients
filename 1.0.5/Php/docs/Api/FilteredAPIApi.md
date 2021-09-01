# Swagger\Client\FilteredAPIApi

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1KnowledgeBasesIdFilteredQuestionsPost**](FilteredAPIApi.md#v1knowledgebasesidfilteredquestionspost) | **POST** /v1/knowledge-bases/{id}/filtered/questions | Fetch a (list of) Question(s) depend on specified Filters
[**v1KnowledgeBasesIdFilteredThematicsPost**](FilteredAPIApi.md#v1knowledgebasesidfilteredthematicspost) | **POST** /v1/knowledge-bases/{id}/filtered/thematics | Fetch a (list of) Thematic(s) depend on specified Filters

# **v1KnowledgeBasesIdFilteredQuestionsPost**
> \Swagger\Client\Model\InlineResponse2001 v1KnowledgeBasesIdFilteredQuestionsPost($accept_language, $id, $body, $page, $limit)

Fetch a (list of) Question(s) depend on specified Filters

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\FilteredAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$accept_language = "accept_language_example"; // string | Language locale to filter api results
$id = 56; // int | The knowledgebase Id that needs to be fetched.
$body = new \Swagger\Client\Model\FilteredQuestionsPayload(); // \Swagger\Client\Model\FilteredQuestionsPayload | **Example of payloads to fetch** :

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

$page = 56; // int | Page identifier
$limit = 56; // int | Items per page

try {
    $result = $apiInstance->v1KnowledgeBasesIdFilteredQuestionsPost($accept_language, $id, $body, $page, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilteredAPIApi->v1KnowledgeBasesIdFilteredQuestionsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **string**| Language locale to filter api results |
 **id** | **int**| The knowledgebase Id that needs to be fetched. |
 **body** | [**\Swagger\Client\Model\FilteredQuestionsPayload**](../Model/FilteredQuestionsPayload.md)| **Example of payloads to fetch** :

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
 **page** | **int**| Page identifier | [optional]
 **limit** | **int**| Items per page | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2001**](../Model/InlineResponse2001.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1KnowledgeBasesIdFilteredThematicsPost**
> \Swagger\Client\Model\InlineResponse2002 v1KnowledgeBasesIdFilteredThematicsPost($accept_language, $id, $body, $page, $limit)

Fetch a (list of) Thematic(s) depend on specified Filters

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
    // Configure HTTP bearer authorization: bearerAuth
    $config = Swagger\Client\Configuration::getDefaultConfiguration()
    ->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Swagger\Client\Api\FilteredAPIApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$accept_language = "accept_language_example"; // string | Language locale to filter api results
$id = 56; // int | The knowledgebase Id that needs to be fetched.
$body = new \Swagger\Client\Model\FilteredThematicsPayload(); // \Swagger\Client\Model\FilteredThematicsPayload | **Example of payloads to fetch** :

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

$page = 56; // int | Page identifier
$limit = 56; // int | Items per page

try {
    $result = $apiInstance->v1KnowledgeBasesIdFilteredThematicsPost($accept_language, $id, $body, $page, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FilteredAPIApi->v1KnowledgeBasesIdFilteredThematicsPost: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **string**| Language locale to filter api results |
 **id** | **int**| The knowledgebase Id that needs to be fetched. |
 **body** | [**\Swagger\Client\Model\FilteredThematicsPayload**](../Model/FilteredThematicsPayload.md)| **Example of payloads to fetch** :

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
 **page** | **int**| Page identifier | [optional]
 **limit** | **int**| Items per page | [optional]

### Return type

[**\Swagger\Client\Model\InlineResponse2002**](../Model/InlineResponse2002.md)

### Authorization

[bearerAuth](../../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)


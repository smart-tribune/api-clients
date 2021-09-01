# swagger_client.GenericAPIApi

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_knowledge_bases_get**](GenericAPIApi.md#v1_knowledge_bases_get) | **GET** /v1/knowledge-bases | Fetch allowed Knowledge bases
[**v1_knowledge_bases_id_contacts_get**](GenericAPIApi.md#v1_knowledge_bases_id_contacts_get) | **GET** /v1/knowledge-bases/{id}/contacts | Fetch available Contact methods
[**v1_knowledge_bases_id_questions_question_id_channels_channel_id_responses_get**](GenericAPIApi.md#v1_knowledge_bases_id_questions_question_id_channels_channel_id_responses_get) | **GET** /v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses | Fetch Response related to a specified Question for a specific Channel
[**v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_post**](GenericAPIApi.md#v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_post) | **POST** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions | Post a Response Satisfaction on a specified Response
[**v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_satisfaction_id_patch**](GenericAPIApi.md#v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_satisfaction_id_patch) | **PATCH** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId} | Update a Response Satisfaction on a specified Response to provide a Reason
[**v1_knowledge_bases_id_reason_comments_get**](GenericAPIApi.md#v1_knowledge_bases_id_reason_comments_get) | **GET** /v1/knowledge-bases/{id}/reason-comments | Fetch available comments for negative vote Reasons
[**v1_knowledge_bases_id_reasons_get**](GenericAPIApi.md#v1_knowledge_bases_id_reasons_get) | **GET** /v1/knowledge-bases/{id}/reasons | Fetch available negative vote Reasons

# **v1_knowledge_bases_get**
> InlineResponse2003 v1_knowledge_bases_get(accept_language)

Fetch allowed Knowledge bases

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GenericAPIApi(swagger_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language locale to filter api results

try:
    # Fetch allowed Knowledge bases
    api_response = api_instance.v1_knowledge_bases_get(accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericAPIApi->v1_knowledge_bases_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language locale to filter api results | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_contacts_get**
> InlineResponse2009 v1_knowledge_bases_id_contacts_get(id, accept_language)

Fetch available Contact methods

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GenericAPIApi(swagger_client.ApiClient(configuration))
id = 56 # int | The Knowledgebase id that needs to be fetched.
accept_language = 'accept_language_example' # str | Language locale to filter api results

try:
    # Fetch available Contact methods
    api_response = api_instance.v1_knowledge_bases_id_contacts_get(id, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericAPIApi->v1_knowledge_bases_id_contacts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Knowledgebase id that needs to be fetched. | 
 **accept_language** | **str**| Language locale to filter api results | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_questions_question_id_channels_channel_id_responses_get**
> InlineResponse2004 v1_knowledge_bases_id_questions_question_id_channels_channel_id_responses_get(id, question_id, channel_id, accept_language)

Fetch Response related to a specified Question for a specific Channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GenericAPIApi(swagger_client.ApiClient(configuration))
id = 56 # int | The Knowledgebase id that needs to be fetched.
question_id = 56 # int | The Question id that needs to be fetched.
channel_id = 56 # int | The Channel id that needs to be fetched.
accept_language = 'accept_language_example' # str | Language locale to filter api results

try:
    # Fetch Response related to a specified Question for a specific Channel
    api_response = api_instance.v1_knowledge_bases_id_questions_question_id_channels_channel_id_responses_get(id, question_id, channel_id, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericAPIApi->v1_knowledge_bases_id_questions_question_id_channels_channel_id_responses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Knowledgebase id that needs to be fetched. | 
 **question_id** | **int**| The Question id that needs to be fetched. | 
 **channel_id** | **int**| The Channel id that needs to be fetched. | 
 **accept_language** | **str**| Language locale to filter api results | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_post**
> InlineResponse2005 v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_post(accept_language, id, question_id, response_id, body=body)

Post a Response Satisfaction on a specified Response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GenericAPIApi(swagger_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language locale to filter api results
id = 56 # int | The knowledgebase id that needs to be fetched.
question_id = 56 # int | The Question id that needs to be fetched.
response_id = 56 # int | The Response id that needs to be fetched.
body = swagger_client.ResponseIdResponsessatisfactionsBody() # ResponseIdResponsessatisfactionsBody |  (optional)

try:
    # Post a Response Satisfaction on a specified Response
    api_response = api_instance.v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_post(accept_language, id, question_id, response_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericAPIApi->v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language locale to filter api results | 
 **id** | **int**| The knowledgebase id that needs to be fetched. | 
 **question_id** | **int**| The Question id that needs to be fetched. | 
 **response_id** | **int**| The Response id that needs to be fetched. | 
 **body** | [**ResponseIdResponsessatisfactionsBody**](ResponseIdResponsessatisfactionsBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_satisfaction_id_patch**
> InlineResponse2008 v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_satisfaction_id_patch(accept_language, id, question_id, response_id, satisfaction_id, body=body)

Update a Response Satisfaction on a specified Response to provide a Reason

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GenericAPIApi(swagger_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language locale to filter api results
id = 56 # int | The knowledgebase id that needs to be fetched.
question_id = 56 # int | The Question id that needs to be fetched.
response_id = 56 # int | The Response id that needs to be fetched.
satisfaction_id = 56 # int | The Response satisfaction id that needs to be fetched.
body = swagger_client.ResponsessatisfactionsSatisfactionIdBody() # ResponsessatisfactionsSatisfactionIdBody |  (optional)

try:
    # Update a Response Satisfaction on a specified Response to provide a Reason
    api_response = api_instance.v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_satisfaction_id_patch(accept_language, id, question_id, response_id, satisfaction_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericAPIApi->v1_knowledge_bases_id_questions_question_id_responses_response_id_responses_satisfactions_satisfaction_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language locale to filter api results | 
 **id** | **int**| The knowledgebase id that needs to be fetched. | 
 **question_id** | **int**| The Question id that needs to be fetched. | 
 **response_id** | **int**| The Response id that needs to be fetched. | 
 **satisfaction_id** | **int**| The Response satisfaction id that needs to be fetched. | 
 **body** | [**ResponsessatisfactionsSatisfactionIdBody**](ResponsessatisfactionsSatisfactionIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_reason_comments_get**
> InlineResponse2007 v1_knowledge_bases_id_reason_comments_get(id, accept_language, start_date, channel, extended=extended)

Fetch available comments for negative vote Reasons

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GenericAPIApi(swagger_client.ApiClient(configuration))
id = 56 # int | The Knowledgebase id that needs to be fetched.
accept_language = 'accept_language_example' # str | Language locale to filter api results
start_date = 'start_date_example' # str | Start Date in yyyy-mm-dd format. Comments fetched are created at startDate (between 00:00:00 and 23:59:59)
channel = 'channel_example' # str | The channel name of the responses affected by comments
extended = true # bool | used to display additional information : thematics list and response content associated to the question (optional)

try:
    # Fetch available comments for negative vote Reasons
    api_response = api_instance.v1_knowledge_bases_id_reason_comments_get(id, accept_language, start_date, channel, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericAPIApi->v1_knowledge_bases_id_reason_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Knowledgebase id that needs to be fetched. | 
 **accept_language** | **str**| Language locale to filter api results | 
 **start_date** | **str**| Start Date in yyyy-mm-dd format. Comments fetched are created at startDate (between 00:00:00 and 23:59:59) | 
 **channel** | **str**| The channel name of the responses affected by comments | 
 **extended** | **bool**| used to display additional information : thematics list and response content associated to the question | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_knowledge_bases_id_reasons_get**
> InlineResponse2006 v1_knowledge_bases_id_reasons_get(id, accept_language)

Fetch available negative vote Reasons

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GenericAPIApi(swagger_client.ApiClient(configuration))
id = 56 # int | The Knowledgebase id that needs to be fetched.
accept_language = 'accept_language_example' # str | Language locale to filter api results

try:
    # Fetch available negative vote Reasons
    api_response = api_instance.v1_knowledge_bases_id_reasons_get(id, accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericAPIApi->v1_knowledge_bases_id_reasons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Knowledgebase id that needs to be fetched. | 
 **accept_language** | **str**| Language locale to filter api results | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


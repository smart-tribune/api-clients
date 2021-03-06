
/*
 * Smart Tribune V2 API
 *
 * The purpose of this API is to allow developers to build front-end interfaces for displaying knowledge base data (Faq, Helpbox, Chatbot ...) ## Authorization and API Requests To access the API, all requests need an api-token to be passed in the Authorization request header as a bearer token. **Authorization**: Bearer api-token You can retrieve your api-token using the POST request to **_/v1/auth**.  ## Rate Limiting  We currently limit the number of API requests per IP address on a specific window of 1s. When the rate limit is exceeded for a given API endpoint, the API will return either HTTP 429 Too Many Requests or HTTP 503 Service Unavailable response.  ### Find below Standard API rate limits per window:  | Endpoints | User limit per window | |---|---| | POST  *_/v1/auth* | 2 | | GET   *_/v1/knowledge-bases* | 2 | | POST  *_/v1/knowledge-bases/{id}/filtered/questions* | 10 | | POST  *_/v1/knowledge-bases/{id}/filtered/thematics* | 10 | | GET   *_/v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses* | 10 | | POST  *_/v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions* | 2 | | GET   *_/v1/knowledge-bases/{id}/reasons* | 2 | | GET   *_/v1/knowledge-bases/{id}/reasons-comments* | 2 | | PATCH *_/v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId}* | 2 | | GET *_/v1/knowledge-bases/{id}/contacts* | 2 | 
 *
 * API version: 1.0.5
 * Contact: devs@smart-tribune.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

import (
	"context"
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"
	"fmt"
	"github.com/antihax/optional"
)

// Linger please
var (
	_ context.Context
)

type FilteredAPIApiService service
/*
FilteredAPIApiService Fetch a (list of) Question(s) depend on specified Filters
 * @param ctx context.Context - for authentication, logging, cancellation, deadlines, tracing, etc. Passed from http.Request or context.Background().
 * @param acceptLanguage Language locale to filter api results
 * @param id The knowledgebase Id that needs to be fetched.
 * @param optional nil or *FilteredAPIApiV1KnowledgeBasesIdFilteredQuestionsPostOpts - Optional Parameters:
     * @param "Body" (optional.Interface of FilteredQuestionsPayload) -  **Example of payloads to fetch** :

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

     * @param "Page" (optional.Int32) -  Page identifier
     * @param "Limit" (optional.Int32) -  Items per page
@return InlineResponse2001
*/

type FilteredAPIApiV1KnowledgeBasesIdFilteredQuestionsPostOpts struct {
    Body optional.Interface
    Page optional.Int32
    Limit optional.Int32
}

func (a *FilteredAPIApiService) V1KnowledgeBasesIdFilteredQuestionsPost(ctx context.Context, acceptLanguage string, id int32, localVarOptionals *FilteredAPIApiV1KnowledgeBasesIdFilteredQuestionsPostOpts) (InlineResponse2001, *http.Response, error) {
	var (
		localVarHttpMethod = strings.ToUpper("Post")
		localVarPostBody   interface{}
		localVarFileName   string
		localVarFileBytes  []byte
		localVarReturnValue InlineResponse2001
	)

	// create path and map variables
	localVarPath := a.client.cfg.BasePath + "/v1/knowledge-bases/{id}/filtered/questions"
	localVarPath = strings.Replace(localVarPath, "{"+"id"+"}", fmt.Sprintf("%v", id), -1)

	localVarHeaderParams := make(map[string]string)
	localVarQueryParams := url.Values{}
	localVarFormParams := url.Values{}

	if localVarOptionals != nil && localVarOptionals.Page.IsSet() {
		localVarQueryParams.Add("page", parameterToString(localVarOptionals.Page.Value(), ""))
	}
	if localVarOptionals != nil && localVarOptionals.Limit.IsSet() {
		localVarQueryParams.Add("limit", parameterToString(localVarOptionals.Limit.Value(), ""))
	}
	// to determine the Content-Type header
	localVarHttpContentTypes := []string{"application/json"}

	// set Content-Type header
	localVarHttpContentType := selectHeaderContentType(localVarHttpContentTypes)
	if localVarHttpContentType != "" {
		localVarHeaderParams["Content-Type"] = localVarHttpContentType
	}

	// to determine the Accept header
	localVarHttpHeaderAccepts := []string{"application/json"}

	// set Accept header
	localVarHttpHeaderAccept := selectHeaderAccept(localVarHttpHeaderAccepts)
	if localVarHttpHeaderAccept != "" {
		localVarHeaderParams["Accept"] = localVarHttpHeaderAccept
	}
	localVarHeaderParams["Accept-Language"] = parameterToString(acceptLanguage, "")
	// body params
	if localVarOptionals != nil && localVarOptionals.Body.IsSet() {
		
		localVarOptionalBody:= localVarOptionals.Body.Value()
		localVarPostBody = &localVarOptionalBody
	}
	r, err := a.client.prepareRequest(ctx, localVarPath, localVarHttpMethod, localVarPostBody, localVarHeaderParams, localVarQueryParams, localVarFormParams, localVarFileName, localVarFileBytes)
	if err != nil {
		return localVarReturnValue, nil, err
	}

	localVarHttpResponse, err := a.client.callAPI(r)
	if err != nil || localVarHttpResponse == nil {
		return localVarReturnValue, localVarHttpResponse, err
	}

	localVarBody, err := ioutil.ReadAll(localVarHttpResponse.Body)
	localVarHttpResponse.Body.Close()
	if err != nil {
		return localVarReturnValue, localVarHttpResponse, err
	}

	if localVarHttpResponse.StatusCode < 300 {
		// If we succeed, return the data, otherwise pass on to decode error.
		err = a.client.decode(&localVarReturnValue, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
		if err == nil { 
			return localVarReturnValue, localVarHttpResponse, err
		}
	}

	if localVarHttpResponse.StatusCode >= 300 {
		newErr := GenericSwaggerError{
			body: localVarBody,
			error: localVarHttpResponse.Status,
		}
		if localVarHttpResponse.StatusCode == 200 {
			var v InlineResponse2001
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 400 {
			var v ModelError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 401 {
			var v UnauthorizedError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 403 {
			var v ForbiddenError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 404 {
			var v NotFoundError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 429 {
			var v TooManyRequestError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 503 {
			var v ServiceUnavailableError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		return localVarReturnValue, localVarHttpResponse, newErr
	}

	return localVarReturnValue, localVarHttpResponse, nil
}
/*
FilteredAPIApiService Fetch a (list of) Thematic(s) depend on specified Filters
 * @param ctx context.Context - for authentication, logging, cancellation, deadlines, tracing, etc. Passed from http.Request or context.Background().
 * @param acceptLanguage Language locale to filter api results
 * @param id The knowledgebase Id that needs to be fetched.
 * @param optional nil or *FilteredAPIApiV1KnowledgeBasesIdFilteredThematicsPostOpts - Optional Parameters:
     * @param "Body" (optional.Interface of FilteredThematicsPayload) -  **Example of payloads to fetch** :

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

     * @param "Page" (optional.Int32) -  Page identifier
     * @param "Limit" (optional.Int32) -  Items per page
@return InlineResponse2002
*/

type FilteredAPIApiV1KnowledgeBasesIdFilteredThematicsPostOpts struct {
    Body optional.Interface
    Page optional.Int32
    Limit optional.Int32
}

func (a *FilteredAPIApiService) V1KnowledgeBasesIdFilteredThematicsPost(ctx context.Context, acceptLanguage string, id int32, localVarOptionals *FilteredAPIApiV1KnowledgeBasesIdFilteredThematicsPostOpts) (InlineResponse2002, *http.Response, error) {
	var (
		localVarHttpMethod = strings.ToUpper("Post")
		localVarPostBody   interface{}
		localVarFileName   string
		localVarFileBytes  []byte
		localVarReturnValue InlineResponse2002
	)

	// create path and map variables
	localVarPath := a.client.cfg.BasePath + "/v1/knowledge-bases/{id}/filtered/thematics"
	localVarPath = strings.Replace(localVarPath, "{"+"id"+"}", fmt.Sprintf("%v", id), -1)

	localVarHeaderParams := make(map[string]string)
	localVarQueryParams := url.Values{}
	localVarFormParams := url.Values{}

	if localVarOptionals != nil && localVarOptionals.Page.IsSet() {
		localVarQueryParams.Add("page", parameterToString(localVarOptionals.Page.Value(), ""))
	}
	if localVarOptionals != nil && localVarOptionals.Limit.IsSet() {
		localVarQueryParams.Add("limit", parameterToString(localVarOptionals.Limit.Value(), ""))
	}
	// to determine the Content-Type header
	localVarHttpContentTypes := []string{"application/json"}

	// set Content-Type header
	localVarHttpContentType := selectHeaderContentType(localVarHttpContentTypes)
	if localVarHttpContentType != "" {
		localVarHeaderParams["Content-Type"] = localVarHttpContentType
	}

	// to determine the Accept header
	localVarHttpHeaderAccepts := []string{"application/json"}

	// set Accept header
	localVarHttpHeaderAccept := selectHeaderAccept(localVarHttpHeaderAccepts)
	if localVarHttpHeaderAccept != "" {
		localVarHeaderParams["Accept"] = localVarHttpHeaderAccept
	}
	localVarHeaderParams["Accept-Language"] = parameterToString(acceptLanguage, "")
	// body params
	if localVarOptionals != nil && localVarOptionals.Body.IsSet() {
		
		localVarOptionalBody:= localVarOptionals.Body.Value()
		localVarPostBody = &localVarOptionalBody
	}
	r, err := a.client.prepareRequest(ctx, localVarPath, localVarHttpMethod, localVarPostBody, localVarHeaderParams, localVarQueryParams, localVarFormParams, localVarFileName, localVarFileBytes)
	if err != nil {
		return localVarReturnValue, nil, err
	}

	localVarHttpResponse, err := a.client.callAPI(r)
	if err != nil || localVarHttpResponse == nil {
		return localVarReturnValue, localVarHttpResponse, err
	}

	localVarBody, err := ioutil.ReadAll(localVarHttpResponse.Body)
	localVarHttpResponse.Body.Close()
	if err != nil {
		return localVarReturnValue, localVarHttpResponse, err
	}

	if localVarHttpResponse.StatusCode < 300 {
		// If we succeed, return the data, otherwise pass on to decode error.
		err = a.client.decode(&localVarReturnValue, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
		if err == nil { 
			return localVarReturnValue, localVarHttpResponse, err
		}
	}

	if localVarHttpResponse.StatusCode >= 300 {
		newErr := GenericSwaggerError{
			body: localVarBody,
			error: localVarHttpResponse.Status,
		}
		if localVarHttpResponse.StatusCode == 200 {
			var v InlineResponse2002
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 400 {
			var v ModelError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 401 {
			var v UnauthorizedError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 403 {
			var v ForbiddenError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 404 {
			var v NotFoundError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 429 {
			var v TooManyRequestError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		if localVarHttpResponse.StatusCode == 503 {
			var v ServiceUnavailableError
			err = a.client.decode(&v, localVarBody, localVarHttpResponse.Header.Get("Content-Type"));
				if err != nil {
					newErr.error = err.Error()
					return localVarReturnValue, localVarHttpResponse, newErr
				}
				newErr.model = v
				return localVarReturnValue, localVarHttpResponse, newErr
		}
		return localVarReturnValue, localVarHttpResponse, newErr
	}

	return localVarReturnValue, localVarHttpResponse, nil
}

# io.swagger.client - Kotlin client library for Smart Tribune V2 API

## Requires

* Kotlin 1.4.30
* Gradle 5.3

## Build

First, create the gradle wrapper script:

```
gradle wrapper
```

Then, run:

```
./gradlew check assemble
```

This runs all tests and packages the library.

## Features/Implementation Notes

* Supports JSON inputs/outputs, File inputs, and Form inputs.
* Supports collection formats for query parameters: csv, tsv, ssv, pipes.
* Some Kotlin and Java types are fully qualified to avoid conflicts with types defined in Swagger definitions.
* Implementation of ApiClient is intended to reduce method counts, specifically to benefit Android targets.

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://api-gateway.app.smart-tribune.com/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**v1AuthPost**](docs/AuthenticationApi.md#v1authpost) | **POST** /v1/auth | Authenticate through our API
*FilteredAPIApi* | [**v1KnowledgeBasesIdFilteredQuestionsPost**](docs/FilteredAPIApi.md#v1knowledgebasesidfilteredquestionspost) | **POST** /v1/knowledge-bases/{id}/filtered/questions | Fetch a (list of) Question(s) depend on specified Filters
*FilteredAPIApi* | [**v1KnowledgeBasesIdFilteredThematicsPost**](docs/FilteredAPIApi.md#v1knowledgebasesidfilteredthematicspost) | **POST** /v1/knowledge-bases/{id}/filtered/thematics | Fetch a (list of) Thematic(s) depend on specified Filters
*GenericAPIApi* | [**v1KnowledgeBasesGet**](docs/GenericAPIApi.md#v1knowledgebasesget) | **GET** /v1/knowledge-bases | Fetch allowed Knowledge bases
*GenericAPIApi* | [**v1KnowledgeBasesIdContactsGet**](docs/GenericAPIApi.md#v1knowledgebasesidcontactsget) | **GET** /v1/knowledge-bases/{id}/contacts | Fetch available Contact methods
*GenericAPIApi* | [**v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet**](docs/GenericAPIApi.md#v1knowledgebasesidquestionsquestionidchannelschannelidresponsesget) | **GET** /v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses | Fetch Response related to a specified Question for a specific Channel
*GenericAPIApi* | [**v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost**](docs/GenericAPIApi.md#v1knowledgebasesidquestionsquestionidresponsesresponseidresponsessatisfactionspost) | **POST** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions | Post a Response Satisfaction on a specified Response
*GenericAPIApi* | [**v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch**](docs/GenericAPIApi.md#v1knowledgebasesidquestionsquestionidresponsesresponseidresponsessatisfactionssatisfactionidpatch) | **PATCH** /v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId} | Update a Response Satisfaction on a specified Response to provide a Reason
*GenericAPIApi* | [**v1KnowledgeBasesIdReasonCommentsGet**](docs/GenericAPIApi.md#v1knowledgebasesidreasoncommentsget) | **GET** /v1/knowledge-bases/{id}/reason-comments | Fetch available comments for negative vote Reasons
*GenericAPIApi* | [**v1KnowledgeBasesIdReasonsGet**](docs/GenericAPIApi.md#v1knowledgebasesidreasonsget) | **GET** /v1/knowledge-bases/{id}/reasons | Fetch available negative vote Reasons

<a name="documentation-for-models"></a>
## Documentation for Models

 - [io.swagger.client.models.AnyOfFilteredQuestionsPayloadSearchFiltersItems](docs/AnyOfFilteredQuestionsPayloadSearchFiltersItems.md)
 - [io.swagger.client.models.AnyOfFilteredQuestionsPayloadSearchFiltersOperatorsItems](docs/AnyOfFilteredQuestionsPayloadSearchFiltersOperatorsItems.md)
 - [io.swagger.client.models.AnyOfFilteredThematicsPayloadSearchFiltersItems](docs/AnyOfFilteredThematicsPayloadSearchFiltersItems.md)
 - [io.swagger.client.models.Auth](docs/Auth.md)
 - [io.swagger.client.models.Channel](docs/Channel.md)
 - [io.swagger.client.models.Contact](docs/Contact.md)
 - [io.swagger.client.models.ContactConfiguration](docs/ContactConfiguration.md)
 - [io.swagger.client.models.Content](docs/Content.md)
 - [io.swagger.client.models.Error](docs/Error.md)
 - [io.swagger.client.models.FilteredQuestionsData](docs/FilteredQuestionsData.md)
 - [io.swagger.client.models.FilteredQuestionsDataLinkedQuestion](docs/FilteredQuestionsDataLinkedQuestion.md)
 - [io.swagger.client.models.FilteredQuestionsPayload](docs/FilteredQuestionsPayload.md)
 - [io.swagger.client.models.FilteredThematicsPayload](docs/FilteredThematicsPayload.md)
 - [io.swagger.client.models.ForbiddenError](docs/ForbiddenError.md)
 - [io.swagger.client.models.Image](docs/Image.md)
 - [io.swagger.client.models.InlineResponse200](docs/InlineResponse200.md)
 - [io.swagger.client.models.InlineResponse2001](docs/InlineResponse2001.md)
 - [io.swagger.client.models.InlineResponse2002](docs/InlineResponse2002.md)
 - [io.swagger.client.models.InlineResponse2003](docs/InlineResponse2003.md)
 - [io.swagger.client.models.InlineResponse2004](docs/InlineResponse2004.md)
 - [io.swagger.client.models.InlineResponse2005](docs/InlineResponse2005.md)
 - [io.swagger.client.models.InlineResponse2006](docs/InlineResponse2006.md)
 - [io.swagger.client.models.InlineResponse2007](docs/InlineResponse2007.md)
 - [io.swagger.client.models.InlineResponse2008](docs/InlineResponse2008.md)
 - [io.swagger.client.models.InlineResponse2009](docs/InlineResponse2009.md)
 - [io.swagger.client.models.KnowledgeBase](docs/KnowledgeBase.md)
 - [io.swagger.client.models.Language](docs/Language.md)
 - [io.swagger.client.models.Meta](docs/Meta.md)
 - [io.swagger.client.models.MetaWithQuery](docs/MetaWithQuery.md)
 - [io.swagger.client.models.NotFoundError](docs/NotFoundError.md)
 - [io.swagger.client.models.Reason](docs/Reason.md)
 - [io.swagger.client.models.ReasonComment](docs/ReasonComment.md)
 - [io.swagger.client.models.Response](docs/Response.md)
 - [io.swagger.client.models.ResponseIdResponsessatisfactionsBody](docs/ResponseIdResponsessatisfactionsBody.md)
 - [io.swagger.client.models.ResponsessatisfactionsSatisfactionIdBody](docs/ResponsessatisfactionsSatisfactionIdBody.md)
 - [io.swagger.client.models.SearchFiltersOperatorsTag](docs/SearchFiltersOperatorsTag.md)
 - [io.swagger.client.models.SearchFiltersOperatorsThematic](docs/SearchFiltersOperatorsThematic.md)
 - [io.swagger.client.models.SearchFiltersTagName](docs/SearchFiltersTagName.md)
 - [io.swagger.client.models.SearchFiltersThematicName](docs/SearchFiltersThematicName.md)
 - [io.swagger.client.models.SearchFiltersThematicSlug](docs/SearchFiltersThematicSlug.md)
 - [io.swagger.client.models.ServiceUnavailableError](docs/ServiceUnavailableError.md)
 - [io.swagger.client.models.Tag](docs/Tag.md)
 - [io.swagger.client.models.Thematic](docs/Thematic.md)
 - [io.swagger.client.models.TooManyRequestError](docs/TooManyRequestError.md)
 - [io.swagger.client.models.UnauthorizedError](docs/UnauthorizedError.md)

<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="bearerAuth"></a>
### bearerAuth



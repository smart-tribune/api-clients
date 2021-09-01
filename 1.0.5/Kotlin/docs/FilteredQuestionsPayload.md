# FilteredQuestionsPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**inline**](#ChannelEnum) |  |  [optional]
**promoted** | [**kotlin.Boolean**](.md) |  |  [optional]
**frequent** | [**kotlin.Boolean**](.md) |  |  [optional]
**query** | [**kotlin.String**](.md) |  |  [optional]
**useSuggester** | [**kotlin.Boolean**](.md) |  |  [optional]
**excludedQuestions** | [**kotlin.Array&lt;kotlin.Int&gt;**](.md) |  |  [optional]
**questionSlug** | [**kotlin.String**](.md) |  |  [optional]
**searchFilters** | [**kotlin.Array&lt;AnyOfFilteredQuestionsPayloadSearchFiltersItems&gt;**](.md) |  |  [optional]
**searchFiltersOperators** | [**kotlin.Array&lt;AnyOfFilteredQuestionsPayloadSearchFiltersOperatorsItems&gt;**](.md) |  |  [optional]
**limit** | [**kotlin.Int**](.md) |  |  [optional]

<a name="ChannelEnum"></a>
## Enum: channel
Name | Value
---- | -----
channel | faq, push, bot

# coding: utf-8

"""
    Smart Tribune V2 API

    The purpose of this API is to allow developers to build front-end interfaces for displaying knowledge base data (Faq, Helpbox, Chatbot ...) ## Authorization and API Requests To access the API, all requests need an api-token to be passed in the Authorization request header as a bearer token. **Authorization**: Bearer api-token You can retrieve your api-token using the POST request to **/v1/auth**.  ## Rate Limiting  We currently limit the number of API requests per IP address on a specific window of 1s. When the rate limit is exceeded for a given API endpoint, the API will return either HTTP 429 Too Many Requests or HTTP 503 Service Unavailable response.  ### Find below Standard API rate limits per window:  | Endpoints | User limit per window | |---|---| | POST  */v1/auth* | 2 | | GET   */v1/knowledge-bases* | 2 | | POST  */v1/knowledge-bases/{id}/filtered/questions* | 10 | | POST  */v1/knowledge-bases/{id}/filtered/thematics* | 10 | | GET   */v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses* | 10 | | POST  */v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions* | 2 | | GET   */v1/knowledge-bases/{id}/reasons* | 2 | | GET   */v1/knowledge-bases/{id}/reasons-comments* | 2 | | PATCH */v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId}* | 2 | | GET */v1/knowledge-bases/{id}/contacts* | 2 |   # noqa: E501

    OpenAPI spec version: 1.0.5
    Contact: devs@smart-tribune.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FilteredQuestionsPayload(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel': 'str',
        'promoted': 'bool',
        'frequent': 'bool',
        'query': 'str',
        'use_suggester': 'bool',
        'excluded_questions': 'list[int]',
        'question_slug': 'str',
        'search_filters': 'list[AnyOfFilteredQuestionsPayloadSearchFiltersItems]',
        'search_filters_operators': 'list[AnyOfFilteredQuestionsPayloadSearchFiltersOperatorsItems]',
        'limit': 'int'
    }

    attribute_map = {
        'channel': 'channel',
        'promoted': 'promoted',
        'frequent': 'frequent',
        'query': 'query',
        'use_suggester': 'useSuggester',
        'excluded_questions': 'excludedQuestions',
        'question_slug': 'questionSlug',
        'search_filters': 'searchFilters',
        'search_filters_operators': 'searchFiltersOperators',
        'limit': 'limit'
    }

    def __init__(self, channel=None, promoted=None, frequent=None, query=None, use_suggester=None, excluded_questions=None, question_slug=None, search_filters=None, search_filters_operators=None, limit=None):  # noqa: E501
        """FilteredQuestionsPayload - a model defined in Swagger"""  # noqa: E501
        self._channel = None
        self._promoted = None
        self._frequent = None
        self._query = None
        self._use_suggester = None
        self._excluded_questions = None
        self._question_slug = None
        self._search_filters = None
        self._search_filters_operators = None
        self._limit = None
        self.discriminator = None
        if channel is not None:
            self.channel = channel
        if promoted is not None:
            self.promoted = promoted
        if frequent is not None:
            self.frequent = frequent
        if query is not None:
            self.query = query
        if use_suggester is not None:
            self.use_suggester = use_suggester
        if excluded_questions is not None:
            self.excluded_questions = excluded_questions
        if question_slug is not None:
            self.question_slug = question_slug
        if search_filters is not None:
            self.search_filters = search_filters
        if search_filters_operators is not None:
            self.search_filters_operators = search_filters_operators
        if limit is not None:
            self.limit = limit

    @property
    def channel(self):
        """Gets the channel of this FilteredQuestionsPayload.  # noqa: E501


        :return: The channel of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this FilteredQuestionsPayload.


        :param channel: The channel of this FilteredQuestionsPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["faq", "push", "bot"]  # noqa: E501
        if channel not in allowed_values:
            raise ValueError(
                "Invalid value for `channel` ({0}), must be one of {1}"  # noqa: E501
                .format(channel, allowed_values)
            )

        self._channel = channel

    @property
    def promoted(self):
        """Gets the promoted of this FilteredQuestionsPayload.  # noqa: E501


        :return: The promoted of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: bool
        """
        return self._promoted

    @promoted.setter
    def promoted(self, promoted):
        """Sets the promoted of this FilteredQuestionsPayload.


        :param promoted: The promoted of this FilteredQuestionsPayload.  # noqa: E501
        :type: bool
        """

        self._promoted = promoted

    @property
    def frequent(self):
        """Gets the frequent of this FilteredQuestionsPayload.  # noqa: E501


        :return: The frequent of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: bool
        """
        return self._frequent

    @frequent.setter
    def frequent(self, frequent):
        """Sets the frequent of this FilteredQuestionsPayload.


        :param frequent: The frequent of this FilteredQuestionsPayload.  # noqa: E501
        :type: bool
        """

        self._frequent = frequent

    @property
    def query(self):
        """Gets the query of this FilteredQuestionsPayload.  # noqa: E501


        :return: The query of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this FilteredQuestionsPayload.


        :param query: The query of this FilteredQuestionsPayload.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def use_suggester(self):
        """Gets the use_suggester of this FilteredQuestionsPayload.  # noqa: E501


        :return: The use_suggester of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: bool
        """
        return self._use_suggester

    @use_suggester.setter
    def use_suggester(self, use_suggester):
        """Sets the use_suggester of this FilteredQuestionsPayload.


        :param use_suggester: The use_suggester of this FilteredQuestionsPayload.  # noqa: E501
        :type: bool
        """

        self._use_suggester = use_suggester

    @property
    def excluded_questions(self):
        """Gets the excluded_questions of this FilteredQuestionsPayload.  # noqa: E501


        :return: The excluded_questions of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_questions

    @excluded_questions.setter
    def excluded_questions(self, excluded_questions):
        """Sets the excluded_questions of this FilteredQuestionsPayload.


        :param excluded_questions: The excluded_questions of this FilteredQuestionsPayload.  # noqa: E501
        :type: list[int]
        """

        self._excluded_questions = excluded_questions

    @property
    def question_slug(self):
        """Gets the question_slug of this FilteredQuestionsPayload.  # noqa: E501


        :return: The question_slug of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: str
        """
        return self._question_slug

    @question_slug.setter
    def question_slug(self, question_slug):
        """Sets the question_slug of this FilteredQuestionsPayload.


        :param question_slug: The question_slug of this FilteredQuestionsPayload.  # noqa: E501
        :type: str
        """

        self._question_slug = question_slug

    @property
    def search_filters(self):
        """Gets the search_filters of this FilteredQuestionsPayload.  # noqa: E501


        :return: The search_filters of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: list[AnyOfFilteredQuestionsPayloadSearchFiltersItems]
        """
        return self._search_filters

    @search_filters.setter
    def search_filters(self, search_filters):
        """Sets the search_filters of this FilteredQuestionsPayload.


        :param search_filters: The search_filters of this FilteredQuestionsPayload.  # noqa: E501
        :type: list[AnyOfFilteredQuestionsPayloadSearchFiltersItems]
        """

        self._search_filters = search_filters

    @property
    def search_filters_operators(self):
        """Gets the search_filters_operators of this FilteredQuestionsPayload.  # noqa: E501


        :return: The search_filters_operators of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: list[AnyOfFilteredQuestionsPayloadSearchFiltersOperatorsItems]
        """
        return self._search_filters_operators

    @search_filters_operators.setter
    def search_filters_operators(self, search_filters_operators):
        """Sets the search_filters_operators of this FilteredQuestionsPayload.


        :param search_filters_operators: The search_filters_operators of this FilteredQuestionsPayload.  # noqa: E501
        :type: list[AnyOfFilteredQuestionsPayloadSearchFiltersOperatorsItems]
        """

        self._search_filters_operators = search_filters_operators

    @property
    def limit(self):
        """Gets the limit of this FilteredQuestionsPayload.  # noqa: E501


        :return: The limit of this FilteredQuestionsPayload.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this FilteredQuestionsPayload.


        :param limit: The limit of this FilteredQuestionsPayload.  # noqa: E501
        :type: int
        """

        self._limit = limit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FilteredQuestionsPayload, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FilteredQuestionsPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

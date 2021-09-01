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

class FilteredQuestionsDataLinkedQuestion(object):
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
        'id': 'int',
        'title': 'str',
        'slug': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'slug': 'slug'
    }

    def __init__(self, id=None, title=None, slug=None):  # noqa: E501
        """FilteredQuestionsDataLinkedQuestion - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._slug = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if slug is not None:
            self.slug = slug

    @property
    def id(self):
        """Gets the id of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501


        :return: The id of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FilteredQuestionsDataLinkedQuestion.


        :param id: The id of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501


        :return: The title of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FilteredQuestionsDataLinkedQuestion.


        :param title: The title of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def slug(self):
        """Gets the slug of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501


        :return: The slug of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this FilteredQuestionsDataLinkedQuestion.


        :param slug: The slug of this FilteredQuestionsDataLinkedQuestion.  # noqa: E501
        :type: str
        """

        self._slug = slug

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
        if issubclass(FilteredQuestionsDataLinkedQuestion, dict):
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
        if not isinstance(other, FilteredQuestionsDataLinkedQuestion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
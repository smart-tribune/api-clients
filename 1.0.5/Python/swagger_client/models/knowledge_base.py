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

class KnowledgeBase(object):
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
        'name': 'str',
        'account': 'int',
        'languages': 'list[Language]',
        'channels': 'list[Channel]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'account': 'account',
        'languages': 'languages',
        'channels': 'channels'
    }

    def __init__(self, id=None, name=None, account=None, languages=None, channels=None):  # noqa: E501
        """KnowledgeBase - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._account = None
        self._languages = None
        self._channels = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if account is not None:
            self.account = account
        if languages is not None:
            self.languages = languages
        if channels is not None:
            self.channels = channels

    @property
    def id(self):
        """Gets the id of this KnowledgeBase.  # noqa: E501


        :return: The id of this KnowledgeBase.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KnowledgeBase.


        :param id: The id of this KnowledgeBase.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this KnowledgeBase.  # noqa: E501


        :return: The name of this KnowledgeBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KnowledgeBase.


        :param name: The name of this KnowledgeBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account(self):
        """Gets the account of this KnowledgeBase.  # noqa: E501


        :return: The account of this KnowledgeBase.  # noqa: E501
        :rtype: int
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this KnowledgeBase.


        :param account: The account of this KnowledgeBase.  # noqa: E501
        :type: int
        """

        self._account = account

    @property
    def languages(self):
        """Gets the languages of this KnowledgeBase.  # noqa: E501


        :return: The languages of this KnowledgeBase.  # noqa: E501
        :rtype: list[Language]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this KnowledgeBase.


        :param languages: The languages of this KnowledgeBase.  # noqa: E501
        :type: list[Language]
        """

        self._languages = languages

    @property
    def channels(self):
        """Gets the channels of this KnowledgeBase.  # noqa: E501


        :return: The channels of this KnowledgeBase.  # noqa: E501
        :rtype: list[Channel]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this KnowledgeBase.


        :param channels: The channels of this KnowledgeBase.  # noqa: E501
        :type: list[Channel]
        """

        self._channels = channels

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
        if issubclass(KnowledgeBase, dict):
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
        if not isinstance(other, KnowledgeBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class ReasonComment(object):
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
        '_date': 'str',
        'comment': 'str',
        'question_title': 'str',
        'question_id': 'int',
        'reason_title': 'str',
        'thematics': 'str',
        'response_content': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'comment': 'comment',
        'question_title': 'questionTitle',
        'question_id': 'questionId',
        'reason_title': 'reasonTitle',
        'thematics': 'thematics',
        'response_content': 'responseContent'
    }

    def __init__(self, _date=None, comment=None, question_title=None, question_id=None, reason_title=None, thematics=None, response_content=None):  # noqa: E501
        """ReasonComment - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._comment = None
        self._question_title = None
        self._question_id = None
        self._reason_title = None
        self._thematics = None
        self._response_content = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if comment is not None:
            self.comment = comment
        if question_title is not None:
            self.question_title = question_title
        if question_id is not None:
            self.question_id = question_id
        if reason_title is not None:
            self.reason_title = reason_title
        if thematics is not None:
            self.thematics = thematics
        if response_content is not None:
            self.response_content = response_content

    @property
    def _date(self):
        """Gets the _date of this ReasonComment.  # noqa: E501


        :return: The _date of this ReasonComment.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ReasonComment.


        :param _date: The _date of this ReasonComment.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def comment(self):
        """Gets the comment of this ReasonComment.  # noqa: E501


        :return: The comment of this ReasonComment.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ReasonComment.


        :param comment: The comment of this ReasonComment.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def question_title(self):
        """Gets the question_title of this ReasonComment.  # noqa: E501


        :return: The question_title of this ReasonComment.  # noqa: E501
        :rtype: str
        """
        return self._question_title

    @question_title.setter
    def question_title(self, question_title):
        """Sets the question_title of this ReasonComment.


        :param question_title: The question_title of this ReasonComment.  # noqa: E501
        :type: str
        """

        self._question_title = question_title

    @property
    def question_id(self):
        """Gets the question_id of this ReasonComment.  # noqa: E501


        :return: The question_id of this ReasonComment.  # noqa: E501
        :rtype: int
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this ReasonComment.


        :param question_id: The question_id of this ReasonComment.  # noqa: E501
        :type: int
        """

        self._question_id = question_id

    @property
    def reason_title(self):
        """Gets the reason_title of this ReasonComment.  # noqa: E501


        :return: The reason_title of this ReasonComment.  # noqa: E501
        :rtype: str
        """
        return self._reason_title

    @reason_title.setter
    def reason_title(self, reason_title):
        """Sets the reason_title of this ReasonComment.


        :param reason_title: The reason_title of this ReasonComment.  # noqa: E501
        :type: str
        """

        self._reason_title = reason_title

    @property
    def thematics(self):
        """Gets the thematics of this ReasonComment.  # noqa: E501


        :return: The thematics of this ReasonComment.  # noqa: E501
        :rtype: str
        """
        return self._thematics

    @thematics.setter
    def thematics(self, thematics):
        """Sets the thematics of this ReasonComment.


        :param thematics: The thematics of this ReasonComment.  # noqa: E501
        :type: str
        """

        self._thematics = thematics

    @property
    def response_content(self):
        """Gets the response_content of this ReasonComment.  # noqa: E501


        :return: The response_content of this ReasonComment.  # noqa: E501
        :rtype: str
        """
        return self._response_content

    @response_content.setter
    def response_content(self, response_content):
        """Sets the response_content of this ReasonComment.


        :param response_content: The response_content of this ReasonComment.  # noqa: E501
        :type: str
        """

        self._response_content = response_content

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
        if issubclass(ReasonComment, dict):
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
        if not isinstance(other, ReasonComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

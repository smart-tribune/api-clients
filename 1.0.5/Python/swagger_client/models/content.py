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

class Content(object):
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
        'body': 'str',
        'html_body': 'str',
        'locale': 'str',
        'status': 'str',
        'images': 'list[Image]'
    }

    attribute_map = {
        'id': 'id',
        'body': 'body',
        'html_body': 'htmlBody',
        'locale': 'locale',
        'status': 'status',
        'images': 'images'
    }

    def __init__(self, id=None, body=None, html_body=None, locale=None, status=None, images=None):  # noqa: E501
        """Content - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._body = None
        self._html_body = None
        self._locale = None
        self._status = None
        self._images = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if body is not None:
            self.body = body
        if html_body is not None:
            self.html_body = html_body
        if locale is not None:
            self.locale = locale
        if status is not None:
            self.status = status
        if images is not None:
            self.images = images

    @property
    def id(self):
        """Gets the id of this Content.  # noqa: E501


        :return: The id of this Content.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Content.


        :param id: The id of this Content.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def body(self):
        """Gets the body of this Content.  # noqa: E501


        :return: The body of this Content.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Content.


        :param body: The body of this Content.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def html_body(self):
        """Gets the html_body of this Content.  # noqa: E501


        :return: The html_body of this Content.  # noqa: E501
        :rtype: str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, html_body):
        """Sets the html_body of this Content.


        :param html_body: The html_body of this Content.  # noqa: E501
        :type: str
        """

        self._html_body = html_body

    @property
    def locale(self):
        """Gets the locale of this Content.  # noqa: E501


        :return: The locale of this Content.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Content.


        :param locale: The locale of this Content.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def status(self):
        """Gets the status of this Content.  # noqa: E501


        :return: The status of this Content.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Content.


        :param status: The status of this Content.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def images(self):
        """Gets the images of this Content.  # noqa: E501


        :return: The images of this Content.  # noqa: E501
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Content.


        :param images: The images of this Content.  # noqa: E501
        :type: list[Image]
        """

        self._images = images

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
        if issubclass(Content, dict):
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
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

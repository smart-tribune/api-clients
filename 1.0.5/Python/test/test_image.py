# coding: utf-8

"""
    Smart Tribune V2 API

    The purpose of this API is to allow developers to build front-end interfaces for displaying knowledge base data (Faq, Helpbox, Chatbot ...) ## Authorization and API Requests To access the API, all requests need an api-token to be passed in the Authorization request header as a bearer token. **Authorization**: Bearer api-token You can retrieve your api-token using the POST request to **/v1/auth**.  ## Rate Limiting  We currently limit the number of API requests per IP address on a specific window of 1s. When the rate limit is exceeded for a given API endpoint, the API will return either HTTP 429 Too Many Requests or HTTP 503 Service Unavailable response.  ### Find below Standard API rate limits per window:  | Endpoints | User limit per window | |---|---| | POST  */v1/auth* | 2 | | GET   */v1/knowledge-bases* | 2 | | POST  */v1/knowledge-bases/{id}/filtered/questions* | 10 | | POST  */v1/knowledge-bases/{id}/filtered/thematics* | 10 | | GET   */v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses* | 10 | | POST  */v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions* | 2 | | GET   */v1/knowledge-bases/{id}/reasons* | 2 | | GET   */v1/knowledge-bases/{id}/reasons-comments* | 2 | | PATCH */v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId}* | 2 | | GET */v1/knowledge-bases/{id}/contacts* | 2 |   # noqa: E501

    OpenAPI spec version: 1.0.5
    Contact: devs@smart-tribune.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.image import Image  # noqa: E501
from swagger_client.rest import ApiException


class TestImage(unittest.TestCase):
    """Image unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImage(self):
        """Test Image"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.image.Image()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

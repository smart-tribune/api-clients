<?php
/**
 * ContactConfigurationTest
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Smart Tribune V2 API
 *
 * The purpose of this API is to allow developers to build front-end interfaces for displaying knowledge base data (Faq, Helpbox, Chatbot ...) ## Authorization and API Requests To access the API, all requests need an api-token to be passed in the Authorization request header as a bearer token. **Authorization**: Bearer api-token You can retrieve your api-token using the POST request to **_/v1/auth**.  ## Rate Limiting  We currently limit the number of API requests per IP address on a specific window of 1s. When the rate limit is exceeded for a given API endpoint, the API will return either HTTP 429 Too Many Requests or HTTP 503 Service Unavailable response.  ### Find below Standard API rate limits per window:  | Endpoints | User limit per window | |---|---| | POST  *_/v1/auth* | 2 | | GET   *_/v1/knowledge-bases* | 2 | | POST  *_/v1/knowledge-bases/{id}/filtered/questions* | 10 | | POST  *_/v1/knowledge-bases/{id}/filtered/thematics* | 10 | | GET   *_/v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses* | 10 | | POST  *_/v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions* | 2 | | GET   *_/v1/knowledge-bases/{id}/reasons* | 2 | | GET   *_/v1/knowledge-bases/{id}/reasons-comments* | 2 | | PATCH *_/v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId}* | 2 | | GET *_/v1/knowledge-bases/{id}/contacts* | 2 |
 *
 * OpenAPI spec version: 1.0.5
 * Contact: devs@smart-tribune.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 3.0.27
 */
/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Please update the test case below to test the model.
 */

namespace Swagger\Client;

/**
 * ContactConfigurationTest Class Doc Comment
 *
 * @category    Class
 * @description ContactConfiguration
 * @package     Swagger\Client
 * @author      Swagger Codegen team
 * @link        https://github.com/swagger-api/swagger-codegen
 */
class ContactConfigurationTest extends \PHPUnit_Framework_TestCase
{

    /**
     * Setup before running any test case
     */
    public static function setUpBeforeClass()
    {
    }

    /**
     * Setup before running each test case
     */
    public function setUp()
    {
    }

    /**
     * Clean up after running each test case
     */
    public function tearDown()
    {
    }

    /**
     * Clean up after running all test cases
     */
    public static function tearDownAfterClass()
    {
    }

    /**
     * Test "ContactConfiguration"
     */
    public function testContactConfiguration()
    {
    }

    /**
     * Test attribute "phone"
     */
    public function testPropertyPhone()
    {
    }

    /**
     * Test attribute "title"
     */
    public function testPropertyTitle()
    {
    }

    /**
     * Test attribute "description"
     */
    public function testPropertyDescription()
    {
    }

    /**
     * Test attribute "apply_all_questions"
     */
    public function testPropertyApplyAllQuestions()
    {
    }

    /**
     * Test attribute "is_active"
     */
    public function testPropertyIsActive()
    {
    }

    /**
     * Test attribute "channels"
     */
    public function testPropertyChannels()
    {
    }

    /**
     * Test attribute "tags"
     */
    public function testPropertyTags()
    {
    }
}

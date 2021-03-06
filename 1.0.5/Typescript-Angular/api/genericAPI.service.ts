/**
 * Smart Tribune V2 API
 * The purpose of this API is to allow developers to build front-end interfaces for displaying knowledge base data (Faq, Helpbox, Chatbot ...) ## Authorization and API Requests To access the API, all requests need an api-token to be passed in the Authorization request header as a bearer token. **Authorization**: Bearer api-token You can retrieve your api-token using the POST request to **_/v1/auth**.  ## Rate Limiting  We currently limit the number of API requests per IP address on a specific window of 1s. When the rate limit is exceeded for a given API endpoint, the API will return either HTTP 429 Too Many Requests or HTTP 503 Service Unavailable response.  ### Find below Standard API rate limits per window:  | Endpoints | User limit per window | |---|---| | POST  *_/v1/auth* | 2 | | GET   *_/v1/knowledge-bases* | 2 | | POST  *_/v1/knowledge-bases/{id}/filtered/questions* | 10 | | POST  *_/v1/knowledge-bases/{id}/filtered/thematics* | 10 | | GET   *_/v1/knowledge-bases/{id}/questions/{questionId}/channels/{channelId}/responses* | 10 | | POST  *_/v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions* | 2 | | GET   *_/v1/knowledge-bases/{id}/reasons* | 2 | | GET   *_/v1/knowledge-bases/{id}/reasons-comments* | 2 | | PATCH *_/v1/knowledge-bases/{id}/questions/{questionId}/responses/{responseId}/responses-satisfactions/{satisfactionId}* | 2 | | GET *_/v1/knowledge-bases/{id}/contacts* | 2 | 
 *
 * OpenAPI spec version: 1.0.5
 * Contact: devs@smart-tribune.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *//* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs';

import { ForbiddenError } from '../model/forbiddenError';
import { InlineResponse2003 } from '../model/inlineResponse2003';
import { InlineResponse2004 } from '../model/inlineResponse2004';
import { InlineResponse2005 } from '../model/inlineResponse2005';
import { InlineResponse2006 } from '../model/inlineResponse2006';
import { InlineResponse2007 } from '../model/inlineResponse2007';
import { InlineResponse2008 } from '../model/inlineResponse2008';
import { InlineResponse2009 } from '../model/inlineResponse2009';
import { NotFoundError } from '../model/notFoundError';
import { ResponseIdResponsessatisfactionsBody } from '../model/responseIdResponsessatisfactionsBody';
import { ResponsessatisfactionsSatisfactionIdBody } from '../model/responsessatisfactionsSatisfactionIdBody';
import { ServiceUnavailableError } from '../model/serviceUnavailableError';
import { TooManyRequestError } from '../model/tooManyRequestError';
import { UnauthorizedError } from '../model/unauthorizedError';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class GenericAPIService {

    protected basePath = 'https://api-gateway.app.smart-tribune.com/';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Fetch allowed Knowledge bases
     * 
     * @param acceptLanguage Language locale to filter api results
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public v1KnowledgeBasesGet(acceptLanguage: string, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse2003>;
    public v1KnowledgeBasesGet(acceptLanguage: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse2003>>;
    public v1KnowledgeBasesGet(acceptLanguage: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse2003>>;
    public v1KnowledgeBasesGet(acceptLanguage: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (acceptLanguage === null || acceptLanguage === undefined) {
            throw new Error('Required parameter acceptLanguage was null or undefined when calling v1KnowledgeBasesGet.');
        }

        let headers = this.defaultHeaders;
        if (acceptLanguage !== undefined && acceptLanguage !== null) {
            headers = headers.set('Accept-Language', String(acceptLanguage));
        }

        // authentication (bearerAuth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }
        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<InlineResponse2003>('get',`${this.basePath}/v1/knowledge-bases`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Fetch available Contact methods
     * 
     * @param id The Knowledgebase id that needs to be fetched.
     * @param acceptLanguage Language locale to filter api results
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public v1KnowledgeBasesIdContactsGet(id: number, acceptLanguage: string, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse2009>;
    public v1KnowledgeBasesIdContactsGet(id: number, acceptLanguage: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse2009>>;
    public v1KnowledgeBasesIdContactsGet(id: number, acceptLanguage: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse2009>>;
    public v1KnowledgeBasesIdContactsGet(id: number, acceptLanguage: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling v1KnowledgeBasesIdContactsGet.');
        }

        if (acceptLanguage === null || acceptLanguage === undefined) {
            throw new Error('Required parameter acceptLanguage was null or undefined when calling v1KnowledgeBasesIdContactsGet.');
        }

        let headers = this.defaultHeaders;
        if (acceptLanguage !== undefined && acceptLanguage !== null) {
            headers = headers.set('Accept-Language', String(acceptLanguage));
        }

        // authentication (bearerAuth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }
        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<InlineResponse2009>('get',`${this.basePath}/v1/knowledge-bases/${encodeURIComponent(String(id))}/contacts`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Fetch Response related to a specified Question for a specific Channel
     * 
     * @param id The Knowledgebase id that needs to be fetched.
     * @param questionId The Question id that needs to be fetched.
     * @param channelId The Channel id that needs to be fetched.
     * @param acceptLanguage Language locale to filter api results
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet(id: number, questionId: number, channelId: number, acceptLanguage: string, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse2004>;
    public v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet(id: number, questionId: number, channelId: number, acceptLanguage: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse2004>>;
    public v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet(id: number, questionId: number, channelId: number, acceptLanguage: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse2004>>;
    public v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet(id: number, questionId: number, channelId: number, acceptLanguage: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet.');
        }

        if (questionId === null || questionId === undefined) {
            throw new Error('Required parameter questionId was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet.');
        }

        if (channelId === null || channelId === undefined) {
            throw new Error('Required parameter channelId was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet.');
        }

        if (acceptLanguage === null || acceptLanguage === undefined) {
            throw new Error('Required parameter acceptLanguage was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdChannelsChannelIdResponsesGet.');
        }

        let headers = this.defaultHeaders;
        if (acceptLanguage !== undefined && acceptLanguage !== null) {
            headers = headers.set('Accept-Language', String(acceptLanguage));
        }

        // authentication (bearerAuth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }
        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<InlineResponse2004>('get',`${this.basePath}/v1/knowledge-bases/${encodeURIComponent(String(id))}/questions/${encodeURIComponent(String(questionId))}/channels/${encodeURIComponent(String(channelId))}/responses`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Post a Response Satisfaction on a specified Response
     * 
     * @param acceptLanguage Language locale to filter api results
     * @param id The knowledgebase id that needs to be fetched.
     * @param questionId The Question id that needs to be fetched.
     * @param responseId The Response id that needs to be fetched.
     * @param body 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost(acceptLanguage: string, id: number, questionId: number, responseId: number, body?: ResponseIdResponsessatisfactionsBody, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse2005>;
    public v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost(acceptLanguage: string, id: number, questionId: number, responseId: number, body?: ResponseIdResponsessatisfactionsBody, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse2005>>;
    public v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost(acceptLanguage: string, id: number, questionId: number, responseId: number, body?: ResponseIdResponsessatisfactionsBody, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse2005>>;
    public v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost(acceptLanguage: string, id: number, questionId: number, responseId: number, body?: ResponseIdResponsessatisfactionsBody, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (acceptLanguage === null || acceptLanguage === undefined) {
            throw new Error('Required parameter acceptLanguage was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost.');
        }

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost.');
        }

        if (questionId === null || questionId === undefined) {
            throw new Error('Required parameter questionId was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost.');
        }

        if (responseId === null || responseId === undefined) {
            throw new Error('Required parameter responseId was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsPost.');
        }


        let headers = this.defaultHeaders;
        if (acceptLanguage !== undefined && acceptLanguage !== null) {
            headers = headers.set('Accept-Language', String(acceptLanguage));
        }

        // authentication (bearerAuth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }
        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<InlineResponse2005>('post',`${this.basePath}/v1/knowledge-bases/${encodeURIComponent(String(id))}/questions/${encodeURIComponent(String(questionId))}/responses/${encodeURIComponent(String(responseId))}/responses-satisfactions`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Update a Response Satisfaction on a specified Response to provide a Reason
     * 
     * @param acceptLanguage Language locale to filter api results
     * @param id The knowledgebase id that needs to be fetched.
     * @param questionId The Question id that needs to be fetched.
     * @param responseId The Response id that needs to be fetched.
     * @param satisfactionId The Response satisfaction id that needs to be fetched.
     * @param body 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch(acceptLanguage: string, id: number, questionId: number, responseId: number, satisfactionId: number, body?: ResponsessatisfactionsSatisfactionIdBody, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse2008>;
    public v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch(acceptLanguage: string, id: number, questionId: number, responseId: number, satisfactionId: number, body?: ResponsessatisfactionsSatisfactionIdBody, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse2008>>;
    public v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch(acceptLanguage: string, id: number, questionId: number, responseId: number, satisfactionId: number, body?: ResponsessatisfactionsSatisfactionIdBody, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse2008>>;
    public v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch(acceptLanguage: string, id: number, questionId: number, responseId: number, satisfactionId: number, body?: ResponsessatisfactionsSatisfactionIdBody, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (acceptLanguage === null || acceptLanguage === undefined) {
            throw new Error('Required parameter acceptLanguage was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch.');
        }

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch.');
        }

        if (questionId === null || questionId === undefined) {
            throw new Error('Required parameter questionId was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch.');
        }

        if (responseId === null || responseId === undefined) {
            throw new Error('Required parameter responseId was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch.');
        }

        if (satisfactionId === null || satisfactionId === undefined) {
            throw new Error('Required parameter satisfactionId was null or undefined when calling v1KnowledgeBasesIdQuestionsQuestionIdResponsesResponseIdResponsesSatisfactionsSatisfactionIdPatch.');
        }


        let headers = this.defaultHeaders;
        if (acceptLanguage !== undefined && acceptLanguage !== null) {
            headers = headers.set('Accept-Language', String(acceptLanguage));
        }

        // authentication (bearerAuth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }
        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<InlineResponse2008>('patch',`${this.basePath}/v1/knowledge-bases/${encodeURIComponent(String(id))}/questions/${encodeURIComponent(String(questionId))}/responses/${encodeURIComponent(String(responseId))}/responses-satisfactions/${encodeURIComponent(String(satisfactionId))}`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Fetch available comments for negative vote Reasons
     * 
     * @param id The Knowledgebase id that needs to be fetched.
     * @param acceptLanguage Language locale to filter api results
     * @param startDate Start Date in yyyy-mm-dd format. Comments fetched are created at startDate (between 00:00:00 and 23:59:59)
     * @param channel The channel name of the responses affected by comments
     * @param extended used to display additional information : thematics list and response content associated to the question
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public v1KnowledgeBasesIdReasonCommentsGet(id: number, acceptLanguage: string, startDate: string, channel: string, extended?: boolean, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse2007>;
    public v1KnowledgeBasesIdReasonCommentsGet(id: number, acceptLanguage: string, startDate: string, channel: string, extended?: boolean, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse2007>>;
    public v1KnowledgeBasesIdReasonCommentsGet(id: number, acceptLanguage: string, startDate: string, channel: string, extended?: boolean, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse2007>>;
    public v1KnowledgeBasesIdReasonCommentsGet(id: number, acceptLanguage: string, startDate: string, channel: string, extended?: boolean, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling v1KnowledgeBasesIdReasonCommentsGet.');
        }

        if (acceptLanguage === null || acceptLanguage === undefined) {
            throw new Error('Required parameter acceptLanguage was null or undefined when calling v1KnowledgeBasesIdReasonCommentsGet.');
        }

        if (startDate === null || startDate === undefined) {
            throw new Error('Required parameter startDate was null or undefined when calling v1KnowledgeBasesIdReasonCommentsGet.');
        }

        if (channel === null || channel === undefined) {
            throw new Error('Required parameter channel was null or undefined when calling v1KnowledgeBasesIdReasonCommentsGet.');
        }


        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (startDate !== undefined && startDate !== null) {
            queryParameters = queryParameters.set('startDate', <any>startDate);
        }
        if (channel !== undefined && channel !== null) {
            queryParameters = queryParameters.set('channel', <any>channel);
        }
        if (extended !== undefined && extended !== null) {
            queryParameters = queryParameters.set('extended', <any>extended);
        }

        let headers = this.defaultHeaders;
        if (acceptLanguage !== undefined && acceptLanguage !== null) {
            headers = headers.set('Accept-Language', String(acceptLanguage));
        }

        // authentication (bearerAuth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }
        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<InlineResponse2007>('get',`${this.basePath}/v1/knowledge-bases/${encodeURIComponent(String(id))}/reason-comments`,
            {
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Fetch available negative vote Reasons
     * 
     * @param id The Knowledgebase id that needs to be fetched.
     * @param acceptLanguage Language locale to filter api results
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public v1KnowledgeBasesIdReasonsGet(id: number, acceptLanguage: string, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse2006>;
    public v1KnowledgeBasesIdReasonsGet(id: number, acceptLanguage: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse2006>>;
    public v1KnowledgeBasesIdReasonsGet(id: number, acceptLanguage: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse2006>>;
    public v1KnowledgeBasesIdReasonsGet(id: number, acceptLanguage: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling v1KnowledgeBasesIdReasonsGet.');
        }

        if (acceptLanguage === null || acceptLanguage === undefined) {
            throw new Error('Required parameter acceptLanguage was null or undefined when calling v1KnowledgeBasesIdReasonsGet.');
        }

        let headers = this.defaultHeaders;
        if (acceptLanguage !== undefined && acceptLanguage !== null) {
            headers = headers.set('Accept-Language', String(acceptLanguage));
        }

        // authentication (bearerAuth) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }
        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<InlineResponse2006>('get',`${this.basePath}/v1/knowledge-bases/${encodeURIComponent(String(id))}/reasons`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}

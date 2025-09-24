## HTTP Status Code Standardization
This document outlines the standard HTTP status codes used by the API. Consistent use of these codes allows for predictable error handling and a better developer experience.

## General Principles
**Successful Responses (2xx)**: The request was successfully received, understood, and processed.

**Client Errors (4xx)**: The request contains bad syntax, invalid parameters, or cannot be fulfilled due to client-side issues (e.g., authentication, authorization, validation). The client should modify the request.

**Server Errors (5xx)**: The server failed to fulfill a valid request due to an internal error. The client cannot fix this; it requires server-side intervention.

##Standard Status Codes Reference
This table lists the most common status codes you will encounter.

| Status Code | Status Text | Description | Common Scenarios |
| :---------- | :---------- | :---------- | :--------------- |
| **200** | OK | The request was successful. | Successful `GET`, `PUT`, or `PATCH` request. |
| **400** | Bad Request | The server cannot process the request due to a client error. | Missing required parameters, invalid JSON syntax, malformed request body. |
| **401** | Unauthorized | Authentication is required and has failed or has not been provided. | Invalid, missing, or expired API key/token. |
| **404** | Not Found | The requested resource could not be found on the server. | Invalid endpoint URL or data not founded. |
| **500** | Internal Server Error | A generic error message when the server encounters an unexpected condition. | Unhandled exceptions, database connection errors. |

# HTTPs REST

Most of the time, we use HTTPs to communicate with REST APIs. This is a quick guide to get you started with HTTPs REST.

## HTTPs

HTTPs is a protocol that allows us to communicate with a server. It's a protocol that is built on top of TCP/IP, and it's the most common protocol used on the internet. The s stands for secure, hoo-ray!

## HTTPs Data Sent

When an HTTPs request is made, it can include several pieces of data:

```json
{
  "url": <string>,
  "http_method": <string>,
  "headers": {
    <header_name>: <header_value>,
    ...
  },
  "body": <body_data>
}
```

Example:

```json
{
  "url": "http://example.com/api/resource",
  "http_method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer token",
    "Other-Header": "value"
  },
  "body": {
    "key1": "value1",
    "key2": "value2"
  }
}
```

1. **URL**: The URL indicates where the request is being sent.
2. **URL Path Parameters**: The path of the url, or the stuff in between "/", can contain data for the server. Such as `https://example.com/user/8as89?create=true`. The path parameter is `8as89`.
3. **URL Query Parameters**: The query of the url, or the stuff after "?", can contain data for the server. The query parameter in this case is `create=true`.
4. **HTTP Methods**: The HTTP Method, such as GET, POST, PUT, DELETE, etc. These methods indicate what the request is trying to do.
5. **Headers**: HTTP headers allow the client and the server to pass additional information with an HTTP request or response. An HTTP header consists of its case-insensitive name followed by a colon ':', then by its value (without line breaks). For examples, headers can be used to specifiy the content type, set cookies, or provide authentication information.
6. **Body**: The body of the request can contain data for the server. The body can be in many different formats, such as JSON, XML, or plain text.
7. **Form Data**: Form data is a special type of body that is used to send data from a form to a server.
8. **Cookies**: Cookies are data stored on the user's computer by the server and sent with every request to the same server. They are used for maintaining a "session" or other data that needs to persist across requests. Cookies are sent through the headers.
9. **Credentials**: Credentials can be sent in various ways, such as in the header (like with a Bearer token), in cookies, or even in the body or URL in some cases.

### Files

When you send a file in an HTTP request, it gets included in the body of the request. The headers are sent to indicate that the body contains form data.

### Maximum size

The max size of an http body is not set by the RFC 2616 standard, however, servers set their own limits. This is usually around 2GB.

Headers are limited to 8KB.

Cookies are limited to 4KB.

## REST

REST is a protocol for interacting with https server endpoints.

```

```

# 0x10. Python - Network #0

## What a URL is
URL stands for Uniform Resource Locator. A URL is nothing more than the address of a given unique resource on the Web. In theory, each valid URL points to a unique resource. Such resources can be an HTML page, a CSS document, an image, etc. In practice, there are some exceptions, the most common being a URL pointing to a resource that no longer exists or that has moved. As the resource represented by the URL and the URL itself are handled by the Web server, it is up to the owner of the web server to carefully manage that resource and its associated URL.

## What HTTP is
The HyperText Transfer Protocol (HTTP) is the underlying network protocol that enables transfer of hypermedia documents on the Web, typically between a browser and a server so that humans can read them. The current version of the HTTP specification is called HTTP/2.

## How to read a URL

![url](https://aprendelibvrefiles.blob.core.windows.net/aprendelibvre-container/course/creacion_de_sitios_web/image/imgscursoweb-01_xl.png)

## The scheme for a HTTP URL
The scheme identifies the protocol to be used to access the resource on the Internet. It can be HTTP (without SSL) or HTTPS (with SSL).

## What a domain name is
Domain name is the address of your website that people type in the browser URL bar to visit your website.
In simple terms, if your website was a house, then your domain name will be its address.

## What a sub-domain is
Subdomains are the part of a domain that comes before the main domain name and domain extension. They can help you organize your website. For example, docs.example.com. In this URL, docs is the subdomain.

## How to define a port number in a URL
Port numbers are sometimes seen in web or other uniform resource locators (URLs). By default, HTTP uses port 80 and HTTPS uses port 443, but a URL like http://www.example.com:8080/path/ specifies that the web browser connects instead to port 8080 of the HTTP server.

## What a query string is
A query string is a part of a uniform resource locator that assigns values to specified parameters. A query string commonly includes fields added to a base URL by a Web browser or other client application, for example as part of an HTML form.
![query](https://help.mixpanel.com/hc/article_attachments/360021921592/Query_String_Param.png)

## What an HTTP request is
An HTTP request is an action to be performed on a resource identified by a given Request-URL. Request methods are case-sensitive, and should always be noted in upper case. There are various HTTP request methods, but each one is assigned a specific purpose.

## What an HTTP response is
An HTTP response is made by a server to a client. The aim of the response is to provide the client with the resource it requested, or inform the client that the action it requested has been carried out; or else to inform the client that an error occurred in processing its request.

## What HTTP headers are
HTTP headers let the client and the server pass additional information with an HTTP request or response. An HTTP header consists of its case-insensitive name followed by a colon (:), then by its value. Whitespace before the value is ignored.

#### Headers can be grouped according to their contexts:
- General headers apply to both requests and responses, but with no relation to the data transmitted in the body.
- Request headers contain more information about the resource to be fetched, or about the client requesting the resource.
- Response headers hold additional information about the response, like its location or about the server providing it.
- Entity headers contain information about the body of the resource, like its content length or MIME type.

## What the HTTP message body is
HTTP Message Body is the data bytes transmitted in an HTTP transaction message immediately following the headers if there are any (in the case of HTTP/0.9 no headers are transmitted).

## What an HTTP request method is
HTTP defines a set of request methods to indicate the desired action to be performed for a given resource. 

Although they can also be nouns, these request methods are sometimes referred to as HTTP verbs. Each of them implements a different semantic, but some common features are shared by a group of them: e.g. a request method can be safe, idempotent, or cacheable.

###### GET
The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
###### HEAD
The HEAD method asks for a response identical to that of a GET request, but without the response body.
###### POST
The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.
###### PUT
The PUT method replaces all current representations of the target resource with the request payload.
###### DELETE
The DELETE method deletes the specified resource.
###### CONNECT
The CONNECT method establishes a tunnel to the server identified by the target resource.
###### OPTIONS
The OPTIONS method is used to describe the communication options for the target resource.
###### TRACE
The TRACE method performs a message loop-back test along the path to the target resource.
###### PATCH
The PATCH method is used to apply partial modifications to a resource.

## What an HTTP response status code is

HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:
    1. Informational responses (100–199)
    2. Successful responses (200–299)
    3. Redirects (300–399)
    4. Client errors (400–499)
    5. Server errors (500–599)

## What an HTTP Cookie is
An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to the user's web browser. The browser may store it and send it back with later requests to the same server. Typically, it's used to tell if two requests came from the same browser — keeping a user logged-in, for example. It remembers stateful information for the stateless HTTP protocol.

Cookies are mainly used for three purposes:
###### Session management
Logins, shopping carts, game scores, or anything else the server should remember
###### Personalization
User preferences, themes, and other settings
###### Tracking
Recording and analyzing user behavior

## How to make a request with cURL
curl is a command-line utility for transferring data from or to a server designed to work without user interaction. With curl, you can download or upload data using one of the supported protocols including HTTP, HTTPS, SCP , SFTP , and FTP . curl provides a number of options allowing you to resume transfers, limit the bandwidth, proxy support, user authentication, and much more.
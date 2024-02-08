"""
                            APPLICATION PROGRAMMING INTERFACE: API
--> APIs enables your software application to interact with another application.
--> A python class exposes an API: names of methods and properties.
    --> Basically, your python code sends and receives data to some class instance by going through an interface
    (the attributes, methods and properties)
--> These days, many applications are "in the cloud",
    --> like CRM applications like salesforce.
    --> Payroll applications
    --> Trading platforms
    --> Automated AI
--> These other applications that are "in the cloud" expose their API via the web using HTTP or HTTP(s) Protocol in
general.
    --> For a website, you request data using a URL. This is called a GET request.
        --> A GET request fetches data

                    HOW A BROWSER RETRIEVES A WEB PAGE
--> The browser uses a GET method/verb:
    --> GET https :// some_site.com /path/to/page.html
    --> https is the Protocol
    --> :// are the separator
    --> some_site.com is the domain
    --> /path/to/page.html: is the resource path to a specific path to a page
    --> URI: some_site.com /path/to/page.html
        --> The path to the domain and resource path are called the URI: Uniform Resource Identifier.
    --> URL: https :// some_site.com /path/to/page.html
        --> included the protocol and the URI
--> The GET also supports query arguments.
    --> Query arguments are basically like named arguments in python functions.
    --> GET https://some_site.com /currentTemp?city=Chicago&units=metric
        --> where & is a separator for the named arguments city and units
--> The web server at the domain waits to receive requests
--> The browser sends request to web server.
--> The server sends back data (often html, but does not have to be html!)
--> The browser displays returned data and renders it in CSS and JavaScript

                        HOW A BROWSER SENDS DATA
--> We can also send data to a web server, e.g user registration data
    --> We use different methods/verbs e.g POST
    --> We need the specific "path" on the web server we need to send the data to (specific URL, i.e Protocol and URI)
        --> We attach this data when request is sent by the browser.
    --> Web server receives the data and does something with it.
        --> and usually returns a response of some kind
--> In general, web servers listen for incoming requests
--> Requests contain:
    --> a method, e.g GET, POST
    --> URL, which specifies exactly what we're trying to access on the system.
    --> Query Arguments (maybe)
    --> "Attached" data (maybe)
--> The set of what URLs, query arguments, methods and data a web server understands as well as the format of what it
returns is basically an API.
--> Data is not necessarily HTML. It can be JSON, XML, etc.

                            REST APIs
--> REST APIs are special types of APIs
    --> REST has to do with how they are implemented and their behaviour.
    --> As users of the API, we don't actually care if it is REST or something else.
--> One of the fundamental characteristics of a REST API is that cals are independent of each other (stateless).
    --> Call to APU does not rely on remembering how you interacted with it in the past.
        --> This is not quite the same with websites where you log in, access pages on the site and the web server
        remembers who you are. Websites are stateful. REST APIs are not stateful.

                        AUTHENTICATION/AUTHORIZATION
--> REST APIs are generally secured.
    --> You need to be authenticated, i.e the web server needs to know who you are.
        --> It is usually a secret token you pass in the request.
        --> Very often tokens are passed in "headers", which is just an extra "bucket" of key-value data that can be
        sent/received along with request.
--> You also need to be authorized to perform the request.
    --> You may be authorized to read some data
    --> but you may not be authorized to create/delete that data.

--> Authentication establishes who you are to the system you are interacting with.
--> Authorization governs what you can/cannot do in the system.

                    API DATA FORMATS
--> Most modern APIs use JSON for sending/receiving data.
    --> sometimes use XML, or even proprietary formats
    --> XML is more powerful than JSON because it offers a lot of functionality and ways of defining a lot of data
    types. It's more verbose but also more powerful.

                        RESOURCES
--> REST APIs allow us to interact with entities called "resources". Resources could be:
    --> Bank Account. We can create a new account, list accounts for a specific customer, get balance, deposit,
    withdraw, delete the account, etc.
    --> Customer. We can create new customer, get customer info, update customer info, delete customer.
    e.g
    --> GET https://URI/customer/12345/account/5523?query=balance
            The webserver responds {"balance": 2123.45, "asOf": "2020-04-05T15:35:45+00:00:00"}
    --> POST https://URI/customer/12345/account/5523?query=balance
            + {"action": "withdraw", "amount":100.0}
            The webserver responds {"balance": 2123.45, "asOf": "2020-04-05T15:35:45+00:00:00"}

                        API Methods.
--> Since humans design/write these APIs, things are not always consistent.
--> GET : retrieves resources(s) and is often used with query arguments
--> POST: is used to create a resource.
    --> Be careful; Issuing the same POST request twice can end up creating two resources.
--> PUT, PATCH : usually used for updating an existing resource.
--> DELETE : used to delete a resource.

                        STATUS CODES:
--> Making an HTTP request (such as GET, POST, PUT, PATCH, DELETE etc) always returns a status code.
    --> plus whatever else the API specifies.
--> 2xx : is for successful responses.
    --> 200 means OK (meaning the request was successful)
    --> 201 means Created (meaning the resource was created successfully)
    --> 202 means Accepted (meaning request accepted, but not finished processing (async)(
--> 4xx : is for unsuccessful responses, meaning you did something wrong.
    --> 400 : means Bad Request (meaning the server did not understand the request)
    --> 401 : means Unauthorized (technically, this means "not authenticated")
    --> 403 : means Forbidden (this means "not authorized")
    --> 404 : means Not Found (meaning server cannot find specified resource)
--> 5xx : Server had an issue (usually not your fault!)

                    FINHUB STOCK API
--> In this course, we'll use FINHUB STOCK API
--> It provides free and paid tiers for getting financial data.
    --> implements REST API
    --> uses JSON
    --> We'll mostly use GET requests
--> Sign up with a free tier account.
"""


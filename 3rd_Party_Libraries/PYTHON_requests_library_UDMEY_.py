"""
                        THE REQUESTS LIBRARY
--> Python has a module in the standard library for making HTTP requests
    --> slightly low level interface (think time vs datetime library)
    --> Usually we use a 3rd Party library: Requests: HTTP for Humans
        --> This library is pretty much recommended to use.

                        MAKING REQUESTS:
--> All standard methods/verbs are implemented as functions. e.g
    --> requests.get(...)
    --> requests.post(...)
    --> requests.put(), etc
--> Common arguments include:
    --> URL : the URL request will be sent to
    --> params : dictionary of query parameters (key=value)
    --> json :JSON sent in request (usually for POST, PUT, etc)
    --> headers : dictionary of headers (key=value), where key is the header name and value is the header value
    and many more

                    RECEIVING RESPONSES
--> A "response object" is the result of making a request (get, post, etc)
--> It has the following properties (amongst others):
    --> status_code : integers value e.g 200, 403
    --> reason : translation of status code e.g OK, Forbidden
    --> text : is the content of the response e.g in JSON or HTML
    --> json : returned deserialized JSON (if any) --> so a dict
        --> reading this property if no JSON is present as a ValueError
    --> headers : when the server responds back, it sends headers which may/may not be useful. headers are usually a
    dictionary.
    --> cookies : cookies are received from server
--> e.g
response = requests.get(url="specify_url (protocol + uri)", params={"specify_parameter_key":"specify_parameter_value"})
response.status_code returns a status_code value
response.reason returns status_code meaning
response.text returns the HTML page browser would display.
response.raise_for_status() raises an Exception if the status code is an error code.
response.cookies

--> Calling an undefined URL returns a bad response. so that why we can get the resonse.status_code, response.reason
and respond.text

"""

from datetime import datetime
import requests

respond = requests.get('https://www.stackoverflow.com')

print(respond.status_code)
print(respond.reason)
print(respond.text)

for key, value in respond.headers.items():
    print(f'{key}:{value}')

query_params = {
    'q': 'python http requests',
    'num': 5
}

response = requests.get(url="https://www.google.com", params=query_params)

print(response.status_code)
print(response.reason)

print(response.headers['content-type'])

print(response.headers['content-encoding'])

print(response.text)

# response.json()

response = requests.get(url='https://www.google.com/some_dummy_page')
print(response.status_code, response.reason)

# You can raise an exception if the status code is an error code or use response.raise_for_status()
# print(response.raise_for_status())
response = requests.get('https://www.stackoverflow.com')
print(response.status_code, response.reason)
print(response.raise_for_status())  # returns None if there is no Exception

response = requests.get('http://nyt.com')
print(response.status_code, response.reason, response.raise_for_status())

# print(response.cookies)

for key, value in response.cookies.items():
    print(f'{key}:{value}')

with open('secrets.txt', 'r') as f:
    API_KEY = next(f).strip()

base_url = 'https://www.finnhub.io/api/v1'

url = f'{base_url}/quote'
params = {
    'token': API_KEY,
    'symbol': 'AAPL'
}

response = requests.get(url, params)

print(response.status_code, response.reason)

print(response.headers)

# print(response.json())

d = response.json()
print(type(d))
print(d)

d = datetime.fromtimestamp(d['t'])
print(d)

params = {
    'symbol': 'MSFT',
    'token': API_KEY
}

response = requests.get(url, params)
print(response.status_code, response.reason)
print(response.json())

headers = {
    'X-finnhub-Token': API_KEY
}

for symbol in ['AAPL', 'MSFT', 'GOOG']:
    try:
        response = requests.get(
            url=url,
            params={'symbol': symbol, 'token': API_KEY}
        )
        print(f'**** {symbol} *****')
        print(response.json())
    except requests.HTTPError as ex:
        print(f'Unable to retreive data for {symbol}:{ex}')

for symbol in ['AAPL', 'MSFT', 'GOOG']:
    try:
        response = requests.get(
            url=url,
            params={'symbol': symbol},
            headers=headers
        )
        print(f'**** {symbol} *****')
        print(response.json())
    except requests.HTTPError as ex:
        print(f'Unable to retrieve data for {symbol}:{ex}')

url = f'{base_url}/stock/profile2'

response = requests.get(
    url=url, params={'symbol': 'AAPL'}, headers=headers
)

print(response.json())

base_webhook_url = f'{base_url}/webhook'

post_data = {
    'event': 'earnings',
    'symbol': 'AAPL',
}

response = requests.post(
    url=f'{base_webhook_url}/add',
    headers=headers,
    json=post_data
)

print(response.status_code, response.reason)
print(response.json())

response = requests.post(
    url=f'{base_webhook_url}/add',
    headers=headers,
    json= {
        'event': 'earnings',
        'symbol': 'MSFT',
    }
)

print(response.status_code, response.reason)
print(response.json())

response = requests.get(
    url=f'{base_webhook_url}/list',
    headers=headers
)
print(response.status_code, response.reason)
print(response.json())

response = requests.post(
    url=f'{base_webhook_url}/delete',
    headers=headers,
    json= {
        'id':14572
    }
)
print(response.status_code, response.reason)
print(response.json())

response = requests.post(
    url=f'{base_webhook_url}/delete',
    headers=headers,
    json= {
        'id':14584
    }
)

response = requests.get(
    url=f'{base_webhook_url}/list',
    headers=headers
)
print(response.status_code, response.reason)
print(response.json())

response = requests.get(
    url=f'{base_webhook_url}/list',
    headers=headers
)
print(response.status_code, response.reason)
print(response.json())


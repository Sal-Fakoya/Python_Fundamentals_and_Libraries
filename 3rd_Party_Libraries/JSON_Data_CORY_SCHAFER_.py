"""JavaScript Object Notation (JSON) --> JSON was inspired by javascript but now independent of any one language. -->
It is a common data format for storing information, communication between web APIs and clients. --> If you want to
build a web API with Python, you will need to understand how to read and write JSON data using Python.

"""

import json
from urllib.request import urlopen

people_string = '''
{
    "people": [
        {
            "name": "John",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
# load into python from string using json.loads(some_json_string)
data = json.loads(people_string)

print(data)

# check type of data
print(type(data))  # returns class dict

print(type(data['people']))  # people value pairs are a list of dictionaries

for person in data['people']:
    print(person)  # returns a dictionary

for person in data['people']:
    print(person['name'])

# to dump a python object in a json string: json.dumps method

for person in data['people']:
    del person['phone']

new_str = json.dumps(data, indent=2, sort_keys=True)
print(new_str)

# loading json file into a python object: json.load(some_json_file)

with open('C:\\Users\\fakoy\\Python_Programming_Udemy2023\\3rd_Party_Libraries\\states_youtube.json', 'r') as f:
    data = json.load(f)

    for state in data['states']:
        # print(state['name'], state['abbreviation'])
        del state['area_codes']


with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)


with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

print(source)
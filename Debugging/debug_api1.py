## Errors were on line result = requests.post('http://httpbin.org/post', json=data) originly it said results.get.
## Also on line first_name, last_name = full_name.split(" ", 1) , added the "", 1 on the split to handle the line with 2 names and a surname.

import requests
import parse
NAMES = [
    'John Smyth',
    'Michael Craig',
    'Poppy-Mae Pate',
    'Vivienne Rennie',
    'Fathima Mccabe',
    'Mai Cordova',
    'Rocío García',
    'Roman Sullivan',
    'John Paul Smith',
    "Séamus O'Carroll",
    'Keagan Berg',
]

sorted_names = []
for name in NAMES:
    data = {
        'custname': name,
    }
    # Request the name from the server
    result = requests.post('http://httpbin.org/post', json=data)
    if result.status_code != 200:
        raise Exception(f'Error accessing server: {result}')
    # Obtain a raw name
    raw_result = result.json()['data']
    ## Extract the name from the result
    full_name = parse.search('"custname": "{name}"', raw_result)['name']
    ## Split it into first name and last name
    first_name, last_name = full_name.split(" ", 1)
    ready_name = f'{last_name}, {first_name}'
    ## Add the name in last_name, first_name format to the list
    sorted_names.append(ready_name)
## Properly sort the list and display the result
sorted_names.sort()
print(sorted_names)

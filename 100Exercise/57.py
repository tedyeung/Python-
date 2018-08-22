'''
Please download the file in the attachment and use Python to print out its content.

Expected output: 

{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
               {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}
'''

import json
import pprint as pp

with open('company1.json') as json_file:
    data = json.load(json_file)

pp.pprint(data)


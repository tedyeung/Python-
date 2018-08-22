'''
Question: Please download the json file in the attachment and use Python to add a new employee to the content of the file so that the file looks like in the expected output below.
'''

import json
from pprint import pprint as pp 

with open("company1.json") as json_file:
    data = json.load(json_file)

pp(data)
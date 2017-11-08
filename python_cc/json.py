# json files

import json

user_num = input('Please add your favourite number: ')

file_name = ('json_file.json')

with open(file_name, 'w') as file_obj:
    json.dumps(user_num, file_obj)
    print('Your favourte number is stored. Number is ', user_num)


import json

file_name = 'json_file.json'

with open(file_name) as file_obg:
    user_num = json.load(file_obg)
    print ('Welcome Back Your number is ', str(user_num)) 
    
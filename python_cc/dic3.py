user_one = {

    'first_name': 'Slavo',
    'last_mame': 'Popovic',
    'age': 35,
    'language': 'Python'
} 

user_two = {
    
    'first_name': 'Nemanja',
    'last_mame': 'Stojanovic',
    'age': 29,
    'language': 'JavaScript'
} 

user_tree = {
    
    'first_name': 'Dragan',
    'last_mame': 'Okiljevic',
    'age': 36,
    'language': 'Python'
} 

users_list = [user_one, user_two, user_tree]

for user in users_list:
    print(user)
print('*************************************')

user_one["age"] = 36
print(user_one)

print('*************************************')






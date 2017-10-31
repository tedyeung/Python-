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

user1 = {
    'name': 'Mark',
    'skills': ['swift', 'java']
}

user2 = {
    'name': 'Caleb',
    'skills': ['swift', 'c#', 'c++']
}

user3 = {
    'name': 'Cris',
    'skills': ['python', 'r', 'scala']
}

new_users = [ user1, user2, user3 ]

for users in new_users:
    print(users)
print('********************************')    


print('Welcome %s, your skills are: ' %user1['name'])
for leng in user1['skills']:
    print(leng)
print ('***********************************')

for user in new_users:
    print('------------------')
    print('Welcome %s, your skills are: ' %user['name'])
    for leng in user['skills']:
        print(leng)

print ('*************************************************************************')
print (' ')

players = {

    'z' : {
        'first_name': 'Zvezdan',
        'last_name': 'Zivkovic',
        'position': 'Left Middfilder / Back'
    },

    'Marco' : {
        'first_name': 'Marko',
        'last_name': 'Marenko',
        'position': 'Goalie'
    },

    'Slavo' : {
        'first_name': 'Slavoljub',
        'last_name': 'Popovic',
        'position': 'Stricker / Middfilder'
    },

    'Edin' : {
        'first_name': 'Edin',
        'last_name': 'Ormedic',
        'position': 'Right Middfilder / Back'
    }

}

for player, player_info in players.items():
    print('\nPlayer nick_name: ', player.title())
    print ('Player info: ')
    print ('\tFirst name: ', player_info['first_name'])
    print ('\tLast name: ', player_info['last_name'])   
    print ('\tPosition: ', player_info['position'])


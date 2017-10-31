rivers = {
    'Belgrade': 'Danube',
    'novi sad': 'sava',
    'kairo': 'nil', 
}

for name, river in rivers.items():
    print(river.title() + ' is from ' + name.title() + '!!')

print ('***************************************************')

users = ['jen', 'slavo', 'nikola', 'nemanja', 'predrag']
favorite_languages = {

    'jen': 'python', 
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'nemanja': 'javaScript',
    'vlastimir': 'swift',
    'marko': 'php'

}

for name in favorite_languages.keys():
    if name in users:
        print('%s, your language is: %s' %(name.title(), favorite_languages[name].title()))
print ('*************************************************************************************') 
for user in users:
    if user not in favorite_languages.keys():
        print ('Dear %s, you need to choose one of the programming languages' %(user))

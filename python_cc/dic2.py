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
    print (name.title() + ' , well done') 

    if name in users:
        print ('Hi %s, you are coding with %s' %(name.title(), favorite_languages[name].title()))


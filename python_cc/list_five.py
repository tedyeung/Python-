# slic list 
print ('Those languages I am willing to learn: ')
languages  = ['Python', 'R', 'Swift', 'JavaScript', 'Ruby', 'C++', 'C', 'php', 'go', 'Scala', 'Java', 'C#', 'Kotlin']
for language in languages[0:4]:
    print (language)

print ('Those languages is good to know:')
for language in languages[5:9]:
    print(language)

print ('if you want to be android and microsoft dev you need to use this: ')
for language in languages[-4:]:
    print(language)

print ('*******************************************************************')

web_development = ['HTML', 'CSS', 'JavaScript', 'Python', 'Node', 'Ruby', 'Java', 'C#']
my_development_list = web_development[0:6]
print('My skills are: ', my_development_list)
my_development_list.append('Swift')
web_development.append('Swift')
print (my_development_list)
print (web_development)


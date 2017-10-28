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


# if statements
language = 'Python'
if 'Python' == language:
    print ('You can work in ML')

if 'python' == language.lower():
    print('You can work with ML but please read about R')

languages = ['Python', 'JavaScript', 'Swift', 'php']

if language in languages:
    print ('Well done you know Python')
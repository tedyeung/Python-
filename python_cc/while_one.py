# while loop, list 
languages = ['Python', 'Swift', 'JavaScript', 'C#', 'R']
need_to_learn = []

print ('\n', '*************************************', '\n')

while languages:
    lang = languages.pop()
    print('You need to learn %s' %lang)
    need_to_learn.append(lang)

print ('\n', '*************************************', '\n')

for x in need_to_learn:
    print ("I will learn: %s " %x)

print ('\n', '*************************************', '\n')

response = {}
question_one = 'What is you name: '
question_two = 'What you want to learn: ' 

status = True

while status: 
    name = input(question_one)
    skill = input(question_two)
    age = input('How old are you? ')
    city = input('Where are you live')

    new_question = input('Do you have any recomendation please answer with y or n: ')

    response["name"] = name.title()
    response["skill"] = skill.title()
    response['age'] = int(age)
    response[city] = city.title()

    if new_question == 'n':
        status = False

print (response)
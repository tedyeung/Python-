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
    new_question = input('Do you have any recomendation please answer with y or n: ')

    response["name"] = name
    response["skill"] = skill

    if new_question == 'n':
        status = False

print (response)
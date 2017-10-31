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

user_one = {}
question_one = 'What is you name: '
question_two = 'What you want to learn: ' 

status = True

while status: 
    name = input(question_one)
    skill = input(question_two)
    age = input('How old are you? ')
    city = input('Where are you live')

    user_one["name"] = name.title()
    user_one["skill"] = skill.title()
    user_one['age'] = int(age)
    user_one[city] = city.title()

    print (user_one)

    new_question = input('If all info are good say y or type n and \nDo it again: ')

    if new_question == 'n':
        status = False

print ('Your info: ', '\n\t', user_one)
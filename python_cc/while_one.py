# while loop, list 
languages = ['Python', 'Swift', 'JavaScript', 'C#', 'R']
need_to_learn = []

while languages:
    for lang in languages:
        print('You need to learn %s' %lang)
        need_to_learn.append(lang)

print ("Your list is: ", need_to_learn)
# writing simpe touple
print ('My tools for Data Science and Machine Learning: ')
languages = ('python', 'r')
for language in languages:
    print(language)

# touple practice
print('My skills are: ')
need_learn = ('python', 'r', 'swift', 'javascript', 'C#')
for language in need_learn:
    print(language)
# test code - touples are immutable
need_learn[0] = 'java'
print(need_learn)

file_name = 'write_greeting.txt'

active = True

while active:
    question = input('Please eneter your name, if you did please type y: ')
    if question != 'y':
        with open(file_name, 'a') as file_obj:
            file_obj.write('**************************\n')
            file_obj.write('Welcome %s!!!!!' %question.title())
            file_obj('***********************************')
    else: 
        print ('Thank you, your name is added to write_greeting.txt')
    

print('Check the file!!!!')

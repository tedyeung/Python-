# input 
message = input('What kind of car would you like to rent: ')
print('Let me take a look if we have that mode ' + message + ' ,this is really nice model!')
print ('\n', '************************************************************************************', '\n ')

# input and if statement , integer 

question = input('How many guest are you expecting? ')
guests = 8
if int(question) < guests:
    print('We have a tabel for you, table will have: %s ' %question)
else:
    print('You have more guest that we can fit let me check if we have table for: %s'   %question)

print ('\n','************************************************************************************', '\n ')

number = input('Add number and please check if is multiple of 9: ')
result = str(int(number) % 9)
if int(number) % 9 == 0:
    print ('Your number %s is multiple by 9' %number)
else: 
    print ('Your number has rimider of %s' %result )



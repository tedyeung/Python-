# input 
message = input('What kind of car would you like to rent: ')
print('Let me take a look if we have that mode ' + message + ' ,this is really nice model!')
print ('************************************************************************************', '\n ')

# input and if statement , integer 

question = input('How many guest are you expecting? ')
guests = 8
if int(question) < guests:
    print('We have a tabel for you, table will have: %s ' %question)
else:
    print('You have more guest that we can fit let me check if we have table for: %s'   %question)

print ('************************************************************************************', '\n ')
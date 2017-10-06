# for loop 
emails = ['slavo@mimicom24.com', 'popovic.slavoljub@gmail.com', 'slavo@slavo7.com', 'slavoljub.popovic@yahoo.com', 'office@mimicom24.com']
for item in emails:
    print(item)
print ('***** cheking ************')
for item in emails:
    if 'gmail' in item:
        print(item)
print ('***** cheking ************')
a = 'Tricky'
for i in a[:3]:
    print(i)
print ('***** while loops ************')
password = ''
while password != 'python123':
    password = input('Enter password again: ')
    if password == 'python123':
        print('You are logged in')
    else:
        print('Sorry, try again')
print ('***** while loops ************')

names = ['slavo', 'marko', 'nened']
email_domain = ['gmail', 'hotmail', 'yahoo']

for i, j in zip(names, email_domains):
    print(i,j)

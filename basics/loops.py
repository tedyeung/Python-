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
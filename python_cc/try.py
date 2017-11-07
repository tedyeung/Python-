print ("Welcome to a simple math operation... devide your favourite numbers!!")
active = True

while active:
    exit = input('if you want to exit , type exit if you want!!')
    q_one = input('Please add your first number: ')
    q_two = input('Please add your 2nd number: ')
    q_one = int(q_one)
    q_two = int(q_two)
    if exit != 'exit':
        try:
            result = q_one/q_two
            print ('Your result is : ', result)
        except:
            print ('Please add numbers or your 2nd number was 0') 
    else:
        active = False
        break

print ('Slavo this try and except block is working find...wow!!!')
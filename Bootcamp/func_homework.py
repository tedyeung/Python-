print ('***** Functions and Methods Homework ******************')

# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4/3)*(3.14)*(rad**3)
print('Volume of a sphere is: ',vol(5));
print('********************************')
# Write a function that checks whether a number is in a given range (Inclusive of high and low)
def ran_bool(num,low,high):
    num_list = [low for low in range(low, high)]
    for x in num_list:
        if num == x:
            return True 
       
print ("Number 3 is in the range (1,10): ", ran_bool(3, 1, 10))
print ("Number 3 is in the range (1,10): ", ran_bool(2,5,11))
print ('*************************************************************')
def ran_check(num,low,high):
    if num in range(low, high+1):
        print ('Number %s is in the range' %str(num))
    else:
        print ('Number %s is out of the range' %str(num))
        
ran_check(3,1,10)
print ('*************************************************************')
def ran_bool(num,low,high):
    return  num in range(low, high+1)

print ("Number 3 is in the range (1,10): ", ran_bool(3, 1, 10))
print ("Number 3 is in the range (1,10): ", ran_bool(2,5,11))
print ('******************************************************************')
# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["upper"])
    print ("No. of Lower case Characters : ", d["lower"])
print('*******************************************************************')
# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    x = []
    x.append(set(l))
    return x
    
print (unique_list([1, 2, 3,3,3,3, 4,4,4,4 ,5,5,5,5,6,6,6,6,]))
print ('*******************************************************')

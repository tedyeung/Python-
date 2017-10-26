# example_one
guest = ['Marko', 'Nikola', 'Dario', 'Zvezdan', 'Bane', 'Milos']
print (guest)
print('***********************')
missing_guest = guest.pop()
print ('Missing guest is: ', missing_guest)
print (guest)
# using del method
del guest[3]
print (guest)
# using remove method
guest.remove('Marko')
print (guest)
# using add method
guest.append('Marinko')
print(guest)
# using insert method
guest.insert(2, 'Dejan')
print (guest)
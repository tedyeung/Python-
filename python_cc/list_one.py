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
guest.remove(0)
print (guest)
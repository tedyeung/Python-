# for loop nubmers
for value in range(1, 21):
    print (value)

print ('*****************************************')

# for 1M loop
# for value in range (1, 1000001):
  #  print (value)

# for min and max loop
one_m = list(range(1, 1000001))
print ('Min number in range from 1 to 1m: ', min(one_m))
print ('Max number in range from 1 to 1m: ', max(one_m))
print ('SUm all numbers in range from 1 to 1m: ', sum(one_m))
# odd numbers
odd_numbers = [number for number in range(1, 21, 2) ]
print(odd_numbers)
# list of numbers multiply by 3
list_numb = []
for number in range(0, 31):
    if (number % 3) == 0:
      list_numb.append(number)
print('List of numbers: ',list_numb)
# cube numbers of list 1 to 10
cube_numbers = []
for number in range (1, 10):
      cube_numbers.append(number**3)
print ('Cube numbers of 1 to 10 are: ', cube_numbers)
# list comprehension
new_list = [number**3 for number in range(1,11)]
print ('Using list comprehension: ', new_list)

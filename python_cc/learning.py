file = 'learning_python.txt'

with open(file) as file_obj:
    lines = file_obj.readlines()

long_string = ''
list_items = []
for line in lines:
    list_items.append(line.rstrip().title())
    long_string += line.rstrip()
print ('List exported from the file: ',list_items)
list_items.pop(0)
print ('List of skills: ', list_items)

print (long_string)
print(len(long_string))

long_string.replace('Whith', 'fuck')
print(long_string)

test = 'Welcome Slavo'
test.replace('Slavo', 'Tamara')
print (test)


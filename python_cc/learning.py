file = 'learning_python.txt'

with open(file) as file_obj:
    lines = file_obj.readlines()

list_items = []
for line in lines:
    list_items.append(line.rstrip().title())

print ('List exported from the file: ',list_items)
list_items.pop(0)
print ('List of skills: ', list_items)
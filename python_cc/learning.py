file = 'learning_python.txt'

with open(file) as file_obj:
    lines = file_obj.readlines()

list_items = []
for line in lines:
    list_items.append(line[1:])

print (list_items)
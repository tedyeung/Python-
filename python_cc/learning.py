file = 'learning_python.txt'

with open(file) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.rstrip())
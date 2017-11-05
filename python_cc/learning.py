file = 'learning_python.txt'

with open(file) as file_obj:
     for line in file_obj:
         print(line.rstrip())
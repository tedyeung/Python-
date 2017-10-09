#open file
file_obj = open("example.txt")
content = file_obj.read()
print(content)
file_obj.close()
# write in to the file
first_python_edit = open('new_example.txt', 'w')
first_python_edit.write('Welcome Slavo, You wrote your first line')
first_python_edit.close()
print(first_python_edit.read())




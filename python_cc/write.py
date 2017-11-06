# writing simple line of code 

file_name = 'write_file.txt'

with open(file_name, 'w') as file_obj:
    file_obj.write('Welcome to Slavo7 Dev File\n')
    file_obj.write('We are here talking about Python, Swift, JavaScript, Mobile Development')

print ('We Just made a write_file.txt')
file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_str = ''
for line in lines:
    pi_str += line.strip()

bday = input('Please eneter your Bday, in the form mmddyy: ')
if bday in pi_str:
    print('Your Birthday appears in the first million digits of pi!')
    print(bday)
else:
    print('Your Bday does not appear in the first million digits of pi!')

    
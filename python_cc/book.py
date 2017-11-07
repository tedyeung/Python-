# analyzing a book words 

file_name = 'book.txt'

with open(file_name, encoding='utf-8') as file_obj:
    content = file_obj.readlines()
   


one_str = ''

for word in content:
    one_str += word.rstrip()


print ('How many word (the) in this book: ')
print ('Result is: ', one_str.lower().count('the'))



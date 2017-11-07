# analyzing a book words 

file_name = 'book.txt'

with open(file_name) as file_obj:
    content = file_obj.encode('utf-8').read()
    print (content)




'''
Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

Expected output:

10 

'''

def str_len(file):
    with open(file) as f:
        data = f.read()
    
    return len(data.split(" "))

print(str_len('words1.txt'))


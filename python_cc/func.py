# simple fucntion
def greet():
    print('Hello Slavo, you need to learn a lot!!')

greet()

print('\n************************************************\n')
# simple func with argument
def book(my_book):
    print ('Slavo please finish all book ' + my_book.title())

book('python crash course')

print('\n*******************************************************\n')

# func for the t-shirt

def tshrt(size ='L', text = 'i am python developer'):
    print('Your text will be ', text.title())
    print('Size of t-shirt will be: ', str(size))

tshrt(48, 'love python')
    
print('\n*******************************************************\n')    
# func for the t-shirt   

tshrt()

print('\n*******************************************************\n')
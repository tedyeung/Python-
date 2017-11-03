# new function 
def list_todo(*todo):
    print('You need to learn: ', '\t')
    for todos in todo:
        print(todos)

list_todo('web site', 'python', 'swift', 'machine learning', 'data science', 'deep learning')


# new function 
def list_todo(*todo):
    for todos in todo:
        print('You need to learn ', todo.title)

list_todo('web site', 'python', 'swift', 'machine learning', 'data science', 'deep learning')


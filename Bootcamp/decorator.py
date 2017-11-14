def info(full_name, age=35):
    full_name()
    print ("Age: ", age)

@info
def full_name():
    print ( 'Full name: Slavo Popovic')


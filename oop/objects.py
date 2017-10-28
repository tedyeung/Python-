# simple objects
l = [1, 2, 3]
l.count(2)
# sample class
class Sample (object):
    pass 
x = Sample()
print(type(x))
print ('*******************')
# new class
class Dog(object):
    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed='Lab')
print(sam)
print(sam.breed)
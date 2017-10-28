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
  # class object attributes
    species = 'mammal'
    def __init__(self, breed),name:
        self.breed = breed
        self.name = name

sam = Dog(breed='Lab', name = 'Ari')
print(sam)
print(sam.breed)
print(sam.species)


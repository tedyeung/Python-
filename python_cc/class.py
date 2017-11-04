class Restaurant():

    def __init__(self, restauarant_name, restaurant_type):
        self.restauarant_name = restauarant_name 
        self.restaurant_type = restaurant_type
    
    def describe_restaurant(self):
        print ('Welcome to %s, We are %s ' %(self.restauarant_name.title(), self.restaurant_type.title()))


restaurant = Restaurant('pasta and...', 'italian restaurante')

print ('Welcome to ', restaurant.restauarant_name.title())
print (restaurant.describe_restaurant())
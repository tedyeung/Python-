class Restaurant():
    
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.number_served = 0

    def info(self):
        print('Welcome to %s, we are located in %s' %(self.name.title(), self.place.title()))
        print('We have ' + str(self.number_served) + ' customers, we just opened')

    def set_number_surved(self, num):
        surved = num + self.number_served
        return surved
 
    def increment_surved(self, new_surved):
        new_surved_num = served + new_surved
        return new_surved_num
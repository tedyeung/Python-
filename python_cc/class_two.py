# new class practice

class Restaurant():

    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.number_served = 0

    def set_number_surved(self, num):
        surved = num + self.number_served
        return surved
 
    def increment_surved(self, new_surved):
        new_surved_num = set_number_surved + new_surved
        return new_surved_num

    

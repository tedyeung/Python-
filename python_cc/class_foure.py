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

# adding class inside the class 

class IceCreamStand(Restaurant):
    
    def __init__(self, name, place):
        super().__init__(name, place)
        self.flavors = ['chocolate', 'vanilla', 'Nutella']

    def info_ice_creame(self):
        print ('Welcome to ' + self.name.title() + ',We are in ' + self.place.title())
        print('Choose flavor:')
        for flavor in self.flavors:
            print('\t\t', flavor)
        
        

iceCream = IceCreamStand('pane dolce', 'fort lauderdale')
iceCream.info_ice_creame()


# new class 

class User():
    
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login = 0
        self.password = ''
    
    def greet(slef):
        print('Welcome %s %s, you registration is ready.' %(self.first_name.title(), self.last_name.title()))

    def skill(self):
        print('Please enter your bio %s' %self.first_name.tittle())

    def user_info(self):
        print('\n*************************************************************\n')
        print('Your info \nFull name: %s %s\nAge: %s\nCity: %s' %(self.first_name.title(), self.last_name.title(), str(self.age), self.city.title()))
        print('\n*************************************************************\n')
    
    def login_att(self):
        psw = self.password
        active = True
        while active:
            psw = input("Please add your password: ")
            if psw == 'mimicom2433062fl':
                active = False
                self.login = 0 
                print ('Well Done')
            else:
                self.login = self.login + 1
                print('This is your ', self.login,' try')

        print ('You have %s logs' %str(self.login), '!We did reset of your attempts!')


class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privilages = ['can add post', 'can delete post', 'add user', 'remove user']

    def show_privilages(self):
        print('Admin has those privilages:')
        for priv in self.privilages:
            print('\t\t', priv)


admin = Admin('Slavo', 'Popovic', 35, 'pompano beach')

admin.user_info()
admin.show_privilages()
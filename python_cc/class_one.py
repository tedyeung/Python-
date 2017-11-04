# making class user

class User():
    
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def greet(slef):
        print('Welcome %s %s, you registration is ready.' %(self.first_name.title(), self.last_name.title()))

    def skill(self):
        print('Please enter your bio %s' %self.first_name.tittle())

    def user_info(self):
        print('\n*************************************************************\n')
        print('Your info \nFull name: %s %s\nAge: %s\nCity: %s' %(self.first_name.title(), self.last_name.title(), str(self.age), self.city.title()))
        print('\n*************************************************************\n')


slavo_user = User('slavo', 'popovic', 35, 'fort lauderdale')
tamara_user = User('tamara', 'nakic', 33, 'pompano beach')
nenad_user = User('nenad', 'sotirovic', 37, 'Dobrec')
milos_user = User('milos', 'puric', 36, 'belgrade')

slavo_user.user_info()
tamara_user.user_info()
nenad_user.user_info()
milos_user.user_info()

        

    

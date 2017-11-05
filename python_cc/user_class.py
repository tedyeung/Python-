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

# Privilage class

class Privilage():
    
    def __init__(self):
        self.privilage = ['can add post', 'can delete post', 'add user', 'remove user']

    def show_privilage(self):
        print('Admin has those privilages:')
        for priv in self.privilage:
            print('\t\t', priv)


class Admin(User):
    
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privilages = Privilage()
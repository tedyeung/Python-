from user_cl_one import User

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
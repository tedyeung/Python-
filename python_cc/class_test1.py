class Privilage():
    
    def __init__(self):
        self.privilage = ['can add post', 'can delete post', 'add user', 'remove user']

    def show_privilage(self):
        print('Admin has those privilages:')
        for priv in self.privilage:
            print('\t\t', priv)

privil = Privilage()
privil.show_privilage()
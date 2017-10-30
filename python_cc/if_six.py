usernames = ['John', 'Nenad', 'Dragan', 'Marko', 'Jovan', 'Mark', 'Slavo']
admin = 'Slavo'
for username in usernames:
    if admin in usernames:
        print ('Welcome %s, you are admin of this group' %(admin))
    else:
        print ('Welcome %s, you sign up for Mimicom24' %(username))

print ('Thank You all')
print ('***********************************')
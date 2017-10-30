usernames = ['John', 'Nenad', 'Dragan', 'Marko', 'Jovan', 'Mark', 'Slavo']
admins = ['Slavo']
for username in usernames:
    if username in admins:
        print ('Welcome %s, you are admin of this group' %(username))
    else:
        print ('Welcome %s, you sign up for Mimicom24' %(username))

print ('Thank You all')
print ('***********************************')
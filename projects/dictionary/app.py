import json

data = json.load(open('data.json'))

def import_key ():
    word = input('Please add a word that you are interesting: ')
    if word in data:
        return (data[word])
    else: 
        print ("This word is out of the range")

print (import_key())

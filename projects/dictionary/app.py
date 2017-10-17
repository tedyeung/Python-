import json

data = json.load('data.json')

def import_key ():
    word = input('Please add a word that you are interesting: ')
    return (data[word])

print (import_key())

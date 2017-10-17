import json
from difflib import SequenceMatcher

data = json.load(open('data.json'))

def import_key ():
    word = input('Please add a word that you are interesting: ')
    word = word.lower()
    if word in data:
        return (data[word])
    elif len(get_close_matches(w, data.keys())) > 0:
        print ('Did you mean %s please type again:' % get_close_matches(w, data.keys()))[0])
    else: 
        print ("This word is out of the range")

print (import_key())

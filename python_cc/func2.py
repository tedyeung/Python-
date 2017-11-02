# simple func with 2 arg

def city_coutry (city, coutry):
    print(coutry.title(), ',' , city.title())

city_coutry('Belgrade', 'Serbia')
city_coutry('new york', 'usa')
city_coutry('london','england')

# write a simple func that outpu is dic

def make_album(artist, song):
    album = {
        'name': artist,
        'song': song
    }
    return album

active = True
while active:
    artist = input('Please add the name of the artist: ')
    song = input('Plase add a song: ') 
    question = input('Type N to go out! ')
    if question != 'N':
        print('I will ask you again')
    else:
        active = False
        print ('Thank You')

make_album(artist, song)

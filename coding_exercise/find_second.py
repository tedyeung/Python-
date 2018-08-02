danton = "De l'audace, encore de l'audace, toujours de l'audace"


def find_second(str, word):
    start_index  = str.find(word)
    return str.find(word, start_index + 1)


print find_second(danton, 'audace')
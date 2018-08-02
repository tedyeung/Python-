danton = "De l'audace, encore de l'audace, toujours de l'audace"


def find_second(str, index):
    start_index  = str.find('audace')
    return str.find('audace', start_index + 1)


print find_second(danton, 'audace')
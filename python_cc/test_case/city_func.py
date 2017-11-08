def city_country (city, country,  population=0):
    formated_place = city.title() + ',' + country.title()
    if population:
        formated_place += ' - population ' + str(population)
    return formated_place

print (city_country('belgrade', 'serbia'))
    
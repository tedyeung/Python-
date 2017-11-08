def city_country (city, country,  population=0):
    formated_place = city.title() + ',' + country.title()
    if population:
        formated_place += ' - population ' + str(population)
    return formated_place

print (city_country('belgrade', 'serbia', 7000000))
print (city_country('new york', 'usa', 24000000))
    
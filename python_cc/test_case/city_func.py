def city_country (city, country, population):
    formated_place = city.title() + ',' + country.title()
    formated_place += ' - population ' + str(population)
    return formated_place

print (city_country('belgrade', 'serbia', 70000000))
    
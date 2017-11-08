import unittest
from city_func import city_country

class CityTest(unittest.TestCase):
    def name_test_case(self):
        name_title = city_country("belgrade", 'serbia')
        self.assertEqual(name_title,'Belgrade,Serbia')
    
    def name_test_case_population(self):
        name_title_population('belgrade', 'serbia', 7000000)
        self.assertEqual(name_title_population, 'Belgrade, Serbia - population 7000000 ')

unittest.main()
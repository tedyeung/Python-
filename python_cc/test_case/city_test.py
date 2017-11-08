import unittest
from city_func import city_country

class CityTest(unittest.TestCase):
    def name_test_case(self):
        name_title = city_country("belgrade", 'serbia')
        self.assertEqual(name_title,'Belgrade,Serbia')

unittest.main()
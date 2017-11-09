import unittest

from employee import Employee

class TestCase(unittest.TestCase):
    
    def setUP(self):
        self.slavo = Employee('slavo', 'popovic', 125000)

    def test_give_default_raise(self):
        self.slavo.give_raise()
        self.assertEqual(self.slavo.salary, 125000)

    def test_give_raise(self):
        self.slavo.give_raise(25000)
        self.assertEqual(self.slavo.salary, 150000)


unittest.main()
        
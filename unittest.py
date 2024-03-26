import unittest

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

class TestLeapYear(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2004))
        self.assertTrue(is_leap_year(2400))
        self.assertTrue(is_leap_year(1600))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2200))
        self.assertFalse(is_leap_year(2300))
        self.assertFalse(is_leap_year(2500))
        self.assertFalse(is_leap_year(1700))

if __name__ == '__main__':
    unittest.main()

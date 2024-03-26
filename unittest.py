import unittest
from leapyear import leapyear 

class TestLeapYear(unittest.TestCase):

  def test_leap_year_divisible_by_400(self):
    self.assertTrue(leapyear(2000))
    
  def test_leap_year_divisible_by_4_not_100(self):
    self.assertTrue(leapyear(2004))  

  def test_not_leap_year_divisible_by_100_not_400(self):
    self.assertFalse(leapyear(1900))  

  def test_not_leap_year_not_divisible_by_4(self):
    self.assertFalse(leapyear(2001))  

  def test_negative_year(self):
    self.assertFalse(leapyear(-2000)) 



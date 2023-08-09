import unittest
from math import pi
from function import area_of_circle


class TestArea(unittest.TestCase):
    def test_area_of_circle_works(self):
        self.assertAEquals(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)

    def test_area_function_reject_negative_value(self):
        self.assertRaises(ValueError, area_of_circle, -2)

    def  test_area_function_reject_string_value(self):
        self.assertRaises(TypeError, area_of_circle,"Asa")





import unittest
from areacircle import area_of_circle
from math import pi


# def area_of_circle(r):
#     if r<0:
#         raise ValueError('Negative radius value error') # Raise an error if supplied radius is negative. Helps with unit testing as well.
#     return pi*(r**2)


print(area_of_circle(3))

class Test_Area_of_Circle_input(unittest.TestCase):
    # test methods must start with test so that it runs automatically
    # if it does not begin with test, it will not run automatically
    def test_area(self):
        # Test radius >= 0
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(3.5), pi * 3.5**2) 
        self.assertAlmostEqual(area_of_circle(5), pi * 5**2)

    def test_values(self):
        # Test that bad values are caught
        self.assertRaises(ValueError, area_of_circle, -1)

if __name__ == '__main__':
    unittest.main()


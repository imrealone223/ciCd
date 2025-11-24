import unittest
import math
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    
    def test_area_positive_integers(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), 4 * math.pi)
        self.assertAlmostEqual(area(5), 25 * math.pi)
    
    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(1.5), math.pi * 2.25)
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)
    
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            area(-5.5)
    
    def test_area_invalid_types(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            area([1])
        with self.assertRaises(TypeError):
            area(None)
    
    def test_perimeter_positive_integers(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)
    
    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(1.5), 3 * math.pi)
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)
    
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-1)
        with self.assertRaises(ValueError):
            perimeter(-2.5)
    
    def test_perimeter_invalid_types(self):
        with self.assertRaises(TypeError):
            perimeter("10")
        with self.assertRaises(TypeError):
            perimeter({})
        with self.assertRaises(TypeError):
            perimeter(None)

if __name__ == '__main__':
    unittest.main()
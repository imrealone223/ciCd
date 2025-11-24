import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    
    def test_area_positive_integers(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(5, 5), 25)
        self.assertEqual(area(10, 4), 40)
    
    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(2.5, 3.5), 8.75)
        self.assertAlmostEqual(area(1.5, 4.0), 6.0)
    
    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-2, 3)
        with self.assertRaises(ValueError):
            area(2, -3)
        with self.assertRaises(ValueError):
            area(-2, -3)
    
    def test_area_invalid_types(self):
        with self.assertRaises(TypeError):
            area("2", 3)
        with self.assertRaises(TypeError):
            area(2, [3])
        with self.assertRaises(TypeError):
            area(None, 5)
    
    def test_perimeter_positive_integers(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(5, 5), 20)
        self.assertEqual(perimeter(10, 4), 28)
    
    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0)
        self.assertAlmostEqual(perimeter(1.5, 4.0), 11.0)
    
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(0, 0), 0)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-2, 3)
        with self.assertRaises(ValueError):
            perimeter(2, -3)
        with self.assertRaises(ValueError):
            perimeter(-2, -3)
    
    def test_perimeter_invalid_types(self):
        with self.assertRaises(TypeError):
            perimeter("2", 3)
        with self.assertRaises(TypeError):
            perimeter(2, [3]) 
        with self.assertRaises(TypeError):
            perimeter(None, 5)
        with self.assertRaises(TypeError):
            perimeter(2, "3") 

if __name__ == '__main__':
    unittest.main()
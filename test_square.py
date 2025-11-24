import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    
    def test_area_positive_integers(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10), 100)
    
    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(2.5), 6.25)
        self.assertAlmostEqual(area(1.5), 2.25)
    
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-2)
        with self.assertRaises(ValueError):
            area(-5.5)
    
    def test_area_invalid_types(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            area([2])
        with self.assertRaises(TypeError):
            area(None)
    
    def test_perimeter_positive_integers(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
    
    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)
        self.assertAlmostEqual(perimeter(1.5), 6.0)
    
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-2)
        with self.assertRaises(ValueError):
            perimeter(-3.5)
    
    def test_perimeter_invalid_types(self):
        with self.assertRaises(TypeError):
            perimeter("10")
        with self.assertRaises(TypeError):
            perimeter([2]) 
        with self.assertRaises(TypeError):
            perimeter(None)
        with self.assertRaises(TypeError):
            perimeter({"key": "value"}) 

if __name__ == '__main__':
    unittest.main()
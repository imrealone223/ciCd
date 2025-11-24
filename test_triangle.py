import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    
    def test_area_positive_integers(self):
        self.assertEqual(area(2, 3), 3)
        self.assertEqual(area(5, 4), 10)
        self.assertEqual(area(6, 8), 24)
    
    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(2.5, 4.0), 5.0)
        self.assertAlmostEqual(area(3.0, 5.5), 8.25)
    
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
        self.assertEqual(perimeter(2, 3, 4), 9)
        self.assertEqual(perimeter(5, 5, 5), 15)
        self.assertEqual(perimeter(3, 4, 5), 12)
    
    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.0), 10.0)
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.0), 7.0)
    
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 3, 4), 7)
        self.assertEqual(perimeter(2, 0, 4), 6)
        self.assertEqual(perimeter(2, 3, 0), 5)
        self.assertEqual(perimeter(0, 0, 0), 0)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-2, 3, 4)
        with self.assertRaises(ValueError):
            perimeter(2, -3, 4)
        with self.assertRaises(ValueError):
            perimeter(2, 3, -4)
        with self.assertRaises(ValueError):
            perimeter(-2, -3, -4)
    
    def test_perimeter_invalid_types(self):
        with self.assertRaises(TypeError):
            perimeter("2", 3, 4)
        with self.assertRaises(TypeError):
            perimeter(2, "3", 4)
        with self.assertRaises(TypeError):
            perimeter(2, 3, [4])
        with self.assertRaises(TypeError):
            perimeter(None, 3, 4)

if __name__ == '__main__':
    unittest.main()
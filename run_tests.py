import unittest
import sys

if __name__ == '__main__':
    print("Запуск unit-тестов для геометрических фигур")
    print("=" * 50)
    
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 50)
    if result.wasSuccessful():
        print("Все тесты прошли успешно!")
    else:
        print(f"Тесты не пройдены: {len(result.failures)} failures, {len(result.errors)} errors")
    
    sys.exit(0 if result.wasSuccessful() else 1)
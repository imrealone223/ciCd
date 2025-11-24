# Unit-тесты и CI/CD для геометрических фигур

Лабораторная работа №5 по написанию unit-тестов

## Описание
Проект содержит модули для вычисления площадей и периметров геометрических фигур с unit-тестами.

## Функциональность
- circle.py - площадь и длина окружности круга
- rectangle.py - площадь и периметр прямоугольника
- square.py - площадь и периметр квадрата
- triangle.py - площадь и периметр треугольника

## Запуск тестов
### Способ 1: Запуск всех тестов через скрипт
python run_tests.py

### Способ 2: Запуск через unittest discovery
python -m unittest discover -v

### Способ 3: Запуск конкретного теста
python -m unittest test_circle.py -v
python -m unittest test_rectangle.py -v
python -m unittest test_square.py -v
python -m unittest test_triangle.py -v

### Способ 4: Запуск тестов через GitHub Actions на двух runner'ах: ubuntu-latest и windows-latest

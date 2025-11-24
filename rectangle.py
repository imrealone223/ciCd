def area(a, b): 
    '''
    Возвращает площадь прямоугольника.

        Параметры:
            a (int/float): ширина прямоугольника
            b (int/float): длина прямоугольника
    
        Возвращаемое значение:
            area (int/float): произведение a и b
            
        Исключения:
            ValueError: если стороны отрицательные
            TypeError: если стороны не числа
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b 

def perimeter(a, b): 
    '''
    Возвращает периметр прямоугольника.

        Параметры:
            a (int/float): ширина прямоугольника
            b (int/float): длина прямоугольника
    
        Возвращаемое значение:
            perimeter (int/float): удвоенная сумма a и b
            
        Исключения:
            ValueError: если стороны отрицательные
            TypeError: если стороны не числа
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (a + b)
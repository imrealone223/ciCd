def area(a, h): 
    '''
    Возвращает площадь треугольника.

        Параметры:
            a (int/float): сторона треугольника, к которой проведена высота h
            h (int/float): высота треугольника
    
        Возвращаемое значение:
            area (int/float): произведение a и h, деленное на 2
            
        Исключения:
            ValueError: если сторона или высота отрицательные
            TypeError: если сторона или высота не числа
    '''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Сторона и высота должны быть числами")
    if a < 0 or h < 0:
        raise ValueError("Сторона и высота не могут быть отрицательными")
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Возвращает периметр треугольника.

        Параметры:
            a (int/float): первая сторона треугольника
            b (int/float): вторая сторона треугольника
            c (int/float): третья сторона треугольника
    
        Возвращаемое значение:
            perimeter (int/float): сумма a, b и c
            
        Исключения:
            ValueError: если стороны отрицательные
            TypeError: если стороны не числа
    '''    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Все стороны должны быть числами")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a + b + c
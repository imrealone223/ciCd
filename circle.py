import math

def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
            r (int/float): радиус круга
    
        Возвращаемое значение:
            area (float): квадрат радиуса r, умноженный на число pi
            
        Исключения:
            ValueError: если радиус отрицательный
            TypeError: если радиус не число
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r

def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r (int/float): радиус круга
    
        Возвращаемое значение:
            perimeter (float): удвоенный r, умноженный на число pi
            
        Исключения:
            ValueError: если радиус отрицательный
            TypeError: если радиус не число
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r
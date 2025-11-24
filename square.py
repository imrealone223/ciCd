def area(a):
    '''
    Возвращает площадь квадрата.

        Параметры:
            a (int/float): сторона квадрата
    
        Возвращаемое значение:
            area (int/float): квадрат a
            
        Исключения:
            ValueError: если сторона отрицательная
            TypeError: если сторона не число
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return a * a

def perimeter(a):
    '''
    Возвращает периметр квадрата.

        Параметры:
            a (int/float): сторона квадрата
    
        Возвращаемое значение:
            perimeter (int/float): учетверенное a
            
        Исключения:
            ValueError: если сторона отрицательная
            TypeError: если сторона не число
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return 4 * a
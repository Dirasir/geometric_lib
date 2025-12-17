import math


def area(r):
    '''
    Вычисляет площадь круга.
    
      Параметры:
          r (float): радиус круга
          
      Возвращает:
          float: площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет длину окружности.
    
      Параметры:
          r (float): радиус окружности
          
      Возвращает:
          float: длина окружности
    '''
    return 2 * math.pi * r
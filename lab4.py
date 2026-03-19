from typing import Callable
def error_deco(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка в функции '{func.__name__}' : {e}")
            return None
    return wrapper

def range_checker(min, max):
    def deco(func):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not (min <= arg <= max):
                    print(f"Ошибка: аргумент {i} ({arg}) вне допустимого диапазона")
                    return None
            for key, value in kwargs.items():
                if not (min <= value <= max):
                    print(f"Ошибка: аргумент '{key}' ({value}) вне допустимого диапазона")
                    return None
            return func(*args, **kwargs)
        return wrapper
    return deco

@error_deco
def divide(a, b):
    return a / b

@error_deco
def list_element(list, index):
    return list[index]

range_check = range_checker(0, 100)

@range_check
def percentage(value, value1):
    return (value / value1) * 100

@range_check
def sum(a, b, c):
    return a + b + c

print(divide(5, 0))
print(list_element([1, 2, 3, 4, 5], 5))
print(percentage(100, 90))
print(sum(100, 5, 3))

'''
Необходимо реализовать декоратор @strict Декоратор проверяет соответствие типов переданных в вызов функции аргументов
типам аргументов, объявленным в прототипе функции. (подсказка: аннотации типов аргументов можно получить из атрибута
объекта функции func.__annotations__ или с помощью модуля inspect) При несоответствии типов бросать исключение TypeError
Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str Гарантируется, что в
декорируемых функциях не будет значений параметров, заданных по умолчанию
'''


def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for arg, (name, expected_type) in zip(args, annotations.items()):
            # Проверяем, что тип аргумента соответствует ожидаемому типу
            if not isinstance(arg, expected_type) or (expected_type in [int, float] and isinstance(arg, bool)):
                raise TypeError(f"Argument '{name}' must be of type {expected_type.__name__}, got {type(arg).__name__}")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two_ints(a: int, b: int) -> int:
    return a + b


@strict
def sum_two_strs(a: str, b: str) -> str:
    return a + b


@strict
def sum_two_bools(a: bool, b: bool) -> bool:
    return a + b


@strict
def sum_two_floats(a: float, b: float) -> float:
    return a + b

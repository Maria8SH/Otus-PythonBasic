"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import List


def power_numbers(*args: int) -> List:
    return [el ** 2 for el in args]


print(power_numbers(1, 2, 5, 7))
"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
   >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
"""


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def filter_numbers(numbers_list: List, filter_type) -> List:
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers_list))
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers_list))
    if filter_type == PRIME:
        return list(filter(is_prime, numbers_list))


print(filter_numbers([2, 3, 4, 5], 'prime'))
"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""

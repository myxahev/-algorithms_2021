"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

from timeit import timeit
from cProfile import run

enter_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(timeit("func_1(enter_num)", number=3700000, globals=globals()))
run('func_1(enter_num)')

def func_2(nums):
    return nums[::2]

print(timeit("func_2(enter_num)", number=3700000, globals=globals()))
run('func_2(enter_num)')

"""
Выводы: Добавил другой вариант более быстрого решения в котором используется механизм срезов которые считаются быстрыми т.к. они встроенные.
"""
# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик
import math


class PrimeNumbers:
    def __init__(self, n):
        self.prime_numbers = []
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        while self.i < self.n:
            self.i += 1
            for prime in self.prime_numbers:
                if self.i % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i
        else:
            raise StopIteration()


"""
prime_number_iterator = PrimeNumbers(n=1000)
for number in prime_number_iterator:
    print(number)
"""


#  после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    # Оптимизируем генератор тем , что не будем проверять четные числа кроме двойки,
    # т.к. они все делятся на 2 и все числа котрые делятся на 5 кремя пятерки
    # соответственно он должен стать работать еще быстрее
    yield 2
    prime_numbers = [2]
    for number_ in range(3, n + 1, 2):
        for prime in prime_numbers:
            if number_ % prime == 0:
                break
        else:
            if number_ > math.sqrt(n):
                yield number_
            else:
                prime_numbers.append(number_)
                yield number_


def happy_numbers(numbers):
    """Возвращает True, если переданное число - счастливое"""
    list_numbers = []
    numbers = str(numbers)
    if len(numbers) < 2:
        return False
    else:
        for dig in numbers:
            list_numbers.append(int(dig))
        middle = len(list_numbers) // 2
        return True if sum(list_numbers[:middle]) == sum(list_numbers[-1:-(middle + 1):-1]) else False


def palindrom(numbers):
    """Возвращает True, если переданное число - палиндром"""
    numbers = str(numbers)
    if len(numbers) > 1:
        middle = len(numbers) // 2
        return True if numbers[:middle] == numbers[-1:-(middle + 1):-1] else False


def auto_morph(numbers):
    """Возвращает True, если переданное число автоморфное, т.е при возведении в квадрат заканчивается на само себя"""
    x = numbers ** 2
    return True if str(x).endswith(str(numbers)) else False


happy_nums = list(filter(happy_numbers, prime_numbers_generator(10000)))  # список простых чисел и счастивых
for number in happy_nums:
    print(f'{number} - простое и счастливое число')

palindrom_nums = list(filter(palindrom, prime_numbers_generator(10000)))  # список простых чисел и палиндромов
for number in palindrom_nums:
    print(f'{number} - палиндром и простое число')

happy_pal = filter(palindrom, happy_nums)  # список простых, счастливых палиндромов
for number in happy_pal:
    print(f'{number} - палиндром, счастливое и простое число')

auto_morph_nums = list(filter(auto_morph, prime_numbers_generator(10000)))
for number in auto_morph_nums:
    print(f'{number} - автоморфное простое число')

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


func_list = [happy_numbers, palindrom]


def prime_numbers_generator2(n, list_=None):
    def funcs(num, lists=list_):
        if lists is not None:
            list_bool = [func(num) for func in lists]
            return list_bool
        else:
            return [True]

    if False not in funcs(2):
        yield 2
    prime_numbers = [2]
    for number_ in range(3, n + 1, 2):
        for prime in prime_numbers:
            if number_ % prime == 0:
                break
        else:
            if number_ > math.sqrt(n):
                if False not in funcs(number_):
                    yield number_
            else:
                prime_numbers.append(number_)
                #  Для таких случаев в python есть встроенная функция all,
                #  которая возвращает True, если bool(x) является True для
                #  всех элементов переданного на вход объекта:
                #  if all(funcs(number_)):
                if False not in funcs(number_):
                    yield number_


for number in prime_numbers_generator2(10000, func_list):
    print(number)

# зачет!

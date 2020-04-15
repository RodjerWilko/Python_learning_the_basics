# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random

ENLIGHTENMENT_CARMA_LEVEL = 777


class MyBaseException(Exception):
    pass


class IamGodError(MyBaseException):

    def __str__(self):
        return 'IamGodError'


class DrunkError(MyBaseException):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(MyBaseException):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(MyBaseException):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(MyBaseException):
    def __str__(self):
        return 'DepressionError'


class SuicideError(MyBaseException):
    def __str__(self):
        return 'SuicideError'


exceptions = [IamGodError, DrunkError, CarCrashError, GluttonyError,
              DepressionError, SuicideError]


def one_day():
    dice = random.randint(0, 13)
    if dice == 12:
        except_ = exceptions[random.randint(0, 5)]
        raise except_
    else:
        return random.randint(1, 8)


total_carma = 0
total_days = 0

while True:
    if total_carma >= ENLIGHTENMENT_CARMA_LEVEL:
        print(f'Поздравляю за {total_days} дней Ваша карма стала 777 или выше и Вы вышли из бесконечного цикла!!!')
        break
    else:
        try:
            print(total_carma)
            carma = one_day()
            total_days += 1
            total_carma += carma
        except MyBaseException as exc:
            print(f'Вылетело исключение {exc}')
            with open(file='error_log.txt', mode='a') as f:
                f.write(f'{str(exc)}\r')

# https://goo.gl/JnsDqu

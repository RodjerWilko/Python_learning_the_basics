# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'
import os

PATH_OUT = os.path.normpath('function_errors.log')


def log_errors(func):  # ОБЫЧНЫЙ ДЕКОРАТОР
    def surrogate(param):
        try:
            result = func(param)
            return result(param)
        except Exception as e:
            with open(file=PATH_OUT, mode='a', encoding='UTF-8') as ff:
                ff.write(
                    f'имя функции:<{func.__name__}> параметры вызова: <{param} >'
                    f' тип ошибки:  <{e}> текст ошибки :<{e.args}\n>')

    return surrogate


def log_errors_file(file):  # УСЛОЖНЕННЫЙ ДЕКОРАТОР
    def log_errors2(func):
        def surrogate(param):
            try:
                result = func(param)
                return result(param)
            except Exception as e:
                with open(file=os.path.normpath(file), mode='a', encoding='UTF-8') as ff:
                    ff.write(
                        f'имя функции:<{func.__name__}> параметры вызова: <{param} >'
                        f' тип ошибки:  <{e}> текст ошибки :<{e.args}\n>')

        return surrogate

    return log_errors2


@log_errors_file('function_errors.log')
def perky(param):
    return param / 0


@log_errors_file('function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]

for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

perky(param=42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

# зачет!

# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import os


class NotNameError(Exception):
    pass


class NotMailError(Exception):
    pass


def check_valid(stroke):
    stroke = stroke.replace('\n', '').split(' ')
    if len(stroke) < 3:
        raise ValueError('Не указан один из параметров')
    elif not stroke[0].isalpha():
        raise NotNameError('Указано некорректное имя')
    elif '@' not in stroke[1] and '.' not in stroke[0]:
        raise NotMailError('Указана некорректныая почта')
    elif int(stroke[2]) > 99 or int(stroke[2]) < 10:
        raise ValueError('Указан некорректный возраст')
    else:
        return True


PATH = 'registrations.txt'
total_strokes = 0
total_good_log = 0
total_bad_log = 0

with open(file='registrations_good.log', mode='a', encoding='utf8') as log_g, open(file='registrations_bad.log',
                                                                                   mode='a', encoding='utf8') as log_b:
    if os.path.exists(PATH):
        with open(file='registrations.txt', mode='r', encoding='utf-8')as ff:
            for line in ff:
                total_strokes += 1
                try:
                    if check_valid(line):
                        log_g.write(line)
                        total_good_log += 1
                except Exception as exc:
                    log_b.write(f'{line[:-1]} - {exc}\n')
                    total_bad_log += 1

        if (total_good_log + total_bad_log) == total_strokes:
            print('Проверка файла прошла успешно!')
    else:
        print(f'Такого пути : {PATH} - не сущестует')

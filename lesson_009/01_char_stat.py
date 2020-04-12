# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import zipfile


class StatDescending:
    """Упорядочивание по частоте - по убыванию"""

    def __init__(self, file_name):
        self.file_name = file_name

    def unzip(self):
        file_name = os.path.normpath(self.file_name)
        if file_name.endswith('.zip'):
            file = zipfile.ZipFile(file_name, 'r')
            for filename in file.namelist():
                file.extract(filename)
        self.file_name = filename

    def get_stat_dict(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        chars = {}
        with open(self.file_name, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in chars:
                            chars[char] += 1
                        else:
                            chars[char] = 1
        return chars

    def sort_dict(self):
        chars_list = list(self.get_stat_dict().items())
        chars_list.sort(key=lambda i: i[1], reverse=True)
        return chars_list

    def print_stat(self):
        chars_list = self.sort_dict()
        total = 0
        print('+----------+----------+')
        print('|{char_n:^10}|{quantity_n:^10}|'.format(char_n='буква', quantity_n='частота'))
        print('+----------+----------+')

        for char in chars_list:
            print(f'|{char[0]:^10}|{char[1]:^10}|')
            total += char[1]

        print('+----------+----------+')
        print('|{total_nam:^10}|{total_var:^9} |'.format(total_nam='итого', total_var=total))
        print('+----------+----------+')


char_stat = StatDescending(file_name='python_snippets\\voyna-i-mir.txt.zip')
char_stat.print_stat()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

# TODO Отлично получилось. Вы сделали то что нужно.
#  Можно сделать ещё один шаг для унификации кода и сокращении
#  дублирования. Функции sort_dict у всех классов очень похожи и отличаются только
#  индексом в ламбда функции (0 или 1) и направлением сортировки reverse=True|False.
#  Можно сделать для этих настроек сортировки две переменные класса. Тогда
#  sort_dict, в котором эти переменные будут использоваться останеться только в родительском
#  классе. А в классах наследниках нужно будет только менять эти переменные:
#  StatAscending(StatDescending):
#      sort_order = False
#      sort_key = 1

class StatAscending(StatDescending):
    """Упорядочивание по частоте - по возрастанию"""

    def sort_dict(self):
        chars_list = list(self.get_stat_dict().items())
        # TODO вместо lambda в качестве ключа сортировки можно
        #  использовать operator.itemgetter
        chars_list.sort(key=lambda i: i[1], reverse=False)
        return chars_list


class StatAlphaAscending(StatDescending):
    """Упорядочивание по алфавиту - по возрастанию"""

    def sort_dict(self):
        chars_list = list(self.get_stat_dict().items())
        chars_list.sort(key=lambda i: i[0], reverse=False)
        return chars_list


class StatAlphaDescending(StatDescending):
    """Упорядочивание по алфавиту - по убыванию"""

    def sort_dict(self):
        chars_list = list(self.get_stat_dict().items())
        chars_list.sort(key=lambda i: i[0], reverse=True)
        return chars_list


# TODO Лучше использовать библиотеку os.path или pathlib для формирования
#  корректных путей к файлам.
char_stat2 = StatAscending(file_name='python_snippets\\voyna-i-mir.txt.zip')
char_stat2.print_stat()

char_stat3 = StatAlphaAscending(file_name='python_snippets\\voyna-i-mir.txt.zip')
char_stat3.print_stat()

char_stat4 = StatAlphaDescending(file_name='python_snippets\\voyna-i-mir.txt.zip')
char_stat4.print_stat()
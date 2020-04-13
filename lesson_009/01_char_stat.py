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
import operator
import os
import zipfile


class StatDescending:
    """Упорядочивание по частоте - по убыванию"""

    sort_order = True
    sort_key = 1

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
                        # TODO Пропустил при прошлой проверке. Следующие строки можно
                        #  немного оптимизировать.
                        #  Подобная конструкций со словарём может
                        #  быть значительно упрощена, если заменить словарь на
                        #  defaultdict или Counter из библиотеки collections.
                        #  Нужно будет chars = {} заменить на collections.defaultdict(int),
                        #  а из следующих 4 строк оставить одну с +=.  Похожим способом можно
                        #  применить collections.Counter.
                        if char in chars:
                            chars[char] += 1
                        else:
                            chars[char] = 1
        return chars

    def sort_dict(self):
        chars_list = list(self.get_stat_dict().items())
        chars_list.sort(key=operator.itemgetter(self.sort_key), reverse=self.sort_order)
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


char_stat = StatDescending(file_name=os.path.normpath('python_snippets\\voyna-i-mir.txt.zip'))
char_stat.print_stat()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class StatAscending(StatDescending):
    """Упорядочивание по частоте - по возрастанию"""

    sort_order = False
    sort_key = 1


class StatAlphaAscending(StatDescending):
    """Упорядочивание по алфавиту - по возрастанию"""

    sort_order = False
    sort_key = 0


class StatAlphaDescending(StatDescending):
    """Упорядочивание по алфавиту - по убыванию"""

    sort_order = True
    sort_key = 0


char_stat2 = StatAscending(file_name=os.path.normpath('python_snippets\\voyna-i-mir.txt.zip'))
char_stat2.print_stat()

char_stat3 = StatAlphaAscending(file_name=os.path.normpath('python_snippets\\voyna-i-mir.txt.zip'))
char_stat3.print_stat()

char_stat4 = StatAlphaDescending(file_name=os.path.normpath('python_snippets\\voyna-i-mir.txt.zip'))
char_stat4.print_stat()

# -*- coding: utf-8 -*-

import os
import shutil
import time

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

PATH = 'icons'
DESTINATION_PATH = 'icons_by_year'


class CopyByDate:

    def __init__(self, path, destination_path):
        self.path = path
        self.destination_path = destination_path

    def copy_files(self):
        count = 0
        count_copy = 0
        if os.path.exists(self.path):
            os.makedirs(self.destination_path, exist_ok=True)
            for dirpath, dirnames, filenames in os.walk(self.path):
                count += len(filenames)
                for file in filenames:
                    full_file_path = os.path.join(dirpath, file)
                    secs = os.path.getmtime(full_file_path)
                    file_time = time.gmtime(secs)
                    os.makedirs(os.path.join(self.destination_path, str(file_time[0]), str(file_time[1])), exist_ok=True)
                    full_file_destination = os.path.join(self.destination_path, str(file_time[0]), str(file_time[1]), file)
                    shutil.copy2(full_file_path, full_file_destination)
                    count_copy += 1
            if count == count_copy:
                print('Копирование прошло успешно!')
        else:
            print(f'"{self.path}" - Такого пути не существует')


copy = CopyByDate(PATH, DESTINATION_PATH)
copy.copy_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


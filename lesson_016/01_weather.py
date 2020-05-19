# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database

import datetime
from itertools import zip_longest
import requests
import cv2
from bs4 import BeautifulSoup
from playhouse.db_url import connect
from dateutil.relativedelta import relativedelta

from models import dbp, UserTable

CITY = 'cheboksary'
NOW_DATE = datetime.datetime.now()
IMAGE = 'python_snippets/external_data/probe.jpg'


PICTURES = {
    'облачно': 'python_snippets/external_data/weather_img/cloud.jpg',
    'дождь': 'python_snippets/external_data/weather_img/rain.jpg',
    'снег': 'python_snippets/external_data/weather_img/snow.jpg',
    'ясно': 'python_snippets/external_data/weather_img/sun.jpg'
}


class WeatherMaker:

    def __init__(self, city):
        self.city = city
        self.weather_list = []
        self.today_date_pars = 0
        self.month = NOW_DATE
        self.year = NOW_DATE.strftime("%Y")
        self.months_pars = [
            NOW_DATE - relativedelta(months=1),
            NOW_DATE,
            NOW_DATE + relativedelta(months=1)
        ]
        self.week_back = NOW_DATE - relativedelta(days=7)
        self.temp_list = []

    def pars(self):
        """парсим погоду с mail.ru за предыдущий, текущий и следующий месяц"""
        for month in self.months_pars:
            response = requests.get(
                f'https://pogoda.mail.ru/prognoz/cheboksary/{month.strftime("%B").lower()}-{self.year}/')
            if response.status_code == 200:
                html_doc = BeautifulSoup(response.text, features='html.parser')
                list_of_dates = html_doc.find_all('div', {'class': 'day__date'})
                list_of_t_day = html_doc.find_all('div', {'class': 'day__temperature'})
                list_of_t_night = html_doc.find_all('span', {'class': 'day__temperature__night'})
                list_of_desc = html_doc.find_all('div', {'class': 'day__description'})
                for date, temp_d, temp_n, weather_name in zip_longest(list_of_dates, list_of_t_day, list_of_t_night,
                                                                      list_of_desc, fillvalue=''):
                    weather_dict = {}
                    if date.text.startswith('Сегодня'):
                        date = date.text.split('Сегодня')[1].lstrip()
                        self.today_date_pars = date
                    else:
                        date = date.text
                    weather_dict['дата'] = date
                    weather_dict['температура_днем'] = temp_d.text.split()[0][:-1]
                    weather_dict['температура_ночью'] = temp_n.text[:-1]
                    if not weather_name:
                        weather_dict['погода'] = weather_name
                    else:
                        weather_dict['погода'] = weather_name.text.replace('\n', '')
                    self.weather_list.append(weather_dict)

    def print_14_day(self, mode, n):
        """выводит в консоль прогноз за предыдущие(mode=last_d) 'n' дней или cледующие(mode=next_d) в отличии от mode
        """
        for i, day in enumerate(self.weather_list):
            if self.today_date_pars == day['дата']:
                if mode == 'last_d':
                    print(f'\nПогода на {n} дней назад: ')
                    self.temp_list = []
                    for day_dict in self.weather_list[i - n:i]:
                        self.write_temp_dict(day_dict)
                        print(
                            f'Дата : {day_dict["дата"]}, Погода: {day_dict["погода"]}, '
                            f'Температура днем: {day_dict["температура_днем"]}, '
                            f'Температура ночью: {day_dict["температура_ночью"]}')

                elif mode == 'next_d':
                    print(f'\nПогода на {n} дней вперед: ')
                    self.temp_list = []
                    for day_dict in self.weather_list[i:i + n]:
                        self.write_temp_dict(day_dict)
                        print(
                            f'Дата : {day_dict["дата"]}, Погода: {day_dict["погода"]}, '
                            f'Температура днем: {day_dict["температура_днем"]}, '
                            f'Температура ночью: {day_dict["температура_ночью"]}')

    def write_temp_dict(self, day_dict):  # запись во временный словарь
        temp_dict = {}
        temp_dict['дата'] = day_dict["дата"]
        temp_dict['погода'] = day_dict["погода"]
        temp_dict['температура_днем'] = day_dict["температура_днем"]
        temp_dict['температура_ночью'] = day_dict["температура_ночью"]
        self.temp_list.append(temp_dict)


class ImageMaker:
    def __init__(self, w_dict):
        self.image = cv2.imread(IMAGE)
        self.date = w_dict['дата']
        self.t_day = w_dict['температура_днем']
        self.t_night = w_dict['температура_ночью']
        self.desc = w_dict['погода']

    def create_picture(self):
        image_with_line = self.sun()

        image_with_line = self.write_text(image_with_line, f'Дата: {self.date}', (0, 30))
        image_with_line = self.write_text(image_with_line, f'Температура днем: {self.t_day}', (0, 70))
        image_with_line = self.write_text(image_with_line, f'Температу ночью: {self.t_night}', (0, 110))
        image_with_line = self.write_text(image_with_line, f'Погода: {self.desc}', (0, 150))

        image_weather = cv2.imread(PICTURES[self.desc])
        width1, height1 = image_with_line.shape[:2]
        width2, height2 = image_weather.shape[:2]
        image_with_line[width1 - width2:, height1 - height2:] = image_weather[:]
        cv2.imshow('weather', image_with_line)
        cv2.waitKey(0)

    def write_text(self, image, text, org):
        image_ = cv2.putText(image, text, org, fontFace=cv2.FONT_HERSHEY_COMPLEX,
                             fontScale=1,
                             color=(0, 0, 0))
        return image_

    def sun(self):
        image = self.image.copy()
        for x in range(0, 255):
            cv2.line(image, (0, x), (510, x), (x, 255, 255), 1)
        return image

    def rain(self):
        image = self.image.copy()
        for x in range(0, 255):
            cv2.line(image, (0, x), (510, x), (255, x, x), 1)
        return image

    def snow(self):
        image = self.image.copy()
        for x in range(0, 255):
            y = 0
            if y > 64:
                y = 0
            else:
                y = x
            cv2.line(image, (0, x), (510, x), (255, 191 + y, x), 1)
        return image

    def cloud(self):
        image = self.image.copy()
        for x in range(0, 128):
            cv2.line(image, (0, x), (510, x), (128 + x, 128 + x, 128 + x), 1)
        return image


class DatabaseUpdater:
    """Класс работы с базой данных, поключение, добавление данных, получение данных

    """
    # TODO Хорошо бы параметром передавать и ссылку и dbp
    # TODO И в init инициализировать это всё. В init Так же можно создание таблицы добавить
    db = connect('postgresql://postgres:123456@localhost:5432/weather')
    dbp.initialize(db)

    def add_days(self, w_list):  # добавление выбранного диапозон в базу
        dbp.create_tables([UserTable], safe=True)
        for day in w_list:
            new_w = UserTable(date=day['дата'], t_day=day['температура_днем'], t_night=day['температура_ночью'],
                              desc=day['погода'])
            new_w.save()

    def get_days(self):  # получение всех данных из базы
        for day in UserTable.select():
            print(
                f'Дата: {day.date}, Погода: {day.desc}, Температура днем {day.t_day}, Температура ночью {day.t_night}')

# TODO Менюшки хорошо бы вынести в отдельный модуль (как было с игрой быки и коровы)
# TODO И там объединить в класс. + можно по желанию добавить argparse
def menu_first():  # вывод меню №1 с дальнейшей логикой
    print('\nВыберите диапозон дат для вывода прогноза на консоль:')
    print('\n1. Прогноз с сегодняшнего дня и на 14 дней вперед \n2. Прогноз на 14 дней назад')

    user_input = input('\nВведите номер пункта меню: ')

    if user_input == '1':
        weather.print_14_day('next_d', 14)
    elif user_input == '2':
        weather.print_14_day('last_d', 14)
    else:
        print('Введен неверный номер')
        menu_first()


def menu_second():  # вывод меню №2 с дальнейшей логикой
    print('\nХотите записать резльтаты в базу данных?')
    print('\n1. Да \n2. Нет')

    user_input = input('\nВведите номер пункта меню: ')

    if user_input == '1':
        try:
            base.add_days(weather.temp_list)
        except Exception:
            print('Возникла ошибка, попробуйте еще раз')
            menu_second()
        else:
            print('Данные успешно добавлены в базу')
    elif user_input == '2':
        pass
    else:
        print('Введен неверный номер')
        menu_second()


def menu_third():  # вывод меню №3 с дальнейшей логикой
    print('\nХотите сделать открытку с прогнозом')
    print('\n1. Да \n2. Нет')

    user_input = input('\nВведите номер пункта меню: ')

    if user_input == '1':
        print('\nВыберите дату для открытки')
        for i, day in enumerate(weather.temp_list):
            print(f'{i + 1}. {day["дата"]}')
        user_input2 = int(input('\nВыберите номер дня: '))
        image_maker = ImageMaker(weather.temp_list[user_input2 - 1])
        image_maker.create_picture()

    elif user_input == '2':
        pass
    else:
        print('Введен неверный номер')
        menu_third()


def menu_fours():
    print('\nХотите получить резльтаты находящиеся в базе?')
    print('\n1. Да \n2. Нет')

    user_input = input('\nВведите номер пункта меню: ')

    if user_input == '1':
        try:
            base.get_days()
        except Exception:
            print('Возникла ошибка, возможно в базе еще нет данных попробуйте еще раз')
            menu_fours()
        else:
            print('')
    elif user_input == '2':
        pass
    else:
        print('Введен неверный номер')
        menu_fours()


weather = WeatherMaker(CITY)
weather.pars()
base = DatabaseUpdater()
print('Погода прошлой недели: ')
weather.print_14_day('last_d', 7)
# TODO Тут стоит какой-то цикл создать, а нужные менюшки вызывать по выбору пользователя
menu_first()
menu_second()
menu_third()
menu_fours()

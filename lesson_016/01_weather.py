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
from weather_menu import WeatherMenu as Wm
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

URL = 'postgresql://postgres:123456@localhost:5432/weather'


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


class ImageMaker:
    def __init__(self):
        self.image = ''
        self.date = ''
        self.t_day = ''
        self.t_night = ''
        self.desc = ''

    def create_picture(self, w_dict):
        self.image = cv2.imread(IMAGE)
        self.date = w_dict['дата']
        self.t_day = w_dict['температура_днем']
        self.t_night = w_dict['температура_ночью']
        self.desc = w_dict['погода']

        image_with_line = self.gradient()

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

    def gradient(self):
        list_col = []
        if self.desc == 'ясно':
            list_col = [0, 255, 255, 0, 0]
        elif self.desc == 'дождь':
            list_col = [255, 0, 0, 0, 0]
        elif self.desc == 'облачно':
            list_col = [128, 128, 128, 0, 0]
        elif self.desc == 'снег':
            list_col = [255, 191, 0, 0, 0]
        image = self.image.copy()
        while list_col[4] < 255:
            for i, j in enumerate(list_col):
                if j < 255:
                    list_col[i] += 1
            cv2.line(image, (0, list_col[3]), (510, list_col[4]), (list_col[0], list_col[1], list_col[2]), 1)
        return image


class DatabaseUpdater:
    """Класс работы с базой данных, поключение, добавление данных, получение данных """

    def __init__(self, url, proxy):
        self.dbp = proxy
        self.db = connect(url)
        self.dbp.initialize(self.db)
        self.dbp.create_tables([UserTable], safe=True)

    def add_days(self, w_list):  # добавление выбранного диапозон в базу
        for day in w_list:
            new_w = UserTable(date=day['дата'],
                              t_day=day['температура_днем'],
                              t_night=day['температура_ночью'],
                              desc=day['погода']
                              )
            new_w.save()

    def get_days(self):  # получение всех данных из базы
        for day in UserTable.select():
            print(
                f'Дата: {day.date},'
                f' Погода: {day.desc},'
                f' Температура днем {day.t_day},'
                f' Температура ночью {day.t_night}'
            )


weather = WeatherMaker(CITY)
weather.pars()
base = DatabaseUpdater(URL, dbp)
image_maker = ImageMaker()
menu = Wm(weather.weather_list, weather.today_date_pars, base, weather, image_maker)
print('Погода прошлой недели: ')
menu.print_14_day('last_d', 7)

while True:
    print('\n1. Получить прогнозы за другой диапазон дат'
          '\n2. Записать полученные прогнозы в базу данных'
          '\n3. Создать открытку-прогноз по выбранной дате'
          '\n4. Выгрузить из базы данных все прогнозы'
          '\nЧтобы остановить выйти из программы введите "q"'
          )
    user_input = input('\nВведите пункт меню: ')
    if user_input == '1':
        menu.first()
    elif user_input == '2':
        menu.second()
    elif user_input == '3':
        menu.third()
    elif user_input == '4':
        menu.fours()
    elif user_input == 'q':
        break
    else:
        print('Введен неверный пункт меню')
#зачет!
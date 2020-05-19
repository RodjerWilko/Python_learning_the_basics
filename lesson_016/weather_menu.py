class WeatherMenu:
    def __init__(self, weather_list, today_date_pars, base, weather, image_maker):
        self.temp_list = []
        self.weather_list = weather_list
        self.today_date_pars = today_date_pars
        self.base = base
        self.weather = weather
        self.image_maker = image_maker

    def print_14_day(self, mode, n):
        """
        выводит в консоль прогноз за предыдущие(mode=last_d) 'n' дней или cледующие(mode=next_d) в отличии от mode
        """
        for i, day in enumerate(self.weather_list):
            if self.today_date_pars == day['дата']:
                if mode == 'last_d':
                    print(f'\nПолучены прогнозы на {n} дней назад: ')
                    self.temp_list = []
                    for day_dict in self.weather_list[i - n:i]:
                        self.write_temp_dict(day_dict)
                        print(
                            f'Дата : {day_dict["дата"]}, Погода: {day_dict["погода"]}, '
                            f'Температура днем: {day_dict["температура_днем"]}, '
                            f'Температура ночью: {day_dict["температура_ночью"]}')

                elif mode == 'next_d':
                    print(f'\nПолучены прогнозы на {n} дней вперед: ')
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

    def first(self):  # вывод меню №1 с дальнейшей логикой
        print('\nВыберите диапозон дат для вывода прогноза на консоль:')
        print('\n1. Прогноз с сегодняшнего дня и на 14 дней вперед'
              '\n2. Прогноз на 14 дней назад'
              '\nЧтобы вернуться в главное меню введите "q"')

        user_input = input('\nВведите номер пункта меню: ')

        if user_input == '1':
            self.print_14_day('next_d', 14)
        elif user_input == '2':
            self.print_14_day('last_d', 14)
        elif user_input == 'q':
            return
        else:
            print('Введен неверный номер')
            self.first()

    def second(self):  # вывод меню №2 с дальнейшей логикой
        print('\nХотите записать резльтаты в базу данных?')
        print('\n1. Да \n2. Нет(вернуться в главное меню)')

        user_input = input('\nВведите номер пункта меню: ')

        if user_input == '1':
            try:
                self.base.add_days(self.temp_list)
            except Exception:
                print('Возникла ошибка, попробуйте еще раз')
                self.second()
            else:
                print('Данные успешно добавлены в базу')
        elif user_input == '2':
            return
        else:
            print('Введен неверный номер')
            self.second()

    def third(self):  # вывод меню №3 с дальнейшей логикой
        print('\nХотите сделать открытку с прогнозом')
        print('\n1. Да \n2. Нет(вернуться в главное меню)')

        user_input = input('\nВведите номер пункта меню: ')

        if user_input == '1':
            print('\nВыберите дату для открытки')
            for i, day in enumerate(self.temp_list):
                print(f'{i + 1}. {day["дата"]}')
            user_input2 = int(input('\nВыберите номер дня: '))
            self.image_maker.create_picture(self.temp_list[user_input2 - 1])

        elif user_input == '2':
            return
        else:
            print('Введен неверный номер')
            self.third()

    def fours(self):
        print('\nХотите получить резльтаты находящиеся в базе?')
        print('\n1. Да \n2. Нет(вернуться в главное меню)')

        user_input = input('\nВведите номер пункта меню: ')

        if user_input == '1':
            try:
                self.base.get_days()
            except Exception:
                print('Возникла ошибка, возможно в базе еще нет данных попробуйте еще раз')
                self.fours()
            else:
                print('')
        elif user_input == '2':
            return
        else:
            print('Введен неверный номер')
            self.fours()

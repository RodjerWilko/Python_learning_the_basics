# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...

import csv
import datetime
import json
import time
from decimal import Decimal

from termcolor import cprint, COLORS

remaining_time = '123456.0987654321'
field_names = ['current_location', 'current_experience', 'time left', 'current_date']
DICT_TEXTS = {
    'win': "\nУРА!!!! ВЫ ВЫБРАЛИСЬ ИЗ ПОДЗЕМЕЛЬЯ И УБИЛИ ВСЕХ МОНСТРОВ!!!!",
    'lose_time': """\nВы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
                     \rУ вас темнеет в глазах... прощай, принцесса...
                     \rНо что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
                     \rНу, на этот-то раз у вас все получится! Трепещите, монстры!
                     \rВы осторожно входите в пещеру...""",
    'exit': "\nВы вышли, но мы все равно записали когда это было",
    'begin': """\n...Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой,
                 \rпостоянно выходящей из берегов. Из-за этого подземелье регулярно затапливается, монстры выживают,
                 \rно не герои, рискнувшие спуститься к ним в поисках приключений.
                 \rПочуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. 
                 \rНа защиту всех деревень не хватило солдат и вас, как известного в этих краях героя,
                 \rнаняли для их спасения....""",
    'rules': """\nПРАВИЛА ИГРЫ:
                \rПо мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
                \rв каждую локацию можно попасть только один раз,
                \rи выйти из нее нельзя (то есть двигаться можно только вперед).

                \rЧтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
                \rЕсли до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
                \rготовый к следующей попытке (игра начинается заново)."""
}


class Game:

    def __init__(self):
        self.curr_loc = {}  # текущая локация (значение из словаря локации)
        self.curr_loc_n = ''  # имя текущей локации (ключ из словаря локации)
        self.curr_exp = 0  # текущий опыт
        self.list_mons = []  # временный список монстров в текущей локации
        self.list_rooms = []  # временный список локация для перехода в текущей локации
        self.elaps_time = Decimal('0.00')  # времени прошло
        self.rem_time = Decimal(remaining_time)  # общее время изначально
        self.time_left = Decimal('0.00')  # оставшееся время
        self.user_num = 0  # ввод пользователя
        self.num_mon = 0  # ввод пользователя
        self.user_input = 0  # ввод пользователя
        self.mons = ''  # текущий монстр

    def open_json(self):
        """создает файл csv с названиями таблиц и обнуляет значения атрибутов"""
        with open('rpg.json', 'r')as file_map:
            self.curr_loc = json.load(file_map)
            self.curr_exp = 0
            self.rem_time = Decimal(remaining_time)
            self.elaps_time = Decimal('0.00')
        with open('score.csv', 'a', newline='') as out_csv:
            writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=field_names)
            writer.writeheader()

    def where_i_am(self):
        """
        проверяет сколько времени осталось до наводнения, в какой локации находится игрок
        и записывает текущих монстров и локации во временные списки

        """
        self.time_left = self.rem_time - self.elaps_time
        self.list_mons = []
        self.list_rooms = []
        for k, v in self.curr_loc.items():
            self.curr_loc_n = k
            cprint(f'\n<<<Вы находитесь в {self.curr_loc_n}>>>', color='green')
        cprint(f'\nУ вас {self.curr_exp} опыта и осталось {self.time_left} секунд до наводнения',
               color='yellow')
        if (self.rem_time - self.elaps_time) < 0:  # если времени осталось меньше нуля вызов game_over('lose_time')
            self.game_over('lose_time')
        else:
            if 'Hatch' in self.curr_loc_n:  # если в имени текущей локации есть 'Hatch' то вызов game_over('win')
                self.game_over('win')
            else:
                cprint(f'Прошло времени: {self.elaps_time}\n', color='white')
                cprint('Внутри вы видите:', color='white')
                for loc_k, loc_v in self.curr_loc.items():
                    for i, cont in enumerate(loc_v):
                        if type(cont) == str:
                            cprint(f'- Монстра {cont} ', color='grey')
                            self.list_mons.append(cont)
                        else:
                            for k, v in cont.items():
                                cprint(f"- Вход в локацию:  {k}", color='grey')
                                self.list_rooms.append([k, i])

    def error_message(self):
        """ вывод сообщения об ошибке с паузой в 2 секунды"""

        cprint('\n!!! ОШИБКА! ВЫ ВВЕЛИ НЕВРНЫЙ СИМВОЛ !!!', color='red')
        time.sleep(2)

    def main_menu_choose(self):
        """ вывод выбора действия с получением ответа от пользователя"""
        cprint('Выберите действие:'
               '\n1.Атаковать монстра'
               '\n2.Перейти в другую локацию'
               '\n3.Сдаться и выйти из игры', color='white')
        self.user_input = int(input('Введите число: '))

    def attack_monster(self):
        """ вывод меню атаки монстра, с получением от пользователя номера монстра"""
        print('\nВы выбрали сражаться с монстром')
        for i, mon in enumerate(self.list_mons):
            cprint(f'{i + 1}.{mon}', color='grey')
        self.num_mon = int(input('\nВведите номер монстра с которым хотите сразиться: '))
        if self.num_mon > len(self.list_mons) or self.num_mon <= 0:
            raise IndexError

    def logic_attack_monster(self):
        """логика атаки монстра"""
        self.mons = self.list_mons[self.num_mon - 1]
        mons_pars = self.mons.split('_')
        exp = int(mons_pars[1].replace('exp', ''))
        tm = float(mons_pars[2].replace('tm', ''))
        self.curr_exp += exp
        self.curr_loc[self.curr_loc_n].remove(self.mons)
        self.elaps_time += int(tm)

    def go_to_location(self):
        """вывод меню перехода в локацию, с получением от пользователя номера локации"""
        print('\nВы выбрали переход в локацию')
        for n, loc in enumerate(self.list_rooms):
            cprint(f'{n + 1}.{loc[0]}', color='grey')
        self.user_num = int(input('\nВведите номер локации в которую хотите перейти: '))
        if self.user_num > len(self.list_rooms) or self.user_num <= 0:
            raise IndexError

    def logic_go_to_location(self):
        """логика перехода в локацию"""
        self.test_location()
        tm = self.list_rooms[self.user_num - 1][0].split('_')[2]
        tm = Decimal(tm.replace('tm', ''))
        self.elaps_time += tm
        self.time_left = self.rem_time - self.elaps_time
        self.write_csv()

    def final_room(self):
        """логика если пользователь выбрал финальную локацию"""
        win_room_tm = self.list_rooms[self.user_num - 1][0]
        win_room_tm = win_room_tm.split('_')
        win_room_tm = Decimal(win_room_tm[1].replace('tm', ''))
        if self.curr_exp >= 280:
            self.test_location()
            self.elaps_time += win_room_tm
        else:
            cprint('\n!!! ОЧКОВ ОПЫТА НЕДОСТАТОЧНО ЧТОБЫ ОТКРЫТЬ ЛЮК !!!', color='red')
            time.sleep(2)

    def what_i_can_do(self):
        """меню с выводом вариантов действий"""
        try:
            self.main_menu_choose()
        except ValueError:
            self.error_message()
        else:

            if self.user_input == 1:  # сразиться с монстром
                if self.list_mons:
                    try:
                        self.attack_monster()
                        self.logic_attack_monster()
                    except Exception:
                        self.error_message()
                else:
                    self.error_message()

            elif self.user_input == 2:  # переход в локацию
                if not self.list_rooms:
                    self.error_message()
                else:
                    try:
                        self.go_to_location()
                        if 'Hatch' in self.list_rooms[self.user_num - 1][0]:
                            self.final_room()
                        else:
                            self.logic_go_to_location()
                    except Exception:
                        self.error_message()

            elif self.user_input == 3:  # выход из игры по желанию пользователя
                self.game_over('exit')

            else:
                self.error_message()

    def test_location(self):  # проверка на правильно введенную локацию
        try:
            self.curr_loc = self.curr_loc[self.curr_loc_n][self.list_rooms[self.user_num - 1][1]]
        except IndexError:
            self.error_message()

    def except_continue(self):
        time.sleep(2)
        self.what_i_can_do()

    def write_csv(self):  # запись в csv файл результатов игры
        date = datetime.datetime.now()
        dict_end = [{'current_location': self.curr_loc_n,
                     'current_experience': self.curr_exp,
                     'time left': self.rem_time - self.elaps_time,
                     'current_date': date.strftime("%Y-%m-%d %H:%M")}]

        with open('score.csv', 'a', newline='') as out_csv:
            writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=field_names)
            writer.writerows(dict_end)

    def game_over(self, text):
        """варианты окончанию игры в зависимости от победы проигрыша или выбора пользователя"""
        if text == 'exit':  # если пользователь сам выбрал выход
            print(DICT_TEXTS['exit'])
            self.write_csv()
            time.sleep(2)
            exit()

        elif text == 'lose_time':  # Если закончилось время
            cprint(DICT_TEXTS['lose_time'], color='red')
            time.sleep(4)
            self.open_json()
            self.where_i_am()
            self.write_csv()

        else:  # если пользоватеь победил
            for color in COLORS:
                cprint(DICT_TEXTS['win'], color=color)
                time.sleep(0.5)
            self.write_csv()
            exit()


def start_game():
    """ старт игры """
    g = Game()
    g.open_json()
    cprint(DICT_TEXTS['begin'], color='green')
    cprint(DICT_TEXTS['rules'], color='cyan')
    while True:
        g.where_i_am()
        g.what_i_can_do()


if __name__ == '__main__':
    start_game()

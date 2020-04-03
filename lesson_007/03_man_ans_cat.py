# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py
# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.
# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)
# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня
# Человеку и коту надо вместе прожить 365 дней.


class Cat:

    def __init__(self):
        self.fullness = 50
        self.house = None
        self.name = 'кот'

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        cprint('{} поел'.format(self.name), color='magenta')
        self.fullness += 20
        self.house.cat_food -= 10

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='magenta')
        self.fullness -= 10

    def tear_wallpaper(self):
        cprint('{} подрал обои'.format(self.name), color='magenta')
        self.fullness -= 10
        self.house.mud += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20 and self.house.cat_food > 10:
            self.eat()
        elif self.house.cat_food < 10:
            self.tear_wallpaper()
        elif dice == 1:
            self.tear_wallpaper()
        elif dice == 2:
            self.sleep()
        else:
            self.sleep()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def clean_house(self):
        cprint('{} убрался дома'.format(self.name), color='magenta')
        self.house.mud -= 100
        self.fullness += 20

    def pickup_cat(self, _cat):
        cprint('{} подобрал кота, по имени {}'.format(self.name, _cat.name), color='magenta')

        _cat.house = self.house

    def buy_cat_food(self):
        if self.house.cat_food <= 10:
            if self.house.money >= 50:
                cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
                self.house.money -= 50
                self.house.cat_food += 50
            else:
                cprint('{} деньги кончились!'.format(self.name), color='red')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food < 20:
            self.buy_cat_food()
        elif self.house.money < 50:
            self.work()
        elif self.house.mud > 150:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.cat_food = 0
        self.mud = 0

    def __str__(self):
        return 'В доме еды для человека осталось {}, еды для кота осталось {} денег осталось {},' \
               ' грязи в доме {}'.format(self.food, self.cat_food, self.money, self.mud)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

my_sweet_home = House()
man = Man('Вася')
cats = []
for i in range(0, 4):
    cats.append(Cat())

man.go_to_the_house(my_sweet_home)
for cat in cats:
    man.pickup_cat(cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    man.act()
    for cat in cats:
        cat.act()

    print('--- в конце дня ---')
    print(man)
    for cat in cats:
        print(cat)
    print(my_sweet_home)

# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# ####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.filth = 0

    def act(self):
        self.filth += 5

    def __str__(self):
        return 'В доме : денег : {}, еды : {}, грязи : {}'.format(self.money, self.food, self.filth)


class Human:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return 'Я - {}, сытость : {}, счастье : {}'.format(self.name, self.fullness,
                                                           self.happiness)

    def eat(self):
        if self.house.food <= 0:
            cprint('В доме кончилась еда', color='red')
        else:
            self.fullness += 30
            self.house.food -= 30
            cprint('{} поел'.format(self.name), color='green')


class Husband(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.filth > 90:
            self.happiness -= 10
        if self.fullness < 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        if self.happiness < 10:
            cprint('{} умер от депресии'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 20:
            self.work()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.gaming()
        else:
            self.work()

    # TODO Вы не меняете поведение родительского метода,
    #  не нужно его переопределять.
    def eat(self):
        super().eat()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        cprint('{} сходил на работу'.format(self.name), color='green')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} поиграл в танчики'.format(self.name), color='green')


class Wife(Human):

    # TODO Вы не меняете поведение родительского метода __init__
    #  не нужно его переопределять.
    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    # TODO Вы не меняете поведение родительского метода __str__
    #  не нужно его переопределять.
    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.filth > 90:
            self.happiness -= 10
        if self.fullness < 0:
            cprint('{} умерла от голода'.format(self.name), color='red')
            return
        if self.happiness < 10:
            cprint('{} умерла от депресии'.format(self.name), color='red')
            return
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.filth > 90:
            self.clean_house()
        else:
            self.buy_fur_coat()

    # TODO Вы не меняете поведение родительского метода,
    #  не нужно его переопределять.
    def eat(self):
        super().eat()

    def shopping(self):
        if self.house.money < 30:
            cprint('В доме не хватает денег на еду', color='red')
            return
        self.house.money -= 30
        self.house.food += 30
        self.fullness -= 10
        cprint('{} сходила в магащин за едой'.format(self.name), color='green')

    def buy_fur_coat(self):
        if self.house.money < 350:
            cprint('В доме не хватает денег на шубу', color='red')
            return
        self.house.money -= 350
        self.happiness += 60
        self.fullness -= 10
        cprint('{} купила шубу'.format(self.name), color='green')

    def clean_house(self):
        self.fullness -= 10
        self.house.filth -= 100
        cprint('{} убралась дома'.format(self.name), color='green')


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='white')
    home.act()
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')


# ####################################################### Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


# ####################################################### Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.happiness = 100

    # TODO Вы не меняете поведение родительского метода,
    #  не нужно его переопределять.
    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness < 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        if self.fullness < 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food <= 0:
            cprint('В доме кончилась еда', color='red')
        else:
            self.house.food -= 10
            cprint('{} поел'.format(self.name), color='green')

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='green')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

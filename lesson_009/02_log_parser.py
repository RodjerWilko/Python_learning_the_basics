# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


FILE_IN = 'events.txt'
FILE_OUT = 'out.txt'


class LogParserByMinute:
    """Подсчитывает число событий за минуту"""

    def __init__(self, file_in, file_out):
        self.file_in = file_in
        self.file_out = file_out

    def get_log_dict(self):
        my_log_list = []
        with open(file=self.file_in, mode='r') as file:
            for line in file:
                my_log_list.append(line.split('-'))

        my_log_dict = []

        for day in my_log_list:
            my_dict = {'year': day[0].lstrip('['), 'month': day[1], 'day': day[2].split(' ')[0],
                       'hour': day[2].split(' ')[1].split(':')[0], 'minute': day[2].split(' ')[1].split(':')[1],
                       'second': day[2].split(' ')[1].split(':')[2].rstrip(']'),
                       'status': day[2].split(' ')[2].rstrip('\n'),
                       'count': 0}
            my_log_dict.append(my_dict)
        return my_log_dict

    def get_stat_list(self):
        log_sum = []

        for day in self.get_log_dict():
            if day['status'] == 'NOK':
                # TODO Вы немного переусложинили условия обработки строк.
                #  Можно не разделять дату на дни, месяцы, ...
                #  Достаточно сделать срез строки на нужном сндексе.
                #  Для года из строки нужно вырезать символы с 2 по 5,
                #  чтобы получилась строка 2018, для месяца нужно вырезать 2018-05 и т. д.
                if log_sum:
                    for i, day2 in enumerate(log_sum):
                        if day['year'] == day2['year']:
                            if day['month'] == day2['month']:
                                if day['day'] == day2['day']:
                                    if day['hour'] == day2['hour']:
                                        if day['minute'] == day2['minute']:
                                            day2['count'] += 1
                                        else:
                                            if i == (len(log_sum) - 1):
                                                log_sum.append(day)
                                            else:
                                                continue
                                    else:
                                        if i == (len(log_sum) - 1):
                                            log_sum.append(day)
                                        else:
                                            continue
                                else:
                                    if i == (len(log_sum) - 1):
                                        log_sum.append(day)
                                    else:
                                        continue
                            else:
                                if i == (len(log_sum) - 1):
                                    log_sum.append(day)
                                else:
                                    continue
                        else:
                            if i == (len(log_sum) - 1):
                                log_sum.append(day)
                            else:
                                continue
                else:
                    log_sum.append(day)
            else:
                continue
        return log_sum

    def write_out(self):

        with open(self.file_out, 'w') as file_out:
            for x in self.get_stat_list():
                file_out.write(f'[{x["year"]}-{x["month"]}-{x["day"]} {x["hour"]}:{x["minute"]}] {x["count"]}\n')


parser = LogParserByMinute(FILE_IN, FILE_OUT)
parser.write_out()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

class LogParserByHours(LogParserByMinute):
    """Подсчитывает число событий за час"""

    def get_stat_list(self):
        log_sum = []

        for day in self.get_log_dict():
            if day['status'] == 'NOK':
                if log_sum:
                    for i, day2 in enumerate(log_sum):
                        if day['year'] == day2['year']:
                            if day['month'] == day2['month']:
                                if day['day'] == day2['day']:
                                    if day['hour'] == day2['hour']:
                                        day2['count'] += 1
                                    else:
                                        if i == (len(log_sum) - 1):
                                            log_sum.append(day)
                                        else:
                                            continue
                                else:
                                    if i == (len(log_sum) - 1):
                                        log_sum.append(day)
                                    else:
                                        continue
                            else:
                                if i == (len(log_sum) - 1):
                                    log_sum.append(day)
                                else:
                                    continue
                        else:
                            if i == (len(log_sum) - 1):
                                log_sum.append(day)
                            else:
                                continue
                else:
                    log_sum.append(day)
            else:
                continue
        return log_sum

    def write_out(self):

        with open(self.file_out, 'w') as file_out:
            for x in self.get_stat_list():
                file_out.write(f'[{x["year"]}-{x["month"]}-{x["day"]} {x["hour"]}:00] {x["count"]}\n')


class LogParserByMonth(LogParserByMinute):
    """Подсчитывает число событий за месяц"""

    def get_stat_list(self):
        log_sum = []

        for day in self.get_log_dict():
            if day['status'] == 'NOK':
                if log_sum:
                    for i, day2 in enumerate(log_sum):
                        if day['year'] == day2['year']:
                            if day['month'] == day2['month']:
                                day2['count'] += 1
                            else:
                                if i == (len(log_sum) - 1):
                                    log_sum.append(day)
                                else:
                                    continue
                        else:
                            if i == (len(log_sum) - 1):
                                log_sum.append(day)
                            else:
                                continue
                else:
                    log_sum.append(day)
            else:
                continue
        return log_sum

    def write_out(self):

        with open(self.file_out, 'w') as file_out:
            for x in self.get_stat_list():
                file_out.write(f'[{x["year"]}-{x["month"]}] {x["count"]}\n')


class LogParserByYear(LogParserByMinute):
    """Подсчитывает число событий за год"""

    def get_stat_list(self):
        log_sum = []

        for day in self.get_log_dict():
            if day['status'] == 'NOK':
                if log_sum:
                    for i, day2 in enumerate(log_sum):
                        if day['year'] == day2['year']:
                            day2['count'] += 1
                        else:
                            if i == (len(log_sum) - 1):
                                log_sum.append(day)
                            else:
                                continue
                else:
                    log_sum.append(day)
            else:
                continue
        return log_sum

    def write_out(self):

        with open(self.file_out, 'w') as file_out:
            for x in self.get_stat_list():
                file_out.write(f'[{x["year"]}] {x["count"]}\n')


parser = LogParserByHours(FILE_IN, FILE_OUT)
parser.write_out()
parser = LogParserByMonth(FILE_IN, FILE_OUT)
parser.write_out()
parser = LogParserByYear(FILE_IN, FILE_OUT)
parser.write_out()

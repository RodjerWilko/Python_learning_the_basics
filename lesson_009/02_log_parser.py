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
        my_log_dict = []
        with open(file=self.file_in, mode='r') as file:
            for line in file:
                if line.split(' ')[2].replace('\n', '') == 'NOK':
                    my_log_list.append(line.replace('\n', ''))

        for day in my_log_list:
            my_dict = {
                'day': day,
                'count': 0
            }

            my_log_dict.append(my_dict)

        return my_log_dict

    def get_stat_list(self):
        log_sum = []
        for day in self.get_log_dict():
            if log_sum:
                for i, day2 in enumerate(log_sum):
                    if day['day'][1:17] == day2['day'][1:17]:
                        day2['count'] += 1
                    else:
                        if i == (len(log_sum) - 1):
                            log_sum.append(day)
            else:
                day['count'] = 1
                log_sum.append(day)

        return log_sum

    def write_out(self):
        with open(self.file_out, 'w') as file_out:
            for x in self.get_stat_list():
                file_out.write(f'{x["day"][0:17]}] {x["count"]}\n')


parser = LogParserByMinute(FILE_IN, FILE_OUT)
parser.write_out()


class LogParserByHours(LogParserByMinute):
    """Подсчитывает число событий за час"""

    def get_stat_list(self):
        log_sum = []
        for day in self.get_log_dict():
            if log_sum:
                for i, day2 in enumerate(log_sum):
                    if day['day'][1:14] == day2['day'][1:14]:
                        day2['count'] += 1
                    else:
                        if i == (len(log_sum) - 1):
                            log_sum.append(day)
            else:
                day['count'] = 1
                log_sum.append(day)

        return log_sum

    def write_out(self):
        with open(self.file_out, 'w') as file_out:
            for x in self.get_stat_list():
                file_out.write(f'{x["day"][0:14]}:00] {x["count"]}\n')


class LogParserByMonth(LogParserByMinute):
    """Подсчитывает число событий за месяц"""

    def get_stat_list(self):
        log_sum = []
        for day in self.get_log_dict():
            if log_sum:
                for i, day2 in enumerate(log_sum):
                    if day['day'][1:8] == day2['day'][1:8]:
                        day2['count'] += 1
                    else:
                        if i == (len(log_sum) - 1):
                            log_sum.append(day)
            else:
                day['count'] = 1
                log_sum.append(day)

        return log_sum

    def write_out(self):
        with open(self.file_out, 'w') as file_out:
            for x in self.get_stat_list():
                file_out.write(f'{x["day"][0:8]}] {x["count"]}\n')


class LogParserByYear(LogParserByMinute):
    """Подсчитывает число событий за год"""

    def get_stat_list(self):
        log_sum = []
        for day in self.get_log_dict():
            if log_sum:
                for i, day2 in enumerate(log_sum):
                    if day['day'][1:5] == day2['day'][1:5]:
                        day2['count'] += 1
                    else:
                        if i == (len(log_sum) - 1):
                            log_sum.append(day)
            else:
                day['count'] = 1
                log_sum.append(day)

        return log_sum

    def write_out(self):
        with open(self.file_out, 'w') as file_out:
            for x in self.get_stat_list():
                file_out.write(f'{x["day"][0:5]}] {x["count"]}\n')


parser = LogParserByHours(FILE_IN, FILE_OUT)
parser.write_out()
parser = LogParserByMonth(FILE_IN, FILE_OUT)
parser.write_out()
parser = LogParserByYear(FILE_IN, FILE_OUT)
parser.write_out()

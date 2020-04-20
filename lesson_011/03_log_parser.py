# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
import os

PATH = os.path.normpath('events.txt')


def pars_gen(mode):
    """Статистика по минутам параметр - "minute", по часам - "hour",
     по дням - "day", по месяцам - "month", по годам - "year" """

    mode_dict = {
        'minute': [1, 17],
        'hour': [1, 14],
        'day': [1, 10],
        'month': [1, 8],
        'year': [1, 5]
    }

    start_n = mode_dict[mode][0]
    end_n = mode_dict[mode][1]

    data = None
    count = 1
    with open(file=PATH, mode='r') as file:
        for line in file:
            if line.split(' ')[2].replace('\n', '') == 'NOK':
                if data:
                    if line[start_n:end_n] == data:
                        count += 1
                    else:
                        yield data, count
                        data = line[start_n:end_n]
                        count = 1
                else:
                    data = line[start_n:end_n]
        yield data, count


grouped_events = pars_gen(mode='minute')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

# зачет!

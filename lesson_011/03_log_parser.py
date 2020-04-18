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


def pars_gen():
    my_log_list = []
    my_log_dict = []
    with open(file=PATH, mode='r') as file:
        for line in file:
            if line.split(' ')[2].replace('\n', '') == 'NOK':
                my_log_list.append(line.replace('\n', ''))
    for day in my_log_list:
        my_dict = {
            'day': day,
            'count': 0
        }
        my_log_dict.append(my_dict)

    log_sum = []
    for day in my_log_dict:
        if log_sum:
            for i, day2 in enumerate(log_sum):
                # TODO Нужно предусмотреть настройку для задания разных
                #  интервалов группировки событий: минута, час, ...
                if day['day'][1:17] == day2['day'][1:17]:
                    day2['count'] += 1
                else:
                    if i == (len(log_sum) - 1):
                        log_sum.append(day)
        else:
            day['count'] = 1
            log_sum.append(day)

    for x in log_sum:
        yield x.values()

# TODO События в файле отсортированы по возрастанию даты и времени.
#  Поэтому нет необходимости предварительно обработать данные, и только после этого
#  возвращать. Такой подход не оптимален из-за необходимости хранить все данные.
#  Нужно переделать код таким образом, чтобы возвращать (yield) результат сразу после
#  его получения. Т. е. хранить нужно только строку с текущим периодом времени.
#  При обработке строки проверять что период совпадает и тогда нужно только увеличить
#  счётчик. Если не совпадает, то возвращаете период и накопленное количество событий.
#  И заменяете старый период на новый. После завершения цикла по строкам файлов
#  Заключительным yield возвращаете последний накопленный результат.


grouped_events = pars_gen()
for group_time, event_count in grouped_events:
    print(f'[{group_time[1:17]}] {event_count}')

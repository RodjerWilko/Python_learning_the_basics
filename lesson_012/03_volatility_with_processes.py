# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#

import multiprocessing
import operator
import os
import sys
import time

PATH = os.path.normpath('trades')
files = []


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


class Volatility(multiprocessing.Process):

    def __init__(self, path, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.ticks_volat = {}
        self.max_vol = 0
        self.min_vol = sys.maxsize
        self.name = ''
        self.collector = collector

    def run(self):
        with open(file=self.path, mode='r')as ff:
            self.name = self.path.split('_')[1][0:4]
            ff.readline()
            for line in ff:
                content = line.split(',')
                if float(content[2]) > self.max_vol:
                    self.max_vol = float(content[2])
                if float(content[2]) < self.min_vol:
                    self.min_vol = float(content[2])
        self.collector.put(self.volat())

    def volat(self):
        dict_volat = {}
        average_price = (self.max_vol + self.min_vol) / 2
        volatility = (self.max_vol - self.min_vol) / average_price * 100
        dict_volat['name'] = self.name
        dict_volat['volatility'] = volatility
        return dict_volat


@time_track
def main():
    collector = multiprocessing.Queue()
    tickers = {}
    tickers_null = []
    for dirpath, dirnames, filenames in os.walk(PATH):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            files.append(full_path)

    vols = [Volatility(path=file, collector=collector) for file in files]
    for vol in vols:
        vol.start()

    for vol in vols:
        vol.join()

    while not collector.empty():
        data = collector.get()
        if data.ticks_volat['volatility'] == 0.0:
            tickers_null.append('тикер ' + data.ticks_volat['name'])
        else:
            tickers[data.ticks_volat['name']] = data.ticks_volat['volatility']

    tickers = sorted(tickers.items(), key=operator.itemgetter(1))

    tickers_null = sorted(tickers_null)

    print('            максимальная волатильность:')
    for tick in tickers[:-4:-1]:
        print(f'тикер {tick[0]} - {tick[1]:.2f} %')
    print('            миниимальная волатильность:')
    for tick in tickers[:3]:
        print(f'тикер {tick[0]} - {tick[1]:.2f} %')
    print('            нулевая волатильность:')
    print(', '.join(tickers_null))


if __name__ == '__main__':
    main()

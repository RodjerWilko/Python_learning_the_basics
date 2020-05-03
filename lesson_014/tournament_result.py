from bowling import Bowling


class TourResWriter:

    def __init__(self, file_in, file_out='tournament_result.txt'):
        self.file_in = file_in
        self.file_out = file_out
        self.tour_stat = {}

    def tour_result(self):
        """Выводит результат в файл tournament_result.txt"""
        winner = {"name": '', "score": 0}

        with open(file=self.file_in, mode='r', encoding='utf8') as file_in:
            with open(file=self.file_out, mode='w', encoding='utf8') as file_out:
                for line in file_in:
                    line_rep = line.replace('\t', ' ')
                    line_pars = line_rep.split(' ')

                    if line_pars[0] == '###':  # Если начало тура
                        file_out.write(f'{line}')
                        winner['name'] = ''
                        winner['score'] = 0  # Обнуляет победителя тура, при начале нового

                    elif line_pars[0] == 'winner':  # Если конец тура
                        self.tour_stat[winner['name']]['winners'] += 1
                        file_out.write(f"winner is {winner['name']}")

                    elif line == '\n':  # Если пустая строка
                        continue

                    else:  # Если результа участника
                        for x in line_pars[::-1]:
                            if x == '':
                                line_pars.remove(x)

                        name = line_pars[0]
                        result = line_pars[1]
                        b = Bowling(result.replace('\n', ''))
                        score = b.get_score()

                        if score > winner['score']:
                            winner['name'] = name
                            winner['score'] = score

                        line = line_rep.replace('\n', '')
                        file_out.write(f'{line.ljust(32, " ")}{score}\n')

                        if name in self.tour_stat:
                            self.tour_stat[name]['games'] += 1
                        else:
                            self.tour_stat[name] = {'games': 1, 'winners': 0}

        self.print_term()

    def print_term(self):
        self.tour_stat = sorted(self.tour_stat.items(), key=lambda item: item[1]['winners'], reverse=True)

        print('+----------+------------------+--------------+')
        print('|{player:^10}|{play_g:^18}|{win_g:^14}|'.format(player='Игрок', play_g='сыграно матчей',
                                                               win_g='всего побед'))
        print('+----------+------------------+--------------+')

        for player in self.tour_stat:
            print(f'|{player[0]:^10}|{player[1]["games"]:^18}|{player[1]["winners"]:^14}|')
        print('+----------+------------------+--------------+')

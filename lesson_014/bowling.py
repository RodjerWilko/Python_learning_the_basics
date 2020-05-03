class Bowling:

    def __init__(self, game_result):
        """Если rules равно True, то подсчитывается по новым правилам, если False то по старым"""
        self.game_result = game_result
        self.dict = {
            'X': self.strike,
            '/': self.spare,
            '-': self.zero,
        }
        self.throw_num = 1
        self.total_score = 0
        self.frames = 0

    def strike(self, i):
        """X"""

        if self.throw_num == 1:
            return 20
        else:
            raise Exception('Страйк может быть только первым броском')

    def spare(self, i):
        """/"""

        if self.throw_num == 2:
            self.throw_num = 1
            return 15
        else:
            raise Exception('Спэир может быть только вторым броском')

    def zero(self, i=0):
        """-"""

        if self.throw_num == 1:
            self.throw_num = 2
            return 0
        else:
            self.throw_num = 1
            return 0

    def point(self, i):
        """digit"""

        if self.throw_num == 1:
            if i != (len(self.game_result) - 1):
                if self.game_result[i + 1] == '/':
                    self.throw_num = 2
                    return 0
                elif self.game_result[i + 1] == '-':
                    self.throw_num = 2
                    return self.game_result[i]
                elif self.game_result[i + 1].isdigit:
                    if (int(self.game_result[i]) + int(self.game_result[i + 1])) >= 10:
                        raise Exception('Больше 10 в одном фрейме или не указан Spare')
                    else:
                        self.throw_num = 2
                        return self.game_result[i]

            else:
                raise Exception('Некорректное число бросков')

        elif self.throw_num == 2 and i == (len(self.game_result) - 1):
            return self.game_result[i]
        else:
            self.throw_num = 1
            return self.game_result[i]

    def get_score(self):
        for i, char in enumerate(self.game_result):
            if self.throw_num == 1:
                self.frames += 1
            if char.isdigit():
                self.total_score += int(self.point(i))
            elif char in self.dict:
                self.total_score += self.dict[char](i)
            else:
                raise Exception('Некорректный символ')

        if self.frames < 10:
            raise Exception('Сыграно меньше 10 фреймов')
        else:
            return self.total_score


class NewRulesBowling(Bowling):

    def strike(self, i):
        """X"""

        if self.throw_num == 1:
            if i == (len(self.game_result) - 2):
                return 20
            elif i == (len(self.game_result) - 1):
                return 10
            else:
                return 10 + self.get_score_one_throw(self.game_result[i + 1], i + 1) \
                       + self.get_score_one_throw(self.game_result[i + 2], i + 2)
        else:
            raise Exception('Страйк может быть только первым броском')

    def spare(self, i):
        """/"""

        if self.throw_num == 2:
            self.throw_num = 1
            if i == (len(self.game_result) - 1):
                return 10
            else:
                if self.game_result[i + 1].isdigit():
                    return 10 + int(self.game_result[i + 1])
                elif self.game_result[i + 1] == 'X':
                    return 20
                else:
                    return 10
        else:
            raise Exception('Спэир может быть только вторым броском')

    def get_score_one_throw(self, char, i):
        if char.isdigit():
            return int(char)
        elif char == '/':
            if self.game_result[i - 1] == '-':
                return 10
            else:
                return 10 - int(self.game_result[i - 1])
        elif char == 'X':
            return 10
        elif char == '-':
            return 0
        else:
            raise Exception('Некорректный символ')

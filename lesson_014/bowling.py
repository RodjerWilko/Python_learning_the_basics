def get_score(game_result):
    list_result = list(game_result)
    total_score = 0

    for i, char in enumerate(list_result):
        if char == 'X':
            total_score += 20
        elif char == '-':
            if list_result[i + 1].isdigit():
                total_score += int(list_result[i + 1])
                del list_result[i + 1]
            elif list_result[i + 1] == '-':
                total_score += 0
                del list_result[i + 1]
            else:
                total_score += 15
                del list_result[i + 1]
        elif char.isdigit():
            if list_result[i + 1].isdigit():
                total_score += int(char) + int(list_result[i + 1])
                del list_result[i + 1]
            elif list_result[i + 1] == '/':
                total_score += 15
                del list_result[i + 1]
            elif list_result[i + 1] == '-':
                total_score += int(char)
                del list_result[i + 1]
        else:
            raise ValueError('Неверный тип данных')
    return total_score

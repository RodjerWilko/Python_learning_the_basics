from random import randint

numbers = []
counter_step = 0

# TODO Не самый оптимальный способ генерации числа.
#  В библиотеке random есть более подходящие функции.
#  Например shuffle или sample. С sample можно получить
#  сразу всю случайную последовательность одной командой.
#  Если хотите избегать 0 на первой позиции,
#  то генерировать последовательлность можно в цикле,
#  пока не получится последовательность начинающуася не с 0.
#  Или можно вместо последовательности в 4 символа сгенерировать 5
#  И если на первой позиции 0 сделать срез списка [1:], если не 0 [:4]
#  Функция shuffle позволяет перемешать элементы списка,
#  который можно сделать как list(range(10)). Останется только проверить
#  0 элемент и использовать срез.
def make_number():
    """Заполнить список числами, обнулить счетчики"""
    global numbers
    global counter_step
    numbers = []
    counter_step = 0
    while len(numbers) <= 3:
        number = randint(0, 9)
        if len(numbers) == 0 and number == 0:
            continue
        else:
            if number not in numbers:
                numbers.append(number)


def check_number(user_input):
    """Проверить совпадения списка чисел с вводом пользователя"""
    result_dict = {'bulls': 0, 'cows': 0}
    global counter_step
    list_user_input = []
    for num_user in user_input:
        b = int(num_user)
        list_user_input.append(b)
    for num in numbers:
        # TODO Лучше поменять условия. Сначала найти быка на i-й позиции,
        #  а затем оператором in проверить является ли число коровой.
        if num in list_user_input:
            if numbers.index(num) == list_user_input.index(num):
                result_dict['bulls'] += 1
            else:
                result_dict['cows'] += 1
    counter_step += 1

    return result_dict

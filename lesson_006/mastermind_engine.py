from random import sample

numbers = []
counter_step = 0


def make_number():
    """Заполнить список числами, обнулить счетчики"""
    global numbers
    global counter_step
    numbers = []
    counter_step = 0
    numbers = sample(list(range(10)), 5)
    if numbers[0] == 0:
        numbers = numbers[1:]
    else:
        numbers = numbers[:4]


def check_number(user_input):
    """Проверить совпадения списка чисел с вводом пользователя"""
    result_dict = {'bulls': 0, 'cows': 0}
    global counter_step
    list_user_input = []
    for num_user in user_input:
        b = int(num_user)
        list_user_input.append(b)
    for num_user in list_user_input:
        if num_user == numbers[list_user_input.index(num_user)]:
            result_dict['bulls'] += 1
        # TODO Объедините else и if в один elif.
        else:
            if num_user in numbers:
                result_dict['cows'] += 1
    counter_step += 1

    return result_dict

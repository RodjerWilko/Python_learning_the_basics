from random import randint

numbers = []
counter_step = 0


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
        if num in list_user_input:
            if numbers.index(num) == list_user_input.index(num):
                result_dict['bulls'] += 1
            else:
                result_dict['cows'] += 1
    counter_step += 1

    return result_dict

# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if 0 < int(user_input) <= 12:
    if int(user_input) == 2:
        print('28 дней')
    elif int(user_input) < 8:
        if int(user_input) % 2 == 1:
            print('31 день')
        else:
            print('30 дней')
    else:
        if int(user_input) % 2 == 1:
            print('30 дней')
        else:
            print('31 день')
else:
    print("неверный номер месяца.")

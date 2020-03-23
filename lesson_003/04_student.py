# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

months = 10
total_grant = educational_grant
total_expenses = expenses
while months > 1:
    expenses += expenses*0.03
    total_expenses += expenses
    total_grant += educational_grant
    months -= 1
need_money = total_expenses - total_grant

print('Студенту надо попросить', round(need_money, 2), 'рублей')

# зачет!

# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import argparse
import os

from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date, out_path='ticket.png'):
    font = os.path.join('font', 'RESurFoxes.ttf')
    img = Image.open(os.path.join('images', 'ticket_template.png'))
    fio_coord = (47, 126)
    from_coord = (47, 194)
    to_coord = (47, 261)
    date_coord = (285, 261)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, size=20)

    draw.text(fio_coord, fio, font=font, fill=ImageColor.colormap['black'])
    draw.text(from_coord, from_, font=font, fill=ImageColor.colormap['black'])
    draw.text(to_coord, to, font=font, fill=ImageColor.colormap['black'])
    draw.text(date_coord, date, font=font, fill=ImageColor.colormap['black'])

    img.save(out_path)
    img.show()


# make_ticket('Иванов И.И.', 'ЧЕБОКСАРЫ', 'МОСКВА', '31.12')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


parser = argparse.ArgumentParser(description='Fill a ticket')
parser.add_argument('--fio', action="store", type=str, dest="fio")
parser.add_argument('--from', action="store", type=str, dest="from_")
parser.add_argument('--to', action="store", type=str, dest="to")
parser.add_argument('--date', action="store", type=str, dest="date")
parser.add_argument('--save_to', action="store", type=str, default='ticket.png', dest="save_to")
args = parser.parse_args()
make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, out_path=args.save_to)

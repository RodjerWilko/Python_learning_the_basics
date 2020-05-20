import os
from io import BytesIO

from PIL import Image, ImageColor, ImageDraw, ImageFont
import requests

TEMPLATE_PATH = os.path.join('files', 'ticket_template.png')
FONT_PATH = os.path.join('files', 'RESurFoxes.ttf')
FONT_SIZE = 20
NAME_OFFSET = (47, 126)
CITY_OUT_OFFSET = (47, 194)
CITY_IN_OFFSET = (47, 261)
DATE_OFFSET = (285, 261)
AVATAR_SIZE = 100
AVATAR_OFFSET = (290, 75)


def generate_ticket(name, city_out, city_in, date_flight, email):
    font = FONT_PATH
    img = Image.open(TEMPLATE_PATH)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, size=FONT_SIZE)

    draw.text(NAME_OFFSET, name, font=font, fill=ImageColor.colormap['black'])
    draw.text(CITY_OUT_OFFSET, city_out, font=font, fill=ImageColor.colormap['black'])
    draw.text(CITY_IN_OFFSET, city_in, font=font, fill=ImageColor.colormap['black'])
    draw.text(DATE_OFFSET, date_flight, font=font, fill=ImageColor.colormap['black'])

    response = requests.get(url=f'https://api.adorable.io/avatars/{AVATAR_SIZE}/{email}')
    avatar_file_like = BytesIO(response.content)
    avatar = Image.open(avatar_file_like)

    img.paste(avatar, AVATAR_OFFSET)

    temp_file = BytesIO()
    img.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file

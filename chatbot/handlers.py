import re
import vk_api.utils

import settings

re_name = re.compile(r'^[\w\-\s]{3,40}$')
re_email = re.compile(r'(|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|)')
re_phone = re.compile(r'\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b')
re_date = re.compile(r'\d{2}-\d{2}-\d{4}')


def handle_name(text, context):
    match = re.match(re_name, text)
    if match:
        context['name'] = text
        return True
    else:
        return False


def handle_city_out(text, context):
    if text in settings.FLIGHT_SCHEDULE:
        context['city_out'] = text
        return True
    else:
        return False


def handle_city_in(text, context):
    if text in settings.FLIGHT_SCHEDULE[context['city_out']]:
        context['city_in'] = text
        return True
    else:
        return False


def handle_phone_number(text, context):
    match = re.findall(re_phone, text)
    if match:
        context['phone'] = text
        return True
    else:
        return False


def handle_email(text, context):
    match = re.findall(re_email, text)
    if match:
        context['email'] = text
        return True
    else:
        return False


def handle_date(text, context):
    match = re.match(re_date, text)
    if match:
        context['date'] = text
        return True
    else:
        return False


def handle_flights(text, context):
    for flight in context['num_of_flights']:
        if flight[0] == text:
            context['num_flight'] = text
            context['date_flight'] = flight[1]
            context['time_flight'] = flight[2]
            return True
    return False


def handle_sits(text, context):
    if 0 < int(text) < 6:
        context['sits'] = text
        return True
    else:
        return False


def handle_comment(text, context):
    context['comment'] = text
    return True


def handle_correct_data(text, context):
    if text == 'да':
        return True
    elif text == 'нет':
        return False
    else:
        return

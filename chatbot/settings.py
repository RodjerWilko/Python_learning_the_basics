GROUP_ID = 194634835
TOKEN = '93e01439e949317333e343425db0a3138dcd02b5f46bfcc45369df306892096b5e84a09ababb0bb49760b'

INTENTS = [
    {"name": "Помощь",
     "tokens": ("/help",),
     "scenario": None,
     "answer": "Это чат-бот предназначенный для заказа билета на самолет,"
               " чтобы заказать билет включите помощника командой - /ticket, чтобы в процессе заказа начать заново -"
               "наберите также - /ticket"
     },
]

SCENARIO = {
    "ticket": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "\nВы запустили помощника для заказа билета на самолет \nВведите Ваше имя: ",
                "failure_text": "Введите корректное имя ",
                "fail_action": None,
                "handler": "handle_name",
                "next_step": "step2"
            },

            "step2": {
                "text": "\nВведите Ваш e-mail, мы отправим на него все данные: ",
                "failure_text": "Введите корректный e-mail ",
                "fail_action": None,
                "handler": "handle_email",
                "next_step": "step3"
            },

            "step3": {
                "text": "\nВведите город отправения: ",
                "failure_text": "Выберите из списка доступных городов: ",
                "fail_action": 'fail_city_out_action',
                "handler": "handle_city_out",
                "next_step": "step4"
            },
            "step4": {
                "text": "Введите город назначения:",
                "failure_text": "Выберите из списка доступных городов: ",
                "fail_action": 'fail_city_in_action',
                "action": "check_flights_action",
                "handler": "handle_city_in",
                "next_step": "step5"
            },
            "step5": {
                "text": "Введите дату вылета в формате дд-мм-гггг: ",
                "failure_text": "Введена неверная дата",
                "handler": "handle_date",
                "next_step": "step6"
            },
            "step6": {
                "text": 'Из города {city_out} в город {city_in} есть рейсы:',
                "action": 'list_flights',
                "failure_text": "Такого рейса нет",
                "handler": "handle_flights",
                "next_step": "step7"
            },

            "step7": {
                "text": "Выберите количество мест от 1 до 5:  ",
                "failure_text": "Введено неверное количество мест",
                "handler": "handle_sits",
                "next_step": "step8"
            },

            "step8": {
                "text": "Введите комментарий для заказа: ",
                "failure_text": "Введен неверный город",
                "handler": "handle_comment",
                "next_step": "step9"
            },
            "step9": {
                "text": "Проверьте правильность введенных Вами данных (Если все верно напишите ДА, иначе НЕТ): ",
                "failure_text": "Введите ДА или НЕТ",
                "action": 'correct_check',
                "fail_action": "not_yes",
                "handler": "handle_correct_data",
                "next_step": "step10"
            },
            "step10": {
                "text": "Укажите свой номер телефона: ",
                "action": 'send_image',
                "failure_text": "Введен неверный номер телефона",
                "handler": "handle_phone_number",
                "next_step": "step11"
            },
            "step11": {
                "text": "Спасибо за заказ, мы отправим данные Вам на email: {email}.",
                "failure_text": None,
                "handler": None,
                "next_step": None
            }
        }
    }
}

DEFAULT_ANSWER = 'Наберите команду - /help для помощи'

list_city = ['москва', 'париж', 'санкт-петербург', 'нью-йорк']

DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='123456',
    host='127.0.0.1',
    database='chatbot'
)

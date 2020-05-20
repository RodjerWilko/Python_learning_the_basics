from pony.orm import db_session
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import requests
import vk_api.utils
import logging
import handlers
from generate_flights import generate_flights
from models import UserState, Registration
from generate_ticket import generate_ticket

try:
    import settings
except ImportError:
    exit('Do cp settings.py.default settings.py and set token')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(
        '%(asctime)s -%(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
    file_handler = logging.FileHandler('bot.log', mode='a', encoding='utf8')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
    log.addHandler(stream_handler)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)
    stream_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot для Vk.com
    Use python 3.8
    """

    def __init__(self, _group_id, _token):
        """

        :param _group_id: group id из группы в vk
        :param _token: секретный токен
        """
        self.group_id = _group_id
        self.token = _token
        self.vk = vk_api.VkApi(token=_token)
        self.long_poll = VkBotLongPoll(self.vk, _group_id)
        self.api = self.vk.get_api()
        self.FLIGHT_SCHEDULE = generate_flights()

    def run(self):
        """Запуск бота"""
        for event in self.long_poll.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события')

    @db_session
    def on_event(self, event):
        """
        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.debug('Мы такое пока не обрабатываем %s', event.type)
            return
        user_id = event.object['message']['peer_id']
        text = event.obj['message']['text'].lower()
        state = UserState.get(user_id=str(user_id))

        if text == '/ticket':
            if state:
                state.delete()
                self.send_text(self.start_scenario(scenario_name='ticket', user_id=user_id), user_id)
            else:
                self.send_text(self.start_scenario(scenario_name='ticket', user_id=user_id), user_id)
        elif text == '/help':
            self.send_text(settings.INTENTS[0]['answer'], user_id)
        elif text == 'нет' and state.step_name == 'step9':
            state.delete()
            self.send_text(self.start_scenario(scenario_name='ticket', user_id=user_id), user_id)
        else:
            if state is not None:
                self.send_text(self.continue_scenario(user_id, text, state), user_id)
            else:
                self.send_text(settings.DEFAULT_ANSWER, user_id)

        if state is not None:
            steps = settings.SCENARIO[state.scenario_name]['steps']
            step = steps[state.step_name]
            if 'action' in step:
                if step['action'] == 'list_flights':
                    self.dispatcher(user_id, state)
                elif step['action'] == 'correct_check':
                    self.correct_check(user_id, state)

    def send_text(self, text_to_send, user_id):
        self.api.messages.send(
            message=text_to_send,
            random_id=vk_api.utils.get_random_id(),
            peer_id=user_id
        )

    def send_image(self, state, user_id):
        image = generate_ticket(
            name=state.context['name'],
            city_out=state.context['city_out'],
            city_in=state.context['city_in'],
            date_flight=state.context['date_flight'],
            email=state.context['email']
        )
        upload_url = self.api.photos.getMessagesUploadServer()['upload_url']
        upload_data = requests.post(url=upload_url, files={'photo': ('image.png', image, 'image/png')}).json()
        image_data = self.api.photos.saveMessagesPhoto(**upload_data)

        owner_id = image_data[0]['owner_id']
        media_id = image_data[0]['id']
        attachment = f'photo{owner_id}_{media_id}'

        self.api.messages.send(
            attachment=attachment,
            random_id=vk_api.utils.get_random_id(),
            peer_id=user_id
        )

    def correct_check(self, user_id, state):  # формирует и выводит на экран введеные данные для проверки
        text = f'\nгород отправления: \n{state.context["city_out"].capitalize()}\n ' \
               f'\nгород назначения: \n{state.context["city_in"].capitalize()}\n' \
               f'\nдата отправления: \n{state.context["date_flight"]}\n' \
               f'\nномер рейса: \n№{state.context["num_flight"]}\n' \
               f'\nвремя отправления: \n{state.context["time_flight"]}\n' \
               f'\nколичество мест: \n{state.context["sits"]}\n' \
               f'\nваш комментарий:\n{state.context["comment"]}\n'
        self.send_text(text, user_id)

    def fail_city_out_action(self, user_id):  # вывод на экран возможных городов отправления
        text = ''
        for city in self.FLIGHT_SCHEDULE:
            text += '\n' + city.capitalize()
        self.send_text(text, user_id)

    def fail_city_in_action(self, user_id, state):  # вывод на экран возможных городов прибытия
        text = ''
        for city in self.FLIGHT_SCHEDULE[state.context['city_out']]:
            text += '\n' + city.capitalize()
        self.send_text(text, user_id)

    def check_flights_action(self, user_id, state):  # проверка есть ли между городами рейсы, если нет то выдает текст
        print(state.context)
        if not self.FLIGHT_SCHEDULE[state.context['city_out']][state.context['city_in']]:
            text = 'Между данными городами нет рейсов, попробуйте заново'
            self.send_text(text, user_id)
            print(type(state.context['email']))
            Registration(
                name=state.context['name'],
                email=state.context['email'],
                date_flight=state.context['date_flight'],
                time_flight=state.context['time_flight'],
                city_out=state.context['city_out'],
                city_in=state.context['city_in'],
                sits=state.context['sits'],
                comment=state.context['comment'],
                phone=state.context['phone']
            )

            state.delete()
            self.start_scenario(scenario_name='ticket', user_id=user_id)

    def dispatcher(self, user_id, state):
        """создает и выводит список доступных полетов в зависимости от выбора пользователя """
        count = 0
        user_date = state.context['date']
        list_flights = ''
        state.context['num_of_flights'] = []
        for num, date, time in self.FLIGHT_SCHEDULE[state.context['city_out']][state.context['city_in']]:
            if date >= user_date and count != 5:
                list_flights += f'\n№ рейса: {num}\nдата отправления: {date} \nвремя отправления: {time}\n'
                state.context['num_of_flights'].append([num, date, time])
                count += 1
        list_flights += '\nВыберите номер рейса из списка: '
        self.send_text(list_flights, user_id)

    def start_scenario(self, scenario_name, user_id):
        """начинает сценарий """
        scenario = settings.SCENARIO[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        UserState(scenario_name=scenario_name, step_name=first_step, context={}, user_id=str(user_id))
        return text_to_send

    def continue_scenario(self, user_id, text, state):
        """продолжает сценарий"""
        steps = settings.SCENARIO[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context, flight_schedule=self.FLIGHT_SCHEDULE):  # если хэндлер выернул True
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
            else:
                print(state)
                print(state.context['email'])
                print(type(state.context['email']))
                Registration(
                    name=state.context['name'],
                    email=state.context['email'],
                    date_flight=state.context['date_flight'],
                    time_flight=state.context['time_flight'],
                    city_out=state.context['city_out'],
                    city_in=state.context['city_in'],
                    sits=state.context['sits'],
                    comment=state.context['comment'],
                    phone=state.context['phone']
                )

                state.delete()
            if 'action' in step:  # если в описании шага есть 'action'
                if step['action'] == 'check_flights_action':
                    if not self.FLIGHT_SCHEDULE[state.context['city_out']][state.context['city_in']]:
                        self.check_flights_action(user_id, state)
                        text_to_send = 'Введите город отправения: '
                elif step['action'] == 'send_image':
                    self.send_image(state, user_id)

        else:  # если хэндлер вернул False
            text_to_send = step['failure_text'].format(**state.context)
            if 'fail_action' in step:
                if step['fail_action'] == 'fail_city_out_action':
                    self.fail_city_out_action(user_id)
                elif step['fail_action'] == 'fail_city_in_action':
                    self.fail_city_in_action(user_id, state)
        return text_to_send


if __name__ == '__main__':
    log = logging.getLogger('bot')
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import vk_api.utils
import logging
import handlers

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


class UserState:
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


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
        self.user_states = dict()

    def run(self):
        """Запуск бота"""
        for event in self.long_poll.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события')

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

        if text == '/ticket':
            text_to_send = self.start_scenario(scenario_name='ticket', user_id=user_id)
        elif text == '/help':
            text_to_send = settings.INTENTS[0]['answer']
        elif text == 'нет' and self.user_states[user_id].step_name == 'step7':
            text_to_send = self.start_scenario(scenario_name='ticket', user_id=user_id)
        else:
            if user_id in self.user_states:
                text_to_send = self.continue_scenario(user_id, text)
            else:
                text_to_send = settings.DEFAULT_ANSWER
        self.api.messages.send(
            message=text_to_send,
            random_id=vk_api.utils.get_random_id(),
            peer_id=user_id
        )

        if user_id in self.user_states:
            state = self.user_states[user_id]
            steps = settings.SCENARIO[state.scenario_name]['steps']
            step = steps[state.step_name]
            if 'action' in step:
                if step['action'] == 'list_flights':
                    self.dispatcher(user_id, state)
                elif step['action'] == 'correct_check':
                    self.correct_check(user_id, state)

    def correct_check(self, user_id, state):  # формирует и выводит на экран введеные данные для проверки
        text = f'\nгород отправления: \n{state.context["city_out"].capitalize()}\n ' \
               f'\nгород назначения: \n{state.context["city_in"].capitalize()}\n' \
               f'\nдата отправления: \n{state.context["date_flight"]}\n' \
               f'\nномер рейса: \n№{state.context["num_flight"]}\n' \
               f'\nвремя отправления: \n{state.context["time_flight"]}\n' \
               f'\nколичество мест: \n{state.context["sits"]}\n' \
               f'\nваш комментарий:\n{state.context["comment"]}\n'
        self.api.messages.send(
            message=text,
            random_id=vk_api.utils.get_random_id(),
            peer_id=user_id
        )

    def fail_city_out_action(self, user_id):  # вывод на экран возможных городов отправления
        text = ''
        for city in settings.FLIGHT_SCHEDULE:
            text += '\n' + city.capitalize()
        self.api.messages.send(
            message=text,
            random_id=vk_api.utils.get_random_id(),
            peer_id=user_id
        )

    def fail_city_in_action(self, user_id, state):  # вывод на экран возможных городов прибытия
        text = ''
        for city in settings.FLIGHT_SCHEDULE[state.context['city_out']]:
            text += '\n' + city.capitalize()
        self.api.messages.send(
            message=text,
            random_id=vk_api.utils.get_random_id(),
            peer_id=user_id
        )

    def check_flights_action(self, user_id, state):  # проверка есть ли между городами рейсы, если нет то выдает текст
        print(state.context)
        if not settings.FLIGHT_SCHEDULE[state.context['city_out']][state.context['city_in']]:
            text = 'Между данными городами нет рейсов, попробуйте заново'
            self.api.messages.send(
                message=text,
                random_id=vk_api.utils.get_random_id(),
                peer_id=user_id
            )
            self.user_states.pop(user_id)
            self.start_scenario(scenario_name='ticket', user_id=user_id)

    def dispatcher(self, user_id, state):
        """создает и выводит список доступных полетов в зависимости от выбора пользователя """
        count = 0
        user_date = state.context['date']
        list_flights = ''
        state.context['num_of_flights'] = []
        for num, date, time in settings.FLIGHT_SCHEDULE[state.context['city_out']][state.context['city_in']]:
            if date >= user_date and count != 5:
                list_flights += f'\n№ рейса: {num}\nдата отправления: {date} \nвремя отправления: {time}\n'
                state.context['num_of_flights'].append([num, date, time])
                count += 1
        list_flights += '\nВыберите номер рейса из списка: '
        self.api.messages.send(
            message=list_flights,
            random_id=vk_api.utils.get_random_id(),
            peer_id=user_id
        )

    def start_scenario(self, scenario_name, user_id):
        """начинает сценарий """
        scenario = settings.SCENARIO[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        """продолжает сценарий"""
        state = self.user_states[user_id]
        steps = settings.SCENARIO[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):  # если хэндлер выернул True
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
            else:
                print(state.context)
                self.user_states.pop(user_id)
            if 'action' in step:  # если в описании шага есть 'action'
                if step['action'] == 'check_flights_action':
                    if not settings.FLIGHT_SCHEDULE[state.context['city_out']][state.context['city_in']]:
                        self.check_flights_action(user_id, state)
                        text_to_send = 'Введите город отправения: '

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

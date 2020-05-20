from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY
from pony.orm import db_session, rollback
from vk_api.bot_longpoll import VkBotMessageEvent

from bot import Bot
from generate_ticket import generate_ticket


def isolate_db(test_func):
    def wrapper(*args, **kwargs):
        with db_session:
            test_func(*args, **kwargs)
            rollback()

    return wrapper


class Test1(TestCase):
    RAW_EVENT = {'type': 'message_new',
                 'object': {
                     'message': {
                         'date': 1587984421,
                         'from_id': 594253363,
                         'id': 70,
                         'out': 0,
                         'peer_id': 594253362,
                         'text': 'ac',
                         'conversation_message_id': 70,
                         'fwd_messages': [],
                         'important': False,
                         'random_id': 0,
                         'attachments': [],
                         'is_hidden': False
                     },
                     'client_info': {
                         'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
                         'keyboard': True,
                         'inline_keyboard': True,
                         'lang_id': 0
                     }
                 },
                 'group_id': 194634835,
                 'event_id': 'b2de1165685155db8ebbb06f1ec68260e005acbd'}

    CONTEXT = {
        'city_out': 'москва',
        'city_in': 'санкт-петербург',
        'date': '10-04-2020',
        'num_of_flights': [['1', '10-05-2020', '14:00'], ['2', '11-05-2020', '14:00'], ['3', '12-05-2020', '14:00'],
                           ['4', '13-05-2020', '14:00'], ['5', '14-05-2020', '14:00']], 'num_flight': '5',
        'date_flight': '14-05-2020',
        'time_flight': '14:00',
        'sits': '4',
        'comment': '1',
        'phone': '89176561453'
    }

    @isolate_db
    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.asser_called()
                bot.on_event.asser_any_call(obj)
                assert bot.on_event.call_count == count

    def test_on_event(self):  # проверяем на стандартный ответ
        event = VkBotMessageEvent(self.RAW_EVENT)
        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=f"Наберите команду - /help для помощи",
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['message']['peer_id']
        )

    def test_on_event1(self):  # проверка на ответ после /ticket
        event = deepcopy(self.RAW_EVENT)
        event['object']['message']['text'] = '/ticket'
        event = VkBotMessageEvent(event)
        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=f"\nВы запустили помощника для заказа билета на самолет \nВведите Ваше имя: ",
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['message']['peer_id']
        )

    def test_on_event2(self):  # проверка на ответ после /help
        event = deepcopy(self.RAW_EVENT)
        event['object']['message']['text'] = '/help'
        event = VkBotMessageEvent(event)
        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot.on_event(event)

        send_mock.assert_called_once_with(
            message=f"Это чат-бот предназначенный для заказа билета на самолет, чтобы заказать "
                    f"билет включите помощника командой - /ticket, чтобы в процессе заказа начать"
                    f" заново -наберите также - /ticket",
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['message']['peer_id']
        )

    def test_correct_check(self):  # проверка правильности вывода введеных данных
        user_id = self.RAW_EVENT['object']['message']['peer_id']
        state = Mock()
        state.context = self.CONTEXT
        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot.correct_check(user_id, state)

        send_mock.assert_called_once_with(
            message='\nгород отправления: \nМосква\n \nгород назначения: \nСанкт-петербург\n\nдата отправления:'
                    ' \n14-05-2020\n\nномер рейса: \n№5\n\nвремя отправления: \n14:00\n\nколичество мест:'
                    ' \n4\n\nваш комментарий:\n1\n',
            random_id=ANY,
            peer_id=user_id
        )

    def test_fail_city_out_action(self):  # проверка списка доступных город для отправлений
        user_id = self.RAW_EVENT['object']['message']['peer_id']
        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot.fail_city_out_action(user_id)

        send_mock.assert_called_once_with(
            message='\nМосква\nСанкт-петербург\nНью-йорк\nПариж',
            random_id=ANY,
            peer_id=user_id
        )

    def test_dispatcher(self):
        user_id = self.RAW_EVENT['object']['message']['peer_id']
        state = Mock()
        state.context = self.CONTEXT
        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot.dispatcher(user_id, state)

        send_mock.assert_called_once_with(
            message='\n№ рейса: 1\nдата отправления: 10-05-2020 \nвремя отправления: 14:00'
                    '\n\n№ рейса: 2\nдата отправления: 11-05-2020 \nвремя отправления: 14:00'
                    '\n\n№ рейса: 3\nдата отправления: 12-05-2020 \nвремя отправления: 14:00'
                    '\n\n№ рейса: 4\nдата отправления: 13-05-2020 \nвремя отправления: 14:00'
                    '\n\n№ рейса: 5\nдата отправления: 14-05-2020 \nвремя отправления: 14:00'
                    '\n\nВыберите номер рейса из списка: ',
            random_id=ANY,
            peer_id=user_id
        )

    def test_image_generation(self):
        with open('files/123.png', 'rb') as avatar_photo:
            avatar_mock = Mock()
            avatar_mock.content = avatar_photo.read()

        with patch('requests.get', return_value=avatar_mock):
            ticket_file = generate_ticket(name='максим', city_out='москва', city_in='париж', date_flight='21-05-2020',
                                          email='123@123.ru')

        with open('files/temp.png', 'rb') as expected_file:
            expected_bytes = expected_file.read()

        assert ticket_file.read() == expected_bytes

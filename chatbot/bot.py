from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api.utils
import logging

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

    def run(self):
        """Запуск бота"""
        for event in self.long_poll.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события')

    def on_event(self, event):
        """
        Отправляет сообщение назад, если это текст
        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            # log.info('Отправляем сообщение назад')
            self.api.messages.send(
                message=f"Мы получили сообщение от Вас : {event.obj['message']['text']}",
                random_id=vk_api.utils.get_random_id(),
                peer_id=event.obj['message']['peer_id']
            )
        else:
            log.debug('Мы такое пока не обрабатываем %s', event.type)


if __name__ == '__main__':
    log = logging.getLogger('bot')
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()

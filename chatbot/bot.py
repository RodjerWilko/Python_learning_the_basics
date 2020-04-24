from random import randint

import vk_api
import vk_api.bot_longpoll

from tok import t

group_id = 194634835


class Bot:
    def __init__(self, _group_id, _token):
        self.group_id = _group_id
        self.token = _token
        self.vk = vk_api.VkApi(token=_token)
        self.long_poll = vk_api.bot_longpoll.VkBotLongPoll(self.vk, group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poll.listen():
            print('Получено событие')
            try:
                self.on_event(event)
            except Exception as exc:
                print(exc)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print(event.obj['message']['text'])
            self.api.messages.send(
                message=f"Мы получили сообщение от Вас : {event.obj['message']['text']}",
                random_id=randint(0, 2 ** 20),
                peer_id=event.obj['message']['peer_id']
            )
        else:
            print('Мы такое пока не обрабатываем', event.type)


if __name__ == '__main__':
    bot = Bot(group_id, t)
    bot.run()

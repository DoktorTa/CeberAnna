import enum

from aiogram import types


class User:
    id: int = 0
    chat_id: int = 0
    tag: str = 'default'
    full_name: str = 'default'
    status: str = ''
    inviter: str = 'default'
    lang: str = 'ru'

    all_status = {
        1: 'ADMIN',
        2: 'STORAGE',
        3: 'PAX',
        4: 'PRESS'
    }

    def __str__(self):
        return f'{self.id}\n' \
               f'{self.tag}\n' \
               f'{self.full_name}\n' \
               f'{self.all_status.get(int(self.status))}\n' \
               f'{self.inviter}\n'

    def init_bot(self, msg: types.Message):
        try:
            self.id = msg.from_user.id
            self.full_name = msg.from_user.full_name
            self.tag = '@' + msg.from_user.username
            self.chat_id = msg.chat.id
            self.lang = msg.from_user.language_code
            return self
        except Exception as e:
            return None

    def init_db_requests(self, db_line: dict):
        try:
            self.id = db_line.get('user_id')
            self.chat_id = db_line.get('chat_id')
            self.full_name = db_line.get('full_name')
            self.tag = db_line.get('user_tag')
            return self
        except Exception as e:
            return None

    def init_db_user(self, db_line: dict):
        try:
            self.id = db_line.get('user_id')
            self.tag = db_line.get('user_tag')
            self.chat_id = db_line.get('chat_id')
            self.full_name = db_line.get('user_name')
            self.status = db_line.get('user_status')
            self.inviter = db_line.get('user_inviter')
            return self
        except Exception as e:
            return None

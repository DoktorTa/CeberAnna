import tabulate

from command.msg.c_users_msg import *
from util.user import User
from util.storage_item import Item
from util import logger
from command_heandler.abstract_ch.abstract_ch_storage import AbsChStorage


class CommandStorage:
    commands = [
        (4, '/create_item'),
        (4, '/show_item'),
        (4, '/update_item')
    ]
    languages = {'ru': MSGCommandUsersRU(),
                 'en': MSGCommandUserEN()}
    logger_err = logger.logger_error
    logger_inf = logger.logger_info

    def __init__(self, ch_storage: AbsChStorage):
        self.ch_storage: AbsChStorage = ch_storage

    def command_create_item_state_0(self, user_req: User) -> str:
        try:
            if True:
                answer = self.languages.get(user_req.lang).create_item
                self.logger_inf.info(msg=f'create_item_stage_0 - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)
            return 'Error'

    def command_create_item_state_1(self, user_req: User, msg_text: str) -> str:
        try:
            if True:

                for str_item in msg_text.replace('\n', '').split(','):
                    try:
                        item = Item().init_str(str_item)
                        self.ch_storage.create_item(item)
                    except Exception as e:
                        self.logger_err.error(e)
                        continue

                answer = self.languages.get(user_req.lang).create_item_good

                self.logger_inf.info(msg=f'create_item_stage_1 - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)
            return 'Error'

    # TODO: Почисти всю эту копипасту к хуям собачим, это блять должно быть сделано уже в 1.1
    def get_all_name_groups(self) -> list:
        try:
            return self.ch_storage.get_all_name_groups()
        except Exception as e:
            self.logger_err.error(e)
            return ['Error']

    def get_all_name_subgroups(self, text_msg):
        try:
            return self.ch_storage.get_all_name_subgroups(text_msg)
        except Exception as e:
            self.logger_err.error(e)
            return ['Error']

    def command_show_item_state_0(self, user_req: User) -> str:
        try:
            if True:
                answer = self.languages.get(user_req.lang).show_item_stage_0
                self.logger_inf.info(msg=f'show_item_stage_0 - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)
            return 'Error'

    def command_show_item_state_1(self, user_req: User) -> str:
        try:
            if True:
                answer = self.languages.get(user_req.lang).show_item_stage_1
                self.logger_inf.info(msg=f'show_item_stage_1 - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)
            return 'Error'

    def command_show_item_state_2(self, user_req: User, msg_text: str) -> str:
        try:
            if True:
                all_requests = [['group', 'subgroup', 'id', 'count']]
                all_item = self.ch_storage.get_all_item_by_sub_group(msg_text)
                all_requests += [str(x).split('\n') for x in all_item]
                all_requests = tabulate.tabulate(all_requests)

                self.logger_inf.info(msg=f'show_item_stage_2 - {user_req.id} - {user_req.tag}')

                return f'`{all_requests}`'
        except Exception as e:
            self.logger_err.error(e)
            return 'Error'

    def command_update_item_state_0(self, user_req: User) -> str:
        try:
            if True:
                answer = self.languages.get(user_req.lang).update_item
                self.logger_inf.info(msg=f'update_item_stage_0 - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)
            return 'Error'

    def command_update_item_state_1(self, user_req: User, msg_text: str) -> str:
        try:
            if True:

                for str_item in msg_text.replace('\n', '').split(','):
                    try:
                        item = Item().init_str(str_item)
                        item_2 = self.ch_storage.get_item_by_subgroup_and_id(item)
                        item_2.count += item.count
                        if item_2.count <= 0:
                            self.ch_storage.delete_item(item_2)
                        else:
                            self.ch_storage.update_item(item_2)
                    except Exception as e:
                        print(e)
                        self.logger_err.error(e)
                        continue

                answer = self.languages.get(user_req.lang).update_item_good

                self.logger_inf.info(msg=f'create_item_stage_1 - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)
            return 'Error'

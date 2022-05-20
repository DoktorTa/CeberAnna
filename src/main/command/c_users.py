import tabulate
from command_heandler.abstract_ch.abstract_ch_requests import AbsChRequests
from command_heandler.abstract_ch.abstract_ch_users import AbsChUsers

from util import logger
from command.msg.c_users_msg import *


class CommandUsers:
    languages = {'RU': MSGCommandUsersRU()}
    logger_err = logger.logger_error
    logger_inf = logger.logger_info
    register_open: bool = True

    def __init__(self, abs_ch_requests: AbsChRequests, abs_ch_users: AbsChUsers):
        self.ch_requests: AbsChRequests = abs_ch_requests
        self.ch_users: AbsChUsers = abs_ch_users

    def command_requests_list(self, user_id_req: int, user_tag_req: str) -> str:
        try:
            if True:  # if check_status(user_requester):
                answer = self.languages.get('RU').requests_users_header
                all_requests = [['user_tag', 'user_id']]
                all_requests += self.ch_requests.get_all_users()
                all_requests = tabulate.tabulate(all_requests)

                self.logger_inf.info(msg=f'requests_list - {user_id_req} - {user_tag_req}')

                return f'{answer}`{all_requests}`'
        except Exception as e:
            self.logger_err.error(e)

    def command_requests_clear(self, user_id_req: int, user_tag_req: str) -> str:
        try:
            if True:
                answer = 'Requests deleted'
                self.ch_requests.clear_requests()
                self.logger_inf.info(msg=f'requests_clear - {user_id_req} - {user_tag_req}')
                return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_start(self, user_id_req: str, user_tag_req: str) -> str:
        try:
            if self.register_open:
                if (self.ch_requests.get_user_by_id(user_id_req) is None) and \
                        (self.ch_users.get_user_by_id(user_id_req) is None):
                    self.ch_requests.create_user(
                        user_id=user_id_req,
                        user_tag='@' + user_tag_req
                    )
                    self.logger_inf.info(msg=f'start_first - {user_id_req} - {user_tag_req}')
                    return 'Wait\n'

            self.logger_inf.info(msg=f'start_second - {user_id_req} - {user_tag_req}')
            return 'User exist\n'
        except Exception as e:
            self.logger_err.error(e)

    def command_close_register(self, user_id_req: str, user_tag_req: str) -> str:
        try:
            if True:
                if self.register_open:
                    self.register_open = False
                    answer = 'Register close!'
                else:
                    self.register_open = True
                    answer = 'Register open!'
                self.ch_requests.clear_requests()
                self.logger_inf.info(msg=f'register_close - {answer} -  {user_id_req} - {user_tag_req}')
                return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_user_list(self, user_id_req: int, user_tag_req: str) -> str:
        try:
            if True:  # if check_status(user_requester):
                answer = 'User in Telegram \n'
                all_requests = [['user_tag', 'user_name', 'user_id', 'user_status', 'user_inviter']]
                all_requests += self.ch_users.get_all_users()
                all_requests = tabulate.tabulate(all_requests)

                self.logger_inf.info(msg=f'user_list - {user_id_req} - {user_tag_req}')

                return f'{answer}`{all_requests}`'
        except Exception as e:
            self.logger_err.error(e)

    def command_add_user(self, user_id_req: int, user_tag_req: str, user_id_dem) -> str:
        try:
            if True:
                self.ch_requests.delete_user(user_id_dem)
        except Exception as e:
            self.logger_err.error(e)



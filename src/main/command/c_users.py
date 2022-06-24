import tabulate
from command_heandler.abstract_ch.abstract_ch_requests import AbsChRequests
from command_heandler.abstract_ch.abstract_ch_users import AbsChUsers

from util import logger
from command.msg.c_users_msg import *
from util.user import User


class CommandUsers:
    languages = {'ru': MSGCommandUsersRU(),
                 'en': MSGCommandUserEN()}
    logger_err = logger.logger_error
    logger_inf = logger.logger_info
    register_open: bool = True

    def __init__(self, abs_ch_requests: AbsChRequests, abs_ch_users: AbsChUsers):
        self.ch_requests: AbsChRequests = abs_ch_requests
        self.ch_users: AbsChUsers = abs_ch_users

    def command_requests_list(self, user_req: User) -> str:
        try:
            if True:  # if check_status(user_requester):
                answer = self.languages.get(user_req.lang).requests_users
                all_requests = [['tag', 'id', 'name']]
                all_requests += self.ch_requests.get_all_users()
                all_requests = tabulate.tabulate(all_requests)

                self.logger_inf.info(msg=f'requests_list - {user_req.id} - {user_req.tag}')

                return f'{answer}`{all_requests}`'
        except Exception as e:
            self.logger_err.error(e)

    def command_requests_clear(self, user_req: User) -> str:
        try:
            if True:
                answer = self.languages.get(user_req.lang).requests_clear
                self.ch_requests.clear_requests()
                self.logger_inf.info(msg=f'requests_clear - {user_req.id} - {user_req.tag}')
                return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_start(self, user_req: User) -> str:
        try:
            if self.register_open:
                if (self.ch_requests.get_user_by_id(user_req.id) is None) and \
                        (self.ch_users.get_user_by_id(user_req.id) is None):
                    self.ch_requests.create_user(user_req.id, user_req.tag, user_req.full_name, user_req.chat_id)
                    self.logger_inf.info(msg=f'start_first - {user_req.id} - {user_req.tag}')
                    return self.languages.get(user_req.lang).wait

            self.logger_inf.info(msg=f'start_second - {user_req.id} - {user_req.tag}')
            return self.languages.get(user_req.lang).user_exist
        except Exception as e:
            self.logger_err.error(e)

    def command_close_register(self, user_req: User) -> str:
        try:
            if True:
                if self.register_open:
                    self.register_open = False
                    answer = self.languages.get(user_req.lang).register_close
                else:
                    self.register_open = True
                    answer = self.languages.get(user_req.lang).register_open
                self.ch_requests.clear_requests()
                self.logger_inf.info(msg=f'register_close - {answer} -  {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_user_list(self, user_req: User) -> str:
        try:
            if True:  # if check_status(user_requester):
                answer = self.languages.get(user_req.lang).users_list
                all_requests = [['user_tag', 'user_name', 'user_id', 'user_status', 'user_inviter']]
                all_requests += self.ch_users.get_all_users()
                all_requests = tabulate.tabulate(all_requests)

                self.logger_inf.info(msg=f'user_list - {user_req.id} - {user_req.tag}')

                return f'{answer}`{all_requests}`'
        except Exception as e:
            self.logger_err.error(e)

    def command_add_user_state_0(self, user_req: User) -> str:
        try:
            if True:
                answer = self.languages.get(user_req.lang).user_add
                self.logger_inf.info(msg=f'add_user - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_add_user_state_1(self, user_req: User, msg_text: str) -> str:
        try:
            user_id_dem: int = int(msg_text.split()[0])
            user_status_dem: int = int(msg_text.split()[1])
            if True:
                user: User = self.ch_requests.get_user_by_id(user_id_dem)
                if user is not None:
                    user.status = user_status_dem
                    answer = self.languages.get(user_req.lang).user_add_good
                    self.ch_users.add_user(user)
                    self.ch_requests.delete_user(user.id)

                    self.logger_inf.info(msg=f'add_user - {user_req.id} - {user_req.tag} - User_id_dem: {user_id_dem}')

                    return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_del_user_state_0(self, user_req: User) -> str:
        try:
            if True:
                answer = self.languages.get(user_req.lang).user_del
                self.logger_inf.info(msg=f'del_user - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_del_user_state_1(self, user_req: User, msg_text: str) -> str:
        try:
            user_id_dem: int = int(msg_text.split()[0])

            if True:
                user: User = self.ch_users.get_user_by_id(user_id_dem)
                if user is not None:
                    answer = self.languages.get(user_req.lang).user_del_good
                    self.ch_users.delete_user(user)

                    self.logger_inf.info(msg=f'del_user - {user_req.id} - {user_req.tag} - User_id_dem: {user_id_dem}')

                    return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_update_user_state_0(self, user_req: User) -> str:
        try:
            if True:
                answer = self.languages.get(user_req.lang).user_update
                self.logger_inf.info(msg=f'update_user - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)

    def command_update_user_state_1(self, user_req: User, msg_text: str) -> str:
        try:
            msg_group: list = msg_text.split()
            user_id_dem: int = int(msg_group[0])
            user_name_dem: str = str(msg_group[1])
            user_status_dem: int = int(msg_group[2])

            if True:
                user: User = self.ch_users.get_user_by_id(user_id_dem)
                if user is not None:
                    user.full_name = user_name_dem
                    user.status = user_status_dem
                    answer = self.languages.get(user_req.lang).user_update_good
                    self.ch_users.update_user(user)

                    self.logger_inf.info(
                        msg=f'update_user - {user_req.id} - {user_req.tag} - User_id_dem: {user_id_dem}')

                    return answer
        except Exception as e:
            self.logger_err.error(e)


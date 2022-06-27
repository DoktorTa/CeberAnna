from util import logger
from command.msg.help_msg import *
from util.user import User


class CommandHelp:
    logger_err = logger.logger_error
    logger_inf = logger.logger_info

    def command_help(self, user_req: User) -> str:
        try:
            if True:  # if check_status(user_requester):
                answer = ''
                for command, value in help_msg.items():
                    status_command, text_command = value
                    if status_command >= user_req.status:
                        answer += f'{command} - {text_command}\n'

                self.logger_inf.info(msg=f'requests_list - {user_req.id} - {user_req.tag}')

                return answer
        except Exception as e:
            self.logger_err.error(e)

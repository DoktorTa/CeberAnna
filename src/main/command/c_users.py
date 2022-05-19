import logging

import tabulate
from command_heandler import ch_requests, ch_users
from command_heandler.utils import *

from util import logger
from db.db_back_up import *


logger_err = logger.logger_error
logger_inf = logger.logger_info


def command_requests_list(user_id_req: int, user_tag_req: str) -> str:
    try:
        if True:  # if check_status(user_requester):
            answer = 'User tag in Telegram \n' \
                     'Пользователи просят добавить их в группы:\n'
            all_requests = [['user_tag', 'user_id']]
            all_requests += ch_requests.get_all_users()
            all_requests = tabulate.tabulate(all_requests)

            logger_inf.info(msg=f'requests_list - {user_id_req} - {user_tag_req}')

            return f'{answer}`{all_requests}`'
    except Exception as e:
        logger_err.error(e)


def command_start(user_id_req: str, user_tag_req: str) -> str:
    try:
        if (ch_requests.get_user_by_id(user_id_req) is None) and \
                (ch_users.get_user_by_id(user_id_req) is None):
            ch_requests.create_user(
                user_id=user_id_req,
                user_tag='@' + user_tag_req
            )

            logger_inf.info(msg=f'start - {user_id_req} - {user_tag_req}')
            
            return 'Wait\n'
        else:
            return 'User exist\n'
    except Exception as e:
        logger_err.error(e)

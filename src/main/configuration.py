import logging

from util.logger import conf_logging_level
from command.msg.c_users_msg import *

# conf_logging_level(logging.ERROR)


languages = {'ru': MSGCommandUsersRU(),
             'en': MSGCommandUserEN()}
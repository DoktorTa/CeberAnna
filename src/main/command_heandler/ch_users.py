from db import db_users
from command_heandler.abstract_ch.abstract_ch_users import AbsChUsers


class ChUserSQLite(AbsChUsers):

    @staticmethod
    def get_user_by_id(user_tag: str) -> str:
        return db_users.get_user_by_id(user_tag)

    @staticmethod
    def get_all_users() -> list:
        return db_users.get_user_list()

from abc import ABC
from util.user import User


from db import db_users
from command_heandler.abstract_ch.abstract_ch_users import AbsChUsers


class ChUserSQLite(AbsChUsers, ABC):

    @staticmethod
    def get_user_by_id(user_tag: int) -> User:
        return db_users.get_user_by_id(user_tag)

    @staticmethod
    def get_all_users() -> list:
        return db_users.get_user_list()

    @staticmethod
    def add_user(user: User):
        db_users.create_user(user)

    @staticmethod
    def delete_user(user: User):
        db_users.delete_user(user.id)

    @staticmethod
    def update_user(user: User):
        db_users.update_user(user)

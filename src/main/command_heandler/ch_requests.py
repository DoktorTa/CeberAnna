from db import db_requests
from command_heandler.abstract_ch.abstract_ch_requests import *
from typing import List

from util.user import User


class ChRequestsSQLite(AbsChRequests):

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return db_requests.get_user_by_id(user_id)

    @staticmethod
    def get_all_users() -> list:
        return db_requests.get_all_users()

    @staticmethod
    def clear_requests():
        db_requests.clear_table()

    @staticmethod
    def create_user(user_id: int, user_tag: str, full_name: str, chat_id: int):
        db_requests.create_user(user_id, user_tag, full_name, chat_id)

    @staticmethod
    def delete_user(user_id: int):
        db_requests.delete_user(user_id)

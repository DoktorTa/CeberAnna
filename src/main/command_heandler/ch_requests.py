from db import db_requests
from command_heandler.abstract_ch.abstract_ch_requests import *


class ChRequestsSQLite(ChRequests):

    @staticmethod
    def get_user_by_id(user_id: str) -> str:
        return db_requests.get_user_by_id(user_id)

    @staticmethod
    def get_all_users() -> list:
        return db_requests.get_all_users()

    @staticmethod
    def clear_requests():
        db_requests.clear_table()

    @staticmethod
    def create_user(user_id: str, user_tag: str):
        db_requests.create_user(user_id, user_tag)

    @staticmethod
    def delete_user(user_id: str):
        db_requests.delete_user(user_id)

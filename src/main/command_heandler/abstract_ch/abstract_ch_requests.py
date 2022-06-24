from typing import List
from util.user import User
import abc


class AbsChRequests:

    @staticmethod
    @abc.abstractmethod
    def get_user_by_id(user_id: int) -> User:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_all_users() -> list:
        """
        full_name, user_tag, user_id
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def clear_requests():
        pass

    @staticmethod
    @abc.abstractmethod
    def create_user(user_id: int, user_tag: str, full_name: str, chat_id: int):
        pass

    @staticmethod
    @abc.abstractmethod
    def delete_user(user_id: int):
        pass

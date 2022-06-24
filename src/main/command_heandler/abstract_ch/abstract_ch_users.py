import abc
from util.user import User


class AbsChUsers:

    @staticmethod
    @abc.abstractmethod
    def get_user_by_id(user_id: int) -> User:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_all_users() -> list:
        pass

    @staticmethod
    @abc.abstractmethod
    def add_user(user: User) -> list:
        pass

    @staticmethod
    @abc.abstractmethod
    def delete_user(user: User) -> list:
        pass

    @staticmethod
    @abc.abstractmethod
    def update_user(user: User) -> list:
        pass

from db import db_users


def get_user_by_id(user_tag: str) -> str:
    return db_users.get_user_by_id(user_tag)


def get_all_users() -> list:
    pass

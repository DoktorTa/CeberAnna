from db import db_requests


def get_user_by_id(user_id: str) -> str:
    return db_requests.get_user_by_id(user_id)


def get_all_users() -> list:
    return db_requests.get_all_users()


def create_user(user_id: str, user_tag: str):
    db_requests.create_user(user_id, user_tag)


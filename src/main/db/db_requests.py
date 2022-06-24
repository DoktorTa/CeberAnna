from sqlalchemy.engine import LegacyCursorResult

from db import db_map
from util.user import User


def create_user(user_id: int, user_tag: str, full_name: str, chat_id: int) -> None:
    insert_stm = db_map.requests_table.insert().values(
        user_id=user_id,
        user_tag=user_tag,
        full_name=full_name,
        chat_id=chat_id
    )
    db_map.conn.execute(insert_stm)


def delete_user(user_id: int) -> None:
    delete_stm = db_map.requests_table.delete().where(
        db_map.requests_table.c.user_id == user_id)
    db_map.conn.execute(delete_stm)


def clear_table() -> None:
    all_delete_stm = db_map.requests_table.delete()
    db_map.conn.execute(all_delete_stm)


def get_user_by_id(user_id) -> User:
    select = db_map.requests_table.select().where(
        db_map.requests_table.c.user_id == user_id
    )
    result: LegacyCursorResult = db_map.conn.execute(select)
    return User().init_db_requests(result.mappings().first())


def get_all_users() -> list:
    answer = []

    select = db_map.requests_table.select().where()
    result: LegacyCursorResult = db_map.conn.execute(select)

    for row in result:
        answer.append([
            row['user_tag'],
            row['user_id'],
            row['full_name']
        ])
    return answer


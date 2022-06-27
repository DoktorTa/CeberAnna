from sqlalchemy.engine import LegacyCursorResult

from db import db_map
from util.user import User


def get_user_list() -> list:
    answer = []

    select = db_map.user_table.select().where()
    result: LegacyCursorResult = db_map.conn.execute(select)
    for row in result.mappings():
        answer.append(User().init_db_user(row))
        # answer.append([row['user_tag'], row['user_name'], row['user_id'], row['user_status'], row['user_inviter']])

    return answer


def get_user_by_id(user_id: int) -> User:
    select = db_map.user_table.select().where(
        db_map.user_table.c.user_id == user_id
    )
    result: LegacyCursorResult = db_map.conn.execute(select)
    return User().init_db_user(result.mappings().first())


def delete_user(user_id: int) -> None:
    delete_stm = db_map.user_table.delete().where(
        db_map.user_table.c.user_id == user_id)
    db_map.conn.execute(delete_stm)


def create_user(user: User) -> None:

    insert_stm = db_map.user_table.insert().values(
        user_id=user.id,
        user_tag=user.tag,
        user_name=user.full_name,
        user_status=user.status,
        chat_id=user.chat_id,
        user_inviter=user.inviter
    )
    db_map.conn.execute(insert_stm)


def update_user(user: User) -> None:
    update_stm = db_map.user_table.update()\
        .where(db_map.user_table.c.user_id == user.id)\
        .values(
        user_name=user.full_name,
        user_status=user.status
    )
    db_map.conn.execute(update_stm)

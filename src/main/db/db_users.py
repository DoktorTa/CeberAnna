from db import db_map


def get_user_list() -> list:
    answer = []

    select = db_map.user_table.select().where()
    result = db_map.conn.execute(select)
    for row in result:
        answer.append([row['user_tag'], row['user_name'], row['user_id'], row['user_status'], row['user_inviter']])
    return answer


def get_user_by_id(user_id: str) -> (str, str, int, str):
    select = db_map.user_table.select().where(
        db_map.user_table.c.user_id == user_id
    )
    result = db_map.conn.execute(select)
    if not result.all():
        return None
    return result['user_tag'], result['user_name'], result['user_status'], result['user_inviter']


def delete_user(user_id: str) -> None:
    delete_stm = db_map.user_table.delete().where(
        db_map.user_table.c.user_id == user_id)
    db_map.conn.execute(delete_stm)


def create_user(user_id: int, user_tag: str, user_name: str, user_status: int, user_inviter: str) -> None:
    insert_stm = db_map.user_table.insert().values(
        user_id=user_id,
        user_tag=user_tag,
        user_name=user_name,
        user_status=user_status,
        user_inviter=user_inviter
    )
    db_map.conn.execute(insert_stm)


def update_user(user_id: str, user_name: str, user_status: int) -> None:
    update_stm = db_map.user_table.update()\
        .where(db_map.user_table.c.user_id == user_id)\
        .values(
        user_name=user_name,
        user_status=user_status
    )
    db_map.conn.execute(update_stm)

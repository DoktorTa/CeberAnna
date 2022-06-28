from sqlalchemy.engine import LegacyCursorResult

from db import db_map
from util.storage_item import Item


def create_item(item: Item) -> None:
    insert_stm = db_map.storage_table.insert().values(
        name_group=item.name_group,
        name_subgroup=item.name_subgroup,
        name_id=item.name_id,
        count=item.count
    )
    db_map.conn.execute(insert_stm)


def get_all_item_by_sub_group(name_subgroup: str):
    answer = []

    select = db_map.storage_table.select().where(db_map.storage_table.c.name_subgroup == name_subgroup)
    result: LegacyCursorResult = db_map.conn.execute(select)
    for row in result.mappings():
        answer.append(Item().init_db_storage(row))

    return answer


# TODO: Удалить name из названия - перерефактор
def get_all_name_groups():
    answer = set()

    select = db_map.storage_table.select().where()
    result: LegacyCursorResult = db_map.conn.execute(select)
    for i in result.mappings().all():
        answer.add(i.get('name_group'))

    return list(answer)


# TODO: Удалить name из названия - перерефактор
def get_all_name_subgroups(name_group: str):
    answer = set()

    select = db_map.storage_table.select().where(db_map.storage_table.c.name_group == name_group)
    result: LegacyCursorResult = db_map.conn.execute(select)

    for i in result.mappings().all():
        answer.add(i.get('name_subgroup'))

    return list(answer)


def update_item(item: Item):
    update_stm = db_map.storage_table.update().where(
        db_map.storage_table.c.name_id == item.name_id
    ).values(count=item.count)
    db_map.conn.execute(update_stm)


def get_item_by_subgroup_and_id(item: Item):
    select = db_map.storage_table.select().where(db_map.storage_table.c.name_id == item.name_id)
    result: LegacyCursorResult = db_map.conn.execute(select)
    map_item = result.mappings().first()
    return Item().init_db_storage(map_item)


def delete_item(item: Item):
    update_stm = db_map.storage_table.delete().where(
        db_map.storage_table.c.name_id == item.name_id
    )
    db_map.conn.execute(update_stm)

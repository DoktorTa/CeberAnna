from command_heandler.abstract_ch.abstract_ch_storage import AbsChStorage
from util.storage_item import Item
from db import db_storage


class ChStorageSQLite(AbsChStorage):

    @staticmethod
    def create_item(item: Item):
        db_storage.create_item(item)

    @staticmethod
    def get_all_name_groups():
        return db_storage.get_all_name_groups()

    @staticmethod
    def get_all_name_subgroups(name_group: str):
        return db_storage.get_all_name_subgroups(name_group)

    @staticmethod
    def get_all_item_by_sub_group(name_subgroup: str):
        return db_storage.get_all_item_by_sub_group(name_subgroup)

    @staticmethod
    def update_item(item: Item):
        db_storage.update_item(item)

    @staticmethod
    def get_item_by_subgroup_and_id(item: Item):
        return db_storage.get_item_by_subgroup_and_id(item)

    @staticmethod
    def delete_item(item: Item):
        return db_storage.delete_item(item)


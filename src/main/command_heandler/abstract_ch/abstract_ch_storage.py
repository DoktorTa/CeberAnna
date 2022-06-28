from typing import List
from util.storage_item import Item
import abc


class AbsChStorage:

    @staticmethod
    @abc.abstractmethod
    def create_item(item: Item):
        pass

    @staticmethod
    @abc.abstractmethod
    def get_all_name_groups():
        pass

    @staticmethod
    @abc.abstractmethod
    def get_all_name_subgroups(name_group):
        pass

    @staticmethod
    @abc.abstractmethod
    def get_all_item_by_sub_group(name_subgroup):
        pass

    @staticmethod
    @abc.abstractmethod
    def update_item(name_subgroup):
        pass

    @staticmethod
    @abc.abstractmethod
    def get_item_by_subgroup_and_id(item):
        pass

    @staticmethod
    @abc.abstractmethod
    def delete_item(item):
        pass


from aiogram.dispatcher.filters.state import State, StatesGroup


class AddUserState(StatesGroup):
    waiting_msg = State()


class DelUserState(StatesGroup):
    waiting_msg = State()


class UpdateUserState(StatesGroup):
    waiting_msg = State()


class CreateItemState(StatesGroup):
    waiting_msg = State()


class ShowItemState(StatesGroup):
    waiting_group = State()
    waiting_subgroup = State()


class UpdateItemState(StatesGroup):
    waiting_msg = State()

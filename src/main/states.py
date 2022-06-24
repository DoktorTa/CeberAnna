from aiogram.dispatcher.filters.state import State, StatesGroup


class AddUserState(StatesGroup):
    waiting_msg = State()


class DelUserState(StatesGroup):
    waiting_msg = State()


class UpdateUserState(StatesGroup):
    waiting_msg = State()

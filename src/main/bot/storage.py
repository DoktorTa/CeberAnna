from util.storage_item import Item
from aiogram.types import ParseMode
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext

from util.user import User
from bot.bot import dp, storage_com_group
from bot.keyboards import generate_keyboard_by_names
from bot.states import CreateItemState, ShowItemState, UpdateItemState


@dp.message_handler(commands=['create_item'])
async def create_item_command_state_0(message: types.Message):
    user_req: User = User().init_bot(message)
    text = storage_com_group.command_create_item_state_0(user_req)
    await message.reply(text)
    await CreateItemState.waiting_msg.set()


@dp.message_handler(state=CreateItemState.waiting_msg,
                    content_types=types.ContentTypes.TEXT)
async def create_item_command_state_1(message: types.Message, state: FSMContext):
    user_req: User = User().init_bot(message)
    text = storage_com_group.command_create_item_state_1(user_req, message.text)
    await message.reply(text)
    await state.finish()


@dp.message_handler(commands=['show_item'])
async def show_item_command_state_0(message: types.Message):
    user_req: User = User().init_bot(message)
    text = storage_com_group.command_show_item_state_0(user_req)
    btn_names = storage_com_group.get_all_name_groups()
    btns = generate_keyboard_by_names(btn_names)

    await message.reply(text, reply_markup=btns)
    await ShowItemState.waiting_group.set()


@dp.message_handler(state=ShowItemState.waiting_group,
                    content_types=types.ContentTypes.TEXT)
async def show_item_command_state_1(message: types.Message, state: FSMContext):
    user_req: User = User().init_bot(message)
    text = storage_com_group.command_show_item_state_1(user_req)
    btn_names = storage_com_group.get_all_name_subgroups(message.text)
    btns = generate_keyboard_by_names(btn_names)

    await message.reply(text, reply_markup=btns)
    await ShowItemState.waiting_subgroup.set()


@dp.message_handler(state=ShowItemState.waiting_subgroup,
                    content_types=types.ContentTypes.TEXT)
async def show_item_command_state_2(message: types.Message, state: FSMContext):
    user_req: User = User().init_bot(message)
    text = storage_com_group.command_show_item_state_2(user_req, message.text)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)
    await state.finish()


@dp.message_handler(commands=['update_item'])
async def update_item_command_state_0(message: types.Message):
    user_req: User = User().init_bot(message)
    text = storage_com_group.command_update_item_state_0(user_req)
    await message.reply(text)
    await UpdateItemState.waiting_msg.set()


@dp.message_handler(state=UpdateItemState.waiting_msg,
                    content_types=types.ContentTypes.TEXT)
async def update_item_command_state_1(message: types.Message, state: FSMContext):
    user_req: User = User().init_bot(message)
    text = storage_com_group.command_update_item_state_1(user_req, message.text)
    await message.reply(text)
    await state.finish()

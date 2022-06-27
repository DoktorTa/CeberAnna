import asyncio
import datetime
import logging
import sys
import os

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.markdown import code

import configuration
from command_heandler.ch_requests import *
from command_heandler.ch_users import *
from command import c_users, c_help
from util.user import User
from states import *
from db.db_back_up import backup_db
from bot.keyboards import *

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
users_com_group = c_users.CommandUsers(ChRequestsSQLite(), ChUserSQLite())
help_command = c_help.CommandHelp()
languages = configuration.languages

from bot.service_navigation import *


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    menu = None
    user_req: User = User().init_bot(message)
    text = users_com_group.command_start(user_req)

    if text == languages.get(user_req.lang).user_exist:
        menu = get_main_menu_keyboard()

    await message.reply(text, reply_markup=menu)


# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     user_req: User = User().init_bot(message)
#     text = help_command.command_help(user_req)
#     await message.reply(text, parse_mode=ParseMode.MARKDOWN)
#


# @dp.message_handler(commands=['pax'])
# async def pax_command(message: types.Message):
#     user_req: User = User().init_bot(message)
#     if True:
#
#     await message.reply(text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['requester_list'])
async def requester_list_command(message: types.Message):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_requests_list(user_req)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['requester_clear'])
async def requester_clear_command(message: types.Message):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_requests_clear(user_req)
    await message.reply(text)


@dp.message_handler(commands=['close_register'])
async def close_register_command(message: types.Message):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_close_register(user_req)
    await message.reply(text)


@dp.message_handler(commands=['user_list'])
async def list_list_command(message: types.Message):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_user_list(user_req)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['add_user'])
async def add_user_command_state_0(message: types.Message):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_add_user_state_0(user_req)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)
    await AddUserState.waiting_msg.set()


@dp.message_handler(state=AddUserState.waiting_msg,
                    content_types=types.ContentTypes.TEXT)
async def add_user_command_state_1(message: types.Message, state: FSMContext):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_add_user_state_1(user_req, message.text)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)
    await state.finish()


@dp.message_handler(commands=['del_user'])
async def del_user_command_state_0(message: types.Message):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_del_user_state_0(user_req)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)
    await DelUserState.waiting_msg.set()


@dp.message_handler(state=DelUserState.waiting_msg,
                    content_types=types.ContentTypes.TEXT)
async def del_user_command_state_1(message: types.Message, state: FSMContext):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_del_user_state_1(user_req, message.text)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)
    await state.finish()


@dp.message_handler(commands=['update_user'])
async def update_user_command_state_0(message: types.Message):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_update_user_state_0(user_req)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)
    await UpdateUserState.waiting_msg.set()


@dp.message_handler(state=UpdateUserState.waiting_msg,
                    content_types=types.ContentTypes.TEXT)
async def update_user_command_state_1(message: types.Message, state: FSMContext):
    user_req: User = User().init_bot(message)
    text = users_com_group.command_update_user_state_1(user_req, message.text)
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)
    await state.finish()


executor.start_polling(dp)

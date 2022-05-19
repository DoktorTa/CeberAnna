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

from command_heandler import ch_requests
from command import c_users

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
users_com_group = c_users.CommandUsers()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    text = users_com_group.command_start(
        user_id_req=message.from_user.id,
        user_tag_req=message.from_user.username
    )
    await message.reply(text)


@dp.message_handler(commands=['requester_list'])
async def requester_list_command(message: types.Message):
    text = users_com_group.command_requests_list(
        user_id_req=message.from_user.id,
        user_tag_req=message.from_user.username
    )
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['requester_clear'])
async def requester_clear_command(message: types.Message):
    text = users_com_group.command_requests_clear(
        user_id_req=message.from_user.id,
        user_tag_req=message.from_user.username
    )
    await message.reply(text)


@dp.message_handler(commands=['close_register'])
async def close_register_command(message: types.Message):
    text = users_com_group.command_close_register(
        user_id_req=message.from_user.id,
        user_tag_req=message.from_user.username
    )
    await message.reply(text)


executor.start_polling(dp)

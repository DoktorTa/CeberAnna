import asyncio
import datetime
import logging
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


@dp.message_handler(commands=['start'])
async def process_cans_list_command(message: types.Message):
    text = c_users.command_start(
        user_id_req=message.from_user.id,
        user_tag_req=message.from_user.username
    )
    await message.reply(text)


@dp.message_handler(commands=['requester_list'])
async def process_cans_list_command(message: types.Message):
    text = c_users.command_requests_list(message.from_user.username)
    await message.reply(text)

if __name__ == '__main__':
    executor.start_polling(dp)
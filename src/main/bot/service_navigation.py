from util.user import User
from aiogram import Bot, types

from bot.bot import dp, users_com_group, storage_com_group
from bot.keyboards import generate_keyboard_by_names


@dp.message_handler(commands=['users'])
async def users_command(message: types.Message):
    user_req: User = User().init_bot(message)
    btn_names = users_com_group.get_group_users_commands(user_req, users_com_group.commands)
    menu = generate_keyboard_by_names(btn_names, False)
    await message.reply('Ok', reply_markup=menu)


@dp.message_handler(commands=['storage'])
async def storage_command(message: types.Message):
    user_req: User = User().init_bot(message)
    # TODO: Вынеси нахуй это их юзера
    btn_names = users_com_group.get_group_users_commands(user_req, storage_com_group.commands)
    menu = generate_keyboard_by_names(btn_names, False)
    await message.reply('Ok', reply_markup=menu)


#
# @dp.message_handler(commands=['objects'])
# async def objects_command(message: types.Message):
#     user_req: User = User().init_bot(message)
#     btn_names =
#     send_keyboard(message, btn_names)
#
#
# @dp.message_handler(commands=['setting'])
# async def setting_command(message: types.Message):
#     user_req: User = User().init_bot(message)
#     btn_names =
#     send_keyboard(message, btn_names)
#
#
# @dp.message_handler(commands=['send_location'])
# async def send_location_command(message: types.Message):
#     user_req: User = User().init_bot(message)
#     btn_names =
#     send_keyboard(message, btn_names)
#
#
# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     user_req: User = User().init_bot(message)
#     btn_names =
#     send_keyboard(message, btn_names)



from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_menu_keyboard():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    btn_storage = KeyboardButton('/storage')
    btn_pax = KeyboardButton('/users')
    btn_object = KeyboardButton('/object')
    btn_setting = KeyboardButton('/setting')
    btn_share_location = KeyboardButton('/send_location!')
    btn_help = KeyboardButton(r'/help')

    btn.add(btn_storage, btn_object)
    btn.add(btn_pax, btn_setting)
    btn.add(btn_share_location, btn_help)

    return btn


def get_pax_menu_keyboard():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    btn_user_list = KeyboardButton('/user_list')
    btn_requester_list = KeyboardButton('/requester_list')
    btn_requester_clear = KeyboardButton('/requests_clear')
    btn_close_register = KeyboardButton('/close_register')
    btn_add_user = KeyboardButton('/add_user')
    btn_delete_user = KeyboardButton('/delete_user')
    btn_update_user = KeyboardButton('/update_user')
    btn_find_user = KeyboardButton('/find_user')

    btn.add(btn_requester_list, btn_requester_clear)
    btn.add(btn_close_register, btn_user_list)
    btn.add(btn_add_user, btn_delete_user)
    btn.add(btn_update_user, btn_find_user)

    return btn


def generate_keyboard_by_names(names_but: list, one_time_keyboard=True):
    if len(names_but) == 0:
        return None

    but = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=one_time_keyboard)

    iter_name_but = names_but.__iter__()

    while True:
        try:
            left_but_name = next(iter_name_but)
        except StopIteration as ex:
            break

        try:
            right_but_name = next(iter_name_but)
        except StopIteration as ex:
            left_but = KeyboardButton(str(left_but_name))
            but.add(left_but)
            break

        left_but = KeyboardButton(str(left_but_name))
        right_but = KeyboardButton(str(right_but_name))

        but.add(left_but, right_but)

    return but

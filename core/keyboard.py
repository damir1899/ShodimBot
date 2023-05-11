from aiogram.types import *

start_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Зарегистрироваться', request_contact=True),
    KeyboardButton(text='О нас')
)

auth_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Места'),
    KeyboardButton(text='Поиск мест...'),
)
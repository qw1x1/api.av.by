from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

def key():
    perekup = InlineKeyboardBuilder()
    perekup._markup.clear()
    perekup.row(types.InlineKeyboardButton(text=F"Подписка", callback_data="sell"))
    keyboard=perekup.as_markup()
    return keyboard
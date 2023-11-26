from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress



def key():
    perekup = InlineKeyboardBuilder()
    perekup._markup.clear()
    perekup.add(types.InlineKeyboardButton(text="Да", callback_data="perekup_yes"))
    perekup.add(types.InlineKeyboardButton(text="Нет", callback_data="perekup_no"))
    keyboard=perekup.as_markup()
    return keyboard
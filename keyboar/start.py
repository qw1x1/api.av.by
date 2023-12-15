from aiogram import types,F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress



def key():
    perekup = InlineKeyboardBuilder()
    perekup._markup.clear()
    perekup.row(types.InlineKeyboardButton(text=F"Поиск с процентом отклонения от среднерыночной стоимости", callback_data="perekup_yes"))
   # perekup.add(types.InlineKeyboardButton(text="Поиск всех авто с заданым процентом отклонения от среднерыночной стоимости", callback_data="perekup_yes"))
    perekup.row(types.InlineKeyboardButton(text=F"Поиск конкретной марки автомобиля", callback_data="perekup_no"))
    keyboard=perekup.as_markup()
    return keyboard
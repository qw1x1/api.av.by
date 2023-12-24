from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

def key():
    perekup = InlineKeyboardBuilder()
    perekup._markup.clear()
    perekup.row(types.InlineKeyboardButton(text=F"Поиск с процентом отклонения от среднерыночной стоимости", callback_data="perekup_yes"))
    perekup.row(types.InlineKeyboardButton(text=F"Поиск конкретной марки автомобиля", callback_data="perekup_no"))
    keyboard=perekup.as_markup()
    return keyboard
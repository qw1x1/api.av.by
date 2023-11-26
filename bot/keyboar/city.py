from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

async def keyboard(message:types.Message, keybrd:InlineKeyboardBuilder, txt:str):
    with suppress(TelegramBadRequest):
        await message.answer(txt, reply_markup=keybrd)

def api_call(list):
    region_name_list = InlineKeyboardBuilder()
    region_name_list._markup.clear()
    for i in list:
        #region_name_list.adjust(3)
        for key, value in i.items():
            
            region_name_list.add(types.InlineKeyboardButton(text=key, callback_data="city_"+str(key)))
    region_name_list.adjust(3)
    region_name_list=region_name_list.as_markup()
    region_name_list.inline_keyboard.append([types.InlineKeyboardButton(text="Подтвердить", callback_data="city_enter")])
    return region_name_list


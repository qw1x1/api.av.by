from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

async def keyboard(message:types.Message, keybrd:InlineKeyboardBuilder, txt:str):
    with suppress(TelegramBadRequest):
        await message.answer(txt, reply_markup=keybrd.as_markup())

def api_call(list):
    region_name_list = InlineKeyboardBuilder()
    region_name_list._markup.clear()
    for i in list:
        region_name_list.adjust(3)
        for key, value in i.items():
            
            region_name_list.add(types.InlineKeyboardButton(text=key, callback_data="region_"+str(value)))
    
    return region_name_list
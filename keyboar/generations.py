from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from api.av1 import brand
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

async def keyboard(message:types.Message, keybrd:InlineKeyboardBuilder, txt:str):
    with suppress(TelegramBadRequest):
        await message.answer(txt, reply_markup=keybrd.as_markup())

def api_call(list):
    gen_list = InlineKeyboardBuilder()
    gen_list._markup.clear()
    for key, value in list.items():
        gen_list.adjust(3)
        gen_list.add(types.InlineKeyboardButton(text=key, callback_data="gen_"+str(value)))
    return gen_list
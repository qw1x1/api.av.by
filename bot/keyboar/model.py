from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from av1 import brand
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

async def keyboard(message:types.Message, keybrd:InlineKeyboardBuilder, txt:str):
    with suppress(TelegramBadRequest):
        await message.answer(txt, reply_markup=keybrd.as_markup())

def api_call(list):
    model_list = InlineKeyboardBuilder()
    model_list._markup.clear()
    for key, value in list.items():
        model_list.adjust(3)
        model_list.add(types.InlineKeyboardButton(text=key, callback_data="model_"+str(value)))
    return model_list
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from api.av1 import get_city_for_region
import command.start as Start

async def keyboard(message:types.Message, keybrd:InlineKeyboardBuilder(), action:int, txt:str):
        city_list = get_city_for_region(action)
        for i in city_list:
            for key, value in i.items():
                keybrd.add(types.InlineKeyboardButton(text=key, callback_data="city_"+key))
        keybrd.adjust(3)
        await message.answer(txt, reply_markup=keybrd.as_markup())

def NewKeyboard(bilder:InlineKeyboardBuilder(), text):
    new_city = InlineKeyboardBuilder()
    new_city._markup = bilder._markup
    markup_city = new_city.as_markup()
    button=types.InlineKeyboardButton(text=text, callback_data="city_"+text)
    for i in range(0, len(markup_city.inline_keyboard), 1):
         for j in range(0, len(markup_city.inline_keyboard[i]), 1):
            if markup_city.inline_keyboard[i][j] == button:
                del markup_city.inline_keyboard[i][j]
                break
    new_city._markup = markup_city.inline_keyboard
    return new_city

async def new_keyboard(message:types.Message, id, text:str):
    Start.city_bilder[id] = NewKeyboard(Start.city_bilder[id], text)
    await message.edit_text("Выберите город или несколько городов:", reply_markup=Start.city_bilder[id].as_markup())


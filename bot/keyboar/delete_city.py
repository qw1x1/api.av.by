from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
import command.start as Start

async def keyboard(message:types.Message, keybrd:InlineKeyboardBuilder(), mass:list, txt:str):
        city_list = mass
        for i in city_list:
            keybrd.add(types.InlineKeyboardButton(text=i, callback_data="citydel_"+i))
        keybrd.adjust(3)
        await message.answer(txt, reply_markup=keybrd.as_markup())

def NewKeyboard(bilder:InlineKeyboardBuilder(), text):
    new_city = InlineKeyboardBuilder()
    new_city._markup = bilder._markup
    markup_city = new_city.as_markup()
    button=types.InlineKeyboardButton(text=text, callback_data="citydel_"+text)
    for i in range(0, len(markup_city.inline_keyboard), 1):
         for j in range(0, len(markup_city.inline_keyboard[i]), 1):
            if markup_city.inline_keyboard[i][j] == button:
                del markup_city.inline_keyboard[i][j]
                break
    new_city._markup = markup_city.inline_keyboard
    return new_city

async def new_keyboard(message:types.Message, id, text:str):
    Start.del_city_bilder[id] = NewKeyboard(Start.del_city_bilder[id], text)
    await message.edit_text("Выберите город который хотите удалить:", reply_markup=Start.del_city_bilder[id].as_markup())


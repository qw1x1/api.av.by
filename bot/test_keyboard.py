import asyncio, math
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
#from config_reader import config
from bs4 import BeautifulSoup as bs
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Text, CommandObject
import json, io
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot=Bot(token='5628896267:AAEQx6cQLtx9ZX5-g9X8zZ778EyP_XZiQew')
dp = Dispatcher()
user_data = {}


def Keyboard(markup:InlineKeyboardBuilder()): 
    for i in range(21):
           markup.adjust(3)
           markup.add(InlineKeyboardButton(text=i,callback_data="q"))

def NewKeyboard(zalupa:InlineKeyboardBuilder(), val:int,val2:int):
    qwe=InlineKeyboardBuilder()
    qwe._markup=zalupa._markup[val:val2]
    qwe=qwe.as_markup()
    qwe.inline_keyboard.append([types.InlineKeyboardButton(text="<", callback_data="coice_back"),
types.InlineKeyboardButton(text="Подтвердить", callback_data="coice_coice"),
types.InlineKeyboardButton(text=">", callback_data="coice_forward")])
    return qwe

@dp.message(Command("start"))
async def call_backs(message: types.Message):
    builder=InlineKeyboardBuilder()
    Keyboard(builder)
    await message.answer("Выберите бренд автомобиля", reply_markup=NewKeyboard(builder,0,3))
    await message.answer("Выберите бренд автомобиля", reply_markup=NewKeyboard(builder,3,6))
    


async def main():
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
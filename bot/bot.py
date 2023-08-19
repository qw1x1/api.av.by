import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from av1 import brand, Get_model
from aiogram.filters import Text
from contextlib import suppress


BOT_TOKEN = '6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8'
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


model = Get_model()
# bran = brand


@dp.message(Command("start"))
async def bild_mrnu_brend(message: types.Message):
    builder = InlineKeyboardBuilder()
    for key, value in brand.items():
        builder.button(text=key, callback_data=value)
    builder.adjust(3)
#  хз как достать и записать переменную value для передачи 
    await message.answer('Выберете марку автомобиля:', reply_markup=builder.as_markup())

@dp.message(Command("model"))
async def bild_mrnu_model(message: types.Message):
    builde = InlineKeyboardBuilder()
    mode = model.get_data_select_car(str(6) +'/models') # сюда передать id бренда 
    for key, value in mode.items():
        builde.button(text=key, callback_data=value)
    builde.adjust(2)
    await message.answer('Выберете модель автомобиля:', reply_markup=builde.as_markup())


async def main():
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
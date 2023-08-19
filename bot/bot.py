import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.filters import Text
# from contextlib import suppress
# from aiogram.exceptions import TelegramBadRequest

from av1 import brand, Get_model, Pars_info_id_file,  Search_cars


BOT_TOKEN = '6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8'
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

model = Get_model()


@dp.message(Command("start"))
async def bild_mrnu_brend(message: types.Message):
    user_id = message.from_user.id # просто достал user.id, посмотреть как работает
    builder = InlineKeyboardBuilder()

    for key, value in brand.items():
        builder.button(text=key, callback_data=value)
    builder.adjust(3)
#  хз как достать и записать переменную value для передачи, после нажатя кнопки
    await message.answer(f'Выберете марку автомобиля: {(user_id)}', reply_markup=builder.as_markup())

    

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
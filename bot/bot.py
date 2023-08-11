import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Text
import json, io


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

#command=[BotCommand(command="start",description="to start something"),BotCommand(command="stop", description="to stop something")]

   
# Хэндлер на команду /start
#@dp.message(Command("start"))
#async def cmd_start(message: types.Message):
    
#    await message.answer("Hello!")

def list_add():
    cars=InlineKeyboardBuilder()
    with io.open("brand.json",encoding='utf-8') as js_file:
        list=json.load(js_file)
        for key, value in list.items():
            cars.adjust(3)
            cars.add(types.InlineKeyboardButton(
                text=key,
                callback_data=value)
                )
    return cars
# Запуск процесса поллинга новых апдейтов

builder = InlineKeyboardBuilder()

@dp.message(Command("start"))
async def call_backs(message: types.Message):
    builder = list_add()
    await message.answer(
        "Выберите бренд автомобиля",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(Text(startswith=""))
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("ANUS")

async def main():
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
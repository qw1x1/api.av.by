import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from aiogram.types import BotCommand
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
    cars=[]
    with io.open("brand.json",encoding='utf-8') as js_file:
        list=json.load(js_file)

        for country in list:
            cars.append(types.BotCommand(command=country['slug'].replace('-',''),description=country['name']))
    return cars
    

# Запуск процесса поллинга новых апдейтов
async def main():
    cars=list_add()
    await bot.set_my_commands(cars)
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
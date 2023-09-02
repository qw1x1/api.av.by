import asyncio
import logging
from aiogram import Bot, Dispatcher,types
from aiogram.fsm.storage.memory import MemoryStorage
from callbacks import brand, coice, model, delete
from command import start, all, help, mycars
from message import date, output_car, procent 
from aiogram.filters.command import Command
#from msgusr import messageuser
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
storage:MemoryStorage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_routers(brand.router, coice.router, model.router, start.router,
                    date.router, output_car.router, procent.router, all.router, 
                    delete.router, help.router, mycars.router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.message(Command("qwe"))
async def call_backs(message: types.message):
    await bot.send_message(633279160,'ЭЙ, ЛЫСЫЙ ЧЕРВЯК, ТЫ ШО СУКА СПИШЬ?')

if __name__ ==  '__main__':
    asyncio.run(main())
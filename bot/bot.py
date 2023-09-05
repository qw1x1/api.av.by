import asyncio
import logging
from aiogram import Bot, Dispatcher,types
from aiogram.fsm.storage.memory import MemoryStorage
from callbacks import brand, coice, model, delete
from command import start, help, mycars
from message import date, output_car, procent 
from aiogram.filters.command import Command
#from msgusr import messageuser
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
storage:MemoryStorage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_routers(brand.router, coice.router, model.router, start.router,
                    date.router, output_car.router, procent.router,
                    delete.router, help.router, mycars.router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def send_msg(id: int, message: str):
    await bot.send_message(id,message)

if __name__ ==  '__main__':
    asyncio.run(main())
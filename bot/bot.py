import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from callbacks import brand, coice, model
from command import start
from message import date, output_car, procent

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
#bot = Bot(token=str(config.bot_token.get_secret_value()))
bot=Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
# Диспетчер
storage: MemoryStorage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(brand.router, coice.router, model.router,start.router, 
                   date.router, output_car.router, procent.router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
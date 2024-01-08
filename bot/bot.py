import asyncio, logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from callbacks import brand, coice, model, delete, generations, perekup, region, delcity, city
from command import start, help, mycars, addcars, del_city, procent, region_car
from message import output_car
import message.perekup

logging.basicConfig(level=logging.INFO)
bot = Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
storage:MemoryStorage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(brand.router, coice.router, model.router, start.router, delete.router, help.router, mycars.router,
                   generations.router, addcars.router, perekup.router, output_car.router, region.router, 
                   region_car.router, del_city.router, delcity.router, procent.router, city.router,message.perekup.router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ ==  '__main__':
    asyncio.run(main())
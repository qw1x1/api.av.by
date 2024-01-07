import asyncio, logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Text
from aiogram.types.message import ContentType
from aiogram.fsm.storage.memory import MemoryStorage
from callbacks import brand, coice, model, delete, generations, perekup, region, delcity, city
from command import start, help, mycars, addcars, del_city, procent, region_car,menu,poisk
from message import output_car, apshced
from datetime import datetime, timedelta
import message.perekup, message.menu
from apscheduler.schedulers.asyncio import AsyncIOScheduler


logging.basicConfig(level=logging.INFO)
bot = Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
storage:MemoryStorage = MemoryStorage()
dp = Dispatcher(storage=storage)
#scheduler = AsyncIOScheduler(timezone='Europe/Moscow')



dp.include_routers(brand.router, coice.router, model.router, start.router, delete.router, help.router, mycars.router,
                   generations.router, addcars.router, perekup.router, output_car.router, region.router, 
                   region_car.router, del_city.router, delcity.router, procent.router, city.router,message.perekup.router,menu.router,message.menu.router,poisk.router)

async def main():
    #scheduler.add_job(apshced.send_message_time, trigger='interval', seconds=18000, kwargs={'bot': bot})
    #scheduler.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.callback_query(Text(startswith="sell"))
async def callbacks_sell(callback:types.CallbackQuery):
    await callback.message.answer('Подписка в данных момоент не доступна, свяжитесь с https://t.me/qw_1x')
    await callback.answer()
#    await bot.delete_message(callback.from_user.id,callback.message.message_id)
#    await bot.send_invoice(
#        chat_id=callback.from_user.id, 
#        title="Подписка", 
#        description="Подписка", 
#        payload='subscribe', 
#        provider_token='381764678:TEST:74663', 
#        currency='rub',
#        prices=[
#            types.LabeledPrice(label='qwe', amount=50000)
#            ]
#            )

@dp.pre_checkout_query()
async def checkout_query(check: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(check.id,True)

    
@dp.message(F.successful_payment)
async def process_pay(message: types.Message):
    if(message.successful_payment.invoice_payload == 'subscribe'):
        await bot.send_message(message.from_user.id, 'Вам выдана подписка на месяц')

if __name__ ==  '__main__':
    asyncio.run(main())
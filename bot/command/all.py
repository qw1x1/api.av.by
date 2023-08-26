from aiogram import Router, F, types
from aiogram.filters.command import Command
from models import *
from update import Get_data_for_request
import math

router = Router()

@router.message(Command("all"))
async def call(message:types.Message):
    user_id = message.from_user.id # message.from_user.id
    respons = Get_data_for_request(user_id)
    for car in respons:
        list_cars, arg_price = car[0], car[1]
        for item in list_cars:
            txt=f"Среднерыночная стоимость: {math.floor(arg_price)}  "+item['name']+f"\n"+item['lank']+f"\n"+item['parametrs']+f"\n"+item['mileage']+f"\n"+str(item['price'])+" \n"+item['description']+"\n"+item['location']
            await message.answer(text=txt)
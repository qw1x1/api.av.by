from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import callbacks.model as cb_model
import callbacks.brand as cb_brand
from av1 import Pars_info_id_file, Search_cars
import math
from controls import Control_db
from models import *

brand_car_id, model_car_id = '', ''
router = Router()

price_date_procent_dict: dict[str, str, int] = {}

@router.message(StateFilter(cb_model.Inputdata.procent))
async def process_name_sent(message: types.Message, state: FSMContext):
    await state.update_data(procent=message.text)
    price_date_procent_dict[message.from_user.id] = await state.get_data()
    # Завершаем машину состояний
    await state.clear()
    #await message.answer(text=F"{price_date_procent_dict[message.from_user.id]['price']} {price_date_procent_dict[message.from_user.id]['date']} {price_date_procent_dict[message.from_user.id]['procent']}")
    global brand_car_id, model_car_id
    model_car_id = cb_model.model_car_id
    brand_car_id = cb_brand.brand_car_id
    price_min, price_max, year_min, year_max=0,0,0,0
    deviation_procent = 55
    price_min, price_max = price_date_procent_dict[message.from_user.id]['price'].split('-')[0],price_date_procent_dict[message.from_user.id]['price'].split('-')[1]
    year_min, year_max = price_date_procent_dict[message.from_user.id]['date'].split('-')[0],price_date_procent_dict[message.from_user.id]['date'].split('-')[1]
    deviation_procent = price_date_procent_dict[message.from_user.id]['procent']
    pars_info = Pars_info_id_file(brand_id=int(brand_car_id),model_id=int(model_car_id),
                                  year_max=int(year_max),year_min=int(year_min), 
                                  price_max=int(price_max),price_min=int(price_min))
    #await message.answer(F"{price_min} {price_max} {year_min} {year_max}")
    cars_count_page = pars_info()
    if cars_count_page == 0:
        await message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу') 
    else:
        serch_cars_ekz = Search_cars(pars_info.car,pars_info.count_page, deviation_procent)
        serch_car = serch_cars_ekz()
        list_cars, arg_price = serch_car[0], serch_car[1]

        if len(list_cars) != 0:
            with db:
                obj = Control_db(message.from_user.id)
                us = obj.create_user()
                obj.create_request(brand_id=int(brand_car_id),model_id=int(model_car_id),
                                  year_max=int(year_max),year_min=int(year_min), 
                                  price_max=int(price_max),price_min=int(price_min), 
                                  percent_difference=int(deviation_procent), user=us[0])
            for item in list_cars:
                txt=f"Среднерыночная стоимость: {math.floor(arg_price)}  "+item['name']+f"\n"+item['lank']+f"\n"+item['parametrs']+f"\n"+item['mileage']+f"\n"+str(item['price'])+" \n"+item['description']+"\n"+item['location']
                await message.answer(text=txt)
        else:
            await message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу, измените процент отклонения от среднерыночной стоимости')

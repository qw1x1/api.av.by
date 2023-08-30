from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import callbacks.model as cb_model
import callbacks.brand as cb_brand
from api.av1 import Pars_info_id_file, Search_cars
import math
from api.controls import Control_db
from api.models import *
import command.start as Start

router = Router()

price_date_procent_dict: dict[str, str, int] = {}

@router.message(StateFilter(cb_model.Inputdata.procent))
async def process_name_sent(message: types.Message, state: FSMContext):
    try:
        await state.update_data(procent=message.text)
        price_date_procent_dict[message.from_user.id] = await state.get_data()
        await state.clear()


        price_min, price_max, year_min, year_max = 0, 0, 0, 0
        deviation_procent = int(message.text)
        price_min, price_max = price_date_procent_dict[message.from_user.id]['price'].split('-')[0], price_date_procent_dict[message.from_user.id]['price'].split('-')[1]
        year_min, year_max = price_date_procent_dict[message.from_user.id]['date'].split('-')[0], price_date_procent_dict[message.from_user.id]['date'].split('-')[1]
        deviation_procent = int(price_date_procent_dict[message.from_user.id]['procent'])
        pars_info = Pars_info_id_file(brand_id=int(Start.brand[message.from_user.id]), model_id=int(cb_model.id_model[message.from_user.id]),
                                    year_max=int(year_max), year_min=int(year_min), 
                                    price_max=int(price_max), price_min=int(price_min))

        cars_count_page = pars_info()
        if cars_count_page == 0:
            await message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу') 
        else:
            serch_cars_ekz = Search_cars(pars_info.car, pars_info.count_page, deviation_procent)
            serch_car = serch_cars_ekz()
            list_cars, arg_price = serch_car[0], serch_car[1]
            await message.answer(text=f'Среднерыночная стоимость: {math.floor(arg_price)}')
            if len(list_cars) != 0:
                with db:
                    obj = Control_db(message.from_user.id)
                    us = obj.create_user()
                    obj.create_request(brand_id=int(Start.brand[message.from_user.id]), model_id=int(cb_model.id_model[message.from_user.id]),
                                    year_max=int(year_max), year_min=int(year_min), 
                                    price_max=int(price_max), price_min=int(price_min), 
                                    percent_difference=deviation_procent, user=us[0])
                    



                trek = 0
                for item in list_cars:
                    if trek == 10:
                        trek = 0
                        await message.answer(text=f'1 sek') # Тут бы придумать чет чтоб вывод сделать с кнопкой продолжить
                    else:
                        trek += 1
                        txt=f"{item['link']}"
                        await message.answer(text=txt)




            else:
                await message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу, измените процент отклонения от среднерыночной стоимости')
    except:
        await message.answer(text='Введенны не корректные данные')
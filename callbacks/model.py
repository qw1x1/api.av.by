from aiogram import Router, types
from aiogram.filters import Text
from api.av1 import Pars_info_id_file, Search_cars
import math
from api.controls import create_request
from api.models import *
import command.start as Start


router = Router()

id_model = {}

@router.callback_query(Text(startswith="model_"))
async def callbacks_cars(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    id_model[callback.from_user.id] = action
    global brand_car_id, model_car_id
    pars_info = Pars_info_id_file(brand_id=int(Start.brand[callback.from_user.id]), model_id=int(id_model[callback.from_user.id]),
                                 generations_id=0)

    
    cars_count_page = pars_info()
    if cars_count_page == 0:
        await callback.message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу') 
    else:
        serch_cars_ekz = Search_cars(pars_info.car, pars_info.count_page)
        serch_car = serch_cars_ekz()
        list_cars, arg_price = serch_car[0], serch_car[1]
        await callback.message.answer(text=f'Среднерыночная стоимость: {math.floor(arg_price)}')
        if len(list_cars) != 0:
            create_request(brand_id=int(Start.brand[callback.from_user.id]), model_id=int(id_model[callback.from_user.id]), user=callback.from_user.id)
            trek = 0
            for item in list_cars:
                if trek == 10:
                    trek = 0
                    await callback.message.answer(text=f'1 sek') # Тут бы придумать чет чтоб вывод сделать с кнопкой продолжить
                else:
                    trek += 1
                    txt=f"{item['link']}"
                    await callback.message.answer(text=txt)




        else:
            await callback.message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу, измените процент отклонения от среднерыночной стоимости')
        await callback.answer()

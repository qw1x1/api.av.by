from aiogram import Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import callbacks.perekup as procent
from api.av1 import Pars_info_id_file, Search_cars
import math
import api.controls as Controls
from api.models import *
import command.start as Start

router = Router()


@router.message(StateFilter(procent.Inputdata.procent))
async def process_name_sent(message: types.Message, state: FSMContext):
    await state.update_data(procent=message.text)
    Start.procent[message.from_user.id] = await state.get_data()
    await state.clear()

    pars_info = Pars_info_id_file(brand_id=int(Start.brand[message.from_user.id]), 
                                  model_id=int(Model.id_model[message.from_user.id]),generations_id=Start.id_gen[message.from_user.id])


    cars_count_page = pars_info()
    if cars_count_page == 0:
        await message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу') 
    else:
        serch_cars_ekz = Search_cars(pars_info.car, pars_info.count_page, Start.procent[message.from_user.id])
        serch_car = serch_cars_ekz()
        list_cars, arg_price = serch_car[0], serch_car[1]
        await message.answer(text=f'Среднерыночная стоимость: {math.floor(arg_price)}')
        if len(list_cars) != 0:
 #           Controls.create_request(brand_id=int(Start.brand[message.from_user.id]), model_id=int(Start.id_model[message.from_user.id]), 
  #Cюда нужно ввести user=user                                percent_difference=Start.procent[message.from_user.id], user=)




            for item in list_cars:
                await message.answer(text=item)




        else:
            await message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу, измените процент отклонения от среднерыночной стоимости')
    

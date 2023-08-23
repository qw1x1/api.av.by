import asyncio, math
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
#from config_reader import config
from bs4 import BeautifulSoup as bs
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Text, CommandObject
import json, io
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from av1 import brand, Get_model, Pars_info_id_file,  Search_cars, Get_revers_model, revers_brand
from controls import Control_db
from models import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
dp, builder, model, rev_model = Dispatcher(), InlineKeyboardBuilder(), Get_model(),  Get_revers_model()
brand_car_id, model_car_id, user_data = '', '', {}

def keyboard_coice():
    buttons = [
        types.InlineKeyboardButton(text="<", callback_data="coice_back"),
        types.InlineKeyboardButton(text="Подтвердить", callback_data="coice_coice"),
        types.InlineKeyboardButton(text=">", callback_data="coice_forward")
    ]    
    return buttons

def list_add():
    brand_cars=brand.items()
    cars = InlineKeyboardBuilder()
    for key, value in brand_cars:
        cars.adjust(3)
        cars.add(types.InlineKeyboardButton(text=key, callback_data="car_"+str(value)))
    return cars

builder_new = InlineKeyboardBuilder()
def builder_sell(start:int):
    builder_old = list_add()
    stop, builder_new._markup = start*10 if (start*10<=len(builder_old._markup))else len(builder_old._markup), []
    for i in range(stop-10, stop, 1):
        builder_new._markup.append(builder_old._markup[i])
    builder_new._markup.append(keyboard_coice())
    return builder_new

async def new_page(message: types.Message, new_value:int):
    with suppress(TelegramBadRequest):
        await message.edit_text(f"Выберите бренд автомобиля:", reply_markup=builder_sell(new_value).as_markup())

async def keyboard(message:types.Message, keybrd:InlineKeyboardBuilder, txt:str):
    with suppress(TelegramBadRequest):
        await message.answer(txt, reply_markup=keybrd.as_markup())

@dp.message(Command("start"))
async def call_backs(message: types.Message):
    model.user = message.from_user.id
    user_data[message.from_user.id] = 1
    builder = builder_sell(1)
    await message.answer("Выберите бренд автомобиля", reply_markup=builder.as_markup())

@dp.callback_query(Text(startswith="coice_"))
async def callbacks_num(callback:types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 1)
    action = callback.data.split("_")[1]
    if action == "back":
        user_data[callback.from_user.id] = user_value - 1
        await new_page(callback.message, user_value - 1)
    elif action == "forward":
        user_data[callback.from_user.id] = user_value + 1
        await new_page(callback.message, user_value + 1)
    await callback.answer()

def api_call(list):
    model_list = InlineKeyboardBuilder()
    model_list._markup.clear()
    for key, value in list.items():
        model_list.adjust(3)
        model_list.add(types.InlineKeyboardButton(text=key, callback_data="model_"+str(value)))
    return model_list

@dp.callback_query(Text(startswith="car_"))
async def callbacks_cars(callback:types.CallbackQuery):
    action, model_car = callback.data.split("_")[1], {}
    global brand_car_id
    brand_car_id = action
    model_car = model.get_data_select_car(str(action) +'/models')
    models_keyboard = InlineKeyboardBuilder()
    models_keyboard._markup.clear()
    models_keyboard = api_call(model_car)
    await keyboard(callback.message, keybrd=models_keyboard, txt="Выберите марку авто:")
    await callback.answer()

@dp.callback_query(Text(startswith="model_"))
async def callbacks_cars(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    global model_car_id
    global brand_car_id
    model_car_id = action

    ##########################
    #ТУТ БУДЕТ ВВОД ГОДА И ЦЕНЫ
    ##########################
    
    pars_info = Pars_info_id_file(brand_id=brand_car_id,model_id=model_car_id)
    cars_count_page = pars_info()

    if cars_count_page == 0:
        await callback.message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу') 
    else:
        deviation_procent = 60
        serch_cars_ekz = Search_cars(pars_info.car,pars_info.count_page, deviation_procent)
        serch_car = serch_cars_ekz()
        list_cars, arg_price = serch_car[0], serch_car[1]
        if len(list_cars) != 0:

            with db:
                obj = Control_db(callback.message.from_user.id)
                us = obj.create_user()
                percent_difference = 60
                obj.create_request(brand_id=brand_car_id, model_id=model_car_id, percent_difference=percent_difference, year_min=0, year_max=0, price_min=0, price_max=0, user=us[0])

            for item in list_cars:
                txt=f"Среднерыночная стоимость: {math.floor(arg_price)}  "+item['name']+f"\n"+item['lank']+f"\n"+item['parametrs']+f"\n"+item['mileage']+f"\n"+str(item['price'])+" \n"+item['description']+"\n"+item['location']
                await callback.message.answer(text=txt)
        else:
            await callback.message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу, измените процент отклонения от среднерыночной стоимости')
    await callback.answer()

# Вывод машин пользователя
@dp.message(Command("help"))
async def call(message:types.Message):
    user_id = message.from_user.id
    with db:
        obj = Control_db(6315832729)
        respons_re = obj.get_sefch_data_list()
        for item in respons_re:
            drand = revers_brand[item['brand_id']]
            rev_model = Get_revers_model()
            model_car = rev_model.get_data_select_car(str(item['brand_id']) +'/models')
            model = model_car[item['model_id']]
            percent_difference = item['percent_difference']
            # button_del = types.InlineKeyboardButton(text='Удалить', callback_data="car_"+str(item['id']))
            await message.answer(f"{drand, model, percent_difference, item['id']}")

async def main():
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
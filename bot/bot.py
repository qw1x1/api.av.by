import asyncio, math
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
#from config_reader import config
from bs4 import BeautifulSoup as bs
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Text, CommandObject, StateFilter
import json, io
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.storage.memory import MemoryStorage
from av1 import brand, Get_model, Pars_info_id_file,  Search_cars
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Inputdata(StatesGroup):
    prise=State()
    date=State()
    procent=State()


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
#bot = Bot(token=str(config.bot_token.get_secret_value()))
bot=Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
# Диспетчер
storage: MemoryStorage = MemoryStorage()
dp = Dispatcher(storage=storage)
user_data = {}

""" types.InlineKeyboardButton(text="<", callback_data="coice_back"),
types.InlineKeyboardButton(text="Подтвердить", callback_data="coice_coice"),
types.InlineKeyboardButton(text=">", callback_data="coice_forward")"""

builder, model = InlineKeyboardBuilder(), Get_model()
brand_car_id, model_car_id = '', ''


def list_add(cars:InlineKeyboardBuilder()):
    brand_cars=brand.items()
    for key, value in brand_cars:
        cars.adjust(3)
        cars.add(types.InlineKeyboardButton(text=key, callback_data="car_"+str(value)))

def NewKeyboard(cars:InlineKeyboardBuilder(), start:int,stop:int):
    new_cars=InlineKeyboardBuilder()
    new_cars._markup=cars._markup[start:stop]
    new_cars=new_cars.as_markup()
    new_cars.inline_keyboard.append([types.InlineKeyboardButton(text="<", callback_data="coice_back"),
types.InlineKeyboardButton(text="Подтвердить", callback_data="coice_coice"),
types.InlineKeyboardButton(text=">", callback_data="coice_forward")])
    return new_cars

#навигация брендов
async def new_page(message: types.Message, new_value: int):
    with suppress(TelegramBadRequest):
        await message.edit_text(f"Выберите бренд автомобиля: ",reply_markup=NewKeyboard(builder,(new_value*10)-10,new_value*10))

async def keyboard(message: types.Message, keybrd: InlineKeyboardBuilder,txt: str):
    with suppress(TelegramBadRequest):
        await message.answer(txt, reply_markup=keybrd.as_markup())

@dp.message(Command("start"))
async def call_backs(message: types.Message):
    model.user = message.from_user.id
    user_data[message.from_user.id] = 1
    list_add(builder)
    await message.answer("Выберите бренд автомобиля", reply_markup=NewKeyboard(builder,0,10))

@dp.callback_query(Text(startswith="coice_"))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 1)
    action = callback.data.split("_")[1]
    
    if action == "back":
        user_data[callback.from_user.id] = user_value-1
        await new_page(callback.message, user_value-1)
    elif action == "forward":
        user_data[callback.from_user.id] = user_value+1
        await new_page(callback.message, user_value+1)
    await callback.answer()

def api_call(list):
    model_list = InlineKeyboardBuilder()
    model_list._markup.clear()
    for key,value in list.items():
        model_list.adjust(3)
        model_list.add(types.InlineKeyboardButton(text=key, callback_data="model_"+str(value)))
    return model_list

@dp.callback_query(Text(startswith="car_"))
async def callbacks_cars(callback: types.CallbackQuery):
    action, model_car = callback.data.split("_")[1], {}
    global brand_car_id
    brand_car_id=action
    model_car=model.get_data_select_car(str(action) +'/models')
    models_keyboard = InlineKeyboardBuilder()
    models_keyboard._markup.clear()
    models_keyboard = api_call(model_car)

    await keyboard(callback.message,keybrd=models_keyboard,txt="Выберите марку авто:")
    await callback.answer()
price_date_procent_dict: dict[str, str, int] = {}

@dp.callback_query(Text(startswith="model_"))
async def callbacks_cars(callback: types.CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]
    global model_car_id
    model_car_id = action
    await callback.answer()
    ##########################
    #ТУТ БУДЕТ ВВОД ГОДА И ЦЕНЫ
    await callback.message.answer('Введите диапазон цен')
    await state.set_state(Inputdata.prise)
    ##########################

@dp.message(StateFilter(Inputdata.prise))
async def process_name_sent(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(text='Ввежите дату')
    await state.set_state(Inputdata.date)

@dp.message(StateFilter(Inputdata.date))
async def process_name_sent(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer(text='Ввежите процент')
    await state.set_state(Inputdata.procent)

@dp.message(StateFilter(Inputdata.procent))
async def process_name_sent(message: types.Message, state: FSMContext):
    await state.update_data(procent=message.text)
    price_date_procent_dict[message.from_user.id] = await state.get_data()
    # Завершаем машину состояний
    await state.clear()
    #await message.answer(text=F"{price_date_procent_dict[message.from_user.id]['price']} {price_date_procent_dict[message.from_user.id]['date']} {price_date_procent_dict[message.from_user.id]['procent']}")
    global brand_car_id, model_car_id
    price_min, price_max, year_min, year_max=0,0,0,0
    deviation_procent = 55
    price_min, price_max = price_date_procent_dict[message.from_user.id]['price'].split('-')[0],price_date_procent_dict[message.from_user.id]['price'].split('-')[1]
    year_min, year_max = price_date_procent_dict[message.from_user.id]['date'].split('-')[0],price_date_procent_dict[message.from_user.id]['date'].split('-')[1]
    deviation_procent = price_date_procent_dict[message.from_user.id]['procent']
    pars_info = Pars_info_id_file(brand_id=brand_car_id,model_id=model_car_id,
                                  year_max=year_max,year_min=year_min, 
                                  price_max=price_max,price_min=price_min)
    await message.answer(F"{price_min} {price_max} {year_min} {year_max}")
    cars_count_page = pars_info()
    if cars_count_page == 0:
        await message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу') 
    else:
        serch_cars_ekz = Search_cars(pars_info.car,pars_info.count_page, deviation_procent)
        serch_car = serch_cars_ekz()
        list_cars, arg_price = serch_car[0], serch_car[1]

        if len(list_cars) != 0:
            for item in list_cars:
                txt=f"Среднерыночная стоимость: {math.floor(arg_price)}  "+item['name']+f"\n"+item['lank']+f"\n"+item['parametrs']+f"\n"+item['mileage']+f"\n"+str(item['price'])+" \n"+item['description']+"\n"+item['location']
                await message.answer(text=txt)
        else:
            await message.answer(text='В настоящий момент нет ни одного объявления по Вашему запросу, измените процент отклонения от среднерыночной стоимости')
    
async def main():
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
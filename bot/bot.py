import asyncio
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
from av1 import brand, Get_model, Pars_info_id_file,  Search_cars


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
#bot = Bot(token=str(config.bot_token.get_secret_value()))
bot=Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
# Диспетчер
dp = Dispatcher()
user_data = {}
#command=[BotCommand(command="start",description="to start something"),BotCommand(command="stop", description="to stop something")]

#клавиатура выбора
def keyboard_coice():
    buttons = [
        types.InlineKeyboardButton(text="<", callback_data="coice_back"),
        types.InlineKeyboardButton(text="Подтвердить", callback_data="coice_coice"),
        types.InlineKeyboardButton(text=">", callback_data="coice_forward")
    ]    
    return buttons


builder = InlineKeyboardBuilder()
model = Get_model()
brand_car_id=""
model_car_id=""

#Клавиатура из 150 строк
def list_add():
    brand_cars=brand.items()
    cars=InlineKeyboardBuilder()
    for key, value in brand_cars:
        cars.adjust(3)
        cars.add(types.InlineKeyboardButton(
            text=key,
            callback_data="car_"+str(value))
            )
    return cars

#Клавиатура из 10 строк + клавиатура навигации
builder_new=InlineKeyboardBuilder()
def builder_sell(start: int):
    builder_old=list_add()
    stop=start*10 if (start*10<=len(builder_old._markup))else len(builder_old._markup)
    builder_new._markup=[]
    for i in range(stop-10,stop,1):
        builder_new._markup.append(builder_old._markup[i])
    builder_new._markup.append(keyboard_coice())
    return builder_new


#навигация брендов
async def new_page(message: types.Message, new_value: int):
    with suppress(TelegramBadRequest):
        await message.edit_text(
            f"Выберите бренд автомобиля: ",
            reply_markup=builder_sell(new_value).as_markup()
        )

async def keyboard(message: types.Message, keybrd: InlineKeyboardBuilder,txt: str):
    with suppress(TelegramBadRequest):
        await message.answer(
            txt,
            reply_markup=keybrd.as_markup()
        )
    


@dp.message(Command("start"))
async def call_backs(message: types.Message):
    model.user = message.from_user.id
    user_data[message.from_user.id] = 1
    builder = builder_sell(1)
    await message.answer(
        "Выберите бренд автомобиля",
        reply_markup=builder.as_markup()
    )
#свайп клавы
@dp.callback_query(Text(startswith="coice_"))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 1)
    action = callback.data.split("_")[1]
    

    if action == "back":
        user_data[callback.from_user.id] = user_value-1
        await new_page(callback.message, user_value-1)
    #elif action == "coice":
        #user_data[callback.from_user.id] = user_value-1
        #await new_page(callback.message, user_value-1)
    elif action == "forward":
        user_data[callback.from_user.id] = user_value+1
        await new_page(callback.message, user_value+1)

    await callback.answer()

cars=[
    [6,"80"],
    [6,"100"],
    [6,"A6"]
    ]

def api_call(list):
    #вызов api
    #obj.model_id = 
    model_list = InlineKeyboardBuilder()
    #model_list.add([value for key, value in cars.items() if key == model])
    for key,value in list.items():
            model_list.adjust(3)
            model_list.add(types.InlineKeyboardButton(
                text=key,
                callback_data="model_"+str(value))
                )
    return model_list
#передача выбранного бренда api + получение списка моделей
@dp.callback_query(Text(startswith="car_"))
async def callbacks_cars(callback: types.CallbackQuery):
    #user_value = user_data.get(callback.from_user.id, 1)
    action = callback.data.split("_")[1]
    global brand_car_id
    brand_car_id=action
    #await callback.message.answer(callback.data)
    model_car={}
    model_car=model.get_data_select_car(str(action) +'/models')
    models_keyboard=api_call(model_car)
    await keyboard(callback.message,keybrd=models_keyboard,txt="Выберите марку авто:")
    await callback.answer()

@dp.callback_query(Text(startswith="model_"))
async def callbacks_cars(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    global model_car_id
    model_car_id=action
    ##########################
    #ТУТ БУДЕТ ВВОД ГОДА И ЦЕНЫ
    ##########################
    global brand_car_id
    #pars_info=Pars_info_id_file(brand_id=int(brand_car_id),model_id=int(model_car_id))
    pars_info=Pars_info_id_file(brand_id=brand_car_id,model_id=model_car_id)
    cars_count_page=pars_info()
    serch_cars_ekz=Search_cars(pars_info.car,pars_info.count_page)
    list_cars=serch_cars_ekz()
    for item in list_cars:
        txt=f""+item['name']+" "+item['lank']+" "+item['parametrs']+" "+item['mileage']+" "+item['price']+" "+item['description']+" "+item['location']
        #item['name'], item['lank'], item['parametrs'], item['mileage'], item['price'], item['description'], item['location'], sep='\n'
        await callback.message.answer(text=txt)
    await callback.answer()


async def main():
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
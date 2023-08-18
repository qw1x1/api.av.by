import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
# from config_reader import config
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Text
import json, io
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
import api.av1 as av1
from api.av1 import Select_car, Pars_info_id_file, Search_cars


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8")
#bot=Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')
# Диспетчер
dp = Dispatcher()
user_data = {}
#command=[BotCommand(command="start",description="to start something"),BotCommand(command="stop", description="to stop something")]

   
# Хэндлер на команду /start
#@dp.message(Command("start"))
#async def cmd_start(message: types.Message):
    
#    await message.answer("Hello!")

#клавиатура выбора
def keyboard_coice():
    buttons = [
        types.InlineKeyboardButton(text="<", callback_data="coice_back"),
        types.InlineKeyboardButton(text="Подтвердить", callback_data="coice_coice"),
        types.InlineKeyboardButton(text=">", callback_data="coice_forward")
    ]    
    return buttons


brand_count=0
#Клавиатура из 150 строк
def list_add():
    brand=av1.brand.items()
    cars=InlineKeyboardBuilder()
    for key, value in brand:
        cars.adjust(3)
        cars.add(types.InlineKeyboardButton(
            text=key,
            callback_data="car_"+str(value))
            )
    brand_count=len(brand)
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
    
builder = InlineKeyboardBuilder()

@dp.message(Command("start"))
async def call_backs(message: types.Message):
    user_data[message.from_user.id] = 1
    builder = builder_sell(1)
    await message.answer(
        "Выберите бренд автомобиля",
        reply_markup=builder.as_markup()
    )

"""@dp.callback_query(Text(startswith=""))
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("ANUS")
    await callback.answer()"""
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
    for key in list:
                model_list.adjust(3)
                model_list.add(types.InlineKeyboardButton(
                    text=key[1],
                    callback_data=key[0])
                    )
    return model_list
#передача выбранного бренда api + получение списка моделей
@dp.callback_query(Text(startswith="car_"))
async def callbacks_cars(callback: types.CallbackQuery):
    #user_value = user_data.get(callback.from_user.id, 1)
    action = callback.data.split("_")[1]
    #await callback.message.answer(callback.data)
    obj=Select_car()
    obj.get_brand_id(int(action),av1.brand)
    obj.get_data_select_car(str(obj.brand_id) +'/models')
    models_keyboard=api_call(obj.model)
    await keyboard(callback.message,keybrd=models_keyboard,txt="Выберите марку авто:")
    await callback.answer()


async def main():
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Text
import json, io


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
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



#Клавиатура из 150 строк
def list_add():
    cars=InlineKeyboardBuilder()
    with io.open("brand.json",encoding='utf-8') as js_file:
        list=json.load(js_file)
        i=0
        for key, value in list.items():
            cars.adjust(3)
            cars.add(types.InlineKeyboardButton(
                text=key,
                callback_data=value)
                )
            i+=1
    return cars
#Клавиатура из 10 строк + клавиатура навигации
def builder_sell(start: int):
    builder_old=list_add()
    stop=start*10 if (start*10<=len(builder_old._markup))else len(builder_old._markup)
    builder_new=InlineKeyboardBuilder()
    for i in range(stop-10,stop,1):
        builder_new._markup.append(builder_old._markup[i])
    builder_new._markup.append(keyboard_coice())
    return builder_new

async def new_page(message: types.Message, new_value: int):
    await message.edit_text(
        f"Выберите бренд автомобиля: ",
        reply_markup=builder_sell(new_value).as_markup()
    )

    
# Запуск процесса поллинга новых апдейтов

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

async def main():
    await dp.start_polling(bot)
    
if __name__ ==  '__main__':
    asyncio.run(main())
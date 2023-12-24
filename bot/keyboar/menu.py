from aiogram import types

async def menu(message: types.Message):
    kb = [
            [
            types.KeyboardButton(text="Остановить поиск"),
            types.KeyboardButton(text="Продолжить поиск")
            ],
         ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Добро пожаловать в наш бот по поиску автомобилей",reply_markup=keyboard)
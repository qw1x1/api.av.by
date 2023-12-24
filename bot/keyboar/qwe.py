from aiogram import types
from aiogram import F


async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="1"),
            types.KeyboardButton(text="2")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("1. Поиск с процентом отклонения от среднерыночной стоимости.\n 2. Поиск конкретной марки автомобиля.", reply_markup=keyboard)
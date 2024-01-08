from aiogram import types
from aiogram import F


async def menu_perekup(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Изменение процента отклонения"),
            types.KeyboardButton(text="Выбор региона поиска"),
            types.KeyboardButton(text="Удаление выбранных городов")
        ],
        [
            types.KeyboardButton(text="Меню поиска")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Меню:", reply_markup=keyboard)
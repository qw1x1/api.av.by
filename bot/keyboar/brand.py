from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from settings import BRAND as brand
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

builder = InlineKeyboardBuilder()


def list_add(cars:InlineKeyboardBuilder()):
    brand_cars = brand.items()
    for key, value in brand_cars:
        cars.adjust(3)
        cars.add(types.InlineKeyboardButton(text=key, callback_data="car_"+str(value)))

def NewKeyboard(cars:InlineKeyboardBuilder(), start:int, stop:int):
    new_cars = InlineKeyboardBuilder()
    new_cars._markup = cars._markup[start:stop]
    new_cars = new_cars.as_markup()
    new_cars.inline_keyboard.append([types.InlineKeyboardButton(text="<", callback_data="coice_back"),
types.InlineKeyboardButton(text="Подтвердить", callback_data="coice_coice"),
types.InlineKeyboardButton(text=">", callback_data="coice_forward")])
    return new_cars

#навигация брендов
async def new_page(message:types.Message, new_value:int):
    with suppress(TelegramBadRequest):
        await message.edit_text(f"Выберите бренд автомобиля: ", reply_markup=NewKeyboard(builder, (new_value*10)-10, new_value*10))

from aiogram import Router, types
from aiogram.filters.command import Command
from api.models import *
from api.controls import get_sefch_data_list
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(Command("mycars"))
async def call(message:types.Message):
    global user_id
    user_id = message.from_user.id
    cars = InlineKeyboardBuilder()
    cars = cars.as_markup()
    get_sefch_data_list(user_id)

    

from aiogram import Router, F, types
from aiogram.filters.command import Command

import keyboar.brand as kb_brand

router = Router()
user_data = {}
brand={}


@router.message(Command("start"))
async def call_backs(message: types.Message):
    user_data[message.from_user.id] = 1
    brand[message.from_user.id] = 0
    kb_brand.list_add(kb_brand.builder)
    await message.answer("Выберите бренд автомобиля", reply_markup=kb_brand.NewKeyboard(kb_brand.builder, 0, 10))
from aiogram import Router, F, types
from aiogram.filters.command import Command
from av1 import brand, Get_model
import keyboar.brand as kb_brand


router = Router()

model = Get_model()

user_data = {}

@router.message(Command("start"))
async def call_backs(message: types.Message):
    model.user = message.from_user.id
    user_data[message.from_user.id] = 1
    kb_brand.list_add(kb_brand.builder)
    await message.answer("Выберите бренд автомобиля", reply_markup=kb_brand.NewKeyboard(kb_brand.builder,0,10))
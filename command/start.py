from aiogram import Router, F, types
from aiogram.filters.command import Command

import keyboar.start as kb_start

router = Router()
user_data = {}
brand={}
perekup={}
id_model = {}
procent ={}
id_gen={}


@router.message(Command("start"))
async def call_backs(message: types.Message):
    user_data[message.from_user.id] = 1
    brand[message.from_user.id] = 0
    perekup[message.from_user.id]=""
    id_model[message.from_user.id]=0
    procent[message.from_user.id]=0
    id_gen[message.from_user.id]=0
    await message.answer("Вы перекуп?", reply_markup=kb_start.key())

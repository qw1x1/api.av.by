from aiogram import Router, types
from aiogram.filters.command import Command
import keyboar.qwe as qwe

router=Router()
@router.message(Command("poisk"))
async def call_backs(message: types.Message):
    await qwe.cmd_start(message)
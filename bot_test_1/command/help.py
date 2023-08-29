from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("help"))
async def call_backs(message:types.Message):
    await message.answer("Помощ")
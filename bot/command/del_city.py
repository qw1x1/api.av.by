from aiogram import Router, types
from aiogram.filters.command import Command
from api.models import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
import command.start as Start
import keyboar.delete_city as kb_delcity
from api.controls import get_location_user as location

router = Router()

@router.message(Command("deletecity"))
async def call(message:types.Message):
    Start.del_city_bilder[message.from_user.id] = InlineKeyboardBuilder()
    city_user = location(message.from_user.id)
    await kb_delcity.keyboard(message, keybrd=Start.del_city_bilder[message.from_user.id], mass=city_user, txt="Выберите город который хотите удалить:")
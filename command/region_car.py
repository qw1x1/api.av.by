from aiogram import Router, F, types
from aiogram.filters.command import Command
from api.models import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
import command.start as Start
import keyboar.delete_city as kb_delcity
from api.controls import get_location_user as location
import keyboar.region as kb_region
from api.av1 import get_region

router = Router()

@router.message(Command("region"))
async def call(message:types.Message):
    id = message.from_user.id
    keyboard_reg=kb_region.api_call(get_region())
    await kb_region.keyboard(message,keyboard_reg,"Выберите область:")
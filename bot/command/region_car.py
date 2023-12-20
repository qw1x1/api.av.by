from aiogram import Router, types
from aiogram.filters.command import Command
from api.models import *
import keyboar.region as kb_region
from api.av1 import get_region

router = Router()

@router.message(Command("region"))
async def call(message:types.Message):
    id = message.from_user.id ###########################
    keyboard_reg = kb_region.api_call(get_region())
    await kb_region.keyboard(message,keyboard_reg, "Выберите область:")
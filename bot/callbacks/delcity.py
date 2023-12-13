from aiogram import Router, types
from aiogram.filters import Text
from api.models import *
import command.start as Start
import keyboar.delete_city as kb_city
from api.controls import change_location_user
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

router = Router()



@router.callback_query(Text(startswith="citydel_"))
async def callbacks_generation(callback:types.CallbackQuery):
    with suppress(TelegramBadRequest):
        action = callback.data.split("_")[1]
        masscity=Start.delet_city[callback.from_user.id]
        masscity.append(action)
        Start.delet_city[callback.from_user.id]=masscity
        change_location_user(callback.from_user.id,Start.delet_city[callback.from_user.id])
        Start.delet_city[callback.from_user.id]=[]
        await kb_city.new_keyboard(callback.message,action)
        await callback.answer()


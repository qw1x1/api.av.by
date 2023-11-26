from aiogram import Router, types
from aiogram.filters import Text
from api.models import *
import command.start as Start
from api.controls import change_location_user

router = Router()



@router.callback_query(Text(startswith="city_"))
async def callbacks_generation(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    if(action=="enter"):
        change_location_user(callback.from_user.id,Start.id_city[callback.from_user.id])
        await callback.message.answer("Вы успешно выбрали город(а) для поиска авто")
    else:
        masscity=Start.id_city[callback.from_user.id]
        masscity.append(action)
        Start.id_city[callback.from_user.id]=masscity
        await callback.answer()

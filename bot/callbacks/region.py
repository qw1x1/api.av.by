from aiogram import Router, types
from aiogram.filters import Text
from api.av1 import get_city_for_region
import keyboar.city as kb_city
from api.controls import create_request
from api.models import *
import command.start as Start
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()



@router.callback_query(Text(startswith="region_"))
async def callbacks_generation(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    Start.id_region[callback.from_user.id] = action
    #city_keyboard = kb_city.list_add((int(action)))
    Start.city_bilder[callback.message.from_user.id]=InlineKeyboardBuilder()
    await kb_city.keyboard(callback.message, keybrd=Start.city_bilder[callback.message.from_user.id],action=int(action), txt="Выберите город или несколько городов:")
    await callback.answer()

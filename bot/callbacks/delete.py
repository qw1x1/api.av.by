from aiogram import Router, types
from aiogram.filters import Text
from api.controls import delet_reqest
from command import mycars
from api.models import *

router = Router()

@router.callback_query(Text(startswith="delete_"))
async def callbacks_cars(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    user_id = mycars.user_id
    delet_reqest(user_id, int(action))
    await callback.message.answer("Авто удаленно из поиска", show_alert=True)
    await callback.answer()

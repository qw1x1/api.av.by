from aiogram import Router, types
from aiogram.filters import Text
from controls import Control_db
from command import all
from models import *

router = Router()

@router.callback_query(Text(startswith="delete_"))
async def callbacks_cars(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    user_id = all.user_id
    with db:
        obj = Control_db(user_id)
        obj._request_id = int(action) - 1
        obj.get_sefch_data_list()
        obj.delet_reqest()
    await callback.message.answer("Авто удаленно из поиска", show_alert=True)
    await all.call(callback.message)
    await callback.answer()

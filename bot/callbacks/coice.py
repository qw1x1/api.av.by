from aiogram import Router, F, types
import keyboar.brand as kb_brand
from aiogram.filters import Text
import command.start as Start

router = Router()

@router.callback_query(Text(startswith="coice_"))
async def callbacks_num(callback: types.CallbackQuery):
    user_value = Start.user_data.get(callback.from_user.id, 1)
    action = callback.data.split("_")[1]
    
    if action == "back":
        Start.user_data[callback.from_user.id] = user_value-1
        await kb_brand.new_page(callback.message, user_value-1)
    elif action == "forward":
        Start.user_data[callback.from_user.id] = user_value+1
        await kb_brand.new_page(callback.message, user_value+1)
    await callback.answer()
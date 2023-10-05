from aiogram import Router, types
import keyboar.model as kb_model
from aiogram.filters import Text
import command.start as Start
from aiogram.utils.keyboard import InlineKeyboardBuilder
from api.av1 import Get_model_or_generations

router = Router()

@router.callback_query(Text(startswith="car_"))
async def callbacks_cars(callback: types.CallbackQuery):
    action, model_car = callback.data.split("_")[1], {}
    Start.brand[callback.from_user.id] = action
    model_car = Get_model_or_generations(str(action) +'/models')
    models_keyboard = InlineKeyboardBuilder()
    models_keyboard._markup.clear()
    models_keyboard = kb_model.api_call(model_car)

    await kb_model.keyboard(callback.message, keybrd=models_keyboard, txt="Выберите марку авто:")
    await callback.answer()
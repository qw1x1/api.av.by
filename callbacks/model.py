from aiogram import Router, types
from aiogram.filters import Text
from api.av1 import Get_model_or_generations
import keyboar.generations as kb_gen
from api.controls import create_request
from api.models import *
import command.start as Start
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()



@router.callback_query(Text(startswith="model_"))
async def callbacks_generation(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    Start.id_model[callback.from_user.id] = action
    await callback.answer()
    generations_object=Get_model_or_generations(str(Start.brand[callback.from_user.id])+'/models/'+str(action)+'/generations/')
    generations_object()
    gen_keyboard = InlineKeyboardBuilder()
    gen_keyboard._markup.clear()
    gen_keyboard = kb_gen.api_call(generations_object.dikt)
    await kb_gen.keyboard(callback.message, keybrd=gen_keyboard, txt="Выберите поколение авто:")
    await callback.answer()

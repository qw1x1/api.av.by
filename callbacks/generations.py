from aiogram import Router, types
from aiogram.filters import Text
from api.av1 import Pars_info_id_file, Search_cars,Get_model_or_generations
import math
from api.controls import create_request
from api.models import *
import command.start as Start
import callbacks.model as Model


router = Router()



@router.callback_query(Text(startswith="gen_"))
async def callbacks_cars(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    Start.id_gen[callback.from_user.id] = action
   
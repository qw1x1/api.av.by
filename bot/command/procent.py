from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from aiogram.filters import Text
from callbacks.perekup import Inputdata
from aiogram.filters.command import Command
import api.controls as Controls
from api.models import *
import command.start as Start
router = Router()

@router.message(Command("procent"))
async def callbacks_cars(message: types.Message, state:FSMContext):
    await message.answer('Введите процент отклонения от среднерыночной цены')
    await state.set_state(Inputdata.procent)
    Controls.add_procent_user(int(message.from_user.id),percent=int(Start.procent[message.from_user.id]['procent']))
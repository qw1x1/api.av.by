from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from callbacks.perekup import Inputdata
from aiogram.filters.command import Command
from api.models import *
from aiogram.fsm.state import State, StatesGroup
router = Router()

class Inputdata(StatesGroup):
    procent_state = State()

@router.message(Command("procent"))
async def callbacks_cars(message:types.Message, state:FSMContext):
    await message.answer('Введите процент отклонения от среднерыночной цены')
    await state.set_state(Inputdata.procent_state)

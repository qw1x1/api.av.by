from aiogram import Router, types
from aiogram.filters import Text
import api.controls as controls
from command.start import perekup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
router = Router()

class Inputdata(StatesGroup):
    procent = State()

@router.callback_query(Text(startswith="perekup_"))
async def callbacks_cars(callback: types.CallbackQuery, state:FSMContext):
    action = callback.data.split("_")[1]
    if action=="yes":
        controls.create_user(callback.from_user.id)
        perekup[callback.from_user.id]=action
        await callback.message.answer('Введите процент отклонения от среднерыночной цены')
        await state.set_state(Inputdata.procent)
        await callback.answer()
    elif action=="no":
        controls.create_user(callback.from_user.id)
        perekup[callback.from_user.id]=action
        await callback.message.answer("Введите команду /addcars")
        await callback.answer()
    

async def perekup_yes():
    ...

async def perekup_no():
    ...
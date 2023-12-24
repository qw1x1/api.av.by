from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import command.start as start

router = Router()

@router.message(StateFilter(start.Inputdata.perekup_state))
async def process_name_sent(message:types.Message, state:FSMContext):
    await state.update_data(date=message.text)
    await message.answer(text='Введите процент')
    #await state.set_state(cb_model.Inputdata.procent)
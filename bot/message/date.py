from aiogram import Router, types

from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import callbacks.model as cb_model

router = Router()

@router.message(StateFilter(cb_model.Inputdata.prise))
async def process_name_sent(message:types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(text='Введите диапозон дат')
    await state.set_state(cb_model.Inputdata.date)
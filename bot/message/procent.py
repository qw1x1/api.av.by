from aiogram import Router, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import callbacks.model as cb_model

router = Router()

@router.message(StateFilter(cb_model.Inputdata.date))
async def process_name_sent(message:types.Message, state:FSMContext):
    try:
        date_min=int(message.text.split('-')[0])
        date_max=int(message.text.split('-')[1])
        if date_max<=date_min:
            a=10/0
        await state.update_data(date=message.text)
        await message.answer(text='Введите процент отклонения цены')
        await state.set_state(cb_model.Inputdata.procent)
    except:
        await message.answer(text='Введенны не корректные данные')
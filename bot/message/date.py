from aiogram import Router, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import callbacks.model as cb_model

router = Router()

@router.message(StateFilter(cb_model.Inputdata.prise))
async def process_name_sent(message: types.Message, state: FSMContext):
    try:
        price_min=int(message.text.split('-')[0])
        price_max=int(message.text.split('-')[1])
        if price_max<=price_min:
            a=10/0
        await state.update_data(price=message.text)
        await message.answer(text='Введите год (мин. год - макс. год)')
        await state.set_state(cb_model.Inputdata.date)
    except:
        await message.answer(text='Введенны не корректные данные')
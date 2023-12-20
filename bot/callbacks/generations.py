from aiogram import Router, types
from aiogram.filters import Text
import command.start as Start
from aiogram.fsm.context import FSMContext
import callbacks.perekup as perekup

router = Router()

@router.callback_query(Text(startswith="gen_"))
async def callbacks_cars(callback:types.CallbackQuery, state:FSMContext):
    action = callback.data.split("_")[1]
    Start.id_gen[callback.from_user.id] = action
    await callback.message.answer('Введите процент отклонения от среднерыночной цены')
    await state.set_state(perekup.Inputdata.procent)
    await callback.answer()
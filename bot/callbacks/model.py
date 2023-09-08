from aiogram import Router, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import command.start as Start

router = Router()

class Inputdata(StatesGroup):
    prise = State()
    date = State()
    procent = State()

id_model = {}

@router.callback_query(Text(startswith="model_"))
async def callbacks_cars(callback:types.CallbackQuery, state:FSMContext):
    action = callback.data.split("_")[1]
    id_model[callback.from_user.id] = action
    await callback.answer()
    await callback.message.answer('Введите диапазон цен')
    await state.set_state(Inputdata.prise)
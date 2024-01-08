from aiogram import Router, types,F
from aiogram.fsm.context import FSMContext
import command.start as start
from keyboar.sell_key import key
from api.controls import get_subscription_status

router = Router()

@router.message(start.Inputdata.perekup_state, F.text.in_(start.perekup_key))
async def perekup_qwe(message: types.Message, state: FSMContext):
    await state.update_data(perekup=message.text.lower())
    yes_or_no = await state.get_data()
   # if(start.perekup[message.from_user.id]['perekup']=='yes'):
    if(yes_or_no['perekup']=='1'):
        if(get_subscription_status(message.from_user.id)==0):
            await message.answer('Купите подписку:',reply_markup=key())
        else:
            start.perekup[message.from_user.id]='yes'
            await message.answer(text="Введите процент отклонения от среднерыночной цены",reply_markup=types.ReplyKeyboardRemove())
            await state.set_state(start.Inputdata.procent_state)
    elif(yes_or_no['perekup']=='2'):
        start.perekup[message.from_user.id]='no'
        await message.answer("Введите команду /addcars",reply_markup=types.ReplyKeyboardRemove())
        state.clear()

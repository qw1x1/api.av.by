from aiogram import Router, types,F
from aiogram.fsm.context import FSMContext
import command.start as start
from api.controls import set_is_active

router = Router()

@router.message(start.Inputdata.menu, F.text.in_(start.menu_key))
async def menu_qwe(message: types.Message, state: FSMContext):
    await state.update_data(posik=message.text.lower())
    poisk = await state.get_data()
    if(poisk['posik']=='остановить поиск'):
        set_is_active(message.from_user.id,0)
        await state.set_state(start.Inputdata.menu)
        #await state.clear()
    elif(poisk['posik']=='продолжить поиск'):
        set_is_active(message.from_user.id,1)
        await state.set_state(start.Inputdata.menu)
        #await state.clear()
        
@router.message(F.text.lower() == "изменение процента отклонения")
async def procent(message: types.Message):
    await message.answer('Введите /procent')

@router.message(F.text.lower() == "выбор региона поиска")
async def procent(message: types.Message):
    await message.answer('Введите /region')

@router.message(F.text.lower() == "удаление выбранных городов")
async def procent(message: types.Message):
    await message.answer('Введите /deletecity')

@router.message(F.text.lower() == "меню поиска")
async def procent(message: types.Message):
    await message.answer('Введите /poisk')
from aiogram import Router, types
from aiogram.filters.command import Command
import keyboar.menu_perekup as kb_menu
from aiogram.fsm.context import FSMContext
import command.start as Start


router = Router()

@router.message(Command("menu"))
async def call_backs(message: types.Message):
    #await state.set_state(Start.Inputdata.menu)
    await kb_menu.menu_perekup(message)
    
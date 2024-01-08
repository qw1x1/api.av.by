from aiogram import Router, types
from aiogram.filters.command import Command
#import keyboar.start as kb_start
from api.controls import create_user
import keyboar.qwe as qwe
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

class Inputdata(StatesGroup):
    perekup_state = State()
    procent_state = State()
    menu = State()

perekup_key=['1','2']
menu_key=["Остановить поиск", "Продолжить поиск"]
user_data = {}
brand = {}
perekup = {}
id_model = {}
procent = {}
id_gen = {}
id_region = {}
id_city = {}
city_bilder = {}
delet_city = {}
del_city_bilder = {}

@router.message(Command("start"))
async def call_backs(message: types.Message, state: FSMContext):
    user_data[message.from_user.id] = 1
    brand[message.from_user.id] = 0
    perekup[message.from_user.id] = ""
    id_model[message.from_user.id] = 0
    procent[message.from_user.id] = 0
    id_gen[message.from_user.id] = 0
    id_region[message.from_user.id] = 0
    id_city[message.from_user.id] = []
    city_bilder[message.from_user.id] = 0
    delet_city[message.from_user.id] = []
    del_city_bilder[message.from_user.id] = 0
    await qwe.cmd_start(message)
    create_user(message.from_user.id)
    #await message.answer("Выберите подходящий для Вас поиск авто:", reply_markup=kb_start.key())
    await state.set_state(Inputdata.perekup_state)


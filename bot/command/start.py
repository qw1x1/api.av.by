from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import keyboar.start as kb_start
#?from bot import bot

router = Router()
user_data = {}
brand={}
perekup={}
id_model = {}
procent ={}
id_gen={}
id_region={}
id_city={}
city_bilder={}
delet_city={}
del_city_bilder={}

# bot = Bot(token='6315832729:AAGC6fYoRIo6QQH595zsXjgN2pZorwvDGi8')

# id = 633279160
# async def send_msg(id: int, message: str):
#     ...
#     await bot.send_message(id, message)

@router.message(Command("start"))
async def call_backs(message:types.Message):
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
    await message.answer("Вы перекуп?", reply_markup=kb_start.key())


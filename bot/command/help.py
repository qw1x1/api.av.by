from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("help"))
async def call_backs(message:types.Message):
    help = f"СПРАВКА:"f"\n"
    data = f"Для того чтобы задать диапозон дат введите даты в формате 2001-2004"f"\n"
    price = f"Для того чтобы задать диапозон цен введите цены в формате 100-2000"f"\n"
    procent = f"Процент отклонения от среднерыночной стоимости, это на сколько процентов меньше относительно среднерыночной стоимости, будут побдираться для вас авто"f"\n"
    txt = f"{help}"f"\n" + f"{data}"f"\n" + f"{price}"f"\n" + f"{procent}"
    await message.answer(text=txt)
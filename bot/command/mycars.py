from aiogram import Router, F, types
from aiogram.filters.command import Command
from api.models import *
from api.update import Get_data_for_request
from api.controls import Control_db
from api.av1 import revers_brand, Get_revers_model
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(Command("mycars"))
async def call(message:types.Message):
    global user_id
    user_id = message.from_user.id
    cars = InlineKeyboardBuilder()
    cars = cars.as_markup()
    
    with db:
        obj = Control_db(user_id)
        obj.create_user()
        respons_re = obj.get_sefch_data_list()
        if len(respons_re) == 0:
            await message.answer(f'Вы еще не выбрaли ни одного авто')
        else:
            await message.answer("Ваши авто:")
            for item in respons_re:
                drand = revers_brand[item['brand_id']]
                rev_model = Get_revers_model()
                model_car = rev_model.get_data_select_car(str(item['brand_id']) +'/models')
                model = model_car[item['model_id']]
                percent_difference = item['percent_difference']
                cars.inline_keyboard.clear()
                button_del = types.InlineKeyboardButton(text='Удалить', callback_data=f"delete_{item['id']}")
                cars.inline_keyboard.append([button_del])
                await message.answer(f"{drand} {model} Цена: {item['price_min']} - {item['price_max']} Год: {item['year_min']} - {item['year_max']} Процент: {percent_difference}", reply_markup=cars)

    

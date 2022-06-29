from aiogram import types

from data.config import temp, courses, update_courses
from keyboards.inline.all_kb import complete_converter_kb


async def create_order(message):
    update_courses()
    user_id = message.from_user.id
    exchange_rate = float(courses['Courses'][temp[user_id]["type"]])
    amount_give = temp[user_id]["amount_give"]
    amount_recieve = amount_give * exchange_rate
    temp[user_id]["amount_recieve"] = amount_recieve
    temp[user_id]["exchange_rate"] = exchange_rate
    t_give, t_recieve = temp[user_id]["type"].split('/')
    temp[user_id]["label_give"] = t_give
    temp[user_id]["label_recieve"] = t_recieve

    await message.answer(
        text=f'{temp[user_id]["type"]}\n\n' \
             f'Курс обмена: {temp[user_id]["exchange_rate"]}\n'
             f'Вы внесёте: {temp[user_id]["amount_give"]} {t_give}\n'
             f'Вы получите: {temp[user_id]["amount_recieve"]} {t_recieve}\n\n'
             f'Внесение: {temp[user_id]["way_to_give"]}\n'
             f'Получение: {temp[user_id]["way_to_recieve"]}\n\n'
             f'Отправить заявку на обмен? '
             f'(необходимо отправить телефонный номер)',
        reply_markup=complete_converter_kb())


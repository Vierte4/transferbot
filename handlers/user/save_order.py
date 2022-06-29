import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import temp, channel_new
from keyboards.default import user_main_keyboard
from keyboards.inline.operators_kb import new_order
from loader import connection, dp, bot
from utils.manage_db import insert_data


@dp.message_handler(content_types=['contact'], state='*')
async def save_order_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    try:
        await state.finish()
    except:
        return
    label_give = temp[user_id]["label_give"]
    label_recieve = temp[user_id]["label_recieve"]

    contact = message.contact
    created_time = datetime.datetime.now()
    id = insert_data(
        connection=connection,
        fullname=message.from_user.full_name,
        user_id=contact.user_id,
        telephone=contact.phone_number,
        username=message.from_user.username,
        label_give=label_give,
        label_recieve=label_recieve,
        amount_give=temp[user_id]['amount_give'],
        amount_recieve=temp[user_id]['amount_recieve'],
        exchange_rate=temp[user_id]['exchange_rate'],
        way_to_give=temp[user_id]['way_to_give'],
        way_to_recieve=temp[user_id]['way_to_recieve'],
        status='В ожидании',
        created_time=created_time.strftime('%Y-%m-%d %H:%M:%S')
    )

    link = f'@{message.from_user.username}' if message.from_user.username \
        else f'https://web.telegram.org/z/#{user_id}'

    await message.answer(text='Для проведения операции перевода в ближайшее '
                              'время с вами свяжется наш оператор. \n'
                              'Спасибо, что выбрали нас!',
                         reply_markup=user_main_keyboard)

    await bot.send_message(chat_id=channel_new,
                           text=f'id: {id}\n'
                                f'Тип заявки: {temp[user_id]["type"]}\n'
                                f'ФИО: {message.from_user.full_name}\n'
                                f'Номер телефона: {contact.phone_number}\n'
                                f'Способ передачи: {temp[user_id]["way_to_give"]}\n'
                                f'Способ получения: {temp[user_id]["way_to_recieve"]}\n'
                                f'Курс: {temp[user_id]["exchange_rate"]}\n'
                                f'Отдаёт: {temp[user_id]["amount_give"]} {label_give}\n'
                                f'Получает: {temp[user_id]["amount_recieve"]} {label_recieve}\n'
                                f'Заказчик: {link}\n'
                                f'Создано: {created_time.strftime("%d-%m-%Y %H:%M:%S")}',
                           reply_markup=new_order(id))
    temp.pop(user_id)
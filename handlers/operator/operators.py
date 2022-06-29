from aiogram import types

from data.config import channel_new, channel_process, channel_done, \
    channel_trash
from keyboards.inline.operators_kb import new_order, new_order_collback, \
    in_process, in_process_collback, completed_order, deleted_order, \
    completed_order_collback, deleted_order_collback
from loader import connection, dp, bot
from utils.manage_db import start_work, complete_order_bd


@dp.callback_query_handler(new_order_collback.filter())
async def new_order_handler(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('answer')
    id = callback_data.get('id')
    message_txt = call.message.text + f'\nОтветственный: {call.from_user.full_name}'
    if answer == '0':
        start_work(connection=connection, id=id, user=call.from_user)
        await bot.send_message(chat_id=channel_process,
                               text=message_txt,
                               reply_markup=in_process(id))
        await call.message.delete()
    else:
        start_work(connection=connection, id=id, user=call.from_user,
                   status='Удалён')
        await bot.send_message(chat_id=channel_process,
                               text=message_txt,
                               reply_markup=channel_trash(id))
        await call.message.delete()


@dp.callback_query_handler(in_process_collback.filter())
async def process_order_handler(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('answer')
    id = callback_data.get('id')
    message_txt = call.message.text
    if answer == '0':
        complete_order_bd(connection=connection, id=id, status='Готово',
                          operator_id=call.from_user.id)
        await bot.send_message(chat_id=channel_done,
                               text=message_txt,
                               reply_markup=completed_order(id))
        await call.message.delete()
    elif answer == '1':
        complete_order_bd(connection=connection, id=id, status='Вернулась',
                          operator_id=call.from_user.id)
        await bot.send_message(chat_id=channel_new,
                               text=message_txt,
                               reply_markup=new_order(id))
        await call.message.delete()
    elif answer == '2':
        complete_order_bd(connection=connection, id=id, status='Удалена',
                          operator_id=call.from_user.id)
        await bot.send_message(chat_id=channel_trash,
                               text=message_txt,
                               reply_markup=deleted_order(id))
        await call.message.delete()


@dp.callback_query_handler(completed_order_collback.filter())
async def completed_order_handler(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('answer')
    id = callback_data.get('id')
    message_txt = call.message.text
    if answer == '0':
        complete_order_bd(connection=connection, id=id, status='В обработке',
                          operator_id=call.from_user.id)
        await bot.send_message(chat_id=channel_process,
                               text=message_txt,
                               reply_markup=completed_order(id))
        await call.message.delete()
    else:
        complete_order_bd(connection=connection, id=id, status='Удалена',
                          operator_id=call.from_user.id)
        await bot.send_message(chat_id=channel_trash,
                               text=message_txt,
                               reply_markup=deleted_order(id))
        await call.message.delete()


@dp.callback_query_handler(deleted_order_collback.filter())
async def deleted_order_handler(call: types.CallbackQuery, callback_data: dict):
    id = callback_data.get('id')
    message_txt = call.message.text
    complete_order_bd(connection=connection, id=id, status='В обработке',
                      operator_id=call.from_user.id)
    await bot.send_message(chat_id=channel_process,
                           text=message_txt,
                           reply_markup=in_process(id))
    await call.message.delete()

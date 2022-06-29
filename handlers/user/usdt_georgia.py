from aiogram import types

from data.config import temp, georgia_transfer, georgia_transfer_list
from keyboards.inline.exchange_kb import georgia_transfer_callback
from loader import dp
from states.all_state import geo_usdt_state, usdt_geo_state
from utils.create_order import create_order


# GEO -> USDT
@dp.callback_query_handler(georgia_transfer_callback.filter(),
                           state=geo_usdt_state.default)
async def send_amount_handler(call: types.CallbackQuery, callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = georgia_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] = f'USDT/{georgia_transfer[answer][0]}'
    temp[call.from_user.id]['way_to_give'] = georgia_transfer[answer][1]
    temp[call.from_user.id]['way_to_recieve'] = 'Перевод на кошелёк'

    await call.message.answer(text='Какую сумму хотите обменять?')
    await geo_usdt_state.amount.set()


@dp.message_handler(state=geo_usdt_state.amount)
async def send_order_handler(message: types.Message):
    try:
        amount_give = float(message.text.replace(' ', '').replace(',', '.'))
        temp[message.from_user.id]['amount_give'] = amount_give
        await create_order(message)

    except Exception as e:
        await message.answer('Пожалуйста, отправьте в сообщении только число,'
                             'без букв, пробелов и специальных символов')


# USDT -> GEO
@dp.callback_query_handler(georgia_transfer_callback.filter(),
                           state=usdt_geo_state.default)
async def send_amount_handler(call: types.CallbackQuery, callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = georgia_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] = f'USDT/{georgia_transfer[answer][0]}'
    temp[call.from_user.id]['way_to_recieve'] = georgia_transfer[answer][1]
    temp[call.from_user.id]['way_to_give'] = 'Перевод на кошелёк'

    await call.message.answer(text='Какую сумму хотите обменять?')
    await usdt_geo_state.amount.set()


@dp.message_handler(state=usdt_geo_state.amount)
async def send_order_handler(message: types.Message):
    try:
        amount_give = float(message.text.replace(' ', '').replace(',', '.'))
        temp[message.from_user.id]['amount_give'] = amount_give
        await create_order(message)

    except Exception as e:
        await message.answer('Пожалуйста, отправьте в сообщении только число,'
                             'без букв, пробелов и специальных символов')

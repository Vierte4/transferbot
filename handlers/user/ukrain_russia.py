from aiogram import types

from data.config import temp, russia_transfer, russia_transfer_list, \
    ukrain_transfer, ukrain_transfer_list
from keyboards.inline.exchange_kb import ukrain_transfer_callback, \
    russia_transfer_kb, russia_transfer_callback, ukrain_transfer_kb
from loader import dp
from states.all_state import ua_ru_state, ru_ua_state
from utils.create_order import create_order


# Ukrain -> Russia
@dp.callback_query_handler(ukrain_transfer_callback.filter(),
                           state=ua_ru_state.default)
async def choose_way_to_get_handler(call: types.CallbackQuery,
                                    callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = ukrain_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] = ukrain_transfer[answer][0]
    temp[call.from_user.id]['way_to_give'] = ukrain_transfer[answer][1]

    await call.message.answer(text='Как получаете деньги в Грузии?',
                              reply_markup=russia_transfer_kb())


@dp.callback_query_handler(russia_transfer_callback.filter(),
                           state=ua_ru_state.default)
async def send_amount_handler(call: types.CallbackQuery, callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = russia_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] += f'/{russia_transfer[answer][0]}'
    temp[call.from_user.id]['way_to_recieve'] = russia_transfer[answer][1]

    await call.message.answer(text='Какую сумму хотите обменять?')
    await ua_ru_state.amount.set()


@dp.message_handler(state=ua_ru_state.amount)
async def create_order_handler(message: types.Message):
    try:
        amount_give = float(message.text.replace(' ', '').replace(',', '.'))
        temp[message.from_user.id]['amount_give'] = amount_give
        await create_order(message)

    except Exception as e:
        await message.answer('Пожалуйста, отправьте в сообщении только число,'
                             'без букв, пробелов и специальных символов')


# Russia -> Ukrain
@dp.callback_query_handler(russia_transfer_callback.filter(),
                           state=ru_ua_state.default)
async def send_amount_handler(call: types.CallbackQuery, callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = russia_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] = russia_transfer[answer][0]
    temp[call.from_user.id]['way_to_give'] = russia_transfer[answer][1]

    await call.message.answer(text='Как получаете деньги в Украине?',
                              reply_markup=ukrain_transfer_kb())


@dp.callback_query_handler(ukrain_transfer_callback.filter(),
                           state=ru_ua_state.default)
async def choose_way_to_get_handler(call: types.CallbackQuery,
                                    callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = ukrain_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] += f'/{ukrain_transfer[answer][0]}'
    temp[call.from_user.id]['way_to_recieve'] = ukrain_transfer[answer][1]

    await call.message.answer(text='Какую сумму хотите обменять?')
    await ru_ua_state.amount.set()


@dp.message_handler(state=ru_ua_state.amount)
async def create_order_handler(message: types.Message):
    try:
        amount_give = float(message.text.replace(' ', '').replace(',', '.'))
        temp[message.from_user.id]['amount_give'] = amount_give
        await create_order(message)

    except Exception as e:
        await message.answer('Пожалуйста, отправьте в сообщении только число,'
                             'без букв, пробелов и специальных символов')

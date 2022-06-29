from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import temp, georgia_transfer, georgia_transfer_list, \
    russia_transfer, \
    russia_transfer_list
from keyboards.inline.exchange_kb import russia_transfer_callback, \
    georgia_transfer_kb, \
    georgia_transfer_callback, russia_transfer_kb
from loader import dp
from states.all_state import ru_geo_state, \
    geo_ru_state
from utils.create_order import create_order


# Russia -> Georgia
@dp.callback_query_handler(russia_transfer_callback.filter(),
                           state=ru_geo_state.default)
async def choose_way_to_get_handler(call: types.CallbackQuery,
                                    callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = russia_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] = russia_transfer[answer][0]
    temp[call.from_user.id]['way_to_give'] = russia_transfer[answer][1]

    await call.message.answer(text='Как получаете деньги в Грузии?',
                              reply_markup=georgia_transfer_kb())


@dp.callback_query_handler(georgia_transfer_callback.filter(),
                           state=ru_geo_state.default)
async def send_amount_handler(call: types.CallbackQuery, callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = georgia_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] += f'/{georgia_transfer[answer][0]}'
    temp[call.from_user.id]['way_to_recieve'] = georgia_transfer[answer][1]

    await call.message.answer(text='Какую сумму хотите обменять?')
    await ru_geo_state.amount.set()


@dp.message_handler(state=ru_geo_state.amount)
async def create_order_handler(message: types.Message):
    try:
        amount_give = float(message.text.replace(' ', '').replace(',', '.'))
        temp[message.from_user.id]['amount_give'] = amount_give
        await create_order(message)

    except Exception as e:
        print(e)
        await message.answer('Пожалуйста, отправьте в сообщении только число,'
                             'без букв, пробелов и специальных символов')


# Georgia -> Russia
@dp.callback_query_handler(georgia_transfer_callback.filter(),
                           state=geo_ru_state.default)
async def send_amount_handler(call: types.CallbackQuery, callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = georgia_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] = georgia_transfer[answer][0]
    temp[call.from_user.id]['way_to_give'] = georgia_transfer[answer][1]

    await call.message.answer(text='Как получаете деньги в Украине?',
                              reply_markup=russia_transfer_kb())


@dp.callback_query_handler(russia_transfer_callback.filter(),
                           state=geo_ru_state.default)
async def choose_way_to_get_handler(call: types.CallbackQuery,
                                    callback_data: dict):
    answer_n = callback_data.get('answer')
    answer = russia_transfer_list[int(answer_n)]
    temp[call.from_user.id]['type'] += f'/{russia_transfer[answer][0]}'
    temp[call.from_user.id]['way_to_recieve'] = russia_transfer[answer][1]

    await call.message.answer(text='Какую сумму хотите обменять?')
    await geo_ru_state.amount.set()


@dp.message_handler(state=geo_ru_state.amount)
async def create_order_handler(message: types.Message):
    try:
        amount_give = float(message.text.replace(' ', '').replace(',', '.'))
        temp[message.from_user.id]['amount_give'] = amount_give
        await create_order(message)

    except Exception as e:
        await message.answer('Пожалуйста, отправьте в сообщении только число,'
                             'без букв, пробелов и специальных символов')

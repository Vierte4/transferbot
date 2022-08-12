from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import temp
from keyboards.default import user_main_keyboard
from keyboards.inline.exchange_kb import russia_transfer_kb, \
    georgia_transfer_kb, ukrain_transfer_kb
from loader import dp
from states.all_state import ru_geo_state, geo_ru_state, geo_usdt_state, \
    usdt_geo_state, geo_ua_state, ua_geo_state, ru_ua_state, ua_ru_state


@dp.message_handler(commands='Start', state='*')
async def start_comand_handler(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!",
                         reply_markup=user_main_keyboard)


@dp.message_handler(text='🇷🇺 Россия —>\n🇬🇪 Грузия', state='*')
async def russia_georgia_handler(message: types.Message, state: FSMContext):
    temp[message.from_user.id] = {'type': 'RUB'}
    await message.answer(text='Как переводите рубли?',
                         reply_markup=russia_transfer_kb())
    await ru_geo_state.default.set()


@dp.message_handler(text='🇬🇪 Грузия —>\n🇷🇺 Россия', state='*')
async def georgia_russia_handler(message: types.Message, state: FSMContext):
    temp[message.from_user.id] = {'type': 'RUB'}
    await message.answer(text='Как переводите деньги в Грузии?',
                         reply_markup=georgia_transfer_kb())
    await geo_ru_state.default.set()


@dp.message_handler(text='🇺🇦 Украина —>\n🇷🇺 Россия', state='*')
async def georgia_ukrain_handler(message: types.Message, state: FSMContext):
    temp[message.from_user.id] = {'type': 'RUB'}
    await message.answer(text='Как переводите деньги в Украине?',
                         reply_markup=ukrain_transfer_kb())
    await ua_ru_state.default.set()

@dp.message_handler(text='🇷🇺 Россия —>\n🇺🇦 Украина', state='*')
async def georgia_ukrain_handler(message: types.Message, state: FSMContext):
    temp[message.from_user.id] = {'type': 'RUB'}
    await message.answer(text='Как переводите деньги в России?',
                         reply_markup=russia_transfer_kb())
    await ru_ua_state.default.set()


@dp.message_handler(text='🇺🇦 Украина —>\n🇬🇪 Грузия', state='*')
async def georgia_ukrain_handler(message: types.Message, state: FSMContext):
    temp[message.from_user.id] = {'type': 'RUB'}
    await message.answer(text='Как переводите деньги в Украине?',
                         reply_markup=ukrain_transfer_kb())
    await ua_geo_state.default.set()


@dp.message_handler(text='🇬🇪 Грузия —>\n🇺🇦 Украина', state='*')
async def georgia_ukrain_handler(message: types.Message, state: FSMContext):
    temp[message.from_user.id] = {'type': 'RUB'}
    await message.answer(text='Как переводите деньги в Грузии?',
                         reply_markup=georgia_transfer_kb())
    await geo_ua_state.default.set()


@dp.message_handler(text='Покупка USDT в 🇬🇪 Грузии', state='*')
async def usdt_georgia_handler(message: types.Message, state: FSMContext):
    temp[message.from_user.id] = {'type': 'RUB'}
    await message.answer(text='Как переводите деньги в Грузии?',
                         reply_markup=georgia_transfer_kb())
    await geo_usdt_state.default.set()
    

@dp.message_handler(text='Продажа USDT в 🇬🇪 Грузии', state='*')
async def usdt_georgia_handler(message: types.Message, state: FSMContext):
    temp[message.from_user.id] = {'type': 'RUB'}
    await message.answer(text='Как получаете деньги в Грузии?',
                         reply_markup=georgia_transfer_kb())
    await usdt_geo_state.default.set()


@dp.message_handler(text='Главное меню',
                    state='*')
async def return_menu_handler(message: types.Message, state: FSMContext):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!",
                         reply_markup=user_main_keyboard)
    try:
        await state.finish()
    except:
        pass


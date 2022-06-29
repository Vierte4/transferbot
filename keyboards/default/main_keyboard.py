from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇷🇺 Россия —>\n🇬🇪 Грузия'),
            KeyboardButton(text='🇬🇪 Грузия —>\n🇷🇺 Россия'),
        ],
        [
            KeyboardButton(text='🇬🇪 Грузия —>\n🇺🇦 Украина'),
            KeyboardButton(text='🇺🇦 Украина —>\n🇬🇪 Грузия'),
        ],
        [
            KeyboardButton(text='🇷🇺 Россия —>\n🇺🇦 Украина'),
            KeyboardButton(text='🇺🇦 Украина —>\n🇷🇺 Россия'),
        ],
        [
            KeyboardButton(text='Покупка USDT в 🇬🇪 Грузии'),
            KeyboardButton(text='Продажа USDT в 🇬🇪 Грузии'),
        ],

    ],
    resize_keyboard=True
)

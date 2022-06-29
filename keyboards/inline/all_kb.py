from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup

def complete_converter_kb():
    kb = ReplyKeyboardMarkup()

    kb.add(
        InlineKeyboardButton(
            text='Оставить заявку',
            request_contact=True
        )

    )
    kb.add(
        InlineKeyboardButton(
            text=f'Главное меню'
        )
    )

    return kb

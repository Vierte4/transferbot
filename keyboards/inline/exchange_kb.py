from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from data.config import russia_transfer_list, georgia_transfer_list, \
    ukrain_transfer_list

georgia_transfer_callback = CallbackData("georgia_transfer", "answer")
russia_transfer_callback = CallbackData("russia_transfer", "answer")
ukrain_transfer_callback = CallbackData("ukrain_transfer", "answer")
choose_wallet_callback = CallbackData('choose_wallet', 'answe r')
choose_currencies_callback = CallbackData('choose_currencies', 'answer')
ways_to_recieve_exch2_callback = CallbackData('ways_to_recieve_exch2', 'answer')
converter_callback = CallbackData('converter', 'answer')


def russia_transfer_kb():
    kb = InlineKeyboardMarkup()

    for variant in range(len(russia_transfer_list)):
        kb.add(
            InlineKeyboardButton(
                text=russia_transfer_list[variant],
                callback_data=russia_transfer_callback.new(answer=variant)
            )
        )
    return kb


def georgia_transfer_kb():
    kb = InlineKeyboardMarkup()

    for variant in range(len(georgia_transfer_list)):
        kb.add(
            InlineKeyboardButton(
                text=georgia_transfer_list[variant],
                callback_data=georgia_transfer_callback.new(answer=variant)
            )
        )
    return kb


def ukrain_transfer_kb():
    kb = InlineKeyboardMarkup()

    for variant in range(len(ukrain_transfer_list)):
        kb.add(
            InlineKeyboardButton(
                text=ukrain_transfer_list[variant],
                callback_data=ukrain_transfer_callback.new(answer=variant)
            )
        )
    return kb
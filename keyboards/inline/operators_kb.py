from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

new_order_collback = CallbackData("new_order", "answer", "id")
in_process_collback = CallbackData("in_process", "answer", "id")
completed_order_collback = CallbackData("completed_order", "answer", "id")
deleted_order_collback = CallbackData("deleted_order", "answer", "id")


def new_order(id):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton(
        text='Взять в работу',
        callback_data=new_order_collback.new(answer=0, id=id)
    )
    )
    kb.add(InlineKeyboardButton(
        text='Удалить',
        callback_data=new_order_collback.new(answer=1, id=id)
    )
    )

    return kb


def in_process(id):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton(
        text='Завершить',
        callback_data=in_process_collback.new(answer=0, id=id)
    )
    )
    kb.add(InlineKeyboardButton(
        text='Вернуть',
        callback_data=in_process_collback.new(answer=1, id=id)
    )
    )
    kb.add(InlineKeyboardButton(
        text='Удалить',
        callback_data=in_process_collback.new(answer=2, id=id)
    )
    )

    return kb


def completed_order(id):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton(
        text='Восстановить',
        callback_data=completed_order_collback.new(answer=0, id=id)
    )
    )
    kb.add(InlineKeyboardButton(
        text='Удалить',
        callback_data=completed_order_collback.new(answer=1, id=id)
    )
    )

    return kb


def deleted_order(id):
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton(
        text='Восстановить',
        callback_data=deleted_order_collback.new(answer=0, id=id)
    )
    )

    return kb


def complete_converter_kb():
    kb = ReplyKeyboardMarkup()

    kb.add(
        InlineKeyboardButton(
            text='Оставить заявку (Отправить номер телефона)',
            request_contact=True
        )

    )
    kb.add(
        InlineKeyboardButton(
            text=f'Главное меню'
        )
    )

    return kb

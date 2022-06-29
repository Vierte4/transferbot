from aiogram.dispatcher.filters.state import StatesGroup, State


# Russia - Georgia
class ru_geo_state(StatesGroup):
    default = State()
    amount = State()


class geo_ru_state(StatesGroup):
    default = State()
    amount = State()


# Ukrain - Georgia
class ua_geo_state(StatesGroup):
    default = State()
    amount = State()


class geo_ua_state(StatesGroup):
    default = State()
    amount = State()


# Ukrain Russia
class ua_ru_state(StatesGroup):
    default = State()
    amount = State()

class ru_ua_state(StatesGroup):
    default = State()
    amount = State()


class Convert_copmlete(StatesGroup):
    complete = State()

# Georgia USDT
class geo_usdt_state(StatesGroup):
    default = State()
    amount = State()

class usdt_geo_state(StatesGroup):
    default = State()
    amount = State()
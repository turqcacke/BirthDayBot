from aiogram.dispatcher.filters.state import State, StatesGroup


class MenuStates(StatesGroup):
    inline_menu = State()


class InputStates(StatesGroup):
    name = State()
    surname = State()
    date = State()


from aiogram.dispatcher.filters.state import State, StatesGroup


class StateDataNames:
    BIND = 'bind_inline_message'
    INFO_ID = 'bind_info_id'
    LAST_START_ID = 'last_start_id'


class InputStates(StatesGroup):
    name = State()
    surname = State()
    day = State()

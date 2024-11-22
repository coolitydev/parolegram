from aiogram.fsm.state import StatesGroup, State


class PasswordFSM(StatesGroup):
    length = State()

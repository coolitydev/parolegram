from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.keyboards.menu import main_menu
from bot.keyboards.ui import password_generator_UI
from bot.storage.password import PasswordFSM

router = Router(name="command")


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "Привет, я бот для генерации паролей!",
        reply_markup=main_menu
    )


@router.message(Command("generate_password"))
async def start_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data:
        await state.set_state(PasswordFSM.length)
        await message.answer("<b>Напишите желаемую длинну пароля</b>")
        return
    await message.answer(
        f"<b>Длина пароля - {data["length"]} символов</b>",
        reply_markup=password_generator_UI(data=data)
    )

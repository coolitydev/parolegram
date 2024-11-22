from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.storage.password import PasswordFSM
from bot.keyboards.ui import password_generator_UI

router = Router(name="menu")


@router.callback_query(F.data == "start_generate_password")
async def start_generate_password_handler(call: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    if not data:
        await state.set_state(PasswordFSM.length)
        await call.message.edit_text("<b>Напишите желаемую длинну пароля</b>")
        return
    await call.message.edit_text(
        f"<b>Длина пароля - {data["length"]} символов</b>",
        reply_markup=password_generator_UI(data=data)
    )

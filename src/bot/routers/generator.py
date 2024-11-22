from html import escape

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.storage.password import PasswordFSM
from bot.keyboards.ui import password_generator_UI
from bot.utils.pwd_gen import PasswordGenerator

router = Router(name="generator")


@router.message(PasswordFSM.length)
async def length_handler(message: Message, state: FSMContext) -> None:
    if not message.text.isdigit():
        await message.answer("<b>Длина пароля должна быть числом</b>")
        return

    if not (8 <= int(message.text) <= 512):
        await message.answer("<b>Длина пароля должна быть не менее 8 и не более 512 символов</b>")
        return

    length = message.text
    data = await state.get_data()

    if not data:
        data = {
            "length": length,
            "status_letters": True,
            "status_digits": True,
            "status_punctuation": True,
        }
        await state.update_data(data=data)

    data["length"] = length
    await state.update_data(data=data)

    await message.answer(
        f"<b>Длина пароля - {data["length"]} символов</b>",
        reply_markup=password_generator_UI(data=data)
    )


@router.callback_query(F.data == "change_status_letters")
@router.callback_query(F.data == "change_status_digits")
@router.callback_query(F.data == "change_status_punctuation")
async def change_letters_status_handler(call: CallbackQuery, state: FSMContext) -> None:
    symbol = call.data[7:]

    data = await state.get_data()
    data[symbol] = not data[symbol]

    await state.update_data(data=data)
    await call.message.edit_text(
        f"<b>Длина пароля - {data["length"]} символов</b>",
        reply_markup=password_generator_UI(data=data)
    )


@router.callback_query(F.data == "end_generate_password")
async def generate_password_handler(call: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    if not any([data["status_letters"], data["status_digits"], data["status_punctuation"]]):
        await call.answer(
            "Выберите хотя бы один тип символов",
            show_alert=True
        )
        return

    await state.clear()

    try:
        pwd = PasswordGenerator(
            length=int(data["length"]),
            use_letters=data["status_letters"],
            use_digits=data["status_digits"],
            use_punctuation=data["status_punctuation"]
        ).generate()
    except KeyError:
        await call.message.edit_text(
            "<b>Пароль был ранее сгенерирован!</b>\n\n"
            "Нажмите /generate_password для новой генерации"
        )
        return

    await call.message.edit_text(
        f"<b>Сгенерированный пароль:</b>\n\n"
        f"<code>{escape(pwd)}</code>"
    )

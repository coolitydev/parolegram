from typing import Dict, Any

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def password_generator_UI(data: Dict[str, Any]):
    letters_status = "✅" if data["status_letters"] == True else "❌"
    digits_status = "✅" if data["status_digits"] == True else "❌"
    punctuation_status = "✅" if data["status_punctuation"] == True else "❌"

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Буквы:", callback_data="ignore"),
                InlineKeyboardButton(text=letters_status, callback_data="change_status_letters"),
            ],
            [
                InlineKeyboardButton(text="Цифры:", callback_data="ignore"),
                InlineKeyboardButton(text=digits_status, callback_data="change_status_digits"),
            ],
            [
                InlineKeyboardButton(text="Спецсимовлы:", callback_data="ignore"),
                InlineKeyboardButton(text=punctuation_status, callback_data="change_status_punctuation"),
            ],
            [
                InlineKeyboardButton(text="Сгенерировать пароль", callback_data="end_generate_password")
            ]
        ]
    )

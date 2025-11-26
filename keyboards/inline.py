# keyboards/inline.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def settings_menu(lang_texts):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lang_texts.get("change_lang", "Сменить язык"), callback_data="settings:lang")],
            [InlineKeyboardButton(text=lang_texts.get("set_time", "Время рассылки"), callback_data="settings:time")],
        ]
    )
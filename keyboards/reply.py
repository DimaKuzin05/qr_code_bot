# keyboards/reply.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu(lang_texts):
    """
    lang_texts: dict-like with keys 'weather', 'cat', 'settings'
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=lang_texts.get("weather", "Получить погоду"))],
            [KeyboardButton(text=lang_texts.get("cat", "Кота!"))],
            [KeyboardButton(text=lang_texts.get("settings", "Меню настроек"))],
        ],
        resize_keyboard=True
    )
# handlers/settings.py
from aiogram import Router, types
from aiogram.filters import Command
from keyboards.inline import settings_menu
from utils.i18n import t

router = Router()

def register(dp):
    dp.include_router(router)

@router.message(Command("settings"))
async def cmd_settings(message: types.Message):
    lang = getattr(message.from_user, "language_code", None) or "ru"
    texts = {
        "change_lang": t("change_lang", lang),
        "set_time": t("set_time", lang)
    }
    await message.answer(t("settings_header", lang), reply_markup=settings_menu(texts))
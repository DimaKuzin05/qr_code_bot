# handlers/about.py
from aiogram import Router
from aiogram.filters import Command
from aiogram import types
import json
from pathlib import Path

router = Router()

def register(dp):
    dp.include_router(router)

@router.message(Command("about"))
async def cmd_about(message: types.Message):
    p = Path("data/about.json")
    if not p.exists():
        await message.answer("Информация о боте недоступна.")
        return
    try:
        obj = json.loads(p.read_text(encoding="utf-8"))
        # expected fields: name, author, description
        text = f"*{obj.get('name','Bot')}*\n\n{obj.get('description','')}\n\nАвтор(ы): {obj.get('author','')}"
        await message.answer(text, parse_mode="Markdown")
    except Exception:
        await message.answer("Не удалось загрузить about.json — файл повреждён.")
# Вспомогательные скрипты
# Восстановление из CSV

# scripts/restore_from_backup.py
"""
Usage:
    python scripts/restore_from_backup.py data/backups/users_backup_2025...json
"""
import sys
import json
from models.database import get_session, User
from datetime import datetime

def restore(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        obj = json.load(f)

    users = obj.get("users", [])
    inserted = 0
    with get_session() as session:
        for u in users:
            chat_id = u.get("chat_id")
            if not chat_id:
                continue
            existing = session.query(User).filter_by(chat_id=chat_id).first()
            if existing:
                continue
            created_at = None
            if u.get("created_at"):
                try:
                    created_at = datetime.fromisoformat(u["created_at"])
                except Exception:
                    created_at = datetime.utcnow()
            new = User(
                chat_id=chat_id,
                username=u.get("username"),
                first_name=u.get("first_name"),
                lang=u.get("lang") or "ru",
                created_at=created_at or datetime.utcnow()
            )
            session.add(new)
            inserted += 1
    print(f"Done. Inserted {inserted} users.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide path to backup JSON file.")
        sys.exit(1)
    restore(sys.argv[1])
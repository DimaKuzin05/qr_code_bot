from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from utils.config_loader import config
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True, nullable=False)
    username = Column(String)
    first_name = Column(String)
    lang = Column(String, default="ru")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


engine = create_engine(config.DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)


def db():
    """Контекстный менеджер для сессий."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
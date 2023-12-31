from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str       # Название базы данных
    db_host: str        # URL-адрес базы данных
    db_user: str        # Username пользователя базы данных
    db_password: str    # Пароль пользователя


@dataclass
class TgBot:
    token: str          # Токен для доступа к телеграмм-боту
    admin_id: str       # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env()
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_id=list(map(int, env.list('ADMIN_ID')))),
                  db=DatabaseConfig(database=env('DATABASE'),
                                      db_host=env('DB_HOST'),
                                      db_user=env('DB_USER'),
                                      db_password=env('DB_PASSWORD')))

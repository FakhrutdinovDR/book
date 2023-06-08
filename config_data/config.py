from dataclasses import dataclass
from environs import Env

@dataclass()
class TgBot:
    token: str

@dataclass()
class Config:
    bot: TgBot

def loadtoken(path: str | None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(bot=TgBot(token=env('BOT_TOKEN')))

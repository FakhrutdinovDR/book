from aiogram.types import BotCommand
from aiogram import Bot
from lexicon.lexicon import MENU_COMMANDS as menu


async def set_main_menu(bot: Bot):
    botcommands = [BotCommand(command=i[0], description=i[1]) for i in menu.items()]
    await bot.set_my_commands(botcommands)

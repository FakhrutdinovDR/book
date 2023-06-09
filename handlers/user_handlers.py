from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon import MENU_COMMANDS


router: Router = Router()

@router.message(F.text == '/start')
async def proccessingstart(message: Message):
    await message.answer(text=MENU_COMMANDS['start'])

@router.message(F.text == '/help')
async def proccessinghelp(message: Message):
    await message.answer(text=MENU_COMMANDS['help'])


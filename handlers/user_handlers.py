from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon import ANSWER_MENU_COMMANDS
from database.db import User, writeupdateusers, USERS
from keyboards.pagination import create_pagination_keyboard
from services.handling_book_getting import book

router: Router = Router()

@router.message(F.text == '/start')
async def proccessingstart(message: Message):
    USERS.setdefault(str(message.from_user.id), User(message.from_user.id, set()))
    writeupdateusers(USERS)
    await message.answer(text=ANSWER_MENU_COMMANDS['/start'])

@router.message(F.text == '/help')
async def proccessinghelp(message: Message):
    await message.answer(text=ANSWER_MENU_COMMANDS['/help'])

@router.message(F.text == '/beginning')
async def proccessingbegin(message: Message):
    kb = create_pagination_keyboard('backward', '1', 'forward')
    await message.answer(text=book[1], reply_markup=kb)

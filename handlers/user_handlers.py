from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import ANSWER_MENU_COMMANDS
from database.db import User, writeupdateusers, USERS
from keyboards.pagination import create_pagination_keyboard
from services.handling_book_getting import book

router: Router = Router()

# Блок инициализациии работы с ботом и помощи
@router.message(F.text == '/start')
async def proccessingstart(message: Message):
    USERS.setdefault(str(message.from_user.id), User(message.from_user.id, set())) # Добавление в словарь юзера, если его нет еще
    writeupdateusers(USERS) # Обновление файла с юзерами
    await message.answer(text=ANSWER_MENU_COMMANDS['/start'])

@router.message(F.text == '/help')
async def proccessinghelp(message: Message):
    await message.answer(text=ANSWER_MENU_COMMANDS['/help'])

# Блок хендлеров по работе со страницей чтения
@router.message(F.text == '/beginning')
async def proccessingbegin(message: Message):
    user = USERS[str(message.from_user.id)]
    kb = create_pagination_keyboard('backward', '1', 'forward')
    if user.lastpage != 1:
        user.lastpage = 1
    writeupdateusers(USERS)
    await message.answer(text=book[1], reply_markup=kb)

@router.callback_query(F.data == 'forward')
async def proccesingforwardbutton(cb: CallbackQuery):
    user = USERS[str(cb.from_user.id)]
    if user.lastpage < len(book):
        user.lastpage += 1
        writeupdateusers(USERS)
        text = book[user.lastpage]
        kb = create_pagination_keyboard('backward', str(user.lastpage), 'forward')
        await cb.message.edit_text(text=text, reply_markup=kb)
    await cb.answer()

@router.callback_query(F.data == 'backward')
async def proccesingbackwardbutton(cb: CallbackQuery):
    user = USERS[str(cb.from_user.id)]
    if user.lastpage > 1:
        user.lastpage -= 1
        writeupdateusers(USERS)
        text = book[user.lastpage]
        kb = create_pagination_keyboard('backward', str(user.lastpage), 'forward')
        await cb.message.edit_text(text=text, reply_markup=kb)
    await cb.answer()

@router.callback_query(F.data.isdigit())
async def proccessingpagebutton(cb: CallbackQuery):
    user = USERS[str(cb.from_user.id)]
    user.bookmarks.add(user.lastpage)
    writeupdateusers(USERS)
    await cb.answer(text=f'Страница {user.lastpage} добавлена в закладки')

# Хендлер для открытия последней страницы
@router.message(F.text == '/continue')
async def processing_continue_command(message: Message):
    user = USERS[str(message.from_user.id)]
    kb = create_pagination_keyboard('backward', str(user.lastpage), 'forward')
    await message.answer(text=book[user.lastpage], reply_markup=kb)

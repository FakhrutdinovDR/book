from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import ANSWER_MENU_COMMANDS, BOOKMARK_COMMANDS
from database.db import User, writeupdateusers, USERS
from keyboards.pagination import create_pagination_keyboard
from keyboards.bookmarks import create_bookmarks_kb, create_edit_bookmarks_kb
from filters.filters import IsDigitCallbackData, IsDelBookmarkCallbackData
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

# Блок по работе с закладками
@router.message(F.text == '/bookmarks')
async def processing_bookmarks(message: Message):
    user = USERS[str(message.from_user.id)]
    if user.bookmarks:
        kb = create_bookmarks_kb(*user.bookmarks)
        await message.answer(text='Список закладок:', reply_markup=kb)
    else:
        await message.answer(text=BOOKMARK_COMMANDS["no_bookmarks"])

@router.callback_query(IsDigitCallbackData())
async def proccessing_bookmarks_buttonpage(cb: CallbackQuery):
    user = USERS[str(cb.from_user.id)]
    user.lastpage = int(cb.data[:-1])
    kb = create_pagination_keyboard('backward', str(user.lastpage), 'forward')
    await cb.message.edit_text(text=book[user.lastpage], reply_markup=kb)
    await cb.answer()

@router.callback_query(F.data == 'cancel')
async def proccessing_cancel(cb: CallbackQuery):
   await cb.message.edit_text(text=BOOKMARK_COMMANDS['/continue'])
   await cb.answer()

@router.callback_query(F.data == 'edit_bookmarks')
async def proccessing_edit_bk(cb: CallbackQuery):
    user = USERS[str(cb.from_user.id)]
    kb = create_edit_bookmarks_kb(*user.bookmarks)
    await cb.message.edit_text(text='Редактировать закладки', reply_markup=kb)
    await cb.answer()

@router.callback_query(IsDelBookmarkCallbackData())
async def bookmark_del_button(cb: CallbackQuery):
    user = USERS[str(cb.from_user.id)]
    page_num = cb.data.strip('del')
    user.bookmarks = set(filter(lambda x: x != int(page_num), user.bookmarks))
    writeupdateusers(USERS)
    if user.bookmarks:
        kb = create_edit_bookmarks_kb(*user.bookmarks)
        await cb.message.edit_text(text='Редактировать закладки', reply_markup=kb)
    else:
        await cb.message.edit_text(text=BOOKMARK_COMMANDS["no_bookmarks"])
    await cb.answer()
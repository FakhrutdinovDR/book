from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import BOOKMARK_COMMANDS
from services.handling_book_getting import book

def create_bookmarks_kb(*args: int) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(text=f'{button} - {book[button][:100]}', callback_data=f'{str(button)}-'))
    kb_builder.row(InlineKeyboardButton(text=BOOKMARK_COMMANDS['edit_bookmarks'], callback_data='edit_bookmarks'),
                   InlineKeyboardButton(text=BOOKMARK_COMMANDS['cancel'], callback_data='cancel'), width=2)
    return kb_builder.as_markup()

def create_edit_bookmarks_kb(*args: int) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(text=f'{BOOKMARK_COMMANDS["del"]} {button} - {book[button][:100]}', callback_data=f'{button}del'))
    kb_builder.row(InlineKeyboardButton(text=BOOKMARK_COMMANDS['cancel'], callback_data='cancel'), width=2)
    return kb_builder.as_markup()
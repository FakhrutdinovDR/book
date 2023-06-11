from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_PAGE_BUTTONS
from services.handling_book_getting import book

def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON_PAGE_BUTTONS[button] if button in LEXICON_PAGE_BUTTONS else f'{button} из {len(book)}',
        callback_data=button) for button in buttons])

    return kb_builder.as_markup()


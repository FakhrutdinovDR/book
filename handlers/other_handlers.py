from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import OTHER_ANS

router: Router = Router()

@router.message()
async def proccessingother(message: Message):
    await message.answer(text=OTHER_ANS['other'])

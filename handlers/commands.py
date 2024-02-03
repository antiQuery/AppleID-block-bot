from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from block import lock


router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f'Отправь мне почту')
    
@router.message()
async def on_message(message: Message):
    msg = await message.reply('Блокируем...')
    res = await lock(message.text)
    await msg.edit_text(res)
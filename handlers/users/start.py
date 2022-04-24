import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu

from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            active=1
        )

        # ADMINGA xabar beramiz
        msg = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> bazaga qo'shildi."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

        await message.answer("Botimizga xush kelibsiz!")

    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
        await db.set_active(user[0], 1)
        await message.answer("Sizni yana ko'rganimdan xursandman!")

    # ADMINGA xabar beramiz

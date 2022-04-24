import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    son = 0
    users = await db.select_all_users()
    for user in users:
        try:
            user_id = user[3]
            await bot.send_message(
                chat_id=user_id, text="@SariqDev kanaliga obuna bo'ling!")
            if int(user[4]) != 1:
                await db.set_active(user[0], 1)
            son += 1

        except:
            await db.set_active(user[0], 0)
        await asyncio.sleep(0.05)
    await message.reply(f"{son} ta users")


@dp.message_handler(text="/count", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        msg = f"<a href='tg://user?id={user[3]}'>{user[1]}</a> bazaga qo'shildi."
        await message.reply(text=msg)
        await asyncio.sleep(0.05)
        # await message.reply(f"{user[0], user[1]}")

@dp.message_handler(text="/ac_count", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    count = await db.count_active_users()
    await message.reply(count)


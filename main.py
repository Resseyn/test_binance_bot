import asyncio
import logging
import sys
import threading
import time

from aiogram import Bot
from aiogram.enums import ParseMode

from helpers.funcs import parse_data, notification, init_values
from loader import TOKEN
from handlers import dp
from loader import subs

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


async def run():
    task1 = asyncio.create_task(
        get_data())

    task2 = asyncio.create_task(
        run_bot())
    await task1
    await task2


async def get_data():
    while True:
        coins = parse_data()
        await asyncio.sleep(1)
        await notification(bot, coins)

async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    init_values()
    asyncio.run(run())

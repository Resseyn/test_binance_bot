import aiogram.types
from aiogram import F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, InputMediaPhoto, Message

from helpers.funcs import parse_data
from loader import dp
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import subs

@dp.message(CommandStart())
async def start(message: Message):
    builder = ReplyKeyboardBuilder()
    builder.button(text="Подписаться на курсы")
    keyboard = builder.as_markup()
    await message.answer(text="Привет!\nХочешь подписаться на курс криптовалют?",
                         reply_markup=keyboard)


@dp.message()
async def main_menu(message: Message):
    if message.text == "Вывести актуальные цены" or message.text == "Подписаться на курсы":
        subs.add(message.from_user.id)
        data = parse_data()
        rep = "Цены на данный момент:\n\n"
        builder = ReplyKeyboardBuilder()
        builder.button(text="Вывести актуальные цены")
        keyboard = builder.as_markup()
        for coin, val in data.items():
            if float(val[1]) < 0:
                smile = "❌"
            else:
                smile = "✔️"
            rep += f'\t{smile}<strong>{coin}</strong> - {round(float(val[0]), 10)}$, изменение цены: <strong>{val[1]}%</strong>\n'
        await message.answer(text=rep, reply_markup=keyboard)


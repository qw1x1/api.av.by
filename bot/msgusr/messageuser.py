import asyncio
from aiogram import types
from aiogram.filters.command import Command
from aiogram.methods import send_message
from aiogram import Router
import bot.bot as bt

#router = Router()

@bt.dp.message(Command("qwe"))
async def call_backs():
    bt.bot.send_message(5569355585,'хуй')
    








#!/usr/bin/env python3

from socket import gethostname
from telegram import Bot
import asyncio

from config import security
from services.tg import TelegramService


bot = Bot(security.TOKEN)
hostname = gethostname()

async def main():
	tg_bot = TelegramService(hostname, security.STATE_DB, bot)
	msg = tg_bot.get_check_message()
	if (msg is not None):
		await bot.send_message(security.CHAT_ID, msg)

if __name__ == '__main__':
	asyncio.run(main())

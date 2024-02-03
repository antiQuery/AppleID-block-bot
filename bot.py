import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from handlers import commands
from middlewares.antiflood import AntiFloodMiddleware


async def main():
    load_dotenv()
    BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
    
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_API_TOKEN)    
    dp = Dispatcher()

    dp.message.middleware(AntiFloodMiddleware(1))    
    dp.include_routers(commands.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

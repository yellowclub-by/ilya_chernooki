import asyncio
from aiogram import Bot, Dispatcher


TOKEN = "7858050871:AAHQDdZTj8N0BvOfpds0ee3k_S1yMmxxknA"
bot = Bot(token=TOKEN)
dp = Dispatcher()
from handlers.user_private import user_router
dp.include_router(user_router)

async def main():
    print("Bot start")
    await dp.start_polling(bot)


asyncio.run(main())

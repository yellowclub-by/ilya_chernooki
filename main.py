import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode



TOKEN = "7858050871:AAHQDdZTj8N0BvOfpds0ee3k_S1yMmxxknA"
bot = Bot(token=TOKEN,parse_mode=ParseMode.HTML)
dp = Dispatcher()


from handlers.user_private import user_router
from handlers.catalog import catalog_router
from handlers.User_group import group_router



dp.include_router(user_router)
dp.include_router(catalog_router)
dp.include_router(group_router)


async def main():
    print("Bot start")
    await dp.start_polling(bot)


asyncio.run(main())

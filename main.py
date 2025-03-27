import asyncio
from aiogram import Bot,Dispatcher,types


TOKEN = "7858050871:AAHQDdZTj8N0BvOfpds0ee3k_S1yMmxxknA"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer("в работе")
async def main():
    print("Bot start")
    await dp.start_polling(bot)


asyncio.run(main())


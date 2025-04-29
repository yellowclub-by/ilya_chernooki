from aiogram.filters import CommandStart, Command
from aiogram import types,Router,F
from Keyboards import reply

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет это бот для продажи В_баксов", reply_markup=reply.main_kb)

@user_router.message(F.text.lower().contain("каталог"))
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("Добро пожаловать в каталог", reply_markup=reply.catalog_kb)

@user_router.message(Command("donat"))
async def donat(message: types.Message):
    await message.answer("Спасибо за донат")

@user_router.message(Command("support"))
async def support(message: types.Message):
    await message.answer("Это раздел  поддержки")

@user_router.message(Command("basket"))
async def basket(message: types.Message):
    await message.answer("Здесь хранятся ваши выбранные товары")

# @user_router.message(F.text.lower().contains("стои")|F.text.lower().contains("цен"))
# async def echo(message: types.Message):
#     await message.answer("в работе")

from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from keyboards import reply, inline

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет это бот для продажи В_баксов", reply_markup=reply.main_kb)

@user_router.message(F.text.lower()=="каталог")
@user_router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("Добро пожаловать в каталог", reply_markup=reply.catalog_kb)

@user_router.message(Command("donat"))
async def donat(message: types.Message):
    await message.answer("Спасибо за донат")

@user_router.message(F.text.lower()=="поддержка")
@user_router.message(Command("Quations"))
async def Question(message: types.Message):
    await message.answer("Частые вопросы",reply_markup=inline.question())

@user_router.callback_query(F.data.lower().startswith("question"))
async def answer(callback:types.CallbackQuery):
    query = callback.data.split("_")[1]
    if query == "1":
        await callback.message.answer("1 ответ")
    elif query == "2":
        await callback.message.answer("2 ответ")
    elif query == "3":
        await callback.message.answer("3 ответ")
    await callback.answer("ответ отправлен")

@user_router.message(Command("basket"))
async def basket(message: types.Message):
    await message.answer("Здесь хранятся ваши выбранные товары")

@user_router.message(F.text.lower() == "назад")
async def back_menu(message: types.Message):
    await message.answer("главное меню", reply_markup=reply.main_kb)

# @user_router.message(F.text.lower().contains("стои")|F.text.lower().contains("цен"))
# async def echo(message: types.Message):
#     await message.answer("в работе")

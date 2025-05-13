from aiogram import types,Router,F
from aiogram.types import FSInputFile

catalog_router = Router()
@catalog_router.message(F.text.lower()== "1000")
async def first_position(message: types.Message):
    photo = FSInputFile("imag/catalog/a9nhx3AlHxuKt9VneL_hg_GDIFM2acvr2JHzB81tio_1920x1080_1x_0.jpeg")
    await message.answer_photo(photo)
    await message.answer("1000 V_Bucks")


@catalog_router.message(F.text.lower()== "2800")
async def first_position(message: types.Message):
    photo = FSInputFile("imag/catalog/fortnite2800.jpg")
    await message.answer_photo(photo)
    await message.answer("2800 V_Bucks")

@catalog_router.message(F.text.lower()== "BatlPass")
async def first_position(message: types.Message):
    photo = FSInputFile("imag/catalog/maxresdefault.jpg")
    await message.answer_photo(photo)
    await message.answer("BatlPass")

@catalog_router.message(F.text.lower()== "Отряд")
async def first_position(message: types.Message):
    photo = FSInputFile("imag/catalog/download.jpg")
    await message.answer_photo(photo)
    await message.answer("Отряд")
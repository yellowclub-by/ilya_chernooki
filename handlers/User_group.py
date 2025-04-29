from aiogram import types,Router,F
group_router = Router()
no_words = ["кокос","захар","локоть"]

@group_router.message(F.text)
async def cancel_to_words(message:types.Message):
    user_words = message.text.split(" ")
    for word in user_words:
        if word.lower() in no_words:
            await message.answer(F"{message.from_user.first_name} не нарушай правила,Крамбл Куки Захар уже едет")
            break
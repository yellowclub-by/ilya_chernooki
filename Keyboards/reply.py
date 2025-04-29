from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="каталог"),KeyboardButton(text="поддержка"),],
        [KeyboardButton(text="донат"),KeyboardButton(text="корзина"),]
],
    resize_keyboard=True,
    input_field_placeholder="Крамбл куки...."
),
catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="товар 1")]
    ]
)
# support_kb = KeyboardButton(text="поддержка")
# donat_kb = KeyboardButton(text="донат")
# busket_kb = KeyboardButton(text="корзина")
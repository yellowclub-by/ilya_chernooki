from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_btn = KeyboardButton(text="назад")

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="каталог"), KeyboardButton(text="поддержка")],
        [KeyboardButton(text="донат"), KeyboardButton(text="корзина")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Крамбл куки...."
)

catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1000"),KeyboardButton(text="BatlPass")],
        [KeyboardButton(text="Отряд"),KeyboardButton(text="2800")],
        [back_btn]
    ],
)

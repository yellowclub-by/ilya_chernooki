from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def question():
    builder = InlineKeyboardBuilder()
    builder.row(
    InlineKeyboardButton(text="1 вопрос",callback_data="question_1"),
    InlineKeyboardButton(text="2 вопрос", callback_data="question_2"),
    InlineKeyboardButton(text="3 вопрос", callback_data="question_3"),
    width=1
    )
    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
inline_keyboard=[
    [InlineKeyboardButton(text="сайт",url="https://vm.tiktok.com/ZMSNmLe6m/"),
     InlineKeyboardButton(text="сайт",url="https://vm.tiktok.com/ZMSNmLUr5/"),
     InlineKeyboardButton(text="телеграм",url="https://t.me/XZ_chto_pisat_1")
    ]
]


)
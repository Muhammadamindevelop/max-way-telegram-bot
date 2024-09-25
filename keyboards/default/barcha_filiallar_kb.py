from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_barcha_filiallar():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='⬅️ Orqaga'), KeyboardButton(text='▶️ Oldinga')],
            [KeyboardButton(text='MAX WAY ALAYSKIY'), KeyboardButton(text='MAX WAY BERUNIY')]
        ],
        resize_keyboard=True
    )

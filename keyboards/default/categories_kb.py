from loader import db
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_categories_kb():
    tugmalar = []
    menu = ReplyKeyboardBuilder()
    menu.max_width = 2
    
    categories = db.get_categories()
    print(f"{categories=}")
    for category in categories:
        tugmalar.append(
            KeyboardButton(text=category[0])
        )

    menu.row(*tugmalar)

    return menu.as_markup(resize_keyboard = True)

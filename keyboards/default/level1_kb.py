from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def language_buttons():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='Ozbekcha'),
      KeyboardButton(text='Ruscha'),
      KeyboardButton(text='English')]
    ],
    resize_keyboard=True
  )
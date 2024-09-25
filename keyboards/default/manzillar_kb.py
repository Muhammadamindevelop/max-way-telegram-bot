from aiogram.types import ReplyKeyboardMarkup , KeyboardButton


def oldinga():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='⬅️ Orqaga'),KeyboardButton(text='MAX WAY SAYRAM manzil')],
      [KeyboardButton(text='MAX WAY MAKSIM GORKIY manzil'),KeyboardButton(text='MAX WAY SERGELI manzil')],
      [KeyboardButton(text='MAX WAY FONTAN manzil'),KeyboardButton(text='MAX WAY MONOR manzil')]
    ],
    resize_keyboard=True
  )
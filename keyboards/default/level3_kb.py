from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def olib_ketish():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='⬅️ Orqaga'),KeyboardButton(text='📍  Eng yaqin fillialni aniqlash')],
      [KeyboardButton(text='MAX WAY ALAYSKIY'),KeyboardButton(text='MAX WAY BERUNIY')],
      [KeyboardButton(text='MAX WAY AVIASOZLAR'),KeyboardButton(text='MAX WAY RISOVIY')],
      [KeyboardButton(text='MAX WAY PARUS'),KeyboardButton(text='MAX WAY PARKENT')],
      [KeyboardButton(text='MAX WAY UNIVERSAM'),KeyboardButton(text='MAX WAY ROYSON')],
      [KeyboardButton(text='MAX WAY MUQUMIY'),KeyboardButton(text='MAX WAY GRAND MIR')],
      [KeyboardButton(text='MAX WAY SAYRAM'),KeyboardButton(text='MAX WAY MAKSIM GORKIY')],
      [KeyboardButton(text='MAX WAY SERGELI'),KeyboardButton(text='MAX WAY FONTAN')],
      [KeyboardButton(text='MAX WAY MINOR')]
    ],
    resize_keyboard=True 
  )


def yetkazib_berish():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='Lakatsiya yuborish', request_location=True)],
      [KeyboardButton(text='⬅️ Orqaga')]
    ],
    resize_keyboard=True
  )
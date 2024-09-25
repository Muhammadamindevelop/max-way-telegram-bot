from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def buyurtma():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='🚖 Yetkazib berish'),KeyboardButton(text='🏃 Olib ketish')],
      [KeyboardButton(text='⬅️ Orqaga')]
    ],
    resize_keyboard=True 
)


def aksya():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='⬅️ Orqaga')]
    ],
    resize_keyboard=True 
  )

def manzil():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='⬅️ Orqaga'),KeyboardButton(text='▶️ Oldinga')],
      [KeyboardButton(text='MAX WAY ALAYSKIY manzil'),KeyboardButton(text='MAX WAY BERUNIY manzil')],
      [KeyboardButton(text='MAX WAY AVIASOZLAR manzil'),KeyboardButton(text='MAX WAY RISOVIY manzil')],
      [KeyboardButton(text='MAX WAY PARUS manzil'),KeyboardButton(text='MAX WAY PARKENT manzil')],
      [KeyboardButton(text='MAX WAY UNIVERSAM mazil'),KeyboardButton(text='MAX WAY ROYSON manzil')],
      [KeyboardButton(text='MAX WAY MUQUMIY manzil'),KeyboardButton(text='MAX WAY GRANT MIR manzil')]
    ],
    resize_keyboard=True 
  )





def ovqat_buyurtma():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='🗂 | Asosiy menu')]
    ],
    resize_keyboard=True 
  )


def izoh():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='⬅️ Orqaga')]
    ],
    resize_keyboard=True 
  )


def vakansiya():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='⬅️ Orqaga')]
    ],
    resize_keyboard=True 
  )

def haqida():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='⬅️ Orqaga')]
    ],
    resize_keyboard=True 
  )


def sozlamalar():
  return ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text='🇺🇿 Tilni o\'zgartirish'),KeyboardButton(text='Tug\'ilgan kunni qo\'shish')],
      [KeyboardButton(text='Telefon raqamni o\'zgartirish'),KeyboardButton(text='⬅️ Orqaga')]
    ],
    resize_keyboard=True 
  )


def for_yetkazib_berish_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Lokatsiya yuborish', request_location=True)],
            [KeyboardButton(text='⬅️ Orqaga')]
        ],
        resize_keyboard=True
    )
from aiogram.types import KeyboardButton,  ReplyKeyboardMarkup

def menu_button():
  return ReplyKeyboardMarkup(
  keyboard=[
    [KeyboardButton(text='🛍 Buyurtma berish')],
    [KeyboardButton(text='🎉 Aksiya'),KeyboardButton(text='🏘 Barcha fillallar')],
    [KeyboardButton(text='📋 Mening buyurtmalarim'),KeyboardButton(text='✍🏻 Izoh qoldirish')],
    [KeyboardButton(text='💼 Vakansiyalar'),KeyboardButton(text='ℹ️ Biz haqimizda')],
    [KeyboardButton(text='⚙️ Sozlamalar')]
  ],
  resize_keyboard=True 
)
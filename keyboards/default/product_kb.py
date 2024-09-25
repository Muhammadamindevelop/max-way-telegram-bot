from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import db

def make_product_keyboard(category_name:str):
  products = db.get_products_by_categoty_name(category_name)
  buttuns=[]
  print(f'{products=}')
  menu = ReplyKeyboardMarkup(keyboard=[],resize_keyboard=True, row_width=2)
  
  for product in products:
    buttuns.append(
      KeyboardButton(text=product[0])
    )
    
    
  menu.keyboard.append(
    buttuns
  )
  
  return menu 


def make_card_sub_keyboard():
  return ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text='⬅️ Orqaga'),KeyboardButton(text='📥 Savat')
      ]
    ],resize_keyboard=True
  )
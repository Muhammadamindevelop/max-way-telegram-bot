from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import db


def make_categories_kb_for_admin():
  categories = db.get_categories_for_admin()
  keyboards = []
  menu = InlineKeyboardMarkup(inline_keyboard=[])
  
  for category in categories:
    category_id = category[0]
    category_name = category[1]
    print(category_id,category_name)
    
    
    keyboards.append(
      InlineKeyboardButton(text=category_name,  callback_data=str(category_id))
    )
  
  menu.inline_keyboard.append(keyboards)
  
  return menu
  
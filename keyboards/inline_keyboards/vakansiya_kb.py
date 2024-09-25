from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



def make_vacancy_kb(title: str):
  data = f'vacancy:{title}'
  return InlineKeyboardBuilder(
    markup=[
      [
        InlineKeyboardButton(text='Ariza topshirish',callback_data=data)
      ]
    ]
  ).as_markup()
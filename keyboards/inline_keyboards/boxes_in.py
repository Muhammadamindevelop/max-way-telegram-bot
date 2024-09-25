from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

box_kb = InlineKeyboardMarkup(
  inline_keyboard=[
    [InlineKeyboardButton(text='➖',callback_data='minus'),InlineKeyboardButton(text='1',callback_data='soni'),InlineKeyboardButton(text='➕',callback_data='plyus')],
    [InlineKeyboardButton(text='⬇️ Kartoshka-fri ⬇️',callback_data='kartoshka_kategory')],
    [InlineKeyboardButton(text='Kichkina kartoshka-fir')],
    [InlineKeyboardButton(text='⬇️ Souslar ⬇️',callback_data='sous')],
    [InlineKeyboardButton(text='Sarimsoqli sous',callback_data='sarimsoq'),InlineKeyboardButton(text='Ketchup',callback_data='ketchup'),InlineKeyboardButton(text='Sirli sous',callback_data='sirli')],
    [InlineKeyboardButton(text='⬇️ Ichimliklar ⬇️',callback_data='ichimlik')],
    [InlineKeyboardButton(text='Quyma Coca Cola',callback_data='kola'),InlineKeyboardButton(text='Limonli choy',callback_data='choy')],
    [InlineKeyboardButton(text='📥 Savatga qoshish',callback_data='savat')]
  ]
)
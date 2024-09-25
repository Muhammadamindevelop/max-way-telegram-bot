from aiogram import F
from aiogram.types import Message,FSInputFile

from loader import dp
from keyboards.inline_keyboards.boxes_in import box_kb

@dp.message(F.text == 'Maxi BOX Traditsiya')
async def traditsiya(message:Message):
  file = FSInputFile(path='traditsiya.jpg')
  await message.answer('Mahsulot miqdorini tanlang')
  await message.answer_photo(photo=file,caption='Maxi BOX Traditsiya \nOriginal sendvich, kartoshka fri, 0,4 l coca cola, tanlash uchun sous\n\nMaxi BOX Traditsiya 45 000 x 2 = 90 000\nkartoshka-fri :\n- kichik kartoshka-fri     0 x 1 = 0\n\nUmumiy: 90 000 UZS',reply_markup=box_kb())

from aiogram import F
from aiogram.types import Message

from loader import dp
from keyboards.default.level3_kb import olib_ketish 
from keyboards.default.default import menu_button


@dp.message(F.text =='🏃 Olib ketish')
async def ketish(message: Message):
  await message.answer('Filialni tanlang' ,reply_markup=olib_ketish())

@dp.message(F.text == 'MAX WAY BERUNIY')
async def beruiy(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY ALAYSKIY')
async def aviasozlar(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY RISOVIY')
async def risoviy(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY PARUS')
async def parus(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY PARKENT')
async def parkent(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY UNIVERSAM')
async def parus(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY ROYSON')
async def royson(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY MUQUMIY')
async def muqumiy(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY GRANT MIR')
async def grant_mir(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY SAYRAM')
async def sayram(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY MAKSIM GORKIY')
async def maksim_gorkiy(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY SERGILI')
async def sergli(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY FONTAN')
async def fontan(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

@dp.message(F.text == 'MAX WAY MINOR')
async def minor(message: Message):
  await message.answer('Interaktiv menyudan buyurtma bering')
  await message.answer('Kategoriyani tanlang' ,reply_markup=menu_button())

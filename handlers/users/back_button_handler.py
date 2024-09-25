from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loader import dp
from keyboards.default.default import menu_button
from states.states_level import BuyurtmaBerishState
from keyboards.default.level2_kb import buyurtma



@dp.message(F.text == '⬅️ Orqaga', BuyurtmaBerishState)
async def back_to_buyurtma_berish(message:Message,state:FSMContext):
  await message.answer(
    text='Yetkazib berish turini tanlang',
    reply_markup=buyurtma())
  await state.clear()



@dp.message(F.text == '⬅️ Orqaga')
async def main_back_btn_handler(message: Message):
  text = '''Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing\n\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin\n\nmenu '''
  await message.answer(text, reply_markup= menu_button())

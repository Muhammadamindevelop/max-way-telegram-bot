from aiogram import F
from aiogram.types import CallbackQuery,Message
from aiogram.fsm.context import FSMContext

from loader import dp
from states.states_level import VacancyState

@dp.callback_query(F.data.startswich('vacancy'))
async def vacancy_callbeck_query_handler(call:CallbackQuery, state:FSMContext):
  data = call.data.split(":")[-1]
  await state.set_state(VacancyState.fio)
  await state.update_data(vacancy=data)
  await call.message.answer('Familya va Ismingizni kiriting')

@dp.message(VacancyState.fio)
async def  get_fio(message:Message,state:FSMContext):
  await message.answer('Rezumeni yuboring')
  fio = message.text
  await state.update_data(fio=fio)
  await state.set_state(VacancyState.rezume)


@dp.message(VacancyState.rezume)
async def  get_rezume(message:Message,state:FSMContext):
  await message.answer('Telefon raqamingizni yuboring')
  rezume= message.text
  await state.update_data(rezume=rezume)
  await state.set_state(VacancyState.phone_number)

@dp.message(VacancyState.phone_number)
async def  get_phone_number(message:Message,state:FSMContext):
  phone_number= message.text
  await state.update_data(phone_number=phone_number)
  await message.answer('Vakansya qabul qilindi')

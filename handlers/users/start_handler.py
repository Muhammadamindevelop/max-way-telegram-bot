from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loader import dp, db
from keyboards.default.level2_kb import buyurtma, for_yetkazib_berish_kb
from keyboards.default.barcha_filiallar_kb import get_barcha_filiallar
from keyboards.default.categories_kb import get_categories_kb
# states
from states.states_level import BuyurtmaBerishState
from aiogram.filters import CommandStart
from keyboards.default.default import menu_button


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text = '''Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing\n\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin'''
    await message.answer(text, reply_markup=menu_button())


    db.add_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )



@dp.message(F.text == '🛍 Buyurtma berish')
async def buyurtma_berish(message: Message, state: FSMContext):
    await message.answer('Yetkazib berish turini tanlang', reply_markup=buyurtma())

@dp.message(F.text == '🎉 Aksiya')
async def aksiya(message: Message, state: FSMContext):
    pass

@dp.message(F.text == '🏘 Barcha filiallar')
async def barcha_filiallar(message: Message, state: FSMContext):
    await message.answer('Bizning filiallarimiz :', reply_markup=get_barcha_filiallar())

@dp.message(F.text == 'Vakansiyalar')
async def vakansiyalar(message: Message, state: FSMContext):
    vakansiyalar = db.get_vacancies()
    await message.answer('Vakansiyalr:')

    for title in vakansiyalar:
        await message.answer(text=title[0], reply_markup='')


@dp.message(F.text == '🚖 Yetkazib berish')
async def yetkazib_berish(message: Message, state: FSMContext):
    await message.answer('Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring',
        reply_markup=for_yetkazib_berish_kb())
    
    await state.set_state(BuyurtmaBerishState.yetkazib_berish)


@dp.message(BuyurtmaBerishState.yetkazib_berish)
async def get_user_location_handler(message: Message, state: FSMContext):
    if message.location:
        '''
        Shu yerda foydalanuvchi manzili bazaga saqlash kodi bo'lishi kerak
        '''
        await message.answer('kategoriyalardan birini tanlang', reply_markup=get_categories_kb())
        await state.set_state(BuyurtmaBerishState.select_category)
    else:
        await message.answer('Iltimos lokatsiya yuboring!')


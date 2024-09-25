from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from loader import dp, db, bot
from config.config import ADMIN
from states.admin_states import AdminState, AddProduct
from keyboards.inline_keyboards.categories_kb import make_categories_kb_for_admin

@dp.message(Command(commands=['add_category']), F.from_user.id == ADMIN)
async def add_category_handler(message: Message, state: FSMContext):
    await message.answer('Kategoriya nomini yuboring') 
    await state.set_state(AdminState.add_category)


@dp.message(AdminState.add_category, F.from_user.id == ADMIN)
async def get_category_handler(message: Message, state: FSMContext):
    text = message.text
    db.add_category(text)
    await message.answer('qoshildi!') 
    await state.clear()


@dp.message(Command(commands=['add_vacancy']), F.from_user.id == ADMIN)
async def add_category_handler(message: Message, state: FSMContext):
    await message.answer('Vakansiya salrlavhasini yuboring') 
    await state.set_state(AdminState.add_vacancy)


@dp.message(AdminState.add_vacancy, F.from_user.id == ADMIN)
async def get_category_handler(message: Message, state: FSMContext):
    text = message.text
    db.add_vacancy(text)
    await message.answer('qoshildi!')
    await state.clear()


@dp.message(Command(commands=['add_product']), F.from_user.id == ADMIN)
async def add_category_handler(message: Message, state: FSMContext):
    await message.answer('kategoriyani tanlang', reply_markup=make_categories_kb_for_admin())
    await state.set_state(AddProduct.category)


@dp.callback_query(AddProduct.category, F.from_user.id == ADMIN)
async def select_category(call: CallbackQuery, state: FSMContext):
    category = call.data
    await state.update_data(category=category)
    await call.message.answer("Mahsulot nomini kirting")
    
    await call.message.delete()
    
    await state.set_state(AddProduct.name)

@dp.message(AddProduct.name, F.from_user.id == ADMIN)
async def product_name_handler(message: Message, state: FSMContext):
    name = message.text
    await message.answer("Mahsulot tavsifi(description)ni kiriting")
    await state.update_data(name=name)
    await state.set_state(AddProduct.description)


@dp.message(AddProduct.description, F.from_user.id == ADMIN)
async def product_description_handler(message: Message, state: FSMContext):
    description = message.text
    await message.answer("Mahsulot narxini kiriting")
    await state.update_data(description=description)
    
    await state.set_state(AddProduct.price)


@dp.message(AddProduct.price, F.from_user.id == ADMIN)
async def product_price_handler(message: Message, state: FSMContext):
    price = message.text
    await message.answer("Mahsulot rasmini kiriting") 
    await state.update_data(price=price)
    
    await state.set_state(AddProduct.image)


@dp.message(AddProduct.image, F.content_type.in_({'photo'}), F.from_user.id == ADMIN)
async def rasm_handler(message: Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id=file_id)
    file_path = file.file_path
    destination = file_path.replace('photos', 'pictures') 
    await bot.download_file(file_path=file_path, destination=destination)
    
    data = await state.get_data()
    
    file_path = file_path.replace('photos', 'pictures') 

    category = data.get('category')
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')


    db.add_product(
        category_id=int(category),
        name=name,
        description=description,
        price=price,
        image=file_path
    )

    await message.answer('Mahsulot bazaga qo\'shildi') 
    await state.clear()
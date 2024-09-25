from aiogram import F
from aiogram.types import Message, FSInputFile,CallbackQuery
from aiogram.fsm.context import FSMContext

from loader import dp,db
from keyboards.default.level2_kb import buyurtma, aksya, manzil,ovqat_buyurtma,izoh,haqida,sozlamalar
from keyboards.default.default import menu_button
from keyboards.inline_keyboards.vakansiya_kb import make_vacancy_kb
from keyboards.default.categories_kb import get_categories_kb
from keyboards.default.product_kb import make_product_keyboard,make_card_sub_keyboard
from keyboards.inline_keyboards.product_inline import product_plus_minus,savat

from states.states_level import BuyurtmaBerishState

@dp.message(F.text =='🛍 Buyurtma berish')
async def buyurtma_berish(message: Message, state:FSMContext):
  await message.answer('Yetkazib berish turini tanlang' ,reply_markup=buyurtma())

@dp.message(F.text =='🎉 Aksiya')
async def aksiya(message: Message, state:FSMContext):
  await message.answer('Hozirgi vaqtda hech qanday aksiyalar yo\'q',reply_markup=aksya())

@dp.message(F.text =='🏘 Barcha fillallar')
async def barcha_fillallar(message: Message, state:FSMContext):
  await message.answer('Bizning filiallarimiz :',reply_markup= manzil())

@dp.message(F.text =='📋 Mening buyurtmalarim')
async def mening_buyurtmalarim(message: Message, state:FSMContext):
  await message.answer('Sizda buyurtmalar yo\'q', reply_markup=ovqat_buyurtma())

@dp.message(F.text =='✍🏻 Izoh qoldirish')
async def izoh_qoldirish(message: Message, state:FSMContext):
  await message.answer('Izoh qoldiring. Sizning fikringiz biz uchun muhim', reply_markup=izoh()) 

@dp.message(F.text =='💼 Vakansiyalar')
async def vakansiyalar(message: Message, state:FSMContext):
  vacancies = db.get_vacancies()
  await message.answer('💼 Vakansiyalar:')
  
  for title in vacancies:
    await message.answer(text=title[0],reply_markup=make_vacancy_kb(title[0]))

@dp.message(F.text =='ℹ️ Biz haqimizda')
async def biz_haqimizda(message: Message, state:FSMContext):
  file  = FSInputFile(path='photo.jpg')
  await message.answer_photo(photo=file,caption='🍟 Max Way \n☎️ Aloqa markazi: +998712005400',reply_markup=haqida())

@dp.message(F.text =='⚙️ Sozlamalar')
async def nastroyka(message: Message, state:FSMContext):
  await message.answer(text='Sozlamani tanlang', reply_markup=sozlamalar())

@dp.message(F.text == '⬅️ Orqaga')
async def orqaga(message: Message, state:FSMContext):
  await message.answer('🗂 | Asosiy menu',reply_markup=menu_button())


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


@dp.message(BuyurtmaBerishState.select_category)
async def get_product_category_handler(message:Message,state:FSMContext):
  category_name = message.text
  await state.update_data(category_name = category_name)
  
  await message.answer('Mahsulotni tanlang:',reply_markup=make_product_keyboard(category_name))
  await state.set_state(BuyurtmaBerishState.product)

async def calculate_price(price, quantity = 1):
  return price * quantity

@dp.message(F.text == '📥 Savat',BuyurtmaBerishState.product)
async def show_card_handler(message:Message,state: FSMContext):
  tg_id = message.from_user.id
  cards = db.get_user_card(tg_id)
  
  main_text = ''
  for card in cards:
    name, price, quantity = card
    main_text += f"{name} x {quantity} = {price*quantity}\n"
    
  await message.answer(main_text,reply_markup=savat())

@dp.message(BuyurtmaBerishState.product)
async def get_product_handler(message:Message, state:FSMContext):
  product_name = message.text
  name,description,price,image= db.get_product_by_name(product_name)
  
  data = await state.get_data()
  
  quantity = data.get('quantity')
  if not quantity: 
    quantity = 1
  
  jami = await calculate_price(price,quantity)
  await state.update_data(
    price = price,
    quantity = quantity,
    description = description,
    name = name
    )
  
  caption = F"{name}\n{description}\n\n{name}\n{price} x {quantity} = {jami}\numumiy: {jami}"
  photo_file = FSInputFile(path=image)
  
  await message.answer_photo(
    photo=photo_file,
    caption=caption,
    reply_markup=product_plus_minus()
  )


@dp.callback_query(F.data == "plus", BuyurtmaBerishState.product)
async def product_plus(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    quantity = data.get("quantity")
    price = data.get("price")
    name = data.get("name")
    description = data.get("description")
    quantity+=1

    await call.answer("Mahsulot savatga qo'shildi")
    await state.update_data(quantity=quantity)
    jami = await calculate_price(price, quantity)
    caption = f"{name}\n{description}\n\n{name} {price} x {quantity} = {jami}\nUmumiy: {jami}"
    await call.message.edit_caption(caption=caption, reply_markup=product_plus_minus(quantity))



@dp.callback_query(F.data == "minus", BuyurtmaBerishState.product)
async def product_plus(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    quantity = data.get("quantity")
    price = data.get("price")
    name = data.get("name")
    description = data.get("description")
    quantity = data.get("quantity")
    if quantity!=1:
        quantity-=1
        await state.update_data(quantity=quantity)
        
    jami = await calculate_price(price, quantity)
    
    await call.answer("Mahsulot savatdan o'chirildi")
    await state.update_data(quantity=quantity)
    caption = f"{name}\n{description}\n\n{name} {price} x {quantity} = {jami}\nUmumiy: {jami}"
    await call.message.edit_caption(caption=caption, reply_markup=product_plus_minus(quantity))


@dp.callback_query(F.data == 'add_to_card',BuyurtmaBerishState.product)
async def add_to_card_handler(call:CallbackQuery,state:FSMContext):
  data = await state.get_data()
  name = data.get('name')
  quantity = data.get('quantity')
  tg_id  = call.from_user.id
  
  
  db.add_to_card(name,quantity,tg_id)
  
  await call.message.answer('Mashulot bazaga qo\'shildi',reply_markup=make_card_sub_keyboard())
  
  await call.message.delete()

from aiogram import F
from aiogram.types import Message

from loader import dp
from keyboards.default.manzillar_kb import oldinga


@dp.message(F.text == '▶️ Oldinga')
async def old(message:Message):
  await message.answer('Bizning filiallarimiz :', reply_markup=oldinga())


@dp.message(F.text == 'MAX WAY ALAYSKIY manzil')
async def get_brench1(message:Message):
  await message.answer('📍 Filial:  MAX WAY ALAYSKIY \n\n🗺 Manzil:  проспект Амира Темура, 25 \n\n🏢 Orientir:  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude=41.34443 ,
    longitude=69.205021
  )

@dp.message(F.text == 'MAX WAY BERUNIY manzil')
async def get_brench2(message:Message):
  await message.answer('📍 Filial:  MAX WAY BERUNIY \n\n🗺 Manzil:    улица Беруни, 47, Ташкент  \n\n🏢 Orientir: Метро Беруний   \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.318379,
    longitude=69.280708
  )

@dp.message(F.text == 'MAX WAY AVIASOZLAR manzil')
async def get_brench3(message:Message):
  await message.answer('📍 Filial:  MAX WAY AVIOSAOZLAR \n\n🗺 Manzil:  улица Авиасозлар, 23  \n\n🏢 Orientir:  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.290894,
    longitude=69.342153
  )

@dp.message(F.text == 'MAX WAY RISOVIY manzil')
async def get_brench4(message:Message):
  await message.answer('📍 Filial:  MAX WAY RISOVIY \n\n🗺 Manzil:   Узбекистан, Ташкент, Алтынкульская улица, 10   \n\n🏢 Orientir: банкетный зал Тантана  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude=41.274899 ,
    longitude=69.309423
  )

@dp.message(F.text == 'MAX WAY PARUS manzil')
async def get_brench5(message:Message):
  await message.answer('📍 Filial:  MAX WAY PARUS \n\n🗺 Manzil:  улица Катартал, 60/5  \n\n🏢 Orientir: ТЦ Парус  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.293536,
    longitude=  69.212856
  )

@dp.message(F.text == 'MAX WAY PARKENT manzil')
async def get_brench6(message:Message):
  await message.answer('📍 Filial:  MAX WAY PARKENT \n\n🗺 Manzil:  улица Паркент, 30В, Ташкент \n\n🏢 Orientir: Паркентский рынок  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.314772,
    longitude=69.325067
  )

@dp.message(F.text == 'MAX WAY UNIVERSAM manzil')
async def get_brench7(message:Message):
  await message.answer('📍 Filial:  MAX WAY UNIVERSAM \n\n🗺 Manzil:  Узбекистан, Ташкент, проспект Амира Темура, 41/3  \n\n🏢 Orientir: Ориентир: Юнусабад Универсам  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.363468,
    longitude=69.288586
  )

@dp.message(F.text == 'MAX WAY ROYSON manzil')
async def get_brench8(message:Message):
  await message.answer('📍 Filial:  MAX WAY ROYSON \n\n🗺 Manzil:  Узбекистан, Ташкент, улица Заркайнар, 2  \n\n🏢 Orientir: Ориентир: Цирк  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.322643,
    longitude=69.241973
  )

@dp.message(F.text == 'MAX WAY MUQUMIY manzil')
async def get_brench9(message:Message):
  await message.answer('📍 Filial:  MAX WAY MUQUMIY \n\n🗺 Manzil:  улица Чиланзар, Ташкент \n\n🏢 Orientir: Ориентир: Чиланзар 1-й квартал  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.287875,
    longitude=69.229238
  )

@dp.message(F.text == 'MAX WAY GRAND MIR manzil')
async def get_brench10(message:Message):
  await message.answer('📍 Filial:  MAX WAY GRAND MIR \n\n🗺 Manzil:  Узбекистан, Ташкент, улица Шота Руставели, 9А  \n\n🏢 Orientir: Ориентир: Гостиница Гранд Мир  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.295095,
    longitude=69.267970
  )

@dp.message(F.text == 'MAX WAY SAYRAM manzil')
async def get_brench11(message:Message):
  await message.answer('📍 Filial:  MAX WAY SAYRAM \n\n🗺 Manzil:  Узбекистан, Ташкент, улица Юнусота  \n\n🏢 Orientir: Ориентир: Рынок сайрам.    \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.371941,
    longitude=69.310594
  )

@dp.message(F.text == 'MAX WAY MAKSIM GORKIY manzil')
async def get_brench12(message:Message):
  await message.answer('📍 Filial:  MAX WAY MAKSIM GORKIY \n\n🗺 Manzil: махалля Элобод  \n\n🏢 Orientir: Ориентир: Метро буюк ипак йули \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.327072,
    longitude=69.329893
  )

@dp.message(F.text == 'MAX WAY SERGELI manzil')
async def get_brench13(message:Message):
  await message.answer('📍 Filial:  MAX WAY SERGELI \n\n🗺 Manzil:  Узбекистан, Ташкент, Сергелийский район, массив Сергели-VIIIА, 11  \n\n🏢 Orientir: Ориентир: Сергели Дехкон Бозори \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.226369,
    longitude=69.219899
  )

@dp.message(F.text == 'MAX WAY FONTAN manzil')
async def get_brench14(message:Message):
  await message.answer('📍 Filial:  MAX WAY FONTAN \n\n🗺 Manzil:  проспект Амира Темура  \n\n🏢 Orientir: Ориентир: Юнусабадский рынок  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude= 41.362917,
    longitude=69.288864
  )

@dp.message(F.text == 'MAX WAY MINOR')
async def get_brench15(message:Message):
  await message.answer('📍 Filial:  MAX WAY MINOR  \n\n🗺 Manzil:  улица Осиё, 84А, Юнусабадский район, Ташкент   \n\n🏢 Orientir: бывший кинотеатр Казахстан  \n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00')
  await message.answer_location(
    latitude=41.328054,
    longitude=69.282584
  )
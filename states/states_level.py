from aiogram.fsm.state import State, StatesGroup


class BuyurtmaBerishState(StatesGroup):
    yetkazib_berish = State()
    olib_ketish = State()
    select_category = State()
    product = State()


class BarchaFiliallar(StatesGroup):
    choose_filial = State()


class VacancyState(StatesGroup):
    fio = State()
    phone_number = State()
    rezume = State()
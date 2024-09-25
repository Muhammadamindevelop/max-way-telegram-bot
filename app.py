import asyncio
import logging
import sys

    
from loader import dp, bot,db
import handlers.users.start_handler
import handlers.users.start_menu_hender
import handlers.users.olib_ketish
import handlers.users.manzillar
import handlers.users.back_button_handler    
import handlers.users.menu
import handlers.users.vacancy_handler
import handlers.admin.admin_handler

async def main() -> None:
    # db.create_users_table()
    # db.create_category_table()  
    # db.create_products_table()        
    db.create_vacancy_table()  
    db.create_cart_table()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

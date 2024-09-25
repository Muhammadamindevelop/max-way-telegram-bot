import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f"{item} = ?" for item in parameters])
        return sql, tuple(parameters.values())
    
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()

        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()

        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        
        connection.close()

        return data


    def create_users_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS users (
            tg_id INTEGER PRIMARY KEY,
            username VARHCAR(120),
            phone_number VARCHAR(20),
            first_name VARCHAR(120),
            last_name VARCHAR(120),
            language VARCHAR(2)
        )'''
        self.execute(sql)

    def create_category_table(self):
        sql = ''' CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(120)

        )'''
        self.execute(sql)

    def create_products_table(self):
        sql = ''' CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            description TEXT,
            price REAL,
            image VARCHAR(255),
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category(id)
        )'''
        self.execute(sql)
    
    def create_vacancy_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS vacancy(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100),
            is_active BOOLEAN DEFAULT TRUE
        )
        '''
        self.execute(sql)
    
    
    def create_cart_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS card(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            tg_id INTEGER,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
        '''
        self.execute(sql)
    
    
    
    def add_to_card(self,product_name,quantity,tg_id):
        sql = '''INSERT INTO card (product_id,quantity,tg_id) VALUES
        ((SELECT id FROM products WHERE name = ?),?,?)'''
        self.execute(sql, parameters=(product_name,quantity,tg_id,), commit=True)
    
    def delete_user_card(self,tg_id):
        sql='''DELETE FROM card WHERE tg_id = ?'''
        return self.execute(sql,parameters=(tg_id),commit=True)
    
    
    
    def add_vacancy(self,title):
        sql = '''INSERT INTO vacancy (title) VALUES (?)'''
        self.execute(sql, parameters=(title,), commit=True)

    
    def add_category(self, name):
        sql= '''INSERT INTO category (name) VALUES (?)'''
        self.execute(sql, parameters=(name,), commit=True)
    
    
    def add_product(self,category_id,name,description,price,image):
        sql = '''INSERT INTO products
            (name, description, price, image, category_id)
        VALUES
            (?,?,?,?,?)'''
        self.execute(
            sql,
            parameters=(name, description, price, image, category_id),
            commit=True)
    
    
    def add_user(self, tg_id: int, username: str, first_name: str, last_name: str, language: str = 'uz'):
        sql = '''
        INSERT OR IGNORE INTO users 
            (tg_id, username, first_name, last_name, language)
        VALUES
            (?, ?, ?, ?, ?)
        '''
        self.execute(
            sql, 
            parameters=(tg_id, username, first_name, last_name, language), 
            commit=True  
        )

    def update_language(self, language: str, tg_id:int):
        sql = ''' UPDATE users SET language = ? WHERE tg_id = ? '''
        self.execute(
            sql,
            parameters = (language, tg_id),
            commit=True
        )
    
    def get_categories(self):
        sql = '''SELECT name FROM category'''
        return self.execute(sql, fetchall=True)
    
    def get_vacancies(self):
        sql = '''SELECT title FROM vacancy WHERE is_active=1'''
        return self.execute(sql, fetchall=True)
    
    def get_categories_for_admin(self):
        sql = '''SELECT id, name FROM category'''
        return self.execute(sql, fetchall=True)
    
    def get_products_by_categoty_name(self,category_name):
        sql = '''SELECT name FROM products
        WHERE category_id = (SELECT id FROM category WHERE name=?)
        '''
        return self.execute(sql,parameters=(category_name,),fetchall=True)
    
    def get_product_by_name(self,product_name):
        sql ='''SELECT name,description,price,image
        FROM products
        WHERE name = ?
        '''
        return self.execute(sql ,parameters=(product_name,),fetchone=True) 
    
    def get_user_card(self,tg_id):
        sql = '''SELECT products.name, products.price, card.quantity
        FROM card 
        INNER JOIN products 
        ON products.id = card.product_id
        WHERE tg_id = ?'''
        return self.execute(sql, parameters=(tg_id,), fetchall=True)
    
    
    
def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")

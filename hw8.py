

import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)
    return conn


def create_products(conn,  products):
    try:
        sql = '''INSERT INTO  products 
        (product_title, price ,quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql,  products)
        conn.commit()
    except Error as e:
        print(e)
    return conn
def prducts(conn):
    create_products(conn,("Баклажаны",120.00,50))
    create_products(conn,("Брюква",200.00,97))
    create_products(conn,("Кабачки",58.00,360))
    create_products(conn,("Капуста белокочанная",158.20,30))
    create_products(conn,("Капуста квашеная",147.30,44))
    create_products(conn,("Капуста брюссельская",159.55,21))
    create_products(conn,("Капуста кольраби",197.14,23))
    create_products(conn,("Капуста краснокочанная",254.21,354))
    create_products(conn,("Капуста цветная",280.52,164))
    create_products(conn,("Картофель",50.15,543))
    create_products(conn,("Картофель молодой",80.56,450))
    create_products(conn,("Картофель сладкий(батат)",120.35,210))
    create_products(conn,("Лук зелёный",122.39,200))
    create_products(conn,("Лук - порей",198.45,154))
    create_products(conn,("Лук репчатый",134.98,112))

def delete_product(conn, id):
    try:
        sql = '''DELETE FROM  products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)
    return conn


def update_product_quantity(conn,  products):
    try:
        sql = '''UPDATE  products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql,  products)
        conn.commit()
    except Error as e:
        print(e)
    return conn

def update_product_price(conn,  products):
    try:
        sql = '''UPDATE  products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql,  products)
        conn.commit()
    except Error as e:
        print(e)
    return conn


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM  products '''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
    return conn

def select_all_products2(conn):
    try:
        sql = '''SELECT * FROM  products WHERE price < 100 and quantity > 5 '''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
    return conn

def select_all_products3(conn):
    try:
        sql = '''SELECT * FROM  products WHERE product_title LIKE "Картофель%"'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
    return conn



connection = create_connection("hw.db")

create_table_products = '''
CREATE TABLE  products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0

)
'''

if connection is not None:
    print("База данных подключена!")
    # prducts(connection)
    # update_product_quantity(connection, (12, 10))
    # update_product_price(connection, (45.37, 2))
    # delete_product(connection, 16)
    # select_all_products(connection)
    # select_all_products2(connection)
    select_all_products3(connection)



    # create_table(connection,create_table_products)

    print("Готово!")

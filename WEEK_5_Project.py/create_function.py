import pymysql
import os
# from prettytable import from_db_cursor
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
my_host = os.environ.get("mysql_host")
my_user = os.environ.get("mysql_user")
my_password = os.environ.get("mysql_pass")
my_database = os.environ.get("mysql_db")

# Establish a database connection


def create_new_product():

    connection = pymysql.connect(
    host=my_host,
    user=my_user,
    password=my_password,
    database=my_database
)

    product_name= str(input('enter product name: '))
    product_price=float(input('enter product price:'))

    cursor= connection.cursor()  
    sql='''INSERT into product (product_name, product_price) VALUES (%s,%s)'''
    val=(product_name, product_price)                                  
    cursor.execute(sql,val)
    connection.commit()
    # x=from_db_cursor(cursor.execute)

    print(cursor.rowcount, "record(s) affected")
    
    connection.close()
    

def create_new_courier():
    connection = pymysql.connect(
    host=my_host,
    user=my_user,
    password=my_password,
    database=my_database
)

    courier_name= input('enter courier name: ')
    courier_telephone=input('enter courier telephone:')

    cursor= connection.cursor()  
    sql='''INSERT into courier (courier_name, courier_telephone) VALUES (%s,%s)'''
    val=(courier_name, courier_telephone)                                  
    cursor.execute(sql,val)
    connection.commit()
    # x=from_db_cursor(cursor.execute)

    print(cursor.rowcount, "record(s) affected")
    
    connection.close()
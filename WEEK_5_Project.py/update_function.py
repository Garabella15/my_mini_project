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


def update_product():
    from display_table import print_product
    print_product()

    connection = pymysql.connect(
        host=my_host,
        user=my_user,
        password=my_password,
        database=my_database
    )

    
    product_id=int(input('enter product id:'))
    product_name=input('enter product name:')
    product_price=input('enter product price:')
    cursor= connection.cursor()  
    sql = f"UPDATE product set product_name = '{product_name}', product_price = {product_price} where product_id = {product_id} "
    cursor.execute(sql)  
    print(sql)
    connection.commit()  
    print(cursor.rowcount, "record(s) affected")                            
    connection.close()        



def update_courier():
    from display_table import print_courier
    print_courier()

    connection = pymysql.connect(
        host=my_host,
        user=my_user,
        password=my_password,
        database=my_database
    )

    
    courier_id=int(input('enter courier id:'))
    courier_name=input('enter courier name:')
    courier_telephone=input('enter courier phone number:')
    cursor= connection.cursor()  
    sql = f"update courier set courier_name = '{courier_name}', courier_telephone = '{courier_telephone}' where courier_id = {courier_id} "
    cursor.execute(sql)  
    print(sql)
    connection.commit()  
    print(cursor.rowcount, "record(s) affected")                            
    connection.close()        



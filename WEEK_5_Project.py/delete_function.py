# import the pymysql module
import pymysql
import os
from dotenv import load_dotenv
# from prettytable import from_db_cursor

    

# Load environment variables from .env file
load_dotenv()
my_host = os.environ.get("mysql_host")
my_user = os.environ.get("mysql_user")
my_password = os.environ.get("mysql_pass")
my_database = os.environ.get("mysql_db")
 

# Code for creating a connection object
                              

def delete_product():

        from display_table import print_product
        print_product()

        connection = pymysql.connect(
            host = my_host,
            user = my_user,
            password = my_password,
            database = my_database
        ) 

        product_id = int(input('enter product id:'))
        cursor= connection.cursor()                                     
        sql= f"Delete from product where product_id = {product_id}"
        cursor.execute(sql)
        connection.commit()
        
        print(cursor.rowcount, "record inserted.")   
        connection.close()                           

def delete_courier():
    from display_table import print_courier
    print_courier()

    connection = pymysql.connect(
        host = my_host,
        user = my_user,
        password = my_password,
        database = my_database
        ) 

    courier_id = int(input('enter courier id:'))
    cursor= connection.cursor()                                     
    sql= f'Delete from courier where courier_id = {courier_id}'
    cursor.execute(sql)
    connection.commit()
        
    print(cursor.rowcount, "record inserted.")   
    connection.close()  
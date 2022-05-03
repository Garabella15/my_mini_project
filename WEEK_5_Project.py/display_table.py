import pymysql
import os
import csv
from tabulate import tabulate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
my_host = os.environ.get("mysql_host")
my_user = os.environ.get("mysql_user")
my_password = os.environ.get("mysql_pass")
my_database = os.environ.get("mysql_db")

# Establish a database connection

def print_product():

    connection = pymysql.connect(
        host=my_host,
        user=my_user,
        password=my_password,
        database=my_database
    )

        
    cursor= connection.cursor()                                   
    cursor.execute('SELECT * FROM product')
    rows = cursor.fetchall()
    # for row in rows:
    #     print(f'{row[0]} {str(row[1])} {row[2]}')
    print(tabulate(rows, headers=["Name", "price"],tablefmt='grid'))
        
    connection.close()



def print_courier():
    
    connection = pymysql.connect(
        host=my_host,
        user=my_user,
        password=my_password,
        database=my_database
    )

        
    cursor= connection.cursor()                                   
    cursor.execute('SELECT * FROM courier')
    rows = cursor.fetchall()
    # for row in rows:
    #     print(f'{row[0]} {str(row[1])} {row[2]}')
    print(tabulate(rows, headers=["Name", "Telephone"],tablefmt='grid'))    
    connection.close()

def Print_Order():
    data = []
    with open('Order.csv', 'r') as file:     
        reader = csv.DictReader(file, delimiter = ",")       
        for row in reader: 
            data.append(row)                                                          
        print(tabulate(data, headers = "keys",tablefmt = 'grid'))  
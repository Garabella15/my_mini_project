# Example Python program to insert rows into a MySQL database table
import csv
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
my_host = os.environ.get("mysql_host")
my_user = os.environ.get("mysql_user")
my_password = os.environ.get("mysql_pass")
my_database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host=my_host,
    user=my_user,
    password=my_password,
    database=my_database
)

# try:
    # Create a cursor object
cursor= connection.cursor()                                     

    # the line of code is used to import CSV file into the table in Database
# csv_data = csv.reader(open('Product.csv'))
sql="""INSEERT INTO Product(product_name, product_price) VALUES('$product_name','$product_name')"""
# next(csv_data)
# for row in rows:
    # row=[None if cell == '' else cell for cell in row]
cursor.executemany(sql)

# connection.commit()
    
    # Get the primary key value of the last inserted row
    # print("Primary key id of the last inserted row:")
    # print(cursor.lastrowid)

    # SQL Query to retrive the rows
    # sqlQuery = "select * from Employee"   

    #Fetch all the rows - for the SQL Query
    # cursor.execute(sqlQuery)


    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

# except Exception as e:
#     print("Exeception occured:{}".format(e))

# finally:
cursor.close()

connection.close()
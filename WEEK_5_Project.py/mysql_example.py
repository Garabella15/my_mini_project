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

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Execute SQL query
# cursor.execute('SELECT * FROM product')
# cursor.execute('CREATE DATABAsE miniproject')
# sql=('CREATE TABLE courier (courier_id INT NOT NULL AUTO_INCREMENT, courier_name VARCHAR(225) NOT NULL,courier_telephone VARCHAR(225) NOT NULL, PRIMARY KEY (courier_id))')

# cursor.execute(sql)
# Gets all rows from the result
# rows = cursor.fetchall()
# for row in rows:
#     print(f'product_name: {str(row[0])}, product_price: {row[1]}')

# Can alternatively get one result at a time with the below code
# while True:
#     row = cursor.fetchone()
#     if row == None:
#         break
#     print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')
# Closes the cursor so will be unusable from this point 
cursor.close()

# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()
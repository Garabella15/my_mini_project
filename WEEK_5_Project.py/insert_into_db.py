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
    host = my_host,
    user = my_user,
    password = my_password,
    database = my_database
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Add code here to insert a new record
sql = '''INSERT into courier (courier_name, courier_telephone) VALUES (%s,%s)'''
# sql = '''CREATE TABLE product IF NOT EXIST (product_id INT NOT NULL AUTO_INCREMENT, 
# # # product_name VARCHAR(225) NOT NULL,
# # # product_name VARCHAR(225) 
# # # PRIMARY KEY (product_id)'''

val = [('Kelly','07564328232'),
('Alex','07566623498'),
('Jon','07565599730'),
('Xen','07799988811'),
('Billy','07564788869'),
('Maxs','07774300021')
]

cursor.executemany(sql,val)


connection.commit()
print(cursor.rowcount, "was inserted")
cursor.close()
connection.close()
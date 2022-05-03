
# import the mysql client for python

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



    # SQL query string

sqlQuery = "CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"   

 

    # Execute the sqlQuery

cursor.execute(sqlQuery)


    # SQL query string

sqlQuery = "show tables"   

    # Execute the sqlQuery

cursor.execute(sqlQuery)
 
    #Fetch all the rows

rows = cursor.fetchall()
for row in rows:

    print(row)

cursor.close()

connection.close()
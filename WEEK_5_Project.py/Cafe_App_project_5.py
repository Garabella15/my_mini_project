# this app displays menu and allow customer to view, update and delete product and courier

# import csv
# import CSV_write

print(f' ######### Welcome to Ray Cafe ###########')
print(f'#################################################')

def main_options (): 
    print(f'############## You are viewing the main menu ############################')
    print(
    '''
    0. exit the app 
    1. product_options 
    2. Courier_options
    3. Order_options    
    ''')

def product_options(): 
    print(f' ############## you are in the product menu #################')
    print(
    ''' 
    0. return to main menu 
    1. list product  
    2. Create new product 
    3. update product from list 
    4. delete product from list 
    ''')

def Courier_options(): 
    print(f' ############### you are in the Courier menu ################')
    print(
    ''' 
    0. return to main menu 
    1. list Courier  
    2. Create new Courier 
    3. update Courier from list 
    4. delete Courier from list  
    ''')

def Order_options(): 
    print(f' ############ You are in the Order menu ##############')
    print(
    ''' 
    0. return to main menu 
    1. Print Order list 
    2. Enter Customer details
    3. update existing Order Status 
    4. Update exiting Order
    5. delete Courier from Order list  
    ''')


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

cursor= connection.cursor()
while True:
    main_options()
    user_option = int(input('enter main option:'))
    if user_option == 0:
        print('exit the app')
        break


    elif user_option == 1:
        while True:
            product_options() 
            product_menu = int(input('enter order option: '))
            
            
            # Return to main menu
            if product_menu == 0:
                break

            # print prodict table
            elif product_menu == 1:
                from display_table import print_product
                print_product()

            # Create new product
            elif product_menu == 2:
                from create_function import create_new_product
                create_new_product()

            
            elif product_menu == 3:
                from update_function import update_product
                update_product()

            
            elif product_menu == 4:
                from delete_function import delete_product
                delete_product()

                
    elif user_option == 2:
        while True:
            Courier_options() 
            Courier_menu = int(input('enter order option: '))
            
            # Return to main menu
            if Courier_menu == 0:
                break

            # print Order list
            elif Courier_menu == 1:
                from display_table import print_courier
                print_courier()
                       

            # Add Customer Detail
            elif Courier_menu == 2:
                from create_function import create_new_courier
                create_new_courier()

           # updating the courier list
            elif Courier_menu == 3:
                from update_function import update_courier
                update_courier()

            elif Courier_menu == 4:
                from delete_function import delete_courier
                delete_courier()



    elif user_option == 3:
        while True:
            Order_options() 
            Order_menu = int(input('enter order option: '))
            
            # Return to main menu
            if Order_menu == 0:
                break

            # print Order list
            elif Order_menu == 1:
                from display_table import Print_Order
                Print_Order()
            

            # Add Customer Detail to order list
            elif Order_menu == 2:
                from create_order import create_order_list
                create_order_list()
                 
            # update the list of existing order status
            elif Order_menu == 3:
                from Update_Order_status import read_csv
                read_csv('Order.csv')
                print(f'Order status in the order list is updated')
            
            #update the exiting order list
            elif Order_menu == 4:
                from Update_Order_list import update_order
                update_order() 
            
            elif Order_menu == 5:
                from Delete_Order import read_csv
                order=read_csv('Order.csv')

        
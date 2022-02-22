import csv
import CSV_write


print(f' ######### Welcome to Ray Cafe ###########')
print(f'#################################################')

def main_options (): 
    print(f'#########################################################')
    print(
    '''
    0. exit the app 
    1. product_options 
    2. Courier_options
    3. Order_options    
    ''')

def product_options(): 
    print(
    ''' 
    0. return to main menu 
    1. list product  
    2. Create new product 
    3. update product from list 
    4. delete product from list 
    ''')

def Courier_options(): 
    print(
    ''' 
    0. return to main menu 
    1. list Courier  
    2. Create new Courier 
    3. update Courier from list 
    4. delete Courier from list  
    ''')

def Order_options(): 
    print(
    ''' 
    0. return to main menu 
    1. Print Order list 
    2. Enter Customer details
    3. update existing Order Status 
    4. Update exiting Order
    5. delete order from Order list  
    ''')


# Product = [
#     {'Name': 'water', 'price': 1.8},
#     {'Name': 'apple juice', 'price': 1.5},
#     {'Name': 'Mocha', 'price': 1.1},
#     {'Name': 'Orange juice', 'price': 1.2},
#     {'Name': 'White Tea', 'price': 1.67},
#     {'Name': 'Tea', 'price': 1.25},
#     {'Name': 'Coffee', 'price': 1.20}
# ]

Status= ['Received', 'Preparing', 'Out_for_delivery', 'Cancelled','Delivered']

# Courier = [
#     {'Name': 'John', 'telephone': "0789887889"}, {'Name': 'Kelly', 'telephone': "07564328232"},
#     {'Name': 'Alex', 'telephone': "07566623498"}, {'Name': 'Jon', 'telephone': "07565599730"},
#     {'Name': 'James', 'telephone': "07564887744"}
# ]

while True:
    main_options()
    user_option = int(input('enter main option:'))
    if user_option == 0:
        #CSV_write.write_list_of_product_dict_to_csv('Product.csv', Product)
        # CSV_write.write_list_of_Courier_dict_to_csv('Courier.csv', Courier)
        print('exit the app')
        break


    elif user_option == 1:
        while True:
            product_options() 
            product_menu = int(input('enter order option: '))
            
            # Return to main menu
            if product_menu == 0:
                break

            # print prodict list
            elif product_menu == 1:
                import read_file_to_list
                read_file_to_list.read_csv()
             

            # Create new product
            elif product_menu == 2:
                from New_product import create_new_product
                create_new_product()

            
            elif product_menu == 3:
                from Update_product import update_product_list
                update_product_list()

            
            elif product_menu == 4:
                from delete_product import read_csv
                product=read_csv('Product.csv')

                
    elif user_option == 2:
        while True:
            Courier_options() 
            Courier_menu = int(input('enter order option: '))
            
            # Return to main menu
            if Courier_menu == 0:
                break

            # print Order list
            elif Courier_menu == 1:
                import read_file_to_list
                Courier=read_file_to_list.read_courier_csv()
                       

            # Add Customer Detail
            elif Courier_menu == 2:
                from New_Courier import create_new_Courier
                Courier_list=create_new_Courier()

           # updating the courier list
            elif Courier_menu == 3:
                from update_Courier import update_courier_list
                update_courier_list()

            elif Courier_menu == 4:
                from delete_Courier import read_csv
                courier=read_csv('Courier.csv')



    elif user_option == 3:
        while True:
            Order_options() 
            Order_menu = int(input('enter order option: '))
            
            # Return to main menu
            if Order_menu == 0:
                break

            # print Order list
            elif Order_menu == 1:
                from read_file_to_list import read_csv_order
                read_csv_order()
            

            # Add Customer Detail to order list
            elif Order_menu == 2:
                from Customer_detail import create_order_list
                create_order_list()
                
                
            # update the list of existing order status
            elif Order_menu == 3:
                from Update_Order_status import read_csv
                read_csv('Order.csv')
            
            #update the exiting order list
            elif Order_menu == 4:
                from Update_Order_list import update_order
                update_order() 
            
            elif Order_menu == 5:
                from Delete_Order import read_csv
                order=read_csv('Order.csv')


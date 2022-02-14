import csv

print(f' Welcome to Ray Cafe')
print(f'#################################################')

def main_options (): 
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
    5. delete Courier from Order list  
    ''')







elif user_option == 3:
        while True:
            Order_options() 
            Order_menu = int(input('enter order option: '))
            
            # Return to main menu
            if Order_menu == 0:
                break

            # print Order list
            elif Order_menu == 1:
                from Order_status import read_csv
                Order_list=read_csv()
                print(Order_list)

            # Add Customer Detail
            elif Order_menu == 2:
                # from Create_Order_list import create_order_list
                # create_order_list()
                # Order_list.append(Current_Order_list_dictionary)
                input_customer_name = str(input('enter name:'))
                input_customer_address = str(input('enter address:'))
                input_customer_telephone = str(input('enter telephone:'))
                
                from customer_detail import return_list
                Courier_list = return_list('Courier.txt')
                # input_index= int(input('enter index of courier:'))

                index = 0

                for courier in Courier_list:
                    print(index, courier)
                    index +=1
                    
                    # print('courier:', courier, " index ", Courier_list.index(courier) ) 

                input_index= int(input('enter index of courier:'))
                # Order_list
                
                Current_Order_list_dictionary ={'customer name': input_customer_name, 'customer address': input_customer_address,
                'customer telephone': input_customer_telephone, 'courier number': input_index, 'order status': 'preparing'}
                Order_list.append(Current_Order_list_dictionary)
                print(Order_list)

                keys = Order_list[0].keys()
                with open('Order.csv', mode = 'w') as file:
                    fieldname =['customer name', 'customer address', 'customer telephone', 'courier number', 'order status']
                    writer=csv.DictWriter(file, fieldnames=fieldname)
                    writer.writeheader()
                    writer.writerows(Order_list)
                    # writer.writerows(map(Order_list))
                


            elif Order_menu == 3:
                from Update_Order_list import update_order
                update_order(Order_list)
                print(Order_list)
                input_order_index=int(input('enter order index: '))


                for index, status in enumerate(Order_status):
                    print(index, status)
                
                input_order_status_index=int(input('enter index of order status:'))
                Order_list[input_order_index]['order status'] = Order_status[input_order_status_index]
                
                from Order_status import write_csv
                Order=write_csv('Order.csv', Order_list)
                print(Order)
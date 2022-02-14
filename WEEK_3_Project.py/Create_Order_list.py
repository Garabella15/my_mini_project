def create_order_list():
    Order_list = {}
    input_customer_name = str(input('enter name:'))
    input_customer_address = str(input('enter address:'))
    input_customer_telephone = str(input('enter telephone:'))
	
    from customer_detail import return_list
    Courier_list = return_list('Courier.txt')

    for courier in Courier_list:
        print('courier :', courier,  " courier number ", Courier_list.index(courier))
        input_courier_index= int(input('enter index of courier:'))
                
                
    Current_Order_list_dictionary ={'customer name': input_customer_name, 
                                'customer address': input_customer_address,
                                'customer telephone': input_customer_telephone, 
                                'courier number': input_courier_index, 
                                'order status': 'preparing'}
                
    Order_list.append(Current_Order_list_dictionary)







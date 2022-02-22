import csv
def create_order_list():
    Order=[]
    input_customer_name = str(input('enter name:'))
    input_customer_address = str(input('enter address:'))
    input_customer_telephone = str(input('enter telephone:'))
                
    from read_file_to_list import read_courier_csv
    Courier_list = read_courier_csv()
                

    # index = 0

    # for courier in Courier_list:

    #     print(index, courier)
    #     index +=1


    input_index= int(input('enter index of courier:'))
            
                
    Current_Order_list_dictionary ={'customer name': input_customer_name, 'customer address': input_customer_address,
                'customer telephone': input_customer_telephone, 'courier number': input_index, 'status': 'preparing'}

    Order.append(Current_Order_list_dictionary)


    keys = Order[0].keys()
    with open('Order.csv', mode = 'a', newline ='') as file:
        fieldname =['customer name', 'customer address', 'customer telephone', 'courier number', 'status']
        writer=csv.DictWriter(file, fieldnames=fieldname)
        writer.writerows(Order)










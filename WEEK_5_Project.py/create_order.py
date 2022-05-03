import csv
def create_order_list():
    Order=[]
    input_customer_name = str(input('enter name:'))
    input_customer_address = str(input('enter address:'))
    input_customer_telephone = str(input('enter telephone:'))

    product_index=[]
    from read_file_to_list import read_product_csv_with_index
    read_product_csv_with_index()

    x, y, z= input('enter product index:').split(',')
    product_index.append(x)
    product_index.append(y)
    product_index.append(z)
    print(product_index)
                
    from read_file_to_list import read_courier_csv
    read_courier_csv()
        
    input_index= int(input('enter index of courier:'))


    Statuses = ['Received', 'Preparing', 'Out_for_delivery', 'Cancelled','Delivered']

    for index, status in enumerate(Statuses):
        print(index, status)
    print(f'Order status is updated as Received')
    input_status_index=Statuses[0]

                
    Current_Order_list_dictionary ={'customer name': input_customer_name, 'customer address': input_customer_address,
                'customer telephone': input_customer_telephone, 'courier number': input_index, 'status': input_status_index,
                'product': product_index}

    Order.append(Current_Order_list_dictionary)

    keys = Order[0].keys()
    with open('Order.csv', mode = 'a', newline ='') as file:
        fieldname =['customer name', 'customer address', 'customer telephone', 'courier number', 'status','product']
        writer=csv.DictWriter(file, fieldnames=fieldname)
        # writer.writeheader()
        writer.writerows(Order)




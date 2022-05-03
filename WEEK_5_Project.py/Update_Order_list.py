import csv
from pprint import pp
import CSV_write

def update_order():
    from read_file_to_list import read_csv_Order_with_index
    read_csv_Order_with_index()
    
    order=[]
    input_order_index = int(input('enter index of order:'))

    print(f'####### enter customer information #######')

    input_customer_name= str(input('enter customer name:'))
    input_customer_address=str(input('enter customer address:'))
    input_telephone_number=str(input('enter telephone number:'))

    if input_order_index == 0:
        print(f'do not update this property')

    else:

        with open('Order.csv', 'r') as file:      
            reader = csv.DictReader(file)   
            next(reader)
            number = 1    
        
        for row in reader:
            if number == input_order_index:
                row.update({'customer name':input_customer_name, 'customer addresss': input_customer_address,
                'customer telephone':input_telephone_number})                    
                # product_dict={'Name': product[0],'price':product[1]}
            # print(product)            
            order.append(order)
            number += 1
       # pp(product_list)
        CSV_write.write_list_of_order_to_csv_file('Order.csv', order)

        # with open('Order.csv', mode ='w', newline='') as file:
        #     fieldnames = ['customer name', 'customer address', 'customer telephone', 'courier number', 'status','product']
        #     writer = csv.DictWriter(file, fieldnames=fieldnames)
        #     # writer.writeheader()
        #     writer.writerows(order)
            
    print(f'the order list is updated')



                
    


    
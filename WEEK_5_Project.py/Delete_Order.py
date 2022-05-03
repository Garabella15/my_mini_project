import csv
import CSV_write
def read_csv(file_name):
    order = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            order.append(row)
    print (order)

    for index, row in enumerate(order):
        print(index, row)
    input_order_index=int(input('enter index of order:'))
    order.pop(input_order_index)

    CSV_write.write_list_of_order_to_csv_file('Order.csv', order)
    # with open(file_name, mode ='w') as file:
    #     fieldnames = ['customer name','customer address','customer telephone','courier number','status','product']
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerows(order)
    #     print(order)  





import csv
def read_csv(file_name):
    order=[]
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            order.append(row)
    print (order)

    for index, row in enumerate(order):
        print(index, row)

    input_order_index=int(input('enter index of product:'))

    Statuses = ['Received', 'Preparing', 'Out_for_delivery', 'Cancelled','Delivered']

    for index, status in enumerate(Statuses):
        print(index, status)
    
    input_status_index=int(input('enter order status:'))

    order[input_order_index]['status']=Statuses[input_status_index]
    

    with open(file_name, mode ='w') as file:
        
        fieldnames = ['customer name','customer address','customer telephone','courier number','status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(order)
        print(order)  


read_csv('Order.csv')



# customer name, customer address, customer telephone, courier number, status
# Molly, 346 Hollow ways, Oxford, OX3 1PP, 07983265312, 5, Cancelled
# Raymond, 18 Bayswater Crescentt, Leeds, LS5 8QG, 07653218221, 0, delivered
# Rita, 42 woodsley road, Leeds, LS3 1DT, 0746532341, 3, preparing
# Chris, 123 limewalk street, Guildford, GU1 1P, 07655889921, 1, preparing
# mike, 53 lime grove, Oxford, OX3 7LP, 07990023657, 5, preparing

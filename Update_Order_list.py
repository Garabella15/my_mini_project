def update_order_list():
    import csv
    index = 0
    with open('Order.csv', 'r') as file:
        Order_list=csv.reader(file)
        for row in Order_list:
            print(index, row)
            index +=1





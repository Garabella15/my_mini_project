def order_status():
    import csv
    index = 0
    with open('Order_status', 'r') as file:
        Order_list=csv.reader(file)
        for row in Order_list:
            print(index, row)
            index +=1
input_Order_status_index=int(input('enter index of order status'))
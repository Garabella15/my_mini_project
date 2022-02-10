def update_order_list():
    import csv
    index = 0
    with open('Order.csv', 'r') as file:
        Order_list=csv.DictReader(file)
        for row in Order_list:
            print(index, row)
            index +=1

input_order_index= int(input('enter index of Order list: '))



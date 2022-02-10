def order_status():
    import csv
    index = 0
    with open('Order_status.csv', 'r') as file:
        Order_status=csv.reader(file)
        # Order_list=[]
        for row in Order_status:
            print(index, row)
            # print(Order_list)
            index +=1

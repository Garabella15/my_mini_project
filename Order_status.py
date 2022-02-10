def order_status():
    import csv
    # index = 0
    # with open('Order_status.csv', 'r') as file:
    #     Order_status=csv.reader(file)
    #     # Order_list=[]
    #     for row in Order_status:
    #         print(index, row)
    #         # print(Order_list)
    #         index +=1
    with open ('Order_status.csv', newline = '') as file:
        reader = csv.reader(file)
        

        Order_status=[]
        for row in reader:
            Order_status.append(row[:])
        

    for row_num, rows in enumerate(Order_status):
        print('data in row number {} is {}'.format(row_num+1, rows))
    
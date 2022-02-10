def update_order_list():
    import csv
    # index = 0
    # with open('Order.csv', 'r') as file:
    #     Order_list=csv.reader(file)
    #     for row in Order_list:
    #         print(index, row)
    #         index +=1
    with open ('Order.csv', newline = '') as file:
        reader = csv.reader(file)
        headings = next(reader)

        Order_list=[]
        for row in reader:
            Order_list.append(row[:])
        

    for row_num, rows in enumerate(Order_list):
        print('data in row number {} is {}'.format(row_num+1, rows))
    print('headers were: ', headings)
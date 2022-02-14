def update_order(Order_list):
    from Order_status import read_csv
    Order= read_csv()
    for index, order in enumerate(Order_list):
        print(index, order)
    return(Order)


    
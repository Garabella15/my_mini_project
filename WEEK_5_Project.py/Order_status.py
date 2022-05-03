import csv
def read_order_status_csv():
    with open('Order_status.csv', 'r') as file:      
         reader = csv.reader(file, delimiter = ',')
         index =0       
         for index,row in reader:                                                            
            print(row, index)
            index +=1

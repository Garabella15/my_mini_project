import csv
def read_csv():
    with open('Product.csv', 'r') as file:      
         reader = csv.reader(file, delimiter = ",")       
         for row in reader:                                                            
            print(row)
    
def read_courier_csv_file():
    with open('Courier.csv', 'r') as file:      
         reader = csv.reader(file, delimiter = ",")       
         for row in reader:                                                            
            print(row)

def read_index_value_csv():
    with open('Product.csv', 'r') as file:      
         reader = csv.reader(file)       
         for index, product in enumerate(reader):                                                            
            print(index, product)

def read_courier_csv():
    with open('Courier.csv', 'r') as file:      
         reader = csv.reader(file)       
         for index, Courier in enumerate(reader):                                                            
            print(index, Courier)


def read_csv_order():
    with open('Order.csv', 'r') as file:      
         reader = csv.reader(file, delimiter=',')       
         for row in reader:                                                            
            print(row)


def read_csv_Order_with_index():
    with open('Order.csv', 'r') as file:      
         reader = csv.reader(file)       
         for index, order in enumerate(reader):                                                           
            print(index,order)

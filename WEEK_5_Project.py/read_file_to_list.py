import csv
# from tubulate import tubulate
def read_csv():
    product=[]
    with open('Product.csv', 'r') as file:   
         reader = csv.DictReader(file, delimiter = ",")       
         for row in reader:                                                            
            print(row)
    
def read_courier_csv_file():
    with open('Courier.csv', 'r') as file:      
         reader = csv.reader(file, delimiter = ",")       
         for row in reader:                                                            
            print(row)

def read_product_csv_with_index():
    with open('Product.csv', 'r') as file:      
         reader = csv.reader(file)       
         for index, product in enumerate(reader):                                                            
            print(index, product)

def read_courier_csv():
    with open('Courier.csv', 'r') as file:      
         reader = csv.reader(file)       
         for index, Courier in enumerate(reader):                                                            
            print(index, Courier)


# def read_csv_order():
#     with open('Order.csv', 'r') as file:     
#         reader = csv.reader(file, delimiter=',')       
#         for row in reader:                                                            
#             print(row)  


def read_csv_Order_with_index():
    with open('Order.csv', 'r') as file:      
         reader = csv.reader(file)       
         for index, order in enumerate(reader):                                                           
            print(index,order)

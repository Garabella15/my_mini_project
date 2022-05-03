from tabulate import tabulate
import csv


def read_csv_order():
    data =[]
    with open('Order.csv', 'r') as file:     
        reader = csv.DictReader(file, delimiter =",") 
        for row in reader:  
            data.append(row)                                                        
        print(tabulate(data, headers = "keys", tablefmt ='grid'))

read_csv_order()
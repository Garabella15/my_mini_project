import csv
def read_csv():
    
    Order=[]
    with open('Order.csv') as file:
        reader=csv.DictReader(file)
        for row in reader:
            Order.append(row)
    return Order

def write_csv(filename, Order):
    with open(filename, mode = 'w') as file:
        writer=csv.DictWriter(file, fieldnames=Order[0].keys()) 
        writer.writeheader()
        writer.writerows(Order)
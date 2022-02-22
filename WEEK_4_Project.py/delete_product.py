import csv
def read_csv(file_name):
    product = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            product.append(row)
    print (product)

    for index, row in enumerate(product):
        print(index, row)
    input_product_index=int(input('enter index of product:'))
    product.pop(input_product_index)

    with open(file_name, mode ='w') as file:
        
        fieldnames = ['Name', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(product)
        print(product)





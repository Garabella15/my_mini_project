import csv
from pprint import pp
import CSV_write
def update_product_list (): 
    from read_file_to_list import read_index_value_csv
    read_index_value_csv()
    
    product_list=[]
    input_product_index = int(input('enter index of product:'))

    print(f'enter product name and price')

    input_product_name= str(input('enter product name:'))
    input_product_price=str(input('enter price of product:'))

    if input_product_index == 0:
        print(f'do not update this property')

    else:
        with open('Product.csv', 'r') as file:      
         reader = csv.DictReader(file)   
         next(reader)
         number = 1    
        
         for product in reader:
             if number == input_product_index:
                 product.update({'Name':input_product_name,'price':input_product_price})                    
                # product_dict={'Name': product[0],'price':product[1]}
            # print(product)            
             product_list.append(product)
             number += 1
       # pp(product_list)
        with open('Product.csv', mode ='w', newline='') as file:
        
            fieldnames = ['Name', 'price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(product_list)
            

    # CSV_write.write_list_of_product_dict_to_csv('Product.csv', product_list)
    print(f'the product list is updated')


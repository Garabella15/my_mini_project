import csv
from pprint import pp
import CSV_write
def update_courier_list (): 

    from read_file_to_list import read_courier_csv
    read_courier_csv()
    
    Courier_list=[]
    input_Courier_index = int(input('enter index of courier:'))

    print(f'enter courier name and telephone number')

    input_Courier_name= str(input('enter Courier name:'))
    input_telephone_number=str(input('enter telephone number:'))

    if input_Courier_index == 0:
        print(f'do not update this property')

    else:
        with open('Courier.csv', 'r') as file:      
         reader = csv.DictReader(file)   
         next(reader)
         number = 1    
        
         for courier in reader:
             if number == input_Courier_index:
                 courier.update({'Name':input_Courier_name,'telephone':input_telephone_number})                    
                # product_dict={'Name': product[0],'price':product[1]}
            # print(product)            
             Courier_list.append(courier)
             number += 1
       # pp(product_list)
        with open('Courier.csv', mode ='w', newline='') as file:
        
            fieldnames = ['Name', 'telephone']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(Courier_list)
            


    print(f'the product list is updated')


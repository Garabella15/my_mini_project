import csv



def write_list_of_product_dict_to_csv(filename, Product_list):
    with open(filename, mode ='w') as file:
        
        fieldnames = ['Name', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(Product_list)
        return Product_list


def write_list_of_Courier_dict_to_csv(filename, Courier_list):
    with open(filename, mode ='w') as file:
        
        fieldnames = ['Name', 'telephone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(Courier_list)
        return Courier_list


    



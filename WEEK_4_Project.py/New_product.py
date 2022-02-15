def create_new_product():
    import csv
    import CSV_write
    
    input_Product_name = str(input('enter name of product:'))
    input_Product_price = str(input('enter price of product:'))

    from read_file_to_list import read_csv
    Product_list = read_csv('Product.csv')
    
    Product_list_dictionary ={'Name': input_Product_name, 
                                'price': input_Product_price}
                                
    Product_list.append(Product_list_dictionary)   

    CSV_write.write_list_of_product_dict_to_csv('Product.csv', Product_list)
    
    print(Product_list)


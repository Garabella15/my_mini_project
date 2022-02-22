def create_new_product():
    import csv
    import CSV_write
    

    from read_file_to_list import read_csv
    read_csv()
    Product =[]
    input_Product_name = str(input('enter name of product:'))
    input_Product_price = float(input('enter price of product:'))

    
    Product_list_dictionary ={'Name':input_Product_name, 'price' :input_Product_price}
                                
    Product.append(Product_list_dictionary)   

    CSV_write.Append_new_product_to_csv_file('Product.csv', Product)
    
    print(Product)


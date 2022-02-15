def update_product_list (): 
    from read_file_to_list import read_csv
    product = read_csv('Product.csv')
    for index, item in enumerate(product):
        print(index, item)

        input_product_index = int(input('enter index of product:'))
        
        for input_product_name, input_product_price in enumerate (input_product_index):
    
            input_product_name= str(input('enter product name:'))
            input_product_price=str(input('enter price of product:'))

        if input_product_name == 0:
            if  input_product_price == 0:
                print(f' do not update this property')
            else:
                print(f'the product list is updated')
# the line of creates a welcome page on the app
print('Welcome to Ray Cafe')
while True:
        print('main menu option')
        print('0. exit the app')
        print('1. go to product menu')
        product_list =['water', 'orange_juice', 'apple_juice', 'coffee', 'Tea', 'soft drink']
        main_user_input = int(input('enter menu option: '))
        if main_user_input == 0:
                print('exit the app')
                break
        elif main_user_input == 1:
                print('product menu option')

                while True:
                        print('0. return to main menu option')
                        print('1. print product list')
                        print('2. create a new product')
                        print('3. update existing product list')
                        print('4. delete product')
                        user_product_input = int(input('enter product menu option:'))
                        if user_product_input == 0:
                                print('return to main menu option')
                                break
                        elif user_product_input == 1:
                                print(f'list of product {product_list}')
                        elif user_product_input == 2:
                                print('create new product')
                                user_new_product_input=str(input('enter new product:'))
                                product_list.append(user_new_product_input)
                                print(f' print new product list {product_list}')
                        elif user_product_input == 3:
                                product_index = int(input('enter the index of the product:'))
                                product_list[product_index]=input('enter new product:')
                                print(f' print update product list {product_list}')             
                        elif user_product_input == 4:
                                product_index_option = int(input('enter product index:'))
                                del product_list[product_index_option]
                                print(f'print the new product list {product_list}')
                                break
print('Good bye')





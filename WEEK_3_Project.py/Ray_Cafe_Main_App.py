# the following line of code is used to navigate the product and courier main of Ray's Cafe.it
# allows for creating, updating and deleting product and courier in addition to data persistence.


print(f' Welcome to Ray Cafe')

def main_options (): 
    print(
    '''
    0. exit the app 
    1. product_options 
    2. Courier_options
    3. Order_options    
    ''')

def product_options(): 
    print(
    ''' 
    0. return to main menu 
    1. list product  
    2. Create new product 
    3. update product list 
    4. delete product  
    ''')

def Courier_options(): 
    print(
    ''' 
    0. return to main menu 
    1. list Courier  
    2. Create new Courier 
    3. update Courier list 
    4. delete Courier  
    ''')

def create_new_product():
    input_new_product=input('enter new product:')
    add_product_to_file('product.txt', input_new_product)
    # print_product_list() function that prints out product list


def update_product_list (): 
    product_list = display('product.txt')
    product_index= int(input('enter the index of the product:'))
    new_product_name=input('enter another product:')
    product_list[product_index] = new_product_name + '\n'

    with open('product.txt', 'w') as file:
	    file.writelines(product_list)
    



def delete_product_from_list ():
    product_list = display('product.txt')
    input_product_index = int(input('enter product index:'))
    product_list.pop(input_product_index)
    
    with open('product.txt', 'w') as file:
	    file.writelines(product_list.pop)


 


def display(filename):
    # filename = input('Enter name of File: ')
    content_list = []
    # try:
    fo = open(filename, "r")
    lines = fo.readlines()
    for line in lines:
        if line.strip() == "":
            continue
        else:
            content_list.append(line.strip())
    print(content_list)
    return lines
    # except FileNotFoundError as fnfe:
    #     print('Unable to open file: ' + str(fnfe))




def add_product_to_file(filename, product_name):
    
    fd = open(filename, "a+")
    fd.seek(0)
    data = fd.read(100)
    if len(data) > 0:
        fd.write("\n")

    fd.write(product_name)
    fd.close()

# Start Main Menu
while True:
    main_options()
    user_option = int(input('enter main option:'))
    if user_option == 0:
        print('exit the app')
        break
    
    # Enter Product Menu
    elif user_option == 1:
        while True:
            product_options()
            product_menu = int(input('enter product options:'))
            
            # Return to main menu
            if product_menu == 0:
                break

            # Return product list
            elif product_menu == 1:
                product_list = display('product.txt')

            # Create new product 
            elif product_menu == 2:
                create_new_product()
                
                
            # Return updated product list
            elif product_menu == 3:
                update_product_list()
                
            
            # delete item in product list
            elif product_menu == 4:
                Amended_product_list = delete_product_from_list()
                break
                
#enter Courier menu
    # elif user_option == 2: 

    #     while True:
    #         Courier_options()
    #         courier_menu = int(input('enter courier options:'))

    #         # return to main menu
    #         if courier_menu== 0:
    #             break

    #         # print Courier list
    #         elif courier_menu == 1:
    #             Courier_list = display('Courier.txt')
    #             continue
    #         # create new Courier 
    #         elif courier_menu == 2:
    #            import  Create_new_courier.py
                
    #         elif courier_menu == 3:
    #             update_courier_list = item_update()
            
    #         elif courier_menu == 4:
    #             Amended_courier_list = delete_item_list()
                break

# print ('good bye')


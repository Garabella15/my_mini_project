# the following line of code is used to navigate the product and courier main of Ray's Cafe.it
# allows for creating, updating and deleting product and courier in addition to data persistence.


from delete_Courier import delete_Courier_list


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
    3. update product from list 
    4. delete product from list 
    ''')

def Courier_options(): 
    print(
    ''' 
    0. return to main menu 
    1. list Courier  
    2. Create new Courier 
    3. update Courier from list 
    4. delete Courier from list  
    ''')

def Order_options(): 
    print(
    ''' 
    0. return to main menu 
    1. Print Dictionary  
    2. Enter Customer details
    3. update existing Order Status 
    4. Update exiting Order
    5. delete Courier from Order list  
    ''')


Order_list = {}

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
                from New_product import create_new_product
                create_new_product()
                
                
            # Return updated product list
            elif product_menu == 3:
                from Update_product import update_product_list
                update_product_list()
                
            
            # delete item in product list
            elif product_menu == 4:
                from delete_product import delete_product_from_list
                delete_product_from_list()
                break
                

#enter Courier menu
    elif user_option == 2: 
        while True:
            Courier_options()
            courier_menu = int(input('enter courier options:'))

            # return to main menu
            if courier_menu == 0:
                break

            # print Courier list
            elif courier_menu == 1:
                Courier_list = display('Courier.txt')
                
            # create new Courier 
            elif courier_menu == 2:
                from  Create__Courier import create_new_Courier
                create_new_Courier()
                

            # updating the courier list     
            elif courier_menu == 3:
                from update_Courier import update_Courier_list
                update_Courier_list()

            # delete item from the courier list
            elif courier_menu == 4:
                from delete_Courier import delete_Courier_list
                delete_Courier_list()
                break
    

    elif user_option == 3:
        while True:
            Order_options() 
            Order_menu = int(input('enter order option: '))
            
            # Return to main menu
            if Order_menu == 0:
                break

            # print Order list
            elif Order_menu == 1:
                print(Order_list)

            # Add Customer Detail
            elif Order_menu == 2:
                Add_Customer_info = input('enter Customer info:')

            
print ('good bye')


def update_product_list (): 
    product_list = display('product.txt')
    product_index= int(input('enter the index of the product:'))
    new_product_name=input('enter another product:')
    product_list[product_index] = new_product_name + '\n'

    with open('product.txt', 'w') as file:
	    file.writelines(product_list)



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
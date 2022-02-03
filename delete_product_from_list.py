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
def create_new_product():
    input_new_product=input('enter new product:')
    add_product_to_file('product.txt', input_new_product)


def add_product_to_file(filename, product_name):
    
    fd = open(filename, "a+")
    fd.seek(0)
    data = fd.read(100)
    if len(data) > 0:
        fd.write("\n")

    fd.write(product_name)
    fd.close()


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
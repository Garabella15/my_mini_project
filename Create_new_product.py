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
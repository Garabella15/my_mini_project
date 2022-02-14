def create_new_Courier():
    input_new_Courier=input('enter new Courier:')
    add_Courier_to_file('Courier.txt', input_new_Courier)


def add_Courier_to_file(filename, product_name):
    
    fd = open(filename, "a+")
    fd.seek(0)
    data = fd.read(100)
    if len(data) > 0:
        fd.write("\n")

    fd.write(product_name)
    fd.close()    
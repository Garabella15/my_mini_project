# people = ["john", "Rose", "Rita", "kate", "Alex", "Ray", "Jon"]
# people_index = int(input('enter the index of the person:'))
# del people[people_index]
# print(people)

# def my_function(name):
#     print(name)

# my_function('steven')

# def read_file():
#     product_list = []

# file = open('product.txt', "r")
# lines = file.readlines()
# for line in lines:
#     if line.strip() == "":
#         continue
#     else:
#         product_list.append(line.strip())
#     print(product_list) 

# def main_content(file_content):
#     main_content = []

#     for line in file_content:
#         main_content.append(line.strip())
#         return main_content

# file_name= open ('product.txt')
# read_file('Courier.txt')


# opening and appending text in a python file.
# file_object = open('product.txt', 'a')
# file_object.write('cranberry' + '\n')
# file_object.close()


# Open the file in append & read mode ('a+')
# def new_item(file_object):
#     with open("product.txt", "a+") as file_object:
#         file_object.seek(0)
#         data = file_object.read(100)
#         if len(data) > 0:
#             file_object.write("\n")
#             file_object.write("Cranberry")
# 




# def file_read(fname):
#         from itertools import islice
#         with open(fname, "w") as myfile:
#                 myfile.write("Python Exercises\n")
#                 myfile.write("Java Exercises")
#         txt = open(fname)
#         print(txt.read())
# file_read('abc.txt')



  




# def read_product_to_list('Courier.txt'):

# with open('Courier.txt', 'r') as file:
# 	product_name = file.readlines()

# print(product_name)
# product_name[4] = "Sara\n"

# with open('Courier.txt', 'w') as file:
# 	file.writelines(product_name)

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
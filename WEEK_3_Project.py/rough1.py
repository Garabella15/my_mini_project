# print("Enter the Name of File: ", end="")
# filename = input()
# content_list = []
# try:
#     fo = open(filename, "r")
#     lines = fo.readlines()
#     for line in lines:
#         if line.strip() == "":
#             continue
#         else:
#             content_list.append(line.strip())
#     print("\n----The content of file \"", filename, "\"----", sep="")
#     print(content_list)
# except FileNotFoundError:
#     print("\nThe file \"", filename, "\" doesn't found.", sep="")

# product_list = []

# file = open('product.txt', "r")
# lines = file.readlines()
# for line in lines:
#     if line.strip() == "":
#         continue
#     else:
#         product_list.append(line.strip())
#     print(product_list) 

# def Courier_options(): 
#     print(
#     ''' 
#     0. return to main menu 
#     1. list Courier  
#     2. Create new Courier 
#     3. update Courier list 
#     4. delete Courier  
#     ''')
# Courier_options()


# filename = input('Enter name of File: ')
# content_list = []
# try:
#     fo = open(filename, "r")
#     lines = fo.readlines()
#     for line in lines:
#         if line.strip() == "":
#             continue
#         else:
#             content_list.append(line.strip())
#     print(content_list)
# except FileNotFoundError as fnfe:
#     print('Unable to open file: ' + str(fnfe))

from rough import create_new_product
create_new_product()